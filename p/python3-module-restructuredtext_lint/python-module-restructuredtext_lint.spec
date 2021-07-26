%define  modulename restructuredtext_lint

Name:    python3-module-%modulename
Version: 1.2.1
Release: alt2

Summary: reStructuredText linter
License: Unlicense
Group:   Development/Python3
URL:     https://github.com/twolfson/restructuredtext-lint

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docutils >= 0.11

BuildArch: noarch

Source: %modulename-%version.tar.gz

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt2
- Drop python2 support.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
