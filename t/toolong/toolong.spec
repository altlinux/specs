%define _unpackaged_files_terminate_build 1

%def_with check

Name: toolong
Version: 1.4.0
Release: alt1
Summary: A terminal application to view, tail, merge, and search log files.
License: MIT
Group: Editors
Url: https://github.com/Textualize/toolong
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3
BuildRequires: python3(poetry)
BuildRequires: python3-module-poetry-core
BuildRequires: python3(click)
BuildRequires: python3(textual)
BuildRequires: python3-module-typing-extensions

%description
A terminal application to view, tail, merge, and search log files (plus JSONL).

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#package don't have tests

%files
%doc *.md
%_bindir/tl
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Sun Oct 05 2025 Pavel Shilov <zerospirit@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

