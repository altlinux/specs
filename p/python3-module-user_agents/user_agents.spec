%global pypi_name user_agents

Name:           python3-module-%pypi_name
Version:        2.2.0
Release:        alt1

Summary:        A library to identify devices by parsing user agent strings

Group:          Development/Python3
License:        MIT
URL:            https://pypi.python.org/pypi/user-agents

Source:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  rpm-build-python3

%description
A library to identify devices (phones, tablets) and their capabilities
by parsing (browser/HTTP) user agent strings

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.md *.txt
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info

%changelog
* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- Initial build for ALT
