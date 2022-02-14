%define modulename application

Name:    python3-module-%modulename
Version: 3.0.3
Release: alt2

Summary: Basic building blocks for Python applications

License: LGPL-2.0+
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-application

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
BuildRequires: python3-module-zope.interface

BuildArch: noarch

# Source-url: https://github.com/AGProjects/python3-application/archive/release-%version.tar.gz
Source: %name-%version.tar
Patch1: 0001-collections.MutableMapping-was-deprecated-since-Pyth.patch

%add_python3_req_skip __main__

%description
This package is a collection of modules that are useful when building
python applications. Their purpose is to eliminate the need to divert
resources into implementing the small tasks that every application needs
to do in order to run successfully and focus instead on the application
logic itself.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt2
- collections.MutableMapping stopped working since Python 3.10

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- new version 3.0.3

* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)

* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- initial build python3 module for ALT Sisyphus
