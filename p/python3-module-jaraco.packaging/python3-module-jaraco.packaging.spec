%define  modulename jaraco.packaging

Name:    python3-module-%modulename
Version: 6.0
Release: alt1

Summary: Tools to supplement packaging Python releases
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.packaging

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
%python3_sitelibdir/jaraco/
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 6.0-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 5.2-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 5.1-alt1
- Initial build for Sisyphus
