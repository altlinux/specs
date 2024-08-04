%define _name cracklib

Name: %_name-words
Version: 2.10.2
Release: alt1
Epoch: 1

Summary: Well-known words for cracklib
License: Freely distributable
Group: System/Libraries
Url: https://github.com/%_name/%_name

Source: https://github.com/%_name/%_name/releases/download/v%version/%name-%version.xz

BuildArch: noarch

BuildRequires: dos2unix

%description
This is a large dictionary for CrackLib library. If you want your
cracklib-based programs to check your passwords seriously, don't
forget to install this package.

%install
mkdir -p %buildroot%_datadir/%_name
# abcdefghabcdefghabcdefghabcdefgh... very long sequence found in skullsecurity.org/myspace.txt
xzcat %SOURCE0 | dos2unix| \
sed -e '/^abcdefghabcdefghabcdefghabcdefgh/d
/^$/d
/^#\!comment/d
s/^[[:space:]]*//' | \
sort | uniq >%buildroot%_datadir/%_name/%name

%files
%_datadir/%_name/%name

%changelog
* Sun Aug 04 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.10.2-alt1
- 2.10.2

* Sun Jul 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.10.1-alt1
- 2.10.1

* Sun Jul 14 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.10.0-alt1
- 2.10.0

* Mon Apr 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.11-alt1
- 2.9.11

* Tue Mar 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.10-alt1
- 2.9.10

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.8-alt1
- 2.9.8

* Tue Apr 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.7-alt1
- 2.9.7

* Fri Nov 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.6-alt1.1
- words cleanup (ALT #31446)

* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.9.6-alt1
- 2.9.6 (new url & epoch)

* Thu May 17 2007 Alexey Rusakov <ktirf@altlinux.org> 20080507-alt1
- Initial Sisyphus version.

