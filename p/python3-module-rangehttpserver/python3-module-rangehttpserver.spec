%define oname RangeHTTPServer
%define pypi_name rangehttpserver

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: SimpleHTTPServer with support for Range requests
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/danvk/RangeHTTPServer

# Source-url: https://github.com/danvk/%oname.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
SimpleHTTPServer with support for HTTP Range requests, useful for
serving static content (such as video files) that benefit from
seekable HTTP responses.

Run with: python3 -m RangeHTTPServer

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu Apr 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Sisyphus
