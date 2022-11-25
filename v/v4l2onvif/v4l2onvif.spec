Name: v4l2onvif
Version: 0.0.20221106
Release: alt1

Summary: V4L2-based ONVIF implementation
License: GPLv3
Group: System/Servers
Url: https://github.com/mpromonet/v4l2onvif

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ libgsoap-devel liblive555-devel

%package client
Summary: ONVIF client implementation
Group: Video

%package server
Summary: ONVIF server implementation
Group: System/Servers

%description
%summary

%description client
%summary
This package provides client part.

%description server
%summary
This package provides server (NVT/NVS/NVD) part.

%prep
%setup

%build
CXXFLAGS='%optflags' VERSION=%version make

%install
make install DESTDIR=%buildroot%_bindir

%files client
%doc LICENSE README.md
%_bindir/onvif-client

%files server
%doc LICENSE README.md
%_bindir/onvif-server

%changelog
* Fri Nov 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20221106-alt1
- updated to git.897ca50

* Tue Nov 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200924-alt2
- rebuilt with recent live555

* Tue Dec 01 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20200924-alt1
- initial
