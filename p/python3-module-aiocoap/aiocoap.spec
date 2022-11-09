Name: python3-module-aiocoap
Version: 0.4.4
Release: alt1

Summary: The Python CoAP library
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aiocoap/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/aiocoap-*
%python3_sitelibdir/aiocoap
%python3_sitelibdir/aiocoap-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.4-alt1
- 0.4.4 released

