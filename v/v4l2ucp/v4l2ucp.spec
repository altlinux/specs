Name: v4l2ucp
Version: 2.0.2
Release: alt2

Summary: Video for Linux 2 Universal Control Panel
License: GPL
Group: Video
Url: http://v4l2ucp.sourceforge.net

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ libqt4-devel libv4l-devel

%description
This program provides an interface for manipulation the controls
of any V4L2 device.

%prep
%setup

%build
cmake . \
    -DCMAKE_INSTALL_PREFIX=%prefix  \
    -DCMAKE_C_FLAGS:STRING='%optflags' \
    -DCMAKE_CXX_FLAGS:STRING='%optflags'
make

%install
%make_install DESTDIR=%buildroot install

%files
%doc README COPYING
%_bindir/%name
%_bindir/v4l2ctrl
%_desktopdir/%name.desktop
%_iconsdir/%name.png

%changelog
* Thu May 24 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt2
- fix build with recent glibc-kernheaders

* Sat May 14 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

* Thu Oct 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0 released

* Thu Oct 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 released

* Fri Apr 24 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- 1.3 released

* Thu Oct 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- initial build for ALT Linux
