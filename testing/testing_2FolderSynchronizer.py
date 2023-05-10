import filecmp

dir1 = './testing_directories/replica'
dir2 = './testing_directories/source'

# Compare the two directories and get a report object
comparison = filecmp.dircmp(dir1, dir2)

# Check if the two directories are identical
if comparison.diff_files or comparison.left_only or comparison.right_only:
    print("The directories are not identical")
else:
    print("The directories are identical")