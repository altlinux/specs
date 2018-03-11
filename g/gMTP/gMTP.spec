Name: gMTP
Version: 1.3.11
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
%configure
%make_build

%install
%makeinstall_std

%find_lang gmtp

%files -f gmtp.lang
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/gmtp
%_datadir/pixmaps/*
%_datadir/glib-2.0/schemas/*

%changelog
* Sun Mar 11 2018 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt1
- 1.3.11

* Fri Apr 28 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.10-alt1
- 1.3.10

* Thu Jul 12 2012 Paul Wolneykien <manowar@altlinux.ru> 1.3.3-alt1
- Initial release for ALT Linux.
