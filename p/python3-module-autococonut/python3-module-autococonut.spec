%define pypi_nname autococonut
%define _unpackaged_files_terminate_build 1

Name: python3-module-%pypi_nname
Version: 0.9.16
Release: alt1
Summary: a workflow recording tool for Linux
License: GPLv3+
Group: Development/Python
Url: https://pypi.org/project/needly/
Source: %name-%version.tar
BuildArch: noarch

Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadatasfdasdf
%endif
%add_findreq_skiplist %python3_sitelibdir/%pypi_nname/templates/page.pm

%description
AutoCoconut is a tool that enables tracking mouse and keyboard events to make
a workflow report with screenshot illustrations. Such workflow report can be
helpful when creating bug reports, tutorials, or test cases for GUI testing
frameworks, such as OpenQA and others.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%python3_sitelibdir/README.md

%files
%doc README.md
%_bindir/%pypi_nname
%_bindir/%pypi_nname-gui
%python3_sitelibdir/%pypi_nname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_nname}/

%changelog
* Mon Dec 11 2023 Mikhail Chernonog <snowmix@altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus

