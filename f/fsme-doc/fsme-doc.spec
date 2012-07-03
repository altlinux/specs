%define realname fsme_doc
%define ename fsme

Name: fsme-doc
Version: 1.0.2
Release: alt1


Summary: FSME docs
Group: Development/C++
License: GPL
Packager: Pavel Vainerman <pv@altlinux.ru>

Url: http://fsme.sourceforge.net
Source: fsme_doc.tar.bz2
Requires: %ename


%description
Finite State Machine Editor documents

%prep
%setup -q -n %realname

%install
install -d -p -m755 $RPM_BUILD_ROOT%_docdir/%ename-%version
cp --recursive ./ $RPM_BUILD_ROOT%_docdir/%ename-%version

%files
%_docdir/%ename-%version


%changelog
* Fri Feb 18 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt1
- first build


