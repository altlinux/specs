%define _unpackaged_files_terminate_build 1
%define pypi_name youtube-transcript-api
%define mod_name youtube_transcript_api

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.4
Release: alt1.1
Summary: Python API which allows you to retrieve the transcript/subtitles for a given YouTube video
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/youtube-transcript-api/
Vcs: https://github.com/jdepoix/youtube-transcript-api
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-responses

BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-requests
%endif

%description
This is a python API which allows you to retrieve the transcript/subtitles
for a given YouTube video. It also works for automatically generated subtitles,
supports translating subtitles and it does not require a headless browser,
like other selenium based solutions do!

%prep
%setup
%autopatch -p1

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1.1
- Demodernized packaging.

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
