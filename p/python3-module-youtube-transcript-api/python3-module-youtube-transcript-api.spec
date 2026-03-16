%define _unpackaged_files_terminate_build 1
%define pypi_name youtube-transcript-api
%define mod_name youtube_transcript_api

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.4
Release: alt1
Summary: Python API which allows you to retrieve the transcript/subtitles for a given YouTube video
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/youtube-transcript-api/
Vcs: https://github.com/jdepoix/youtube-transcript-api
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a python API which allows you to retrieve the transcript/subtitles
for a given YouTube video. It also works for automatically generated subtitles,
supports translating subtitles and it does not require a headless browser,
like other selenium based solutions do!

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry test
%endif

%build
%pyproject_build

%install
%pyproject_install
# don't ship tests
rm -r %buildroot%python3_sitelibdir/%mod_name/test/

%check
# see .github/workflows/ci.yml
%pyproject_run_pytest -vra

%files
%_bindir/youtube_transcript_api
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1
- 1.2.3 -> 1.2.4.

* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.0.3 -> 1.2.3 (closes: #57088).

* Thu Jul 10 2025 Stanislav Levin <slev@altlinux.org> 1.0.3-alt2
- Skipped tests requiring httpretty.

* Tue Apr 22 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Jan 12 2025 Semen Fomchenkov <armatik@altlinux.org> 0.6.3-alt1
- Initial build.
