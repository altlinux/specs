Version: 1.2.1
Release: alt1.1
Summary: Console Jabber Client
Summary(pl):	CJC - konsolowy klient Jabbera
Name: cjc
%setup_python_module %name
License: GPL
Group: Networking/Instant messaging
Source0: http://cjc.jajcus.net/downloads/cjc-%version.tar.gz
# svn checkout http://cjc.jajcus.net/svn/cjc/trunk cjc
# make version ChangeLog
Url: http://cjc.jajcus.net
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>
BuildRequires: xsltproc docbook-style-xsl
Requires: %packagename = %version

%description
A Jabber client for text terminals with user interface similar to
those known from popular IRC clients.

%description -l pl
Klient Jabbera dla terminali tekstowych z interfejsem u¿ytkownika
podobnym do tego znanego z popularnych klientów IRC.

%package -n %packagename
Group: Development/Python
Summary: Console Jabber Client module
Requires: %name

%description -n %packagename
CJC is a Jabber client for text terminals with user interface similar to
those known from popular IRC clients.

This package provides a module for CJC.

%prep
%setup -n cjc-%version

%build
%make prefix=%prefix XSL_DIR=/usr/share/xml/docbook/xsl-stylesheets

%install
%makeinstall prefix=%prefix
mkdir -p %buildroot%python_sitelibdir
mv %buildroot%_defaultdocdir/cjc %buildroot%_defaultdocdir/cjc-%version
mv %buildroot%_datadir/cjc/cjc %buildroot%python_sitelibdir/

%files -n %packagename
%python_sitelibdir/cjc

%files
%doc %_defaultdocdir/cjc-%version
%_bindir/*
%_datadir/cjc

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild with Python-2.7

* Fri May 20 2011 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1

* Mon Oct 04 2010 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Version up

* Sun Apr 11 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Version up

* Sun Apr 11 2010 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Reorganizing spec

* Sat Dec 19 2009 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Rebuild with python 2.6

* Thu Feb 05 2009 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Version up

* Sat May 17 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt4
- SVN generated file added

* Thu May 15 2008 Fr. Br. George <george@altlinux.ru> 1.0.0-alt3
- Updated to CVS 679

* Wed Dec 27 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- Split into two packages: application and module
- Move module into %python_libdir

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial ALT build from PLD

