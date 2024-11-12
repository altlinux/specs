%define _unpackaged_files_terminate_build 1
%define pypi_name xmldiff

%def_with check

Name: python3-module-xmldiff
Version: 2.6.3
Release: alt1
Summary: A library and command line utility for diffing xml
License: MIT
Group: Development/Python3
Url: https://github.com/Shoobx/xmldiff

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
xmldiff is a library and a command-line utility for making diffs out of XML.
This may seem like something that doesn't need a dedicated utility, but change
detection in hierarchical data is very different from change detection in flat
data. XML type formats are also not only used for computer readable data, it is
also often used as a format for hierarchical data that can be rendered into
human readable formats. A traditional diff on such a format would tell you line
by line the differences, but this would not be be readable by a human. xmldiff
provides tools to make human readable diffs in those situations.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/xmldiff
%_bindir/xmlpatch
%python3_sitelibdir/*

%changelog
* Mon Nov 11 2024 Andrey Kovalev <ded@altlinux.org> 2.6.3-alt1
- Initial build for Sisyphus.
