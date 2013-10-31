Name: yad
Version: 0.23.1
Release: alt1

Summary: Display graphical dialogs from shell scripts or command line
Group: System/Libraries
License: GPL
URL: http://code.google.com/p/yad

BuildRequires: libgtk+3-devel > 3.0.0
BuildRequires: intltool

Source0: %name-%{version}.tar

Packager: Afanasov Dmitry <ender@altlinux.org>

%description
Yad (yet another dialog) is a fork of Zenity with many improvements,
such as custom buttons, additional dialogs, pop-up menu in
notification icon and more.

%prep
%setup -q

%build
%autoreconf
%configure \
    --with-gtk=gtk3 \
    --with-rgb=/usr/share/X11/rgb.txt \
    --enable-icon-browser \
    #
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang yad
%files -f yad.lang
%_bindir/*
#_aclocaldir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_desktopdir/*

%changelog
* Thu Oct 31 2013 Afanasov Dmitry <ender@altlinux.org> 0.23.1-alt1
- initial build

