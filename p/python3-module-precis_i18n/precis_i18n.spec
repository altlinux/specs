%define _unpackaged_files_terminate_build 1
%define pypi_name precis-i18n
%define mod_name precis_i18n

Name:    python3-module-%mod_name
Version: 1.1.0
Release: alt2

Summary: Python3 implementation of PRECIS framework (RFC 8264, RFC 8265, RFC 8266)

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/precis-i18n
VCS:     https://github.com/byllyfish/precis_i18n

Source:  %name-%version.tar
# https://github.com/byllyfish/precis_i18n/pull/39
Patch0: precis_i18n-1.1.0-setup.py-remove-test_suite-as-setuptools-72-dropped.patch

Packager: Grigory Ustinov <grenka@altlinux.org>
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
If you want your application to accept unicode user names and passwords,
you must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform unicode strings into a canonical form,
suitable for comparison.

This module implements the PRECIS Framework as described in:

- PRECIS Framework: Preparation, Enforcement, and Comparison of
Internationalized Strings in Application Protocols (RFC 8264)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Usernames and Passwords (RFC 8265)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Nicknames (RFC 8266)

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc LICENSE.txt *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Migrated from removed setuptools' test command (see #50996).

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Sat Jan 07 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Automatically updated to 1.0.5.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt1
- Automatically updated to 1.0.4.
- Build with check.

* Wed Mar 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Automatically updated to 1.0.3.

* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Automatically updated to 1.0.2.

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Build new version.

* Thu Jun 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus (Closes: #36707).
