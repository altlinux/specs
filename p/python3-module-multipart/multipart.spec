%define  modulename multipart

Name:    python3-module-%modulename
Version: 0.2.4
Release: alt1

Summary: Multipart parser for Python3
License: MIT
Group:   Development/Python3
URL:     https://github.com/defnull/multipart

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
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/__pycache__/%{modulename}*
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus.
