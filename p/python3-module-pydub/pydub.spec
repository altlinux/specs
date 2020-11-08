%define  modulename pydub

Name:    python3-module-%modulename
Version: 0.24.1
Release: alt1

Summary: Manipulate audio with a simple and easy high level interface

License: MIT
Group:   Development/Python3
URL:     https://github.com/jiaaro/pydub

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
%doc *.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
