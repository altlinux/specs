%define  modulename pydata-sphinx-theme

Name:    python3-module-%modulename
Version: 0.6.0
Release: alt1

Summary: Bootstrap-based sphinx theme from the PyData community
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pydata/pydata-sphinx-theme

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pydata_sphinx_theme
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Mon Apr 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.
