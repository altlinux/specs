Name: gMTP
Version: 1.3.3
Release: alt1

Summary: A basic media player client
License: BSD-like
Group: File tools

Source: %name-%version.tar

BuildRequires: libmtp-devel
BuildRequires: libflac-devel
BuildRequires: libid3tag-devel
BuildRequires: libusb-devel
BuildRequires: libvorbis-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgio-devel
BuildRequires: glib2-devel

%description
Supports MTP devices including those with multiple storage devices
(typically mobile phones). Supports Drag'n'Drop interface for
upload/download of files.

%prep
%setup

%build
%make_build gtk3

%install
%make_install \
		DESTDIR=%buildroot \
                PREFIX=%_usr \
        install-gtk3

%make_install \
		DESTDIR=%buildroot \
                PREFIX=%_usr \
	register-gsettings-schemas

%find_lang gmtp

%files -f gmtp.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/gmtp
%_datadir/pixmaps/*
%_datadir/glib-2.0/schemas/*

%changelog
* Thu Jul 12 2012 Paul Wolneykien <manowar@altlinux.ru> 1.3.3-alt1
- Initial release for ALT Linux.
