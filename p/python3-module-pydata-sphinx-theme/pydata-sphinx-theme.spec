%define  modulename pydata-sphinx-theme

Name:    python3-module-%modulename
Version: 0.15.3
Release: alt1

Summary: Bootstrap-based sphinx theme from the PyData community

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pydata-sphinx-theme
VCS:     https://github.com/pydata/pydata-sphinx-theme

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx-theme-builder
BuildRequires: python3-module-nodeenv
BuildRequires: yarn webpack npm
BuildRequires: /proc /dev/pts

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

sed -i "s,^\(node-version = \)".*",\1\"$(node --version | sed 's/v//')\"," pyproject.toml

%build
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
python3 -m nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/pydata_sphinx_theme
%python3_sitelibdir/pydata_sphinx_theme-%version.dist-info

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 0.15.3-alt1
- Build new version.

* Mon Apr 22 2024 Grigory Ustinov <grenka@altlinux.org> 0.15.2-alt1
- Build new version.

* Thu Sep 28 2023 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Build new version.

* Sun May 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Automatically updated to 0.8.1.

* Sun May 16 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Automatically updated to 0.6.3.

* Mon Apr 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
