Name: python3-module-aiohomekit
Version: 2.4.4
Release: alt1

Summary: This library implements the HomeKit protocol
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohomekit/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)
Requires: python3(chacha20poly1305)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/aiohomekitctl
%python3_sitelibdir/aiohomekit
%python3_sitelibdir/aiohomekit-%version.dist-info

%changelog
* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.18-alt1
- 2.2.18 released

