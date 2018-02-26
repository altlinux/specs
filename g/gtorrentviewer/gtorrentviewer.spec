# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/curl-config
# END SourceDeps(oneline)
Name:		gtorrentviewer
Version:	0.2b
Release:	alt4_24
Summary:	A GTK2-based viewer and editor for BitTorrent meta files
Group:		Networking/File transfer
License:	GPL+
URL:		http://gtorrentviewer.sourceforge.net/
Source0:	http://downloads.sf.net/gtorrentviewer/GTorrentViewer-%{version}.tar.gz
Patch0:		gtorrentviewer-0.2b-desktop.patch
Patch1:		gtorrentviewer-0.2b-dso-linking.patch
Patch2:		GTorrentViewer-0.2b-tracker-details-refresh.patch
Patch3:		gtorrentviewer-0.2b-trackerdetails.patch
Patch4:		GTorrentViewer-0.2b-curl-types.patch
BuildRequires:	libcurl-devel libgtk+2-devel >= 2.4 desktop-file-utils gettext intltool

Requires(post):	  desktop-file-utils
Requires(postun): desktop-file-utils
Source44: import.info

%description
GTorrentViewer gives you the ability to see and modify all the possible
information from .torrent files without having to start downloading, and
the ability to see in real time the current number of seeds and peers on
the torrent, so you will always know the status before starting the
download.

%prep
%setup -q -n GTorrentViewer-%{version}

# Let drag and drop work with URIs as well as files (#206262)
%patch0 -p1

# mainwindow.c requires ceil() from libm (#564928)
%patch1 -p1

# Fix crash due to use of uninitialized GValue (#542502, #572806)
%patch2 -p1

# Improve tracker support (#674726)
%patch3 -p1

# <curl/types.h> went away in curl 7.22.0
%patch4 -p1

# curl/types.h are no more; was true for  0.2b-22.
sed -i 's,#include <curl/types.h>,,' src/main.c

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_datadir}/GTorrentViewer/README
desktop-file-install \
	--vendor fedora \
	--add-category X-Fedora \
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/gtorrentviewer.desktop

desktop-file-install --dir %buildroot%_desktopdir \
        --add-category=FileTransfer \
        --add-category=P2P \
        %buildroot%_desktopdir/fedora-gtorrentviewer.desktop

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/gtorrentviewer
%{_datadir}/GTorrentViewer
%{_datadir}/applications/fedora-gtorrentviewer.desktop
%{_datadir}/pixmaps/gtorrentviewer.png
%{_datadir}/pixmaps/gtorrentviewer.xpm
%{_mandir}/man1/gtorrentviewer.1*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_24
- rebuild to get rid of #27020

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_24
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_23
- update to new release by fcimport

* Tue Jul 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_22
- fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2b-alt2_22.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtorrentviewer
  * postclean-03-private-rpm-macros for the spec file

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt2_22
- fixed scripts

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt1_22
- initial release by fcimport

