%define _unpackaged_files_terminate_build 1
%define pypi_name logmerger

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1
Summary: TUI utility to view multiple log files with merged timeline.
License: MIT
Group: System/Configuration/Other
Url: https://github.com/ptmcg/logmerger
Vcs: https://pypi.org/project/logmerger/

BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: alt-pyproject.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(rich)
BuildRequires: python3(littletable)
BuildRequires: python3(textual)
BuildRequires: python3(pyshark)
BuildRequires: python3-module-markdown-it
BuildRequires: python3-module-linkify-it-py

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py3_provides %pypi_name

%description
%name is a TUI for viewing a merged display of multiple log files,
merged by timestamp.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Wed Aug 20 2025 Pavel Shilov <zerospirit@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
