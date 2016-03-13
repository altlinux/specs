%define module_name django-pagination

%def_with python3

Name: python-module-%module_name
Version: 1.0.7
Release: alt2.1

Summary: django-pagination allows for easy Digg-style pagination without modifying your views

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-pagination

Source: %module_name-%version.tar.gz

BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name

%description
django-pagination allows for easy Digg-style pagination without
modifying your views.

%package -n python3-module-%module_name
Summary: django-pagination allows for easy Digg-style pagination without modifying your views
Group: Development/Python3

%description -n python3-module-%module_name
django-pagination allows for easy Digg-style pagination without
modifying your views.

%prep
%setup -n %module_name-%version
find  -type f -name '._*' -exec rm -f '{}' +

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/django_pagination-*
%python_sitelibdir/pagination*

%if_with python3
%files -n python3-module-%module_name
%doc *.txt docs/*
%python3_sitelibdir/django_pagination-*
%python3_sitelibdir/pagination*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.7-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2
- Added module for Python 3

* Fri Apr 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- Initial build for ALT Linux
