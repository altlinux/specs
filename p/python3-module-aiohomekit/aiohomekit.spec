Name: python3-module-aiohomekit
Version: 3.0.9
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
* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.9-alt1
- 3.0.9 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt1
- 2.6.5 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.3-alt1
- 2.6.3 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.4-alt1
- 2.4.4 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.18-alt1
- 2.2.18 released

