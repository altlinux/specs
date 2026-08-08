%global _unpackaged_files_terminate_build 1
%define pypi_name highdicom

%def_with check

Name: python3-module-highdicom
Version: 0.28.1
Release: alt1
Summary: High-level DICOM abstractions
Group: Development/Python3
License: FIXME
BuildArch: noarch
Url: https://pypi.org/project/highdicom/
VCS: https://github.com/ImagingDataCommons/highdicom
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# tests scan every file in the pydicom test data; upstream CI only ever has a
# handful of those files downloaded, so the full pydicom-data set trips over
# gaps in the test harness
Patch0: highdicom-alt-tests-external-data.patch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# tests use pydicom's external test data (eCT_Supplemental.dcm, RG1_UNCR.dcm,
# mlut_18.dcm, vlut_04.dcm, color-pl.dcm); without it pydicom tries to download
# them and burns ~21s of retry backoff per call before failing
BuildRequires: python3-module-pydicom-data
%endif

%description
highdicom is a pure Python package built on top of pydicom to provide a
higher-level application programming interface (API) for working with DICOM
files. Its focus is on common operations required for machine learning,
computer vision, and other similar computational analyses.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/highdicom/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Aug 08 2026 Anton Farygin <rider@altlinux.org> 0.28.1-alt1
- initial build for ALT Linux

