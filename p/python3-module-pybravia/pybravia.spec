Name: python3-module-pybravia
Version: 0.4.1
Release: alt1

Summary: Async interface for controlling Sony Bravia TVs
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pybravia
VCS: https://github.com/Drafteed/pybravia

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

%files
%python3_sitelibdir/pybravia
%python3_sitelibdir/pybravia-%version.dist-info

%changelog
* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.1-alt1
- 0.4.1 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.5-alt1
- 0.2.5 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt1
- 0.2.2 releasead
