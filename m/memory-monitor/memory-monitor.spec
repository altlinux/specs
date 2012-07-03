Name:		memory-monitor
Version:	1.1
Release:	alt2
Summary:	Qt4-based memory monitor
Source0:	http://www.smultron.net/project/memory-monitor/%name-%version.tar.gz
Source1:	%name.png
Source2:	%name.desktop
Url:		http://www.smultron.net/wiki/index.php?title=Memory_monitor
Group:		Monitoring
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>

# Automatically added by buildreq on Fri Jun 06 2008 (-bi)
BuildRequires:	ImageMagick gcc-c++ libqt4-devel

%description
This is a small Qt4 based application for detailed
monitoring of the memory usage of a running Linux
application. Any application can be monitored by picking
it from a dropdown list. Memory monitor will sample
the app each second and draw a plot of memory usage
over time. It can also show mapped memory. 

The data is extracted from various process specific
files in /proc/. A kernel version of 2.6.14 or higher
is required, as most of the data needed was added to
the /proc/ filesystem in this version.

%prep
%setup -q
cp %SOURCE1 ./

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%__install -Dp -m 0755 %name %buildroot%_bindir/%name
%__install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

%files
%doc README
%_bindir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt2
- delete post/postun scripts (new rpm)

* Fri Jun 06 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- initial build for ALT Linux
- added icon from Futurosoft icons for KDE (http://www.kde-look.org/content/show.php?content=50667)
