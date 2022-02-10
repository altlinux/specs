Name: python3-module-spotipy
Version: 2.19.0
Release: alt1

Summary: A light weight Python library for the Spotify Web API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/spotipy/

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
%doc LICENSE.* README.*
%python3_sitelibdir/spotipy
%python3_sitelibdir/spotipy-%version-*-info

%changelog
* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.19.0-alt1
- 2.19.0 released

* Wed Apr 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.18.0-alt1
- 2.18.0 released

* Tue Nov 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.16.1-alt1
- 2.16.1 released

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.16.0-alt1
- 2.16.0 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14.0-alt1
- 2.14.0 released

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.1-alt1
- initial
