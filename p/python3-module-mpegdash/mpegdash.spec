Name: python3-module-mpegdash
Version: 0.4.1
Release: alt1

Summary: MPEG-DASH MPD (Media Presentation Description) Parser
License: MIT
Group: Development/Python
URL: https://pypi.org/project/mpegdash
VCS: https://github.com/sangwonl/python-mpegdash

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v

%files
%python3_sitelibdir/mpegdash
%python3_sitelibdir/mpegdash-%version.dist-info

%changelog
* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.1-alt1
- 0.4.1 released

