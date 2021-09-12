%define oname gevent-ws

Name: python3-module-gevent-ws
Version: 2.1.0
Release: alt1

Summary: Websocket server for gevent.pywsgi

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/gevent-ws/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
A fast, MIT-licensed alternative to the abandoned non-free (as in freedom) gevent-websocket.

Why?
It's MIT-licensed, so it can be included to almost all software (both open-source and closed-source)
without any licensing issues, as opposed to gevent-websocket. And it's several times faster!


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus
