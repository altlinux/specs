%global pypi_name user_agents

%def_with python3

Name:           python-module-%pypi_name
Version:        1.1.0
Release:        alt1
Summary:        A library to identify devices by parsing user agent strings
Group:          Development/Python

License:        MIT
URL:            https://pypi.python.org/pypi/user-agents
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
%if_with python3
BuildRequires:  python3-devel rpm-build-python3
BuildRequires:  python3-module-setuptools
%endif

%description
A library to identify devices (phones, tablets) and their capabilities
by parsing (browser/HTTP) user agent strings

%if_with python3
%package -n python3-module-%pypi_name
Summary:        %summary
Group:          Development/Python

%description -n python3-module-%pypi_name
A library to identify devices (phones, tablets) and their capabilities
by parsing (browser/HTTP) user agent strings
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
%files -n python3-module-%pypi_name
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

