%define module_name django-country-dialcode

%def_with python3

Name: python-module-%module_name
Version: 0.5.1
Release: alt1.git20140716
Summary: Application providing Dialcode and Countries code
License: MIT
Group: Development/Python
Url: https://github.com/Star2Billing/django-country-dialcode

# https://github.com/Star2Billing/django-country-dialcode.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name

%description
Application providing Dialcode and Countries code

%package -n python3-module-%module_name
Summary: Application providing Dialcode and Countries code
Group: Development/Python3

%description -n python3-module-%module_name
Application providing Dialcode and Countries code

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
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
%make -C docs html

%files
%doc HACKING README.rst MIT-LICENSE.txt docs/build/html
%python_sitelibdir/country_dialcode*
%python_sitelibdir/django_country_dialcode*

%if_with python3
%files -n python3-module-%module_name
%doc HACKING README.rst MIT-LICENSE.txt docs/build/html
%python3_sitelibdir/country_dialcode*
%python3_sitelibdir/django_country_dialcode*
%endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20140716
- Version 0.5.1
- Added module for Python 3

* Sat May 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux
