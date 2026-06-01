%def_without bootstrap
%def_with check

%define oname libgravatar

Name: python3-module-libgravatar
Version: 1.0.4
Release: alt1

Summary: A library that provides a Python 3 interface for the Gravatar API
License: GPL-3
Group: Development/Python3
URL: https://pypi.org/project/libgravatar/
VCS: https://github.com/pabluk/libgravatar

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-build
BuildRequires: python3-module-installer

%description
A library that provides a Python 3 interface for the Gravatar API.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%pyproject_build

%install
%pyproject_install

%check
export LC_ALL=en_US.UTF-8

%files
%_usr/lib/python3/site-packages/libgravatar/
%_usr/lib/python3/site-packages/libgravatar-%version.dist-info/


%changelog
* Sat Feb 21 2026 Pavel Vasenkov <pav@altlinux.org> 1.0.4-alt1
- New build for sisyphus

