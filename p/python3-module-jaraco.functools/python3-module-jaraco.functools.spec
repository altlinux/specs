%define  modulename jaraco.functools

Name:    python3-module-%modulename
Version: 2.0
Release: alt1

Summary: Additional functools in the spirit of stdlib's functools
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.functools

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.20-alt1
- Initial build for Sisyphus
