%define oname python-ly

Name: python3-module-ly
Version: 0.9.7
Release: alt1

Summary: Tool and library for manipulating LilyPond files

Url: https://github.com/wbsoft/python-ly
License: GPL
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python3-devel python3-module-setuptools

Conflicts: python-module-ly

%description
This package provides a Python library `ly` containing various Python
modules to parse, manipulate or create documents in LilyPond format.
A command line program `ly` is also provided that can be used to do various
manipulations with LilyPond files.

The LilyPond format is a plain text input format that is used by the
GNU music typesetter LilyPond (www.lilypond.org).

The python-ly package is Free Software, licensed under the GPL. This package
is written by the Frescobaldi developers and is used extensively by the
Frescobaldi project. The main author is Wilbert Berendsen.

You can also read the docs online at http://python-ly.readthedocs.org/.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/ly
%_bindir/ly-server
%python3_sitelibdir/*


%changelog
* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt4
- build python3 module separately

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt3.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt3
- real build with python3

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt2
- build python3 module

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- initial build for ALT Sisyphus

