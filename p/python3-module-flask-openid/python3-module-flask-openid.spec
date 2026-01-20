%define _unpackaged_files_terminate_build 1
%define pypi_nname flask-openid
%define pypi_name Flask-OpenID
%define mod_name flask_openid

Name: python3-module-%pypi_nname
Version: 1.3.1
Release: alt1
Summary: Flask extension for OpenID authentication
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/Flask-OpenID/
Vcs: https://github.com/pallets-eco/flask-openid
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch 

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Flask-OpenID is an extension to Flask that allows you to easily add OpenID
based authentication to your website.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 20 2026 Alexey Rodygin <alehandro@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
