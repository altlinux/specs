Name: multiget
Version: 1.2.0
Release: alt1

Summary: An easy-to-use GUI file downloader
Group: Networking/File transfer
License: GPLv2
Url: http://%name.sourceforge.net

Source: http://downloads.sourceforge.net/%name/%name-%version.src.tar.bz2
Source1: %name.desktop
Source2: %name.png

# from Fedora
Patch: multiget-1.2-fix-gcc43.patch
Patch1: multiget-1.2-includes.patch

BuildRequires: gcc-c++ libglade-devel libwxGTK-devel intltool perl-XML-Parser

%description
MultiGet is an easy-to-use GUI file downloader.
It's programmed in C++ and has a GUI based on wxWidgets. It supports HTTP/FTP
protocols which covers the requirements of most users. It supports multi-task
with multi-thread on multi-server. It supports resuming downloads if the Web
server supports it, and if you like, you can reconfig the thread number without
stopping the current task. It's also support SOCKS 4, 4a, 5 proxy, ftp proxy,
http proxy.

%prep
%setup -qn multiget
%patch -p1 -b .good
%patch1 -p1 -b .includes

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install
# .desktop file
install -pD -m 644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
# icon
install -pD -m 644 %SOURCE2 %buildroot%_datadir/pixmaps/%name.png

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*

%exclude %_prefix/doc/%name

%changelog
* Fri Feb 12 2010 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- first build for Sisyphus

