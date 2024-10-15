%define _unpackaged_files_terminate_build 1
%define pypi_name truststore
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.2
Release: alt1

Summary: Verify certificates using OS trust stores
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/truststore/
Vcs: https://github.com/sethmlarson/truststore

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%endif

%description
Truststore is a library which exposes native system certificate stores
(ie "trust stores") through an ssl.SSLContext-like API. This means that
Python applications no longer need to rely on certifi as a root
certificate store. Native system certificate stores have many helpful
features compared to a static certificate bundle like certifi:

* Automatically update certificates as new CAs are created and removed
* Fetch missing intermediate certificates
* Check certificates against certificate revocation lists (CRLs) to avoid
  monster-in-the-middle (MITM) attacks
* Managed per-system rather than per-application by a operations/IT team
* PyPI is no longer a CA distribution channel

Right now truststore is a stand-alone library that can be installed
globally in your application to immediately take advantage of the benefits
in Python 3.10+. Truststore has also been integrated into pip 24.2+ as the
default method for verifying HTTPS certificates (with a fallback to
certifi).

Long-term the hope is to add this functionality into Python itself. Wish us
luck!

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Deselect tests/test_inject.py::test_requests_works_with_inject because of
# it needs dns resolving, but there's no it within hasher chroot.
%pyproject_run_pytest -Wignore -m "not internet" \
    --deselect="tests/test_inject.py::test_requests_works_with_inject"

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.2-alt1
- Initial build for ALT Sisyphus.

