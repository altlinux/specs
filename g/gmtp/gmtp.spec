Name: gmtp
Version: 1.3.11
Release: alt2

Summary: A basic media player client
License: BSD-3-Clause
Group: File tools
Url: https://gmtp.sourceforge.io/

Provides: gMTP = %version-%release
Obsoletes: gMTP < %version-%release

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
%add_optflags -fcommon
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
%doc AUTHORS COPYING ChangeLog README

%changelog
* Tue Jan 05 2021 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt2
- Package name converted to lowercase
- Fixed build with gcc10
- Fixed license (via nomossa)
- Added docs

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.11-alt1.1
- NMU: added URL

* Sun Mar 11 2018 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt1
- 1.3.11

* Fri Apr 28 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.10-alt1
- 1.3.10

* Thu Jul 12 2012 Paul Wolneykien <manowar@altlinux.ru> 1.3.3-alt1
- Initial release for ALT Linux.
