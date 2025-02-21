
import sqlite3

# Function to create the 'Members' table
def create_members_table():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        )
    ''')

    conn.commit()
    conn.close()

# Function to create the 'WorkoutSessions' table
def create_workouts_table():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WorkoutSessions (
            session_id INT PRIMARY KEY,
            member_id INT,
            session_date DATE,
            session_time VARCHAR(50),
            activity VARCHAR(255),
            FOREIGN KEY (member_id) REFERENCES Members(id)
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a member
def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Members (id, name, age)
            VALUES (?, ?, ?)
        ''', (id, name, age))
        
        conn.commit()
        print("Member added successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            conn.close()

# Function to add a workout session
def add_workout_session(session_id, member_id, session_date, session_time, activity):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
            VALUES (?, ?, ?, ?, ?)
        ''', (session_id, member_id, session_date, session_time, activity))
        
        conn.commit()
        print("Workout session added successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            conn.close()

# Function to update a workout session time
def update_workout_session_time(member_id, new_session_time):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE WorkoutSessions
            SET session_time = ?
            WHERE member_id = ?
        ''', (new_session_time, member_id))
        
        conn.commit()
        print("Workout session updated successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            conn.close()

# Function to delete a member
def delete_member(id):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM Members WHERE id = ?
        ''', (id,))
        
        if cursor.rowcount == 0:
            raise ValueError(f"No member found with id: {id}")
        
        conn.commit()
        print("Member deleted successfully!")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    finally:
        if conn:
            conn.close()

# Example usage
create_members_table()
create_workouts_table()
add_member(1, 'Jane Doe', 28)
add_workout_session(101, 1, '2025-02-20', 'morning', 'Yoga')
update_workout_session_time(1, 'evening')
delete_member(1)
