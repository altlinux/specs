%define oname logilab-constraint

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt2.hg20130911.1.1
Summary: A constraint satisfaction problem solver written in 100%% pure Python

Group: Development/Python
License: GPL
URL: http://www.logilab.org/852/
# hg clone http://hg.logilab.org/review/logilab/constraint
Source: constraint-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#BuildPreReq: python-devel python-module-logilab-common
#buildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-egenix-mx-base python-module-kerberos python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-logilab-common python3-module-logilab-common rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-logilab-common python-tools-2to3
%endif

%description
The constraint package is a constraint satisfaction problem solver
written in 100%% pure Python. The implementation uses constraint
propagation algorithms. Constraints and Domain implementations are
provided to work with finite domains and finite intervals. It should be
fairly easy to add new kind of domains such as finite integer domains,
together with specialized constraints.

%if_with python3
%package -n python3-module-%oname
Summary: A constraint satisfaction problem solver written in 100%% pure Python 3
Group: Development/Python3

%description -n python3-module-%oname
The constraint package is a constraint satisfaction problem solver
written in 100%% pure Python. The implementation uses constraint
propagation algorithms. Constraints and Domain implementations are
provided to work with finite domains and finite intervals. It should be
fairly easy to add new kind of domains such as finite integer domains,
together with specialized constraints.

%package -n python3-module-%oname-tests
Summary: Tests for logilab constraint package (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The constraint package is a constraint satisfaction problem solver
written in 100%% pure Python. The implementation uses constraint
propagation algorithms. Constraints and Domain implementations are
provided to work with finite domains and finite intervals. It should be
fairly easy to add new kind of domains such as finite integer domains,
together with specialized constraints.

This package contains tests for logilab constraint package.
%endif

%package tests
Summary: Tests for logilab constraint package
Group: Development/Python
Requires: %name = %version-%release

%description tests
The constraint package is a constraint satisfaction problem solver
written in 100%% pure Python. The implementation uses constraint
propagation algorithms. Constraints and Domain implementations are
provided to work with finite domains and finite intervals. It should be
fairly easy to add new kind of domains such as finite integer domains,
together with specialized constraints.

This package contains tests for logilab constraint package.

%prep
%setup
touch test/__init__.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
touch ../python3/test/__init__.py
%endif

%build
%python_build
%if_with python3
pushd ../python3
cp setup.py setup.py.bak
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv -f setup.py.bak setup.py
sed -i "s|print.*|print(src, '->', dest, file=sys.stderr)|" setup.py
%python3_build
popd
%endif

%install
%python_install
rm -f %buildroot%python_sitelibdir/logilab/__init__.py*
%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*
%endif

%files
%doc COPYING ChangeLog README doc/* examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test

%files tests
%python_sitelibdir/*/*/test

%if_with python3
%files -n python3-module-%oname
%doc COPYING ChangeLog README doc/* examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.hg20130911.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.hg20130911.1
- NMU: Use buildreq for BR.

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.hg20130911
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.hg20120329
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.0-alt1.hg20120329.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.hg20120329
- Version 0.5.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt3.1
- Rebuild with Python-2.7

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Extracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Rebuilt with python 2.6

* Fri Oct 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

