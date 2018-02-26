Name: gpsbabel
Version: 1.3.6
Release: alt2
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: A tool to convert between various formats used by GPS devices
License: GPL
Group: Sciences/Geosciences
Url: http://www.gpsbabel.org

# http://www.gpsbabel.org/plan9.php?dl=%name-%version.tar
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# Automatically added by buildreq on Fri Sep 12 2008
BuildRequires: libexpat-devel libusb-devel zlib-devel
BuildRequires: texlive-latex-recommended

%description
GPSBabel converts waypoints, tracks, and routes from one format to another,
whether that format is a common mapping format like Delorme, Streets and
Trips, or even a serial upload or download to a GPS unit such as those from
Garmin and Magellan. By flatting the Tower of Babel that the authors of
various programs for manipulating GPS data have imposed upon us, it returns
to us the ability to freely move our own waypoint data between the programs
and hardware we choose to use.

It contains extensive data manipulation abilities making it a
convenient for server-side processing or as the backend for other
tools.

It does not convert, transfer, send, or manipulate maps. We process
data that may (or may not be) placed on a map, such as waypoints,
tracks, and routes.

%prep
%setup -q
%patch -p1
rm -fR coldsync

find . -type f \( -name '*.c' -o -name '*.h' \) -print0 | xargs -r0 chmod a-x

%build
%configure --with-zlib=system --enable-pdb=no
%make_build

cd doc
%make_build
dvips -o gpsbabel.ps doc.dvi

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS README* contrib intdoc gpsbabel.html doc/gpsbabel.ps
%_bindir/%name

%changelog
* Sat Oct 31 2009 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt2
- Rebuilt with texlive.

* Wed Dec 10 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1
- New upstream release.

* Fri Sep 12 2008 Grigory Batalov <bga@altlinux.ru> 1.3.5-alt1
- New upstream release.

* Sun Nov 18 2007 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1
- New upstream release.

* Thu Jun 21 2007 Grigory Batalov <bga@altlinux.ru> 1.3.3-alt1
- Build for ALT Linux.

* Wed Apr 16 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.3-1
- Make first Fedora spec based on the one provided upstream
