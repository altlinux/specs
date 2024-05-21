%define _unpackaged_files_terminate_build 1
%define pypi_name QtAwesome
%define mod_name qtawesome

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: Iconic fonts in PyQt and PySide applications
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/QtAwesome/
Vcs: https://github.com/spyder-ide/qtawesome

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: xvfb-run
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-qt
BuildRequires: python3-module-pyqt5
%endif

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive Icons in PyQt
and PySide applications.

It started as a Python port of the QtAwesome C++ library by Rick Blommers.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- xvfb-run -- python3 example.py
%pyproject_run -- xvfb-run -- pytest -vra

%files
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/qta-browser
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue May 21 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.
- Built from upstream VCS.
- Mapped PyPI name to distro's one.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.3-alt2
- (NMU) Provided PEP503-normalized project name.

* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)

* Thu Jul 30 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.2-alt1
- new version (0.7.2)

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version (0.6.1) with rpmgs script

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1
- initial build for ALT Sisyphus (python3 version)
