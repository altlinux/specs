Name: sercd
Version: 3.0.0
Release: alt1

Summary: Serial port redirector.
License: GPL
Group: System/Kernel and hardware
Url: http://www.lysator.liu.se/~astrand/projects/sercd/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %url/%name-%version.tar.gz


%description
Sercd is a RFC 2217 compliant serial port redirector. 
It is based on sredird


%prep
%setup -q


%build
%configure
%make
%make_build

%install
mkdir -p %buildroot%_sysconfdir
%make_install install DESTDIR=%buildroot
install -m755 -D sercd.xinetd %buildroot/%_sysconfdir/sercd

%files

%_sysconfdir/sercd
%_sbindir/*
%_man8dir/*


%changelog
* Fri Jan 09 2009 Ilya Mashkin <oddity@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Apr 26 2007 Lunar Child <luch@altlinux.ru> 2.3.2-alt2
- added xinetd config

* Mon Apr 23 2007 Lunar Child <luch@altlinux.ru> 2.3.2-alt1
- First build for Alt Linux Sisyphus.




