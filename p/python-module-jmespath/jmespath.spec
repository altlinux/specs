%define oname jmespath

Name: python-module-%oname
Version: 0.9.5
Release: alt2
Summary: JSON Matching Expressions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jmespath/

# https://github.com/boto/jmespath.git
Source: %name-%version.tar
Patch1: %oname-0.9.3-alt-docs.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-sphinx python-module-guzzle_sphinx_theme
BuildRequires: python-module-nose python-module-setuptools
BuildRequires: python-module-hypothesis

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%build
%python_build

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py2
done
popd

%make -C docs html

%check
export LC_ALL=en_US.UTF-8
python setup.py test
PYTHONPATH=$(pwd) py.test ||:

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*

%files docs
%doc docs/_build/html/*

%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Dropped dependency on python-tox.

* Tue Mar 24 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.5-alt1
- new version 0.9.5
- build python2 only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.3-alt1
- Updated to upstream version 0.9.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.git20150712.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.git20150712.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150712
- Version 0.7.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150420
- Version 0.7.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141105
- Initial build for Sisyphus

