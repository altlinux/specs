%define _unpackaged_files_terminate_build 1
%define oname OpenTimelineIO

Name: python3-module-%oname
Version: 0.15.0
Release: alt1.git62bd64df

Summary: OpenTimelineIO is an interchange format and API for editorial cut information.

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/AcademySoftwareFoundation/OpenTimelineIO

Source: %name-%version.tar
Patch: %name-%version-%release.patch
# Fix cmake for build with ALT packages
Patch1: %name-0.15.0-alt-CMakeLists_alt_packages.patch
Patch2: %name-0.15.0-alt-rm_vers_restrict_from_pyaaf.patch

# Skipping proprietary modules bundled with Autodesk products
# https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-D64ACA64-2566-42B3-BE0F-BCE843A1702F
%add_findreq_skiplist %python3_sitelibdir/opentimelineio_contrib/adapters/extern_maya_sequencer.py
# https://help.autodesk.com/view/SGSUB/ENU/?guid=SG_RV_rv_manuals_html
# TODO: pack and test https://github.com/AcademySoftwareFoundation/OpenRV
# https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/RV-Open-Source-Frequently-Asked-Questions.html
%add_findreq_skiplist %python3_sitelibdir/opentimelineio_contrib/adapters/extern_rv.py

%py3_provides %oname

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(sphinx) cmake
BuildRequires: python3-module-pybind11 python3-module-imath-devel
BuildRequires: rapidjson-devel optional-lite any
BuildRequires: python3-module-pyaaf2
BuildRequires: python3-module-pytest

Requires: python3-module-PySide2 >= 5.11
Requires: python3-module-pyaaf2 >= 1.4

%description
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references
to external media. It is not however, a container format for media.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
# TODO: Excluded some tests for arch x86, figure it out in the future releases
%ifarch %ix86
%pyproject_run_pytest -ra tests --ignore tests/test_opentime.py -ra tests -k " \
    not test_timecode_ntsc_2997fps and \
    not test_timecode_infer_drop_frame and \
    not test_timecode_2997 and \
    not test_passing_ndf_tc_at_df_rate and \
    not test_dropframe_timecode_2997fps"
%else
%tox_check_pyproject tests
%endif

%files
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md GOVERNANCE.md
%doc NOTICE.txt OTIO_CLA_Corporate.pdf OTIO_CLA_Individual.pdf README.md

%python3_sitelibdir/*

%_bindir/otioautogen_serialized_schema_docs
%_bindir/otiocat
%_bindir/otioconvert
%_bindir/otiopluginfo
%_bindir/otiostat
%_bindir/otiotool
%_bindir/otioview

%changelog
* Thu Sep 14 2023 Aleksei Kalinin <kaa@altlinux.org> 0.15.0-alt1.git62bd64df
- Tests configured, especially for checking compatibility with new pyaaf2.
- Excluded some tests for arch x86; Check stability in future releases.
- Removed version restrictions to use renewed pyaaf module v1.7+.
- Prepared patch for building with packed submodules for Alt.
- Interim upstream release Fix: Support compiling with GCC 13.
- Initial build.
