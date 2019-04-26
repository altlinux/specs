%define  oname sphinxcontrib-applehelp

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: A sphinx extension which outputs Apple help books

License: BSD
Group:   Development/Python3
URL:     https://github.com/sphinx-doc/sphinxcontrib-applehelp

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib/*
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info

%changelog
* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
