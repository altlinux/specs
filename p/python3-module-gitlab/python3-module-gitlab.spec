%define _unpackaged_files_terminate_build 1
%define module_name gitlab

Name: python3-module-%module_name
Version: 3.6.0
Release: alt1
Summary: A python wrapper for the GitLab API
License: LGPL-3.0
Group: Development/Python3
Url: https://github.com/python-gitlab/python-gitlab
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Python package providing access to the GitLab server API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%module_name
%python3_sitelibdir/%module_name
%python3_sitelibdir/python_%module_name-%version.dist-info
%doc COPYING

%changelog
* Tue Jul 26 2022 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.0-alt1
- Initial build for ALT
