Name: nvdock
Version: 1.0
Release: alt1.3

Summary: A tray icon to easily launch the nvidia-settings control panel

Group: System/Kernel and hardware
License: BSD && AS_IS

Url: http://www.opsat.net/user/bob/projects/nvdock

Source: %url/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Aug 19 2007
BuildRequires: gtk+-devel libgtk+2-common-devel libgtk+2-devel 
Requires: nvidia-settings 

%description
A tray icon to easily launch the nvidia-settings control panel. Now with
temperature reading! Actually it always had temperature reading, nvidia-settings
does that for me.

Author    Bob Majdak Jr <bob@kateos.org>

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_pixmapsdir

install -m 755 build/nvdock %buildroot%_bindir
install -m 644 pixmaps/nvdock.png %buildroot%_pixmapsdir
			  
%post

%preun

%files
%doc COPYING README TODO
%_bindir/*
%_pixmapsdir/*

%changelog
* Sun Dec 05 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.3
- fix Buildreg

* Thu Jul 29 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.2
- fix Buildreg

* Sun Aug 19 2007 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.1
- correct Group

* Sun Aug 19 2007 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1
- initial version



