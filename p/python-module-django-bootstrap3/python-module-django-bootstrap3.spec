%global pypi_name bootstrap3

%def_with python3

Name:           python-module-django-%pypi_name
Version:        8.2.3
Release:        alt2
Summary:        Bootstrap support for Django projects
Group:          Development/Python

License:        Apache
URL:            https://pypi.python.org/pypi/django-bootstrap3
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-django
%if_with python3
BuildRequires:  python3-devel rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-django
%endif

%description
Write Django as usual, and let django-bootstrap3 make template output into Bootstrap 3 code

%if_with python3
%package -n python3-module-django-%pypi_name
Summary:        %summary
Group:          Development/Python

%description -n python3-module-django-%pypi_name
Write Django as usual, and let django-bootstrap3 make template output into Bootstrap 3 code
%endif

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

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-django-%pypi_name
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jun 01 2017 Lenar Shakirov <snejok@altlinux.ru> 8.2.3-alt2
- Pack correct sources

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 8.2.3-alt1
- Initial build for ALT

