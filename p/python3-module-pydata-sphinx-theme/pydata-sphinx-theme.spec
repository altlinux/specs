%define  modulename pydata-sphinx-theme

Name:    python3-module-%modulename
Version: 0.8.1
Release: alt1

Summary: Bootstrap-based sphinx theme from the PyData community

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pydata/pydata-sphinx-theme

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pydata_sphinx_theme
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sun May 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Automatically updated to 0.8.1.

* Sun May 16 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Automatically updated to 0.6.3.

* Mon Apr 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
