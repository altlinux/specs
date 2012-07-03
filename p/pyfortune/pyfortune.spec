Name: pyfortune
Version: 0.1
Release: alt1.1.1

Summary: Python version of ever-popular fortune program.
Summary(ru_RU.UTF8): реализация на Python известной программы fortune
License: GPL3
Group: Games/Other
Url: http://sisyphus.ru/srpm/Sisyphus/pyfortune

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar
BuildArch: noarch

%description
Python version of ever-popular fortune program.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_defaultdocdir/ %buildroot%_bindir/
cp pyfortune %buildroot%_bindir/
#cp TODO ChangeLog COPYING %buildroot%_defaultdocdir/

%files
%doc ChangeLog COPYING TODO
%_bindir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Wed Mar 19 2008 Alexey Morsov <swi@altlinux.ru> 0.1-alt1
- initial release

