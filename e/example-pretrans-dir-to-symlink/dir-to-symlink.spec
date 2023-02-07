Name: example-pretrans-dir-to-symlink
Summary: Example of using %%pretrans to replace directory with a symlink
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
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/a/
# Replace directory with a symlink.
ln -s a %buildroot%_libexecdir/%name/b

%check
cd %buildroot
find .%_libexecdir/%name -ls

# "RPM cannot simply remove a directory when it is replaced by a file or
# symlink, since users may have added or modified files to the directory. To
# protect against accidental data loss, you MUST use the following scriptlet
# which renames the directory with a .rpmmoved suffix so that users can find
# the backed up directory if they need to after the package is upgraded. (It
# also will append an integer to the suffix in the rare event that directory
# also exists.)"
#
%pretrans -p <lua>
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
path = "%_libexecdir/%name/b"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%files
%_libexecdir/%name

%changelog
* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Use scriptlet to replace a directory.

* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Create two directories with the same file.
