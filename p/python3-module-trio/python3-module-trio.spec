%define _unpackaged_files_terminate_build 1

%define  modulename trio

Name:    python3-module-%modulename
Version: 0.19.0
Release: alt1

Summary: Trio - Pythonic async I/O for humans and snake people
License: MIT or Apache 2.0
Group:   Development/Python3
URL:     https://github.com/python-trio/trio

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md *.rst

%changelog
* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.0-alt1
- Updated to upstream version 0.19.0 to fix python-3.10 compatibility issues

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- don't pack tests (ALT bug 39239)

* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
