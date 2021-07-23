%global pypi_name user_agents

Name:           python3-module-%pypi_name
Version:        1.1.0
Release:        alt2
Summary:        A library to identify devices by parsing user agent strings
Group:          Development/Python3

License:        MIT
URL:            https://pypi.python.org/pypi/user-agents
Source0:        %pypi_name-%version.tar

BuildArch:      noarch

BuildRequires:  rpm-build-python3

%description
A library to identify devices (phones, tablets) and their capabilities
by parsing (browser/HTTP) user agent strings

%prep
%setup -n %pypi_name-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

