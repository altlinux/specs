%global pypi_name jsonrpclib
%define version 0.1.3

Name:           python-module-%{pypi_name}
Version:        %{version}
Release:        alt1
Group:          Development/Python
Summary:        This project is an implementation of the JSON-RPC v2.0 specification

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        %{name}-%{version}.tar

BuildArch:      noarch

BuildRequires:  python-module-setuptools

%description
This project is an implementation of the JSON-RPC v2.0 specification

%prep
%setup

%build
%python_build

%install
%python_install

%files
%{python_sitelibdir}/%{pypi_name}*

%changelog
* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.3-alt1
- First build for ALT (based on Mageia 0.1.3-3.mga4.src)

