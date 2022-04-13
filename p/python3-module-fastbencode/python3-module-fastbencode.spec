# -*- coding: utf-8 -*-
%define _unpackaged_files_terminate_build 1

Name: python3-module-fastbencode
Version: 0.0.8
Release: alt2

Summary: An implementation of the bencode serialization format originally used by BitTorrent
License: GPLv2
Group: Development/Python

Url: https://github.com/breezy-team/fastbencode
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: fastbencode-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-Cython

%description
The package includes both a pure-Python version and an optional C extension based on Cython.
Both provide the same functionality, but the C extension provides significantly better performance.

This module is built for python %__python_version

%prep
%setup -n fastbencode-%version
#patch0 -p1

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%files
%python3_sitelibdir/fastbencode
%python3_sitelibdir/*.egg-info
%doc CODE_OF_CONDUCT.md README.md SECURITY.md

%changelog
* Wed Apr 13 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.0.8-alt2
- Fix build requirements

* Tue Apr 12 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.0.8-alt1
- Initial build


