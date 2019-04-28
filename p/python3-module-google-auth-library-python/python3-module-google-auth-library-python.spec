%define  modulename google-auth-library-python

Name:    python3-module-%modulename
Version: 1.6.3
Release: alt1

Summary: Google Auth Python Library
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/google-auth-library-python

Packager: Anton Midyukov <antohami@altlinux.org>

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
%python3_sitelibdir/*
%doc *.md

%changelog
* Sat Apr 27 2019 Anton Midyukov <antohami@altlinux.org> 1.6.3-alt1
- Initial build for Sisyphus
