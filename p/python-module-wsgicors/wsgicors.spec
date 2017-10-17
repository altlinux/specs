%define oname wsgicors

%def_with python3

Name:           python-module-%oname
Version:        0.7.0
Release:        alt1
Summary:        WSGI for Cross Origin Resource Sharing (CORS)
Group:          Development/Python
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/wsgicors
BuildArch:      noarch

# https://github.com/may-day/wsgicors.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(backports.functools_lru_cache)
BuildRequires: python2.7(nose) python2.7(webob) python-module-nose-testconfig
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(nose) python3(webob) python3-module-nose-testconfig
%endif

%py_requires backports.functools_lru_cache

%description
This is a WSGI middleware that answers CORS preflight requests and adds the needed header to the response.

For CORS see: http://www.w3.org/TR/cors/

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        WSGI for Cross Origin Resource Sharing (CORS)

%description -n python3-module-%oname
This is a WSGI middleware that answers CORS preflight requests and adds the needed header to the response.

For CORS see: http://www.w3.org/TR/cors/
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

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

%check
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

python setup.py test

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
