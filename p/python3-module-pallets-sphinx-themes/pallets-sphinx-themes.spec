%define oname Pallets-Sphinx-Themes

Name: python3-module-pallets-sphinx-themes
Version: 1.1.3
Release: alt3

Summary: Sphinx themes for Pallets and related projects.

License: BSD-3-Clause
Group: Development/Python3
Url: https://www.palletsprojects.com/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
#BuildRequires: python3-devel

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
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt3
- build python3 package separately

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- NMU: Fix license.

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
