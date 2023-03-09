%define oname Flask-RESTful
%def_disable check

Name: python3-module-flask-restful
Version: 0.3.9
Release: alt1

Summary: Simple framework for creating REST APIs

License: BSD
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-aniso8601 >= 0.82
BuildRequires: python3-module-flask >= 0.8
BuildRequires: python3-module-six >= 1.3.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-pycrypto >= 2.6

%description
Flask-RESTful provides the building blocks for creating a great REST API.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc AUTHORS.md PKG-INFO LICENSE
%python3_sitelibdir/*

%changelog
* Thu Mar 09 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.9-alt1
- Build new version.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt2
- NMU: cleanup spec, disable tests packing

* Thu Feb 13 2020 Nikita N. <rav263@altlinux.org> 0.3.8-alt1
- Update to 0.3.8.

* Thu Apr 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.3.7-alt1
- Update to 0.3.7.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus.
