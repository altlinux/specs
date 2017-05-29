%global pypi_name user_agents

%def_with python3

Name:           python-module-django-%pypi_name
Version:        0.3.0
Release:        alt1
Summary:        A django package that allows easy identification of visitors information
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/django-user_agents
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
A django package that allows easy identification of visitor's browser,
OS and device information, including whether the visitor uses a mobile phone,
tablet or a touch capable device. Under the hood, it uses user-agents.

%if_with python3
%package -n python3-module-django-%pypi_name
Summary:        %summary
Group:          Development/Python
Requires:  python3-module-django
Requires:  python3-module-django-formtools

%description -n python3-module-django-%pypi_name
A django package that allows easy identification of visitor's browser,
OS and device information, including whether the visitor uses a mobile phone,
tablet or a touch capable device. Under the hood, it uses user-agents.
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
%doc README.rst LICENSE.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-django-%pypi_name
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 0.3.0-alt1
- Initial build for ALT


