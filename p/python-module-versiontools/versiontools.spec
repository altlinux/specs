%define oname versiontools

%def_with python3

Name: python-module-%oname
Version: 1.9.1
Release: alt1
Summary: Smart replacement for plain tuple used in __version__
License: LGPL
Group: Development/Python
Url: http://pypi.python.org/pypi/versiontools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
Smart replacement for plain tuple used in __version__.

%if_with python3
%package -n python3-module-%oname
Summary: Smart replacement for plain tuple used in __version__ (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Smart replacement for plain tuple used in __version__.

%package -n python3-module-%oname-tests
Summary: Tests for versiontools (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Smart replacement for plain tuple used in __version__.

This package contains tests for versiontools.
%endif

%package tests
Summary: Tests for versiontools
Group: Development/Python
Requires: %name = %version-%release

%description tests
Smart replacement for plain tuple used in __version__.

This package contains tests for versiontools.

%package pickles
Summary: Pickles for versiontools
Group: Development/Python

%description pickles
Smart replacement for plain tuple used in __version__.

This package contains pickles for versiontools.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/
mkdir doc/pickle
for i in environment searchindex globalcontext; do
	cp -f %python_sitelibdir_noarch/sphinx/pickle/$i.pickle doc/pickle/
done

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

cp -f doc/conf.py ./
%generate_pickles $PWD $PWD/doc %oname
sphinx-build -E -a -b html -c $PWD -d doctrees doc html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR pickle %buildroot%python_sitelibdir/%oname/

%files
%doc html/*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests.py*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/tests.py*

%if_with python3
%files -n python3-module-%oname
%doc html/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests.py*
%exclude %python3_sitelibdir/%oname/__pycache__/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests.py*
%python3_sitelibdir/%oname/__pycache__/tests.*
%endif

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

