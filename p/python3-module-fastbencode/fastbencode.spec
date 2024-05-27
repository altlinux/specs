Name: python3-module-fastbencode
Version: 0.3.1
Release: alt1

Summary: An implementation of the bencode serialization format originally used by BitTorrent
License: GPLv2
Group: Development/Python3

URL: https://pypi.org/project/fastbencode
VCS: https://github.com/breezy-team/fastbencode
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-Cython
BuildRequires: python3-module-wheel

%description
The package includes both a pure-Python version and an optional C extension based on Cython.
Both provide the same functionality, but the C extension provides significantly better performance.

This module is built for python %__python_version

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
python3 -m unittest

%files
%doc CODE_OF_CONDUCT.md README.md SECURITY.md
%python3_sitelibdir/fastbencode
%python3_sitelibdir/fastbencode-%version.dist-info

%changelog
* Mon May 27 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Automatically updated to 0.3.1.
- Build with check.

* Fri Oct 21 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.0.15-alt1
- Release 0.0.15

* Wed Apr 13 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.0.8-alt2
- Fix build requirements

* Tue Apr 12 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.0.8-alt1
- Initial build
