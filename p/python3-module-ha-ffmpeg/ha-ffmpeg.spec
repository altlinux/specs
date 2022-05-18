Name: python3-module-ha-ffmpeg
Version: 3.0.2
Release: alt1

Summary: Home-Assistant ffmpeg interface
License: BSD
Group: Development/Python
Url: https://pypi.org/project/ha-ffmpeg/

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
%python3_sitelibdir/haffmpeg
%python3_sitelibdir/ha_ffmpeg-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- initial
