%define oname requestbuilder

Name:    python3-module-requestbuilder
Version: 0.7.1
Release: alt2

Summary: Command line-driven HTTP request builder

License: ISC
Group:   Development/Python3
URL:     https://github.com/boto/requestbuilder

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt2
- build python3 module

* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
