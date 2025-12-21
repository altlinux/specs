%define pypi_name flask-sock
%define modname flask_sock

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: WebSocket support for Flask

License: MIT
Group: Development/Python3
Url: https://github.com/miguelgrinberg/flask-sock

# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: python3-module-flask
Requires: python3-module-simple-websocket

%description
WebSocket support for Flask.

This package provides WebSocket support for Flask applications without
requiring a greenlet-based server (gevent, eventlet) to work.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{modname}-%version.dist-info/

%changelog
* Sun Dec 21 2025 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- initial build for ALT Sisyphus
