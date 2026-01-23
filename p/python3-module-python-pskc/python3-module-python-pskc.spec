%define _unpackaged_files_terminate_build 1
%define pypi_name python-pskc
%define mod_name pskc

%def_with check

Name: python3-module-%pypi_name
Version: 1.4
Release: alt1

Summary: Python module for handling PSKC files
License: LGPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/python-pskc/
Vcs: https://github.com/arthurdejong/python-pskc

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra defuse
%pyproject_builddeps_metadata_extra lxml
%pyproject_builddeps_metadata_extra signature
%pyproject_builddeps_check
%endif

%description
A Python module to handle Portable Symmetric Key Container (PSKC) files
as defined in `RFC 6030 <https://tools.ietf.org/html/rfc6030>`_. PSKC
files are used to transport and provision symmetric keys and key meta
data (seed files) to different types of crypto modules, commonly
one-time password systems or other authentication devices.

This module can be used to extract keys from PSKC files for use in an
OTP authentication system. The module can also be used for authoring
PSKC files.

This module should be able to handle most common PSKC files.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# from tox.ini
export TZ='Europe/Amsterdam'
# from setup.cfg
%pyproject_run_pytest \
    -vra \
    -o=addopts='--doctest-modules --doctest-glob="*.doctest"'

%files
%doc COPYING ChangeLog NEWS README
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/csv2pskc
%_bindir/pskc2csv
%_bindir/pskc2pskc

%changelog
* Fri Jan 23 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4-alt1
- Packaged for ALT Sisyphus.
