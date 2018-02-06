%define oname unipath

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.git20150214.2.1
Summary: Object-oriented alternative to os/os.path/shutil
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Unipath/

# https://github.com/mikeorr/Unipath.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Unipath is an object-oriented front end to the file/directory functions
scattered throughout several Python library modules. It's based on Jason
Orendorff's path.py but has a friendlier API and higher-level features.
Unipath is stable, well-tested, and has been used in production since
2008. It runs on Python 2.6+ and 3.3+.

%if_with python3
%package -n python3-module-%oname
Summary: Object-oriented alternative to os/os.path/shutil
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Unipath is an object-oriented front end to the file/directory functions
scattered throughout several Python library modules. It's based on Jason
Orendorff's path.py but has a friendlier API and higher-level features.
Unipath is stable, well-tested, and has been used in production since
2008. It runs on Python 2.6+ and 3.3+.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test -vv test.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv test.py
popd
%endif

%files
%doc CHANGES *.txt *.rst *.html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.txt *.rst *.html
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.git20150214.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt1.git20150214.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150214
- Initial build for Sisyphus

