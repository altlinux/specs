%define version 0.0.0
%define release alt2.svn1916.2
%setup_python_module django-pantheon

%def_with python3

Name: %packagename
Version: %version
Release: alt2.svn1916.2.1

Summary: Pantheon django modules

License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://webnewage.org/projects/p/django-pantheon
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Pantheon django modules

%package -n python3-module-%modulename
Summary: Pantheon django modules
Group: Development/Python3

%description -n python3-module-%modulename
Pantheon django modules

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.0-alt2.svn1916.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt2.svn1916.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.0-alt2.svn1916.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt2.svn1916.1
- Rebuilt with python 2.6

* Sat Feb 14 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt2.svn1916
- critical fix wrong call invalidate function

* Fri Feb 13 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.svn1916
- Initial build for ALT Linux

