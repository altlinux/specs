%define oname firebase_admin

Name: python3-module-firebase_admin
Version: 6.5.0
Release: alt1

Summary: Firebase Admin Python SDK

Url: https://github.com/firebase/firebase-admin-python
License: Apache-2.0
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

%description
The Firebase Admin Python SDK enables server-side (backend) Python developers to integrate Firebase into their services and applications.

%prep
%setup
%__subst "s|requests.packages.urllib3.util|urllib3.util|" firebase_admin/_http_client.py

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Wed Jun 05 2024 Ivan Mazhukin <vanomj@altlinux.org> 6.5.0-alt1
- initial build for ALT Sisyphus

