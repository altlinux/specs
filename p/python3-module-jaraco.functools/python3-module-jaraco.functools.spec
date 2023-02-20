%define  modulename jaraco.functools

Name:    python3-module-%modulename
Version: 3.6.0
Release: alt1

Summary: Additional functools in the spirit of stdlib's functools
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.functools

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-pyproject-installer
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

# According to PEP 420 module can import without __init__.py, but autoprov does not support this behaviour.
# See https://bugzilla.altlinux.org/show_bug.cgi?id=39556
%py3_provides jaraco.functools

%description
%summary

%prep
%setup -n %modulename-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/%{modulename}*

%changelog
* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Tue Sep 27 2022 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- New version.

* Wed Jul 20 2022 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt2
- Built and installed by pyproject_* macros.

* Fri Jul 15 2022 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version.

* Mon Dec 20 2021 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Mon Nov 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Sat Mar 27 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Mon Feb 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.

* Sun Jan 17 2021 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Tue Dec 29 2020 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Wed Dec 25 2019 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Sun Oct 06 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt2
- excluded jaraco init against file conflicts with jaraco.packaging

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.20-alt1
- Initial build for Sisyphus
