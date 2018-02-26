Name: tint2
Version: 0.11
Release: alt1
Summary: Simple panel/taskbar made for modern x window managers

Group: Graphical desktop/Other
License: GPLv2
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://code.google.com/p/%name/

Source: http://tint2.googlecode.com/files/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sat Jul 03 2010
BuildRequires: cmake gcc-c++ imlib2-devel libXcomposite-devel libXdamage-devel libXinerama-devel libXrandr-devel libpango-devel

%description
tint2 is a simple panel/taskbar made for modern x window managers.
It was specifically made for openbox3  but should also work with
other window managers (GNOME, KDE, etc...).

%prep
%setup -q %name-%version

%build
%cmake -DENABLE_TINT2CONF=OFF -DENABLE_EXAMPLES=ON
%make_build -C BUILD/

%install
%makeinstall_std -C BUILD/
install -pD -m 644 %buildroot%_datadir/%name/default_icon.png  %buildroot%_liconsdir/%name.png
rm -rf %buildroot/{%_datadir,%_docdir}/%name

%files
%doc AUTHORS ChangeLog COPYING NEWS README* sample/
%dir %_sysconfdir/xdg/%name/
%config(noreplace) %_sysconfdir/xdg/%name/tint2rc
%_bindir/*
%_man1dir/*
%_liconsdir/*.png

%changelog
* Fri Jul 2 2010 Andrew Clark <andyc@altlinux.org> 0.11-alt1
- version update to 0.11-alt1

* Tue Mar 23 2010 Andrew Clark <andyc@altlinux.org> 0.9-alt1
- initial build for ALT.

