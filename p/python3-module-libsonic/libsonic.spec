Name: python3-module-libsonic
Version: 1.0.0
Release: alt1

Summary: Subsonic REST API
License: GPLv3
Group: Development/Python
Url: https://pypi.org/project/py-sonic/

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
%python3_sitelibdir/libsonic
%python3_sitelibdir/py_sonic-%version.dist-info

%changelog
* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
