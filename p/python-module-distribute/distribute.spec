%define oname distribute

%def_with python3

Name: python-module-%oname
Version: 0.6.24
Release: alt2
Summary: Easily download, build, install, upgrade, and uninstall Python packages
License: ZPL
Group: Development/Python
Url: http://packages.python.org/distribute/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel
BuildPreReq: python-module-sphinx-devel

Provides: python-module-setuptools = %version-%release

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

%package tests
Summary: Tests for Distribute
Group: Development/Python
Requires: %name = %version-%release
Provides: python-module-setuptools-tests = %version-%release

%description tests
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

This package contains tests for Distribute.

%package pickles
Summary: Pickles for Distribute
Group: Development/Python
Provides: python-module-setuptools-pickles = %version-%release

%description pickles
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

This package contains pickles for Distribute.

%package docs
Summary: Documentation for Distribute
Group: Development/Documentation
Provides: python-module-setuptools-docs = %version-%release

%description docs
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

This package contains documentation for Distribute.

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary: Easily download, build, install, upgrade, and uninstall Python3 packages
Provides: python3-module-setuptools = %version-%release

%description -n python3-module-%oname
Distribute is intended to replace Setuptools as the standard method for
working with Python3 module distributions.

%package -n python3-module-%oname-tests
Group: Development/Python3
Summary: Easily download, build, install, upgrade, and uninstall Python3 packages
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Distribute is intended to replace Setuptools as the standard method for
working with Python3 module distributions.
This package contains tests for Distribute.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

#pushd docs
#make pickle
#make html
#popd

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

install -d %buildroot%python_sitelibdir/%oname
#cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -f %buildroot%_bindir/easy_install
ln -s easy_install-%__python_version %buildroot%_bindir/easy_install
%if_with python3
ln -s easy_install-%__python3_version %buildroot%_bindir/easy_install3
%endif

%files
%doc *.txt
%_bindir/easy_install
%_bindir/easy_install-%__python_version
%python_sitelibdir/*
%exclude %python_sitelibdir/setuptools/tests
#exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/setuptools/tests

%files docs
#doc docs/build/html
%doc docs/*.txt

#files pickles
#python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%_bindir/easy_install3
%_bindir/easy_install-%__python3_version
%python3_sitelibdir/setuptools
%python3_sitelibdir/*.py
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/__pycache__/*.pyo
%python3_sitelibdir/__pycache__/*.pyc
%exclude %python3_sitelibdir/setuptools/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/setuptools/tests
%endif

%changelog
* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.24-alt2
- Build with python3 support

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.24-alt1
- Version 0.6.24

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.19-alt3
- Built with sphinx

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.19-alt2
- Bootstraping with Python-2.7 withon sphinx

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.19-alt1
- Version 0.6.19

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.16-alt3
- Set provides of setuptools

* Wed May 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.16-alt2
- Added explicit conflict with python-module-setuptools-tests

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.16-alt1
- Initial build for Sisyphus

