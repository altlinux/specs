Name: lside
Version: 0.1
Release: alt1
License: GPL
Group: System/Kernel and hardware
Url: http://lside.berlios.de
Packager: Eugene Ostapets <eostapets@altlinux.org>

Summary: lside is a utility for displaying information about ide devices in the system 

Source: %name-%version.tar.gz

%description
lside is a utility for displaying information about IDE devices in the 
system. To make use of all the features of this program, you need to 
have a Linux kernel which supports the /proc/ide interface.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc ChangeLog AUTHORS COPYING
%_bindir/*

%changelog
* Sat Jan 26 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- first build

