Name: python3-module-mac-vendor-lookup
Version: 0.1.15
Release: alt1

Summary: Get vendor information from a MAC address
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/mac-vendor-lookup
VCS: https://github.com/bauerj/mac_vendor_lookup

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
touch mac-vendors.txt
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/mac_vendor_lookup
%python3_sitelibdir/mac_vendor_lookup.*
%python3_sitelibdir/*/mac_vendor_lookup.*
%python3_sitelibdir/mac_vendor_lookup-%version.dist-info

%changelog
* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.15-alt1
- 0.1.15 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.12-alt1
- 0.1.12 released
