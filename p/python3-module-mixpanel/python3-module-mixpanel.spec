%define pypi_name mixpanel

Name: python3-module-mixpanel
Version: 5.1.0
Release: alt1

Summary: Official Mixpanel library for Python

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/mixpanel/mixpanel-python

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel


%description
Mixpanel client libraries allow for tracking events and setting properties
on People Analytics profiles from your server-side projects.

This is the official Mixpanel client library for Python. It provides the
primary Mixpanel class for tracking events and sending People Analytics
updates, along with Consumer and BufferedConsumer classes that allow
callers to customize the IO characteristics of their tracking.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# Drop tests bundled inside the package (they pull pytest, respx as runtime deps)
rm -rv %buildroot%python3_sitelibdir/%pypi_name/flags/test_*.py

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- initial build for ALT Sisyphus

