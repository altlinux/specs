%define modulename dukpy

%def_without check

Name: python3-module-dukpy
Version: 0.2.2
Release: alt2

Summary: Simple JavaScript interpreter for Python
Url: https://pypi.python.org/pypi/dukpy/
License: MIT License
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/d/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


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

%build
%python3_build_debug

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
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

