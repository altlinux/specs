%define  modulename jaraco.packaging

Name:    python3-module-%modulename
Version: 10.2.2
Release: alt1

Summary: Tools to supplement packaging Python releases
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.packaging

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %modulename} = %EVR

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
rm -rf %buildroot/%_bindir/

%files
%python3_sitelibdir/jaraco/
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Sat Jun 22 2024 Andrey Cherepanov <cas@altlinux.org> 10.2.2-alt1
- New version.

* Mon Apr 22 2024 Andrey Cherepanov <cas@altlinux.org> 10.1.0-alt1
- New version.

* Fri Apr 19 2024 Stanislav Levin <slev@altlinux.org> 9.7.1-alt1.1
- NMU: mapped PyPI name to distro's one.

* Thu Apr 18 2024 Andrey Cherepanov <cas@altlinux.org> 9.7.1-alt1
- New version.

* Mon Apr 01 2024 Andrey Cherepanov <cas@altlinux.org> 9.5.0-alt1
- New version.

* Mon Jul 10 2023 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Thu Jul 06 2023 Andrey Cherepanov <cas@altlinux.org> 9.3.0-alt1
- New version.

* Mon May 15 2023 Andrey Cherepanov <cas@altlinux.org> 9.2.0-alt1
- New version.

* Thu Dec 29 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.2-alt1
- New version.

* Fri Sep 30 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.1-alt1
- New version.

* Wed Sep 28 2022 Andrey Cherepanov <cas@altlinux.org> 9.1.0-alt1
- New version.

* Fri Feb 11 2022 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Mon Mar 15 2021 Andrey Cherepanov <cas@altlinux.org> 8.2.1-alt1
- New version.

* Tue Dec 29 2020 Andrey Cherepanov <cas@altlinux.org> 8.2.0-alt1
- New version.

* Sun Nov 22 2020 Andrey Cherepanov <cas@altlinux.org> 8.1.1-alt1
- New version.

* Tue Feb 18 2020 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.2-alt1
- New version.

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt2
- fix packing

* Sun Jan 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.1-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 6.0-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 5.2-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 5.1-alt1
- Initial build for Sisyphus
