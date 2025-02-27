%define modulename kalyke-apns

Name: python3-module-%modulename
Version: 1.0.6
Release: alt1
Summary: A library for interacting with APNs and VoIP using HTTP/2
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/kalyke-apns/
Vcs: https://github.com/nnsnodnb/kalyke

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch1: %modulename-%version-poetry-versioning-bypass.patch
Patch2: %modulename-%version-rename-pyjwt-to-jwt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

BuildArch: noarch

%description
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/kalyke
%python3_sitelibdir/kalyke_apns-*.dist-info

%changelog
* Thu Jan 30 2025 Vitaly Churkin <chur1q@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.