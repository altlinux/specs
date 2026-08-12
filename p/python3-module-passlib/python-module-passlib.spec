%define oname passlib

Name:		python3-module-%oname
Version:	1.9.3
Release:	alt1

Summary:	Comprehensive password hashing framework supporting over 30 schemes

License:	BSD
Group:		Development/Python3
URL:		https://github.com/notypecheck/passlib

# Fork of the abandoned passlib (last upstream 1.7.4 from foss.heptapod.net).
# Maintained by notypecheck, published on PyPI as "libpass".
# Source-url: https://github.com/notypecheck/passlib/archive/refs/tags/%version.tar.gz
Source:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_enabled check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-argon2-cffi
%endif

%description
Passlib is a password hashing library for Python 3, which provides
cross-platform implementations of over 30 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This is the maintained fork of passlib (originally hosted at
foss.heptapod.net, last release 1.7.4). It is published on PyPI as
"libpass" but keeps the "passlib" import name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%if_enabled check
pytest
%endif

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/libpass-%version.dist-info/

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- new version 1.9.3 (maintained fork of passlib, published as libpass on PyPI)
- switch to pyproject build (hatchling)
- enable %check (run test suite)
- add test BuildRequires (bcrypt, cryptography, argon2-cffi, pytest)

* Wed Nov 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt2
- remove used code with distutils (ALT bug 48244)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt2
- build python3 package separately, disable tests packing

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.dev0.hg20131228.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt1.dev0.hg20131228.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.hg20131228
- Version 1.7.dev0
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.5.3-alt1
- Initial release for Sisyphus (based on Fedora)
