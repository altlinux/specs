Name: example-pretrans-symlink-to-dir
Summary: Example of using %%pretrans to replace symlink with a directory
Version: 2
Release: alt1
License: GPL-2.0-only
Group:Games/Adventure
BuildArch: noarch
Url: https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/

%description
%summary.

Note that '%%pretrans' scriptlets MUST be written in Lua and thus use -p <lua>
in order to function during initial system installation when no shell has yet
been installed.

%build
date > file.txt

%install
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/dir
# Now make 'symlinked' a directory.
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/symlinked

# "Replacing a symlink to a directory with a regular directory is much simpler,
# since there’s no potential for accidentally removing files added externally.
# The following scriptlet checks for and removes the symlink. There is no need
# to create the directory here, as RPM will do so later in the transaction when
# the package is installed."
#
%pretrans -p <lua>
-- Define the path to the symlink being replaced below.
path = "%_libexecdir/%name/symlinked"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%check
cd %buildroot
find .%_libexecdir/%name -ls

%files
%_libexecdir/%name

%changelog
* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Show usage of scriptlet to replace a symlink to a directory with a directory.

* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Create dir and symlinked dir with a file.
