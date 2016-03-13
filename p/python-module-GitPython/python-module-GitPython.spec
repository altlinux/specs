%define module_name GitPython

%def_with python3

Name: python-module-GitPython
Version: 0.3.6
Release: alt1.1

Summary: GitPython is a python library used to interact with Git repositories

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

# https://github.com/gitpython-developers/GitPython.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

BuildRequires: python-module-setuptools-tests python-module-GitDB
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildRequires: python3-module-setuptools-tests python3-module-gitdb
%endif

%description
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%package -n python3-module-%module_name
Summary: GitPython is a python library used to interact with Git repositories
Group: Development/Python3

%description -n python3-module-%module_name
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/git/test

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/git/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1rc1.2
- Fixed build

* Mon Jul 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1rc1.1
- merge upstream/master

* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt0rc1.1
- 0.3.2-rc1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4.1-alt1.1
- Rebuilt with python 2.6

* Fri Nov 28 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.1.4.1-alt1
- Initial build for ALTLinux Sisyphus

