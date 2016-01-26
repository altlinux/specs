
%def_with python3

Summary: pip installs packages.  Python packages.  An easy_install replacement
Name: python-module-pip
Version: 8.0.2
Release: alt1
Source0: pip-%version.tar.gz
Patch: pip-1.5.6-alt-python3.patch
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://www.pip-installer.org
%setup_python_module pip

BuildRequires: python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
%endif

%description
%summary

%package pickles
Summary: Pickles for pip
Group: Development/Python

%description pickles
%summary

This package contains pickles for pip.

%package docs
Summary: Documentation for pip
Group: Development/Documentation

%description docs
%summary

This package contains documentation for pip.

%package -n python3-module-%modulename
Summary: pip installs packages.  Python packages.  An easy_install replacement
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%if 0
pushd ../python3
%patch -p2
popd
%endif
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%modulename/

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/pip3*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%modulename
%doc *.txt *.rst
%_bindir/pip3*
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 8.0.2-alt1
- Autobuild version bump to 8.0.2

* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 7.1.2-alt2
- New build scheme

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.2-alt1
- Version 7.1.2

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.0-alt1
- Version 7.1.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.6-alt1
- Version 6.0.6

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.3-alt1
- Version 6.0.3

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1
- Version 6.0.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt1
- Version 1.5.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- new version
- spec fixes

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt1
- initial build for ALTLinux
