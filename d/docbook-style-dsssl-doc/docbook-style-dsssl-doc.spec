Name: docbook-style-dsssl-doc
Version: 1.79
Release: alt1

Summary: Documentation on DSSSL stylesheets for DocBook
Group: Publishing
License: Distributable
URL: http://www.nwalsh.com/docbook/dsssl/

BuildArch: noarch

Source0: http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%version.tar.bz2

%description
This package contains the documentation to DocBook DSSSL stylesheets.

%prep
%setup -q -n docbook-dsssl-%version

%files
%doc doc/*

%changelog
* Fri Nov 05 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.79-alt1
- New upstream release

* Fri Mar 14 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.78-alt1
- 1.78

* Thu Aug 01 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.77-alt1
- 1.77

* Mon Mar 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.75-alt1
- 1.75
- fixed spec macro glitch

* Fri Jan 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.74-alt1
- Initial release

