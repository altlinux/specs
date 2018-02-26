%define pname cracklib
Name: %pname-words
Version: 20080507
Release: alt1

Summary: Well-known words for cracklib
License: Freely distributable
Group: System/Libraries
Url: http://sourceforge.net/projects/%pname

Packager: Alexey Rusakov <ktirf@altlinux.org>

Source: http://downloads.sourceforge.net/%pname/%name-%version.gz

BuildArch: noarch

%description
This is a large dictionary for CrackLib library. If you want your
cracklib-based programs to check your passwords seriously, don't
forget to install this package.

%install
mkdir -p %buildroot%_datadir/%pname
gzip -cd %SOURCE0 >%buildroot%_datadir/%pname/%name

%files
%_datadir/%pname/%name

%changelog
* Thu May 17 2007 Alexey Rusakov <ktirf@altlinux.org> 20080507-alt1
- Initial Sisyphus version.

