%define oname pydash
%def_without test

Name: python3-module-%oname
Version: 8.0.6
Release: alt1

Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way

License: MIT License
Group: Development/Python
Url: https://pypi.org/project/pydash/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
kitchen sink of Python utility libraries for doing "stuff" in a functional way.
Based on the Lo-Dash Javascript library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 8.0.6-alt1
- new version 8.0.6
- switch to pyproject build

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt1
- initial build for ALT Sisyphus
