Name:    light-locker
Version: 1.7.0
Release: alt1
Summary: A simple session-locker for lightdm 

# unclear license: https://github.com/the-cavalry/light-locker/issues/33
License: GPLv2+
Group:   Graphical desktop/Other
URL:     https://github.com/the-cavalry/%{name}
Source0: %name-%version.tar

BuildRequires:  libgtk+3-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  xorg-proto-devel
BuildRequires:  libsystemd-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

Requires:       lightdm

%description
%name is a simple locker (forked from gnome-screensaver)
that aims to have simple, sane, secure defaults and be well
integrated with the desktop while not carrying any desktop-
specific dependencies.
It relies on lightdm for locking and unlocking your session.

%prep
%setup -q

%build
sed -e "/XDT_I18N/d" configure.ac.in > configure.ac
%autoreconf
%configure --enable-lock-on-suspend=on --disable-silent-rules --with-gtk3 
%make_build V=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README COPYING COPYING.LIB
%_bindir/*
%_sysconfdir/xdg/autostart/*.desktop
%_datadir/glib-2.0/schemas/apps.*.xml
%_man1dir/*.1*

%changelog
* Tue Feb 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build in Sisyphus (ALT #31807)

