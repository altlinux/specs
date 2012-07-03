Name: dovecot-doc
Version: 1.0.2
Release: alt1.20071030

Summary: Dovecot documentation from wiki pages
License: GPL
Group: System/Servers
Url: http://%name.org/
BuildArch: noarch

Packager: Sergey Ivanov <seriv@altlinux.ru>

Source0: %name-%version.tar.gz

%description
local copy of dovecot-wiki, created from http://wiki.dovecot.org/

%prep
%setup -n %name-%version -q

%build

%install
%__mkdir_p %buildroot%_docdir/%name
%__install *.txt %buildroot%_docdir/%name


%files
%doc *.txt

%changelog
* Wed Oct 31 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt1.20071030
- Upgdared to current state of wiki pages.

* Tue Jul 17 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt1
- Updated from http://wiki.dovecot.org at Jul 17 2007

* Sat Jun 16 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.1-alt1
- Initial build.
