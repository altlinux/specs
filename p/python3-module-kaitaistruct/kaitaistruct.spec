Name: python3-module-kaitaistruct
Version: 0.11
Release: alt1

Summary: Kaitai Struct API for Python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/kaitaistruct
VCS: https://github.com/kaitai-io/kaitai_struct_python_runtime

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_runtimedeps_metadata

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
%python3_sitelibdir/kaitaistruct.*
%python3_sitelibdir/*/kaitaistruct.*
%python3_sitelibdir/kaitaistruct-%version.dist-info

%changelog
* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.11-alt1
- initial
