%define   modulename furo
%def_without docs

Name:     python3-module-%modulename
Version:  2025.12.19
Release:  alt1

Summary:  A clean customizable documentation theme for Sphinx

License:  MIT
Group:    Development/Python3
URL:      https://pypi.org/project/furo
VCS:      https://github.com/pradyunsg/furo

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc /dev/pts
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: yarn node-devel npm python3-module-nodeenv
BuildRequires: python3-module-sphinx-theme-builder

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-sphinx-inline-tabs
BuildRequires: python3-module-sphinx-design
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments
%endif

# sphinx.errors.ThemeError: The 'furo' theme inherits from 'basic-ng'
Requires: python3-module-basic-ng

%description
%summary

%if_with docs
%package doc
Summary: Documentation for %modulename
Group: Development/Documentation

%description doc
This package contains documentation for %modulename.
%endif

%prep
%setup
%patch -p1

node_version=$(node --version|sed -n 's/^v//p')
sed -i "s,^\(node-version = \)".*",\1\"$node_version\"," pyproject.toml

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%if_with docs
%files doc
%doc LICENSE README.md html
%endif

%changelog
* Thu Mar 12 2026 Grigory Ustinov <grenka@altlinux.org> 2025.12.19-alt1
- Automatically updated to 2025.12.19.

* Mon Feb 17 2025 L.A. Kostis <lakostis@altlinux.ru> 2024.08.06-alt1
- 2024.08.06.

* Mon Mar 25 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.01.29-alt1
- 2024.01.29.
- Adopted build process from RH.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 2021.03.20.beta31-alt1
- Initial build for Sisyphus.
