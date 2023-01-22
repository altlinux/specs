%define oname Pallets-Sphinx-Themes

Name: python3-module-pallets-sphinx-themes
Version: 2.0.3
Release: alt1

Summary: Sphinx themes for Pallets and related projects.

License: BSD-3-Clause
Group: Development/Python3
Url: https://www.palletsprojects.com/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
Themes for the Pallets projects. If you're writing an extension, use the
appropriate theme to make your documentation look consistent.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE.rst
%python3_sitelibdir/*

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Build new version.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt3
- build python3 package separately

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- NMU: Fix license.

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
