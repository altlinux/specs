Name: unicode
Version: 0.9.4
Release: alt1.1

Summary: display unicode character properties
License: GPLv3
Group: Text tools

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Url: http://kassiopeia.juls.savba.sk/~garabik/software/unicode/

Source0: %name-%version.tar

%description
unicode is a simple command line utility that displays
properties for a given unicode character, or searches
unicode database for a given name.

%prep
%setup

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -p -m755 unicode paracode %buildroot%_bindir/
install -p -m644 unicode.1 paracode.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*
%doc README* debian/README.Debian debian/changelog debian/copyright

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.4-alt1.1
- Rebuild with Python-2.7

* Sat Mar 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.2-alt1
- initial build
