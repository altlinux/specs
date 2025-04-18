Name: python3-module-mplcursors
Version: 0.6
Release: alt1

Summary: Interactive data selection cursors for Matplotlib
License: Zlib
Group: Development/Python
Url: https://pypi.org/project/mplcursors/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/mplcursors
%python3_sitelibdir/mplcursors-%version.dist-info

%changelog
* Fri Apr 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6-alt1
- 0.6 released

