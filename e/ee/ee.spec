Name: ee
Version: 1.5.2
Release: alt1

Summary: ee - is intended to be a simple, easy to use terminal-based screen oriented editor.

Group: Editors
License: Artistic
URL: http://www.users.qwest.net/~hmahon/sources/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name-%version.tar
Patch1: %name-signal.patch
Patch2: %name-gcc-10.patch
Patch3: %name-Wformat-security.patch

%description
The editor 'ee' (easy editor) is intended to be a simple, easy to use
terminal-based screen oriented editor that requires no instruction to
use.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make

%install
install -pD ee %buildroot%_bindir/%name
install -pD ee.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/*

%changelog
* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 1.5.2-alt1
- Update to 1.5.2
- Apply some patches from gentoo (gcc10 FTBFS fix)

* Thu Jan 14 2010 Sergey Alembekov <rt@altlinux.ru> 1.4.6-alt1
- initial build for Sisyphus
