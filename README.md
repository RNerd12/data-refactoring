# data-refactoring
refactor data present in multiple excel files to uniform format in mongodb
all scripts are run by runner.py,
first run get_headers(), this gets all headers of excel sheets in directories
update header_mappings in configs1.py
run remap_excel() and upload_to_mongo()
