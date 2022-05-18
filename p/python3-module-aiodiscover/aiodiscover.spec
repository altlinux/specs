Name: python3-module-aiodiscover
Version: 1.4.11
Release: alt1

Summary: Async Host discovery
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/bdraco/aiodiscover

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/aiodiscover
%python3_sitelibdir/aiodiscover-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.11-alt1
- 1.4.11 released

