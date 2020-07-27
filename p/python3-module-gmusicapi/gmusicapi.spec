Name: python3-module-gmusicapi
Version: 13.0.0
Release: alt1

Summary: Python API for google music
License: BSD
Group: Development/Python
Url: https://pypi.org/project/gmusicapi/

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
%python3_sitelibdir/gmusicapi
%python3_sitelibdir/gmusicapi-%version-*-info
%exclude %python3_sitelibdir/gmusicapi/test

%changelog
* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0.0-alt1
- initial
