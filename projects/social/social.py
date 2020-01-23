import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
            
        # Add users
        # creates user key with num of relatinships as the value.
        for i in range(num_users):
            self.users[i+1] = int(random.random() * num_users)
            self.friendships[i+1] = set()
        # Create friendships
            j = 0
            while j < (self.users[i+1]):
                friend = int(random.random() * self.users[i+1])
                if friend not in self.friendships[i+1] and friend > 0:
                    self.friendships[i+1].add(friend)
                j+=1

        print(f'users and num of relationships / {self.users}')

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # need to a create the graph

        queue = Queue()
        # enqueues entire set prob need to adjust 
        queue.enqueue(self.friendships[1]) 
        while queue.size() > 0:
            path = queue.dequeue()
            
            vertex = path.pop()
            if vertex not in visited and vertex is not None:
                if vertex == user_id:
                    return path
                visited[user_id] = []
                visited[user_id].append(vertex)
                for next_vertex in self.friendships[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
