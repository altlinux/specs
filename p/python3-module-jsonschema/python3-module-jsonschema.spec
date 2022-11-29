%define oname jsonschema

Name:		python3-module-%oname
Version:	4.17.1
Release:	alt1

Summary:	An implementation of JSON Schema validation for Python

License:	MIT
Group:		Development/Python3
URL:		http://pypi.python.org/pypi/jsonschema/


# Source-url: %__pypi_url %oname
Source0:	%name-%version.tar

BuildArch:	noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling python3-module-hatch-fancy-pypi-readme python3-module-hatch-vcs

# https://bugzilla.altlinux.org/38673
Conflicts: python-module-jsonschema < 2.6.0-alt3

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup

%build
if [ ! -d .git ]; then
    git init
    git config user.email Julian@GrayVines.com
    git config user.name Julian Berman
    git add .
    git commit -m 'release'
    git tag '%version'
fi
%pyproject_build

%install
%pyproject_install
rm -rfv %buildroot%python3_sitelibdir/%oname/benchmarks/

%files
%doc *.rst COPYING
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.org> 4.17.1-alt1
- New version

* Fri Oct 07 2022 Vladimir Didenko <cow@altlinux.org> 4.16.0-alt1
- New version

* Mon Sep 05 2022 Vladimir Didenko <cow@altlinux.org> 4.15.0-alt1
- New version

* Fri May 06 2022 Vladimir Didenko <cow@altlinux.org> 4.5.1-alt1
- Updated to upstream release 4.5.1
- Disable tests run (running tests using nose is broken)

* Mon Aug 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt4
- add Conflicts to old python-module-jsonschema (ALT bug 38673)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt3
- use python3-module-twisted-core-tests for tests
- cleanup spec: add URL for tarball, don't pack sources to gz
- disable tests packing

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- NMU: drop benchmarks packing

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- Updated to upstream release 3.2.0
- Build python3 version as separate package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Updated to upstream release 2.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added module for Python 3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
