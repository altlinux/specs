Name: python3-module-pychromecast
Version: 13.0.4
Release: alt1

Summary: Python library to communicate with the Google Chromecast
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyChromecast/

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
%python3_sitelibdir/pychromecast
%python3_sitelibdir/PyChromecast-%version.dist-info

%changelog
* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.4-alt1
- 13.0.4 released

* Tue Aug 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1.4-alt1
- 12.1.4 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1.2-alt1
- 12.1.2 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3.0-alt1
- 10.3.0

* Sun Sep 27 2020 Anton Midyukov <antohami@altlinux.org> 0.7-alt1
- Initial build for Sisyphus
