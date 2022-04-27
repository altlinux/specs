%define  modulename changelog

Name:    python3-module-%modulename
Version: 0.5.7
Release: alt1

Summary: A Sphinx extension to generate changelog files

License: MIT
Group:   Development/Python3
URL:     https://github.com/sqlalchemyorg/changelog

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Apr 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Initial build for Sisyphus.
