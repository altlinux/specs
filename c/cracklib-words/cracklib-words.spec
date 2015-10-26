%define _name cracklib

Name: %_name-words
Version: 2.9.6
Release: alt1
Epoch: 1

Summary: Well-known words for cracklib
License: Freely distributable
Group: System/Libraries
Url: https://github.com/%_name/%_name

Source: https://github.com/%_name/%_name/releases/download/%_name-%version/%name-%version.gz

BuildArch: noarch

%description
This is a large dictionary for CrackLib library. If you want your
cracklib-based programs to check your passwords seriously, don't
forget to install this package.

%install
mkdir -p %buildroot%_datadir/%_name
gzip -cd %SOURCE0 >%buildroot%_datadir/%_name/%name

%files
%_datadir/%_name/%name

%changelog
* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.6-alt1
- 2.9.6 (new url & epoch)

* Thu May 17 2007 Alexey Rusakov <ktirf@altlinux.org> 20080507-alt1
- Initial Sisyphus version.

