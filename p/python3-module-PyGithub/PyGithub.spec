%define  modulename PyGithub

Name:    python3-module-%modulename
Version: 1.55
Release: alt1

Summary: Typed interactions with the GitHub API v3
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/PyGithub/PyGithub

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
PyGitHub is a Python library to access the GitHub REST API. This library enables
you to manage GitHub resources such as repositories, user profiles,
and organizations in your Python applications.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/github/*
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.55-alt1
- Initial build for Sisyphus.
