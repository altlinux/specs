%define _unpackaged_files_terminate_build 1

%def_with check
%global pypi_name faststream

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: Effortless event stream integration for your services
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch

VCS: https://github.com/airtai/FastStream
Url: https://faststream.ag2.ai/latest/
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%pyproject_builddeps_metadata_extra cli
%pyproject_builddeps_metadata_extra confluent
%pyproject_builddeps_metadata_extra kafka
%pyproject_builddeps_metadata_extra nats
%pyproject_builddeps_metadata_extra rabbit
%pyproject_builddeps_metadata_extra redis
%pyproject_builddeps_metadata_extra mqtt
%endif
BuildRequires: /proc

%description
FastStream simplifies the process of writing producers and consumers for message
queues,  handling  all  the  parsing, networking  and  documentation  generation
automatically.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vv -m "(slow and not connected) or not connected"

%files
%doc LICENSE README.md
%_bindir/faststream
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir_noarch/%{pep427_name %pypi_name}

%changelog
* Fri Jun 05 2026 Egor Ignatov <egori@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Tue Jun 02 2026 Egor Ignatov <egori@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Mar 30 2026 Egor Ignatov <egori@altlinux.org> 0.6.7-alt2
- Revert hostile changes.

* Tue Mar 03 2026 Egor Ignatov <egori@altlinux.org> 0.6.7-alt1
- New version 0.6.7.

* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 0.6.6-alt1
- New version 0.6.6.

* Thu Nov 06 2025 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Thu Jul 24 2025 Egor Ignatov <egori@altlinux.org> 0.5.48-alt1
- New version 0.5.48.

* Tue Jul 15 2025 Egor Ignatov <egori@altlinux.org> 0.5.47-alt1
- New version 0.5.47.

* Tue Jul 08 2025 Egor Ignatov <egori@altlinux.org> 0.5.45-alt1
- New version 0.5.45.

* Wed Jun 25 2025 Egor Ignatov <egori@altlinux.org> 0.5.43-alt1
- New version 0.5.43.

* Fri Apr 11 2025 Egor Ignatov <egori@altlinux.org> 0.5.39-alt1
- New version 0.5.39.

* Thu Mar 27 2025 Egor Ignatov <egori@altlinux.org> 0.5.37-alt1
- New version 0.5.37.

* Tue Mar 18 2025 Egor Ignatov <egori@altlinux.org> 0.5.35-alt1
- New version 0.5.35.

* Tue Jan 14 2025 Egor Ignatov <egori@altlinux.org> 0.5.34-alt1
- New version 0.5.34.

* Sat Dec 21 2024 Egor Ignatov <egori@altlinux.org> 0.5.33-alt1
- New version 0.5.33.

* Thu Dec 05 2024 Egor Ignatov <egori@altlinux.org> 0.5.32-alt1
- New version 0.5.32.

* Thu Nov 28 2024 Egor Ignatov <egori@altlinux.org> 0.5.30-alt1
- First build for ALT.
