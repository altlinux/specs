Summary: A rpm implementation purely in Python
Name: pyrpm
Version: 0.69
Release: alt2.1
License: GPL
Group: System/Base
Url: http://people.redhat.com/laroche/pyrpm
Source: %name-%version.tar.bz2
Packager: Pavlov Konstantin <thresh@altlinux.ru>
BuildRequires: asciidoc
BuildArch: noarch

%py_provides pyrpm

%description
PyRPM is a RPM implementation in Python. It can be used to study how rpm based
software management happens. Also tools can build upon it to handle rpm
packages in general e.g. to extract information, check dependancies or even
install packages.

%prep
%setup -q

%build
%configure
%make

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_cachedir/pyrpm

%files
%doc doc/*.html doc/*.txt
%_bindir/*
%_datadir/pyrpm
%_cachedir/pyrpm

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.69-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.69-alt2
- Rebuilt with python 2.6

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 0.69-alt1.1
- Rebuilt with python-2.5.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.69-alt1
- 0.69 release.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.68-alt1
- 0.68 release.

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.64-alt2
- Added py_provides pyrpm as suggested by bga@.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.64-alt1
- Initial build for ALT Linux.

* Wed Mar 09 2005 Phil Knirsch <pknirsch@redhat.com>
- Initial version
