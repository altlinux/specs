%define _unpackaged_files_terminate_build 1
%define pypi_name nats-py
%define mod_name nats

# tests require running NATS server
%def_without check

Name: python3-module-%pypi_name
Version: 2.13.1
Release: alt1

Summary: Python3 client for NATS
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nats-py/
Vcs: https://github.com/nats-io/nats.py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
An asyncio Python client for the NATS messaging system.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
for workspace in nats nats-server nats-core; do
pushd $workspace
%pyproject_build
popd
done

%install
for workspace in nats nats-server nats-core; do
pushd $workspace
%pyproject_install
popd
done

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/nats_core-0.1.0.dist-info
%python3_sitelibdir/nats_server-0.0.0.dist-info

%changelog
* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.9.0-alt1
- Updated to 2.9.0.

* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Tue Apr 02 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.

* Tue Feb 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Sisyphus.

