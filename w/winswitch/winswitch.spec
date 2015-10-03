Name: winswitch
Version: 0.12.21
Release: alt1

Summary: Front end for controlling remote desktop sessions
License: GPLv3
Group: Networking/Remote access

Url: http://winswitch.org
Source: %name-%version.src.tar.xz

BuildRequires: python-devel rpm-build-python rpm-build-xdg libpng-devel
BuildRequires: python-module-setuptools python-module-pygtk-devel
Requires: python-module-twisted-core-gui python-module-twisted-conch

%define nautilus_lib %_libdir/nautilus

%add_python_req_skip appindicator gtkosx_application nautilus
%add_python_req_skip ntsecuritycon pywintypes
%add_python_req_skip win32api win32con win32event win32file win32gui win32pdh
%add_python_req_skip win32pipe win32process win32security win32ui winerror

%description
Start and control remote GUI sessions via xpra, NX, VNC, RDP
or plain ssh X11 forwarding.  You can start, suspend, resume
and send supported sessions to other clients.

%prep
%setup
# don't skip icewm!
sed -i 's,^OnlyShowIn=,#&,' skel/share/applications/winswitch.desktop

%build
%python_build

%install
%python_install

%ifarch x86_64 ppc64
mkdir -p %buildroot{%nautilus_lib,%python_sitelibdir}
mv %buildroot{/usr/lib/nautilus/extensions-2.0,%nautilus_lib/}
mv %buildroot{/usr/lib/python*/site-packages/%{name}*,%python_sitelibdir}
rmdir %buildroot/usr/lib/{nautilus,python*{/site-packages,}}
%endif

%files
%doc COPYING
%_man1dir/*
%_bindir/*_*
%_bindir/wcw
%_prefix/libexec/%name/
%python_sitelibdir/%{name}*
%nautilus_lib/extensions-2.0/python/nautilus_winswitch.*
%_sysconfdir/%name/
%_desktopdir/%name.desktop
%_datadir/%name/
%_datadir/Thunar/*
%_datadir/Vash/*
%_iconsdir/*.png
%_iconsdir/*/*/*/*.png
%_xdgmimedir/*

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.12.21-alt1
- 0.12.21

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 0.12.20-alt2
- don't filter out WMs for the applet, people can run trayer et al

* Thu Mar 05 2015 Michael Shigorin <mike@altlinux.org> 0.12.20-alt1
- built for ALT Linux as proposed at
  http://krlmlr.github.io/integrating-xpra-with-screen/
  (package based on fedora's 0.12.20 based on Antoine Martin's one)
- spec *cleanup*

