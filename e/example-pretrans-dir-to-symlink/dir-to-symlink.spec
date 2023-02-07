Name: example-pretrans-dir-to-symlink
Summary: Example of using %%pretrans to replace directory with a symlink
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
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/a/
install -Dpm644 file.txt -t %buildroot%_libexecdir/%name/b/

%check
cd %buildroot
find .%_libexecdir/%name -ls

%files
%_libexecdir/%name

%changelog
* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Create two directories with the same file.
