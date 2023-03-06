Name: python3-module-hassil
Version: 1.0.6
Release: alt1

Summary: The Home Assistant Intent Language (HassIL) parser
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/hassil/

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
%_bindir/hassil
%python3_sitelibdir/hassil
%python3_sitelibdir/hassil-%version.dist-info

%changelog
* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt1
- initial
