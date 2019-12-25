%define  modulename jaraco.functools

Name:    python3-module-%modulename
Version: 3.0.0
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
%exclude %python3_sitelibdir/jaraco/__init__*
%exclude %python3_sitelibdir/jaraco/__pycache__/__init__*

%changelog
* Wed Dec 25 2019 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Sun Oct 06 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt2
- excluded jaraco init against file conflicts with jaraco.packaging

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.20-alt1
- Initial build for Sisyphus
