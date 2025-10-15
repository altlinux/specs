Name: python3-module-fnvhash
Version: 0.2.1
Release: alt1

Summary: Pure Python FNV hash implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/fnvhash
VCS: https://github.com/znerol/py-fnvhash

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
%python3_sitelibdir/fnvhash
%python3_sitelibdir/fnvhash-%version.dist-info

%changelog
* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.0-alt1
- initial

