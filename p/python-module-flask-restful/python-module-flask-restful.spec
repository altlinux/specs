%define modname flask-restful
%def_disable check

Name: python-module-%modname
Version: 0.3.6
Release: alt1

Summary: Simple framework for creating REST APIs
License: BSD
Group: Development/Python

URL: https://github.com/flask-restful/flask-restful
BuildArch: noarch

Source: Flask-RESTful-%version.tar.gz

BuildRequires: python-module-setuptools
BuildRequires: python-module-aniso8601 >= 0.82
BuildRequires: python-module-flask >= 0.8
BuildRequires: python-module-six >= 1.3.0
BuildRequires: python-module-pytz
BuildRequires: python-module-pycrypto >= 2.6

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-aniso8601 >= 0.82
BuildRequires: python3-module-flask >= 0.8
BuildRequires: python3-module-six >= 1.3.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-pycrypto >= 2.6


%description
Flask-RESTful provides the building blocks for creating a great REST API.

%package -n python3-module-%modname
Summary: Simple framework for creating REST APIs
Group: Development/Python3

%description -n python3-module-%modname
Flask-RESTful provides the building blocks for creating a great REST API.

%prep
%setup -n Flask-RESTful-%version

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
%doc AUTHORS.md PKG-INFO LICENSE
%python_sitelibdir/*

%files -n python3-module-%modname
%doc AUTHORS.md PKG-INFO LICENSE
%python3_sitelibdir/*

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus.
