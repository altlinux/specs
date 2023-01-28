%define  modulename rst.linker

Name:    python3-module-%modulename
Version: 2.4.0
Release: alt1

Summary: rst.linker provides a routine for adding links and performing other custom replacements to reStructuredText files as a Sphinx extension
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/rst.linker

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm
BuildRequires: python3-module-toml

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%{summary}.

%prep
%setup -n %modulename-%version
echo 'import setuptools; setuptools.setup()' > setup.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%files
%python3_sitelibdir/rst/*.py
%python3_sitelibdir/rst/__pycache__/*
%python3_sitelibdir/rst.linker*
%python3_sitelibdir/*.egg-info

%changelog
* Sat Jan 28 2023 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Fri Aug 26 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Thu Mar 31 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Sun Mar 14 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Thu Oct 29 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version.

* Sun May 03 2020 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2
- Dropped runtime dependency on importlib_metadata.

* Tue Dec 17 2019 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 1.11-alt2
- Added missing runtime dep.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- New version.

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.10-alt1
- New version.

* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.9-alt1
- Initial build for Sisyphus
