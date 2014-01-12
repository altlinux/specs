Name: wbar
Version: 2.3.4
Release: alt1
License: GPLv2+
Group: Accessibility
Summary: A quick launch bar
Url: http://code.google.com/p/wbar/

Source0: %name.tar.bz2
Source1: wbar.desktop
Source2: chromium.png
Source3: computer.png
Source4: exit.png
Source5: terminal.png

# Automatically added by buildreq on Sun Jan 12 2014 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel imlib2 libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstdc++-devel perl-Encode perl-XML-Parser pkg-config sysvinit-utils xorg-xproto-devel
BuildRequires: gcc-c++ imlib2-devel intltool libglade-devel

%description
wbar is a quick launch bar.
* It's cool eye candy
* It's designed with speed in mind
* It's coded in c++ using imlib2
* It's lite & fast

%prep
%setup -n %name

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
make install DESTDIR=%buildroot
mkdir -p %buildroot%_datadir/applications
install -D -m 0644 %SOURCE1 %buildroot%_datadir/applications
install -D -m 0644 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %buildroot%_datadir/pixmaps/wbar

%find_lang %name

%files -f %name.lang
%dir %_sysconfdir/wbar.d
%_bindir/wbar*
%_sysconfdir/wbar.d/*
%_sysconfdir/bash_completion.d/wbar
%_man1dir/wbar*
%_datadir/wbar
%_datadir/man/es/man1/wbar*
%_desktopdir/wbar.desktop
%_pixmapsdir/wbar

%changelog
* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 2.3.4-alt1
- 2.3.4 (based on src.rpm by Muhammad Shaban)

* Tue Mar 30 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3.3-alt1
- initial build for ALT Linux from OpenSUSE package
