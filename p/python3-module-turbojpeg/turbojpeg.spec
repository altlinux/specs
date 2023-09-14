Name: python3-module-turbojpeg
Version: 1.7.1
Release: alt1

Summary: A Python wrapper of libjpeg-turbo for decoding and encoding JPEG image.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyTurboJPEG/

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
%python3_sitelibdir/turbojpeg.*
%python3_sitelibdir/*/turbojpeg.*
%python3_sitelibdir/PyTurboJPEG-%version.dist-info

%changelog
* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.7-alt1
- 1.6.7 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt1
- 1.6.6 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.5-alt1
- 1.6.5 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- initial
