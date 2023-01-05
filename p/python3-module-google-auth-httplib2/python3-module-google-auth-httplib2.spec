%define  modulename google-auth-httplib2

Name:    python3-module-%modulename
Version: 0.1.0
Release: alt1

Summary: This library provides an httplib2 transport for google-auth
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/google-auth-library-python-httplib2

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

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
%python3_sitelibdir/*

%changelog
* Thu Jan 05 2023 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
