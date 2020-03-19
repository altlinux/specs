%define modname flask-restful
%def_disable check

Name: python3-module-%modname
Version: 0.3.8
Release: alt1

Summary: Simple framework for creating REST APIs
License: BSD
Group: Development/Python3

URL: https://github.com/flask-restful/flask-restful
BuildArch: noarch

Source: Flask-RESTful-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-aniso8601 >= 0.82
BuildRequires: python3-module-flask >= 0.8
BuildRequires: python3-module-six >= 1.3.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-pycrypto >= 2.6

%description -n python3-module-%modname
Flask-RESTful provides the building blocks for creating a great REST API.

%prep
%setup -n Flask-RESTful-%version

%build
%python3_build

%install
%python3_install

%files -n python3-module-%modname
%doc AUTHORS.md PKG-INFO LICENSE
%python3_sitelibdir/*

%changelog
* Thu Feb 13 2020 Nikita N. <rav263@altlinux.org> 0.3.8-alt1
- Update to 0.3.8.

* Thu Apr 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.3.7-alt1
- Update to 0.3.7.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus.
