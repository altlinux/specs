%define oname rencode

Name: python3-module-%oname
Version: 1.0.6
Release: alt3

Summary: The rencode module is similar to bencode from the BitTorrent project

Group: Development/Python3
License: LGPL
Url: https://pypi.python.org/pypi/rencode

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/aresch/rencode/archive/v%version.tar.gz
Source: %name-%version.tar
Patch1: CVE-2021-40839.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-Cython python3-module-wheel

%description
The rencode module is similar to bencode from the BitTorrent project.
Forcomplex, heterogeneous data structures with many small elements,
r-encodingstake up significantly less space than b-encodings.
This version of rencode isa complete rewrite in Cython to attempt
to increase the performance over thepure Python module
written by Petru Paler, Connelly Barnes et al.

%prep
%setup
%patch1 -p1

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
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
