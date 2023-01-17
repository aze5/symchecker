# symchecker
checks if a file is a symlink or not

This project was done for a small business that sells electronic components online. They have over 1.3 million files on a NAS device, most of them were symbolic links to a generic image of a component's case.

I was asked to write some code that would check whether a file was a symlink or not and write to a csv the following: filename, l or f (symlink or file), the path to the actual file if it was a symlink.

After completing this, I was asked to write to two different csvs (one for symlinks and one for normal files) as the manager was having some problems using just the one csv. Finally, to make the managers life easier in the future, i was asked to write some code to run sql commands to update his database

Unfortunately, I didn't use git to keep track of all the changes as this was one of my first projects, so this repo only includes the final version.
