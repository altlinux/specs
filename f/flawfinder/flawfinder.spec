# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: flawfinder
Version: 1.27
Release: alt1.2.1

Summary: Examines C/C++ source code for security flaws
Summary(ru_RU.CP1251): Исследует исходный код на С/С++ на предмет ошибок в безопасности

License: GPL
Group: Development/Other
Url: http://www.dwheeler.com/flawfinder/
Packager: Slava Semushin <php-coder@altlinux.ru>

BuildArch: noarch

Source: http://www.dwheeler.com/%name/%name-%version.tar.gz
Patch1: %name-alt-python.patch
Patch2: %name-alt-makefile.patch

# Automatically added by buildreq on Wed Nov 21 2007
BuildRequires: python-modules

%description
Flawfinder scans through C/C++ source code, identifying lines ("hits")
with potential security flaws. By default it reports hits sorted by
severity, with the riskiest lines first.

%description -l ru_RU.CP1251
Flawfinder сканирует исходный код на С/С++, указывая на строки, в
которых содержатся возможные ошибки в безопасности. По умолчанию
программа выводит отчет, отсортированный по предполагаемой серьёзности
ошибок, где строки, требующие пристального внимания с вашей стороны,
располагаются в начале.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%make_build
%{?!_without_check:%{?!_disable_check:%make_build -k check ||:}}

%install
install -pD -m 755 %name %buildroot%_bindir/%name
install -pD -m 644 %name.1 %buildroot%_man1dir/%name.1
bzip2 -9fk ChangeLog

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc announcement README ChangeLog.bz2
%doc test.c test2.c test-results.*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.27-alt1.2.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.27-alt1.1
- Rebuilt with python-2.5.

* Mon Nov 05 2007 Slava Semushin <php-coder@altlinux.ru> 1.27-alt1
- Updated to 1.27 (#10747, freebsd #108951)
- New maintainer
- Added Russian Summary and %%description
- Package test files and tests reults
- Spec cleanup
- Enable _unpackaged_files_terminate_build

* Tue Jun 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.26-alt1
- Updated to 1.26
- Fixed "make check".

* Mon Sep 08 2003 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt2
- Updated buildrequires.

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt1
- Updated to 1.22

* Mon Sep 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.21-alt1
- 1.21
