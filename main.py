from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"  
AUTH = ("neo4j", "senha123") 

driver = GraphDatabase.driver(URI, auth=AUTH)

def create_person(name):
    with driver.session() as session:
        session.run("MERGE (p:Person {name: $name})", name=name)
    print(f"Pessoa '{name}' criada ou já existente.")

def create_friendship(name, friend_name):
    with driver.session() as session:
        session.run("""
            MERGE (a:Person {name: $name})
            MERGE (b:Person {name: $friend_name})
            MERGE (a)-[:KNOWS]->(b)
        """, name=name, friend_name=friend_name)
    print(f"Relacionamento {name} -> {friend_name} criado.")

def list_friends(name):
    with driver.session() as session:
        result = session.run("""
            MATCH (a:Person)-[:KNOWS]->(friend)
            WHERE a.name = $name
            RETURN friend.name AS friend_name
            ORDER BY friend_name
        """, name=name)
        friends = [record["friend_name"] for record in result]
    if friends:
        print(f"Amigos de {name}: {', '.join(friends)}")
    else:
        print(f"{name} não tem amigos cadastrados.")

def update_person(old_name, new_name):
    with driver.session() as session:
        session.run("""
            MATCH (p:Person {name: $old_name})
            SET p.name = $new_name
        """, old_name=old_name, new_name=new_name)
    print(f"Nome atualizado de '{old_name}' para '{new_name}'.")

def delete_person(name):
    with driver.session() as session:
        session.run("""
            MATCH (p:Person {name: $name})
            DETACH DELETE p
        """, name=name)
    print(f"Pessoa '{name}' deletada junto com suas conexões.")

def list_all_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.name AS name ORDER BY name")
        people = [record["name"] for record in result]
    if people:
        print("Todas as pessoas:")
        for p in people:
            print(f"- {p}")
    else:
        print("Nenhuma pessoa cadastrada.")

def list_all_friendships():
    with driver.session() as session:
        result = session.run("""
            MATCH (a:Person)-[:KNOWS]->(b:Person)
            RETURN a.name AS from_name, b.name AS to_name
            ORDER BY from_name, to_name
        """)
        friendships = [(r["from_name"], r["to_name"]) for r in result]
    if friendships:
        print("Todas as amizades:")
        for f in friendships:
            print(f"- {f[0]} -> {f[1]}")
    else:
        print("Nenhuma amizade cadastrada.")

def menu():
    while True:
        print("\n=== Menu Neo4j CRUD ===")
        print("1 - Criar pessoa")
        print("2 - Criar amizade")
        print("3 - Listar amigos")
        print("4 - Atualizar nome da pessoa")
        print("5 - Deletar pessoa")
        print("6 - Listar todas as pessoas")
        print("7 - Listar todas as amizades")
        print("0 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome da pessoa: ")
            create_person(name)
        elif choice == "2":
            name = input("Nome da pessoa principal: ")
            friend_name = input("Nome do amigo: ")
            create_friendship(name, friend_name)
        elif choice == "3":
            name = input("Nome da pessoa para listar amigos: ")
            list_friends(name)
        elif choice == "4":
            old_name = input("Nome atual da pessoa: ")
            new_name = input("Novo nome: ")
            update_person(old_name, new_name)
        elif choice == "5":
            name = input("Nome da pessoa a deletar: ")
            delete_person(name)
        elif choice == "6":
            list_all_people()
        elif choice == "7":
            list_all_friendships()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    try:
        menu()
    finally:
        driver.close()
