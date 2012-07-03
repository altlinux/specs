%define oname logilab-constraint

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.hg20120329
Summary: A constraint satisfaction problem solver written in 100%% pure Python

Group: Development/Python
License: GPL
URL: http://www.logilab.org/852/
# hg clone http://hg.logilab.org/logilab/constraint
Source: constraint-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-module-logilab-common
buildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-logilab-common python-tools-2to3
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
for i in $(find ./ -name '*.py'); do
	if [ "$i" != "./setup.py" ]; then
		2to3 -w -n $i
	fi
done
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

