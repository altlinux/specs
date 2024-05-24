%define modulename dukpy

%def_with check

Name: python3-module-dukpy
Version: 0.3.1
Release: alt1

Summary: Simple JavaScript interpreter for Python
License: MIT License
Group: Development/Python3
URL: https://pypi.org/project/dukpy
VCS: https://github.com/amol-/dukpy

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/d/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar
Patch: Use-system-duktape.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libduktape-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-webassets
%endif

%description
DukPy is a simple javascript interpreter for Python
built on top of duktape engine without any external dependency.
It comes with a bunch of common transpilers built-in for convenience:
CoffeeScript, BabelJS, TypeScript, JSX, LESS
Dukpy has been tested on Python 2.7 and Python 3.4,
dukpy is currently not production ready and might
actually crash your program as it is mostly implemented in C.

%prep
%setup
%patch -p1
# This removed the bundled duktape. The files that form the "Duktape
# 1.x compatible module loading framework" remain. They are some
# compat glue that is not shipped in duktape-devel.
rm -v src/duktape/duk_config.h src/duktape/duktape.c src/duktape/duktape.h

%build
%pyproject_build

%install
%pyproject_install

%check
# These files confuse pytest
rm -rv dukpy
# TestPackageInstaller needs internet connection
%pyproject_run_pytest -k 'not TestPackageInstaller'

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Build new version.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- Build for python2 disabled.

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2.qa1
- NMU: applied repocop patch

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.1.0-alt2
- Rebuild for aarch64

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Sisyphus

