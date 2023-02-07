Name: example-pretrans-symlink-to-dir
Summary: Example of using %%pretrans to replace symlink with a directory
Version: 1
Release: alt1
License: GPL-2.0-only
Group:Games/Adventure
BuildArch: noarch
Url: https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/

%description
%summary.

%build
date > file.txt

%install
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/dir
ln -s dir %buildroot%_libexecdir/%name/symlinked

%check
cd %buildroot
find .%_libexecdir/%name -ls

%files
%_libexecdir/%name

%changelog
* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Create dir and symlinked dir with a file.
