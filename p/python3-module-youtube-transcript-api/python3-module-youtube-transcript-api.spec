%define pypi_name youtube-transcript-api
%define internal_name youtube_transcript_api
%define _unpackaged_files_terminate_build 1
%def_enable check

Name: python3-module-%pypi_name
Version: 0.6.3
Release: alt1

Summary: Python API which allows you to retrieve the transcript/subtitles for a given YouTube video
License: MIT
Group: Development/Python3

URL: https://github.com/jdepoix/youtube-transcript-api
Vcs: https://github.com/jdepoix/youtube-transcript-api
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-poetry
%if_enabled check
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-mock
BuildRequires: python3-module-httpretty
%endif

BuildArch: noarch

%description
This is a python API which allows you to retrieve the transcript/subtitles
for a given YouTube video. It also works for automatically generated subtitles,
supports translating subtitles and it does not require a headless browser,
like other selenium based solutions do!

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc *.md
%_bindir/%internal_name
%python3_sitelibdir/%internal_name
%python3_sitelibdir/%{pyproject_distinfo %internal_name}

%changelog
* Sun Jan 12 2025 Semen Fomchenkov <armatik@altlinux.org> 0.6.3-alt1
- Initial build.
