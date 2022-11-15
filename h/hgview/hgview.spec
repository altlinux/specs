%define _unpackaged_files_terminate_build 1

Name: hgview
Version: 1.14.0
Release: alt2.1

Summary: Qt5 based Mercurial log navigator
License: GPLv2+
Group: Development/Tools

BuildArch: noarch

Url: http://www.logilab.org/project/hgview

# hg clone http://hg.logilab.org/review/hgview
Source0: %{name}-%{version}.tar

Requires: python3-module-qscintilla2-qt5
Requires: mercurial mercurial-hgext

BuildRequires(pre): rpm-build-python3
BuildRequires: mercurial mercurial-hgext asciidoc xmlto python3-module-PyQt5-devel

%add_python3_self_prov_path %buildroot%python3_sitelibdir/hgviewlib/qt5

%description
hgview is a simple tool aiming at visually navigate in a Mercurial
repository history.
It is written in Python/Qt4 with quick and efficient key-based
navigation in mind, trying to be fast enough to be usable for big
repositories.

%prep
%setup

%build
%python3_build

%install
%python3_install
mv %buildroot/usr/man %buildroot/usr/share
rm -rf %buildroot/usr/share/doc/%name
# conflicts with hgext3rd from mercurial
rm -rf %buildroot%python3_sitelibdir/hgext3rd/

%files
%_bindir/*
%python3_sitelibdir/hgviewlib/
%python3_sitelibdir/*.egg-info
%_man1dir/*
%doc ChangeLog README.rst COPYING

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.14.0-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt2
- fix BR: python3-module-PyQt5-devel

* Fri Oct 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- Updated to upstream version 1.14.0.
- Transferred on python3.

* Mon Mar 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.4-alt1
- Updated to upstream version 1.10.4.

* Wed Sep 19 2018 Pavel Moseev <mars@altlinux.org> 1.10.2-alt1
- Updated to upstream version 1.10.2 (closes: 31467)

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1
- automated PyPI update

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1
- Version 1.8.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.0-alt1
- initial build
