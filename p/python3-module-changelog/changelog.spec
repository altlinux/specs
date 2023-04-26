%define  modulename changelog

Name:    python3-module-%modulename
Version: 0.6.0
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
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info
%doc *.rst

%changelog
* Wed Apr 26 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.8-alt1
- Automatically updated to 0.5.8.

* Tue Apr 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Initial build for Sisyphus.
