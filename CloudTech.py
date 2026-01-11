# Class representing a single page
class Page:
    def __init__(self, page_id, process_name=None):
        self.page_id = page_id
        self.process_name = process_name  # None = Free page

    def allocate(self, process_name):
        """Allocate this page to the given process/system."""
        self.process_name = process_name

    def deallocate(self):
        """Free this page."""
        self.process_name = None

    def __str__(self):
        if self.process_name:
            return f"Page {self.page_id}: {self.process_name}"
        else:
            return f"Page {self.page_id}: Free"


# Memory Manager using Paging
class MemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate memory sequentially to a process/system."""
        free_pages = [page for page in self.pages if page.process_name is None]

        # Check if enough free pages are available
        if len(free_pages) < num_pages_requested:
            return False

        # Allocate sequentially
        for page in free_pages[:num_pages_requested]:
            page.allocate(process_name)
        return True

    def print_memory_status(self):
        """Print the current allocation of memory pages."""
        print("\nCurrent Memory Allocation Status:")
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Print total memory used in units."""
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory = used_pages * self.page_size
        print(f"\nTotal Pages Used: {used_pages}")
        print(f"Total Memory Utilized: {total_memory} units")


# Driver Code
memory_manager = MemoryManager(num_pages=200, page_size=8)

# Memory allocation requests
requests = [
    ("Student Records System", 40),
    ("Faculty Management System", 25),
    ("Library Information System", 30),
    ("Online Learning Platform", 35),
    ("Research Database", 50)
]

# Sequentially allocate memory for each system
for process_name, num_pages_requested in requests:
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated:
        print(f"\nAllocated {num_pages_requested} pages for {process_name}")
        memory_manager.print_memory_status()
    else:
        print(f"\n Not enough memory available for {process_name} "
              f"(requested {num_pages_requested} pages)")

# Final memory utilization
memory_manager.print_total_memory_used()
