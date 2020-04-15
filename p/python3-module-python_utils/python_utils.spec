%define oname python_utils

%def_without doc

Name: python3-module-%oname
Version: 2.2.0
Release: alt2

Summary: A module with some convenient utilities not included with the standard Python install
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-utils/

BuildArch: noarch

# https://github.com/WoLpH/python-utils.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-pytest
%if_with doc
BuildRequires: python3-module-sphinx
%endif

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. It is by no means a complete
collection but it has served me quite a bit in the past and I will keep
extending it.

%prep
%setup
%if_with doc
%patch1 -p1

sed -i 's|sphinx-build|&-3|' docs/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with doc
%make -C docs html
%endif

%check
%__python3 setup.py test

%files
%doc *.rst
%if_with doc
%doc docs/_build/html
%endif
%python3_sitelibdir/*

%changelog
* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled build for python-3.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.git20150209
- Version 1.6.2

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141015
- Initial build for Sisyphus

