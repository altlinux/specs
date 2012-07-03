Name: fsme-examples
Version: 1.0.2
Release: alt2


Summary: Examples for Finite State Machine Editor (FSME)
Group: Development/C++
License: GPL
Packager: Pavel Vainerman <pv@altlinux.ru>

Url: http://fsme.sourceforge.net
Source: %name-%version.tar.bz2
Requires: fsme

%define realname examples-%version
%define examplesdir fsme-%version/examples


%description
Finite State Machine Editor examples

%prep
%setup -q -n %realname

%install
install -d -p -m755 $RPM_BUILD_ROOT%_docdir/%examplesdir
cp --recursive ./ $RPM_BUILD_ROOT%_docdir/%examplesdir

%files
%_docdir/%examplesdir


%changelog
* Thu Oct 18 2007 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt2
- rebuild for new version

* Fri Feb 18 2005 Pavel Vainerman <pv@altlinux.ru> 1.0.2-alt1
- first build
