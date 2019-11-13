%define  modulename doc8

Name:    python3-module-%modulename
Version: 0.8.0
Release: alt2

Summary: Style checker for sphinx (or other) rst documentation.
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/openstack/doc8
BuildArch: noarch

Source:  %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-chardet
BuildRequires: python3-module-docutils
BuildRequires: python3-module-restructuredtext_lint >= 0.7
BuildRequires: python3-module-six
BuildRequires: python3-module-stevedore

%description
Doc8 is an opinionated style checker for rst_ (with basic support for
plain text) styles of documentation.

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
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt2
- Build without python2.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
