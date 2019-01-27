import datetime

#Store the next avaliable id for all new notes
last_id = 0

class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note"""

    def __init__(self, memo, tags=""):
        """Initialize a note with a memo and optional
        space-seperated tags. Automatically set the note's
        creation date and a unique id."""

        #Initialize the memo, tags and creation date
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        #create an instance of the last_id to modify it
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text.
        Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and tags."""

        return filter in self.memo or filter in self.tags #Will need to pass values into the filter before we use them

class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched"""
    
    def __init__(self):
        """Initialize a notebook with an empty list"""
        self.notes = []
        
    def new_note(self, memo, tags = ""):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags)) #Creating a new note and appending it to the list of notes in the notebook

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value"""
        self._find_note(note_id)
        if note:
        	note.memo = memo
        	return True
        return False
            
    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value"""
        self._find_note(note_id).tags = tags
            
    def search(self, filter):
        """Find all notes that match the given filter
        string"""
        return [note for note in self.notes if note.match(filter)]
        
        
        
        
