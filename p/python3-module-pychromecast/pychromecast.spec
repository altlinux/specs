Name: python3-module-pychromecast
Version: 10.3.0
Release: alt1

Summary: Python library to communicate with the Google Chromecast
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyChromecast/

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
%python3_sitelibdir/pychromecast
%python3_sitelibdir/PyChromecast-%version-*-info

%changelog
* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3.0-alt1
- 10.3.0

* Sun Sep 27 2020 Anton Midyukov <antohami@altlinux.org> 0.7-alt1
- Initial build for Sisyphus
