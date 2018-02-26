Name: ee
Version: 1.4.6
Release: alt1

Summary: ee - is intended to be a simple, easy to use terminal-based screen oriented editor.

Group: Editors
License: Artistic
URL: http://www.users.qwest.net/~hmahon/sources/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name-%version.tar

%description
The editor 'ee' (easy editor) is intended to be a simple, easy to use
terminal-based screen oriented editor that requires no instruction to
use.

%prep
%setup -n %name-%version

%build
%make

%install
install -pD ee %buildroot%_bindir/%name
install -pD ee.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/*

%changelog
* Thu Jan 14 2010 Sergey Alembekov <rt@altlinux.ru> 1.4.6-alt1
- initial build for Sisyphus
