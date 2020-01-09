%define _unpackaged_files_terminate_build 1
%define oname zope.interface

%def_with check

Name: python-module-%oname
Version: 4.7.1
Release: alt1

Summary: Zope interfaces package
License: ZPL-2.1
Group: Development/Python
# Source-git https://github.com/zopefoundation/zope.interface.git
Url: http://www.python.org/pypi/zope.interface

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx

BuildRequires: python-module-repoze.sphinx.autointerface
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
BuildRequires: python-devel
BuildRequires: python3-dev

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-zope.event
BuildRequires: python-module-coverage
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-coverage
%endif

%description
This is a separate distribution of the %oname package used in
Zope 3, along with the packages it depends on.

%package -n python3-module-%oname
Summary: Zope interfaces package (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This is a separate distribution of the %oname package used in
Zope 3, along with the packages it depends on.

%package -n python3-module-%oname-tests
Summary: Tests for %oname (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.event

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.event

%description tests
This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for %oname.

%prep
%setup
cp -a . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PIP_INDEX_URL=http://host.invalid./
# copy necessary exec deps
tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/coverage .tox/py%{python_version_nodots python}/bin/
tox --sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
# copy necessary exec deps
tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/coverage3 .tox/py%{python_version_nodots python3}/bin/coverage
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd
 
%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/zope/interface/tests
%exclude %python_sitelibdir/zope/interface/common/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/zope/interface/tests
%python_sitelibdir/zope/interface/common/tests

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/interface/tests
%exclude %python3_sitelibdir/zope/interface/common/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/interface/tests
%python3_sitelibdir/zope/interface/common/tests

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 4.7.1-alt1
- Build new version 4.7.1.
- Fix license.

* Fri Apr 19 2019 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- Build new version without bootstrap.

* Wed Apr 03 2019 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1.qa1.1
- Bootstrap for python3.7.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 4.3.3 -> 4.5.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.3-alt1
- automated PyPI update

* Tue Mar 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.4
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 22 2016 Denis Medvedev <nbr@altlinux.org> 4.1.3-alt1.dev0.git20150601.3
- Fix deps for python 3.5

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.2
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.3-alt1.dev0.git20150601.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20150601
- New snapshot

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20141227
- Version 4.1.3.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev.git20140319
- Version 4.1.2dev
- Added docs

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Moved all tests into tests subpackage

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Sat Mar 16 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.5-alt1
- Version 4.0.5

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Don't pack zope*egg-info

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Set as archdep package

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Rebuilt with python 2.6

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.2
- Fixed file conflict with python-module-zope

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.1
- Fixed file conflict with python-module-zope (ALT #21981)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3.0-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Mon Nov 20 2006 Ivan Fedorov <ns@altlinux.ru> 3.1.0-alt1.c1
- 3.1.0c1

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 3.0.1-alt1
- Initial build for ALT Linux.
