Name: python3-module-ha-ffmpeg
Version: 3.2.0
Release: alt1

Summary: Home-Assistant ffmpeg interface
License: BSD
Group: Development/Python
Url: https://pypi.org/project/ha-ffmpeg/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
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
%python3_sitelibdir/haffmpeg
%python3_sitelibdir/ha_ffmpeg-%version.dist-info

%changelog
* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.0-alt1
- 3.1.0 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- initial
