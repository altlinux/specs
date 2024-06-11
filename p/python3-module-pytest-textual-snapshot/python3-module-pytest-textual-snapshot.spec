%define _unpackaged_files_terminate_build 1

Name: python3-module-pytest-textual-snapshot
Version: 0.4.0
Release: alt1

Summary: Snapshot testing for Textual applications
License: MIT
Group: Terminals
Url: https://github.com/Textualize/pytest-textual-snapshot.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%description
A pytest-textual-snapshot test saves an SVG screenshot of a running Textual
app to disk. The next time the test runs, it takes another screenshot and
compares it to the saved one. If the new screenshot differs from the old one,
the test fails. This is a convenient way to quickly and automatically detect
visual regressions in your applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*
%doc README.md

%changelog
* Wed May 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
