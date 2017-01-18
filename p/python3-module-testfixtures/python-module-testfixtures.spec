%define _unpackaged_files_terminate_build 1
%define  modulename testfixtures

Name:    python3-module-%modulename
Version: 4.13.3
Release: alt1

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

Source0:  https://pypi.python.org/packages/fc/c1/b62e96678328d0e7a01e175647f111adb3438fe51776baeeb8e95a8d07f8/testfixtures-%{version}.tar.gz

%py3_provides %modulename
%py3_requires zope.component

%description
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.

%prep
%setup -q -n testfixtures-%{version}

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
%doc *.txt docs/_build/html PKG-INFO README.rst docs
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.13.3-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.9.0-alt1.git20160225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 4.9.0-alt1.git20160225
- New version 

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.git20150130
- Version 4.1.2

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.git20141022
- Initial build for Sisyphus

