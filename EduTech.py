# Class representing a single page
class Page:
    def __init__(self, page_id, process_name=None):
        self.page_id = page_id
        self.process_name = process_name  # None means page is free

    def allocate(self, process_name):
        """Allocate this page to a process"""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate this page (make it free)"""
        self.process_name = None

    def __str__(self):
        if self.process_name:
            return f"Page {self.page_id}: {self.process_name}"
        else:
            return f"Page {self.page_id}: Free"


# Class for managing memory using paging
class MemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate the required number of pages to a process"""
        # Find all free pages
        free_pages = [page for page in self.pages if page.process_name is None]

        # Check if enough free pages are available
        if len(free_pages) < num_pages_requested:
            return False

        # Allocate pages sequentially
        for page in free_pages[:num_pages_requested]:
            page.allocate(process_name)
        return True

    def print_memory_status(self):
        """Display current allocation of memory pages"""
        print("\nCurrent Memory Allocation Status:")
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Display the total memory utilization"""
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory = used_pages * self.page_size
        print(f"\nTotal Pages Used: {used_pages}")
        print(f"Total Memory Utilized: {total_memory} units")


# Driver Code
memory_manager = MemoryManager(num_pages=100, page_size=4)

# Process memory requests
requests = [
    ("Process A", 25),
    ("Process B", 15),
    ("Process C", 30),
    ("Process D", 12),
    ("Process E", 20)
]

# Sequentially allocate memory for each process
for process_name, num_pages_requested in requests:
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated:
        print(f"\n Allocated {num_pages_requested} pages for {process_name}")
        memory_manager.print_memory_status()
    else:
        print(f"\n Not enough memory available for {process_name} "
              f"(requested {num_pages_requested} pages)")

# Final memory utilization
memory_manager.print_total_memory_used()
