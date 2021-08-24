%define _unpackaged_files_terminate_build 1

%define oname jsonpickle

Name: python3-module-%oname
Version: 2.0.0
Release: alt1
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jsonpickle/

BuildArch: noarch

# git://github.com/jsonpickle/jsonpickle.git
Source: %name-%version.tar

Patch1: %oname-alt-disable-pytest-black.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(setuptools_scm) python3(toml)
BuildRequires: python3-module-demjson python3-module-jsonlib
BuildRequires: python3-module-yajl python3-module-ujson
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: /usr/bin/pytest-3 python3-module-pytest-flake8 python3-module-pytest-cov
BuildRequires: python3(pandas)

%py3_provides %oname
%py3_requires demjson jsonlib yajl ujson

%description
jsonpickle converts complex Python objects to and from JSON.

%prep
%setup
%patch1 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build_debug

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
pytest3 -vv

%files
%doc LICENSE
%doc *.rst contrib
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.
- Enabled tests.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.
- Disabled build for python-2.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.5-alt1
- Updated to upstream version 0.9.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

