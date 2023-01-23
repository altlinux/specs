Name: python3-module-mac-vendor-lookup
Version: 0.1.12
Release: alt1

Summary: Get vendor information from a MAC address
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/mac-vendor-lookup/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup
touch mac-vendors.txt

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
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.12-alt1
- 0.1.12 released
