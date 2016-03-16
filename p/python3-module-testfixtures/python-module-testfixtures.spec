%define  modulename testfixtures

Name:    python3-module-%modulename
Version: 4.9.0
Release: alt1.git20160225.1

Summary: A collection of helpers and mock objects for unit tests and doc tests
License: MIT
Group:   Development/Python3
URL:     http://www.simplistix.co.uk/software/python/testfixtures

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools-tests python3-module-tox
BuildPreReq: python3-module-zope.component python-module-pkginfo
BuildPreReq: python3-module-mock python3-module-manuel-tests
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-sphinx python-module-sphinx-devel
BuildPreReq: python-module-manuel python-module-zope.component

Source:  %modulename-%version.tar

%py3_provides %modulename
%py3_requires zope.component

%description
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.

%prep
%setup -n %modulename-%version

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs html SPHINXBUILD=sphinx-build

%check
python3 setup.py test
rm -fR build
py.test-%_python3_version

%files
%doc *.txt docs/_build/html
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.9.0-alt1.git20160225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 4.9.0-alt1.git20160225
- New version 

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.git20150130
- Version 4.1.2

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20141022
- Initial build for Sisyphus

