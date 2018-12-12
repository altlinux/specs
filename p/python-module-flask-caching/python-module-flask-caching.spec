%define modname flask-caching
%def_disable check

Name: python-module-%modname
Version: 1.4.0
Release: alt1

Summary: Cache support for Flask.
License: BSD
Group: Development/Python

URL: https://github.com/sh4nks/flask-caching
BuildArch: noarch

Source: Flask-Caching-%version.tar.gz

BuildRequires: python-module-setuptools
BuildRequires: python-module-flask
BuildRequires: python-module-werkzeug
BuildRequires: python-module-sphinx
BuildRequires: python-module-pytest
BuildRequires: python-module-redis-py


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-flask
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest
BuildRequires: python3-module-redis-py

%description
Adds easy cache support to Flask.

This is a fork of the Flask-Cache extension.

%package -n python3-module-%modname
Summary: Cache support for Flask.
Group: Development/Python3

%description -n python3-module-%modname
Adds easy cache support to Flask.

This is a fork of the Flask-Cache extension.

%prep
%setup -n Flask-Caching-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd


%files
%doc README.md PKG-INFO LICENSE
%python_sitelibdir/*

%files -n python3-module-%modname
%doc README.md PKG-INFO LICENSE
%python3_sitelibdir/*

%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
