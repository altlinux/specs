%def_without bootstrap
%def_with check

%define oname flask-authlib-client

Name: python3-module-flask-authlib-client
Version: 1.0
Release: alt2

Summary: Flask-Authlib-Client is a Flask extension
License: GPL-3
Group: Development/Python3
URL: https://pypi.org/project/Flask-Authlib-Client/
VCS: https://github.com/michaelbukachi/flask-authlib-client

Source: %name-%version.tar
Patch1: fix_time_def.patch

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-build
BuildRequires: python3-module-installer

%description
Flask-Authlib-Client is a Flask extension that adds support for separate 
authorization/resource servers.

%prep
%setup
%autopatch -p1

%build
export LC_ALL=en_US.UTF-8
%pyproject_build

%install
%pyproject_install

# Для отладки (можно убрать после проверки)
echo "=== Installed files ==="
find %buildroot%_prefix/lib/python3/site-packages/ -name "flask_authlib_client*" -ls

%check
export LC_ALL=en_US.UTF-8
# Здесь можно добавить тесты, если они есть
# %{python3} -m pytest

%files
%python3_sitelibdir/flask_authlib_client/
%python3_sitelibdir/flask_authlib_client-*.dist-info/

%changelog
* Mon Jun 15 2026 Pavel Vasenkov <pav@altlinux.org> 1.0-alt2
- Fix time definition (Closes: #59504)

* Sat Feb 21 2026 Pavel Vasenkov <pav@altlinux.org> 1.0-alt1
- New build for sisyphus
