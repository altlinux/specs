%define oname pydash
%def_without test

Name: python3-module-%oname
Version: 5.1.0
Release: alt1

Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way

License: MIT License
Group: Development/Python
Url: https://pypi.org/project/pydash/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.5

%py3_buildrequires pytest

%description
kitchen sink of Python utility libraries for doing "stuff" in a functional way.
Based on the Lo-Dash Javascript library.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%if_with test
%check
PYTHONPATH=%buildroot%python3_sitelibdir/%oname/ pytest3
%endif

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info

%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt1
- initial build for ALT Sisyphus
