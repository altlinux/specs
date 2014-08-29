%define module_name django-cache-utils

%def_with python3

Name: python-module-%module_name
Version: 0.7.2
Release: alt2

Summary: Caching decorator and django cache backend with advanced invalidation ability and dog-pile effect prevention

License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/django-cache-utils

Source: %module_name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

%description
django-cache-utils provides some utils for make cache-related work easier

%package -n python3-module-%module_name
Summary: Caching decorator and django cache backend with advanced invalidation ability and dog-pile effect prevention
Group: Development/Python3

%description -n python3-module-%module_name
django-cache-utils provides some utils for make cache-related work easier

%prep
%setup -n %module_name-%version

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

%files
%doc *.rst
%python_sitelibdir/django_cache_utils-*
%python_sitelibdir/cache_utils*

%if_with python3
%files -n python3-module-%module_name
%doc *.rst
%python3_sitelibdir/django_cache_utils-*
%python3_sitelibdir/cache_utils*
%endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2
- Added module forPython 3

* Wed Aug 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- Initial build for ALT Linux
