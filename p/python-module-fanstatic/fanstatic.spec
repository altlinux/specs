%define oname fanstatic

%def_with python3

Name: python-module-%oname
Version: 0.16
Release: alt1
Summary: Flexible static resources for web applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/fanstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

%if_with python3
%package -n python3-module-%oname
Summary: Flexible static resources for web applications (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

%package -n python3-module-%oname-tests
Summary: Tests for fanstatic (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains tests for fanstatic.
%endif

%package tests
Summary: Tests for fanstatic
Group: Development/Python
Requires: %name = %version-%release

%description tests
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains tests for fanstatic.

%package docs
Summary: Documentation for fanstatic
Group: Development/Documentation

%description docs
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains documentation for fanstatic.

%package pickles
Summary: Pickles for fanstatic
Group: Development/Python

%description pickles
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains pickles for fanstatic.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export LC_ALL=en_US.UTF-8

%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc html
%make -C doc pickle

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/fanstatic/

%files
%doc *.txt
%python_sitelibdir/*
#exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

#files tests
#python_sitelibdir/*/test*

%files docs
%doc doc/_build/html/*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*
%endif

%changelog
* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1
- Version 0.16
- Added docs and pickles

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.4-alt1
- Version 0.11.4
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3-alt1
- Version 0.11.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.2-alt1.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1
- Initial build for Sisyphus

