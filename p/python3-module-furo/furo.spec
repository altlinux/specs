%define modulename furo

Name:     python3-module-%modulename
Version:  2024.01.29
Release:  alt1

Summary:  A clean customizable documentation theme for Sphinx
License:  MIT
Group:    Development/Python3
Url:      https://github.com/pradyunsg/furo

Packager: Grigory Ustinov <grenka@altlinux.org>

Source0:   %name-%version.tar
Source1:   %name-vendor.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc /dev/pts
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: yarn node-devel npm python3-module-nodeenv
BuildRequires: python3-module-sphinx-theme-builder

%description
%summary

%prep
%setup -a1

node_version=$(node --version|sed -n 's/^v//p')
sed -i "s,^\(node-version = \)".*",\1\"$node_version\"," pyproject.toml

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/vendor"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_build

%install
%pyproject_install

# this step requires tons of modules were some are not even built for ALT
#PYTHONPATH=%buildroot%python3_sitelibdir sphinx-build-3 -b html docs html
#rm -rf html/{.buildinfo,.doctrees}

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.dist-info
%doc *.md

%changelog
* Mon Mar 25 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.01.29-alt1
- 2024.01.29.
- Adopted build process from RH.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 2021.03.20.beta31-alt1
- Initial build for Sisyphus.
