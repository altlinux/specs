Name: netams-doc-ru
Version: 3.4.0rc1
Release: alt1

Summary: NeTAMS documentation
Summary(ru_RU.KOI8-R): дПЛХНЕОФБГЙС Л NeTAMS
Summary(ru_RU.CP1251): Документация к NeTAMS

License: BSD
Group: Documentation
Url: http://www.netams.com/doc/

BuildArch: noarch

Packager: Anton Korbin <ahtoh@altlinux.ru>

Source: %name.tar.gz

%description
NeTAMS documentation

%prep
%setup -q -n %name

%build
%__mkdir_p %buildroot%_docdir/%name
%__cp -R * %buildroot%_docdir/%name

%files
%_docdir/%name

%changelog
* Tue Mar 27 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt1
- New version

* Wed Dec 20 2006 Sergei Epiphanov <serpiph@altlinux.ru> 3.3.5-alt1
- New netams doc version for AltLinux

* Wed Dec 14 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.1a-alt1
- New netams doc version for AltLinux

* Fri Nov 04 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.0-alt1
- First netams doc version for AltLinux
