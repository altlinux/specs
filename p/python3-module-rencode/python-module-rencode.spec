%define oname rencode

Name: python3-module-%oname
Version: 1.0.8
Release: alt1

Summary: The rencode module is similar to bencode from the BitTorrent project

Group: Development/Python3
License: LGPL
Url: https://pypi.python.org/pypi/rencode

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/aresch/rencode/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(cython)
BuildRequires: python3(poetry-core)
BuildRequires: python3(wheel)

%description
The rencode module is similar to bencode from the BitTorrent project.
Forcomplex, heterogeneous data structures with many small elements,
r-encodingstake up significantly less space than b-encodings.
This version of rencode isa complete rewrite in Cython to attempt
to increase the performance over thepure Python module
written by Petru Paler, Connelly Barnes et al.

%prep
%setup
sed -i /COMPILE_ARGS/d build.py

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Wed Sep 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Sep 04 2024 Alexander Danilov <admsasha@altlinux.org> 1.0.6-alt3
- Applied security fixes from upstream (Fixes: CVE-2021-40839).

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt2
- build python3 package separately

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Linux Sisyphus
