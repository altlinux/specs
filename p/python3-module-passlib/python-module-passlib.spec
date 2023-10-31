%define oname passlib

# very slow:
%def_disable check

Name:		python3-module-%oname
Version:	1.7.4
Release:	alt2

Summary:	Comprehensive password hashing framework supporting over 20 schemes

License:	BSD and Beerware and Copyright only
Group:		Development/Python3
URL:		https://foss.heptapod.net/python-libs/passlib/-/wikis/home

# Source-url: %__pypi_url %oname
Source:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%if_enabled check
BuildRequires: python3-module-nose
%endif

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It's
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/
sed -i 's|@VERSION@|%version|' docs/conf.py

%build
%python3_build_debug

%install
%python3_install
%python3_prune
# remove unused code with distutils (ALT bug 48244)
rm -rv %buildroot%python3_sitelibdir/passlib/_setup/

%if 0
export PYTHONPATH=$PWD
pushd docs
sphinx-build -b html -d build/doctrees . build/html
popd
%endif

%check
python3 setup.py test

%files
%doc LICENSE README
%python3_sitelibdir/*

%changelog
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
