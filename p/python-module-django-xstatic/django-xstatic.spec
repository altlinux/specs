%define oname django-xstatic

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20140324.1
Summary: Django helpers to use XStatic packages in Django projects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-xstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Gautier/django-xstatic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django python-tools-2to3
%endif

%py_provides django_xstatic
%py_requires django

%description
Use XStatic packages and Django StaticFiles to manage your static files
like jQuery.

%package -n python3-module-%oname
Summary: Django helpers to use XStatic packages in Django projects
Group: Development/Python3
%py3_provides django_xstatic
%py3_requires django

%description -n python3-module-%oname
Use XStatic packages and Django StaticFiles to manage your static files
like jQuery.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20140324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20140324
- Initial build for Sisyphus

