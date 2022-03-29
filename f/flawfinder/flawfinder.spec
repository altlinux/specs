# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%global srcname flawfinder

Name: flawfinder
Version: 2.0.19
Release: alt1

Summary: Examines C/C++ source code for security flaws
License: GPLv2+
Group: Development/Other

Url: http://www.dwheeler.com/flawfinder/
Source: http://www.dwheeler.com/%name/%name-%version.tar.gz

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: flex
BuildRequires: python3-devel python3-module-setuptools

Summary(ru_RU.UTF-8): Исследует исходный код на С/С++ на предмет ошибок в безопасности

%description
Flawfinder scans through C/C++ source code, identifying lines ("hits")
with potential security flaws. By default it reports hits sorted by
severity, with the riskiest lines first.

%description -l ru_RU.UTF-8
Flawfinder сканирует исходный код на С/С++, указывая на строки,
в которых содержатся возможные ошибки в безопасности. По умолчанию
программа выводит отчет, отсортированный по предполагаемой серьёзности
ошибок, где строки, требующие пристального внимания с вашей стороны,
располагаются в начале.

%prep
%setup
rm -f test-results.*
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name '%name' \))

%build
%make_build
%python3_build
%{?!_without_check:%{?!_disable_check:%make_build -k check ||:}}

%install
#makeinstall_std
%python3_install
xz ChangeLog

%files
%python3_sitelibdir/%srcname-%version-py3.10.egg-info
%python3_sitelibdir/__pycache__/%{srcname}*.pyc
%python3_sitelibdir/%{srcname}.py
%_bindir/%name
%_man1dir/%name.1.*
%doc announcement README.md ChangeLog* *.pdf
%doc test/test.c test/test2.c
%{?!_without_check:%{?!_disable_check:%doc test/*.*}}

%changelog
* Tue Mar 29 2022 Ilya Mashkin <oddity@altlinux.ru> 2.0.19-alt1
- 2.0.19
- Update License tag

* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 2.0.10-alt2
- Fixed build --without test
- Converted spec to UTF-8
- Minor spec cleanup

* Thu Oct 31 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.10-alt1
- Version updated to 2.0.10

* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.31-alt1
- Version 1.31

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
