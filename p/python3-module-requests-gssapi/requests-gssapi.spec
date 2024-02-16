%define _unpackaged_files_terminate_build 1

%define pypi_name requests-gssapi
%define mod_name requests_gssapi

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1
Summary: A GSSAPI/SPNEGO authentication handler for python-requests
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/requests-gssapi
Vcs: https://github.com/pythongssapi/requests-gssapi
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# PyPI name
%py3_provides requests-gssapi
Provides: python3-module-requests_gssapi = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
Requests is an HTTP library, written in Python, for human beings.
This library adds optional GSSAPI authentication support and
supports mutual authentication.

It provides a fully backward-compatible shim for the old
python-requests-kerberos library. A more powerful interface is
provided by the HTTPSPNEGOAuth component, but this is of course not
guaranteed to be compatible.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc AUTHORS LICENSE *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 16 2024 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.3 -> 1.3.0.

* Sat Jan 27 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1.1
- NMU: moved on modern pyproject macros.

* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.2.1 -> 1.2.3.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- removed python-2.7 support

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1.

* Mon Jul 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fix regex string escaping

* Fri May 04 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build
