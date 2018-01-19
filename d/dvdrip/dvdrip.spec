%define module_dir Video
%define module_name DVDRip

Name: dvdrip
Version: 0.98.11
Release: alt1.qa3

Summary: DVD ripping graphical tool using transcode
License: GPL/Artistic
Group: Video
Url: http://www.exit1.org/dvdrip

Source: %url/dist/pre/%name-%version.tar.gz
Source1: %name.png

Patch: dvdrip-0.98.2-alt-setlocale.patch

Provides: perl-%module_dir-%module_name
Obsoletes: perl-%module_dir-%module_name

Requires: perl-libintl >= 1.16
Requires: transcode >= 1.0.2
Requires: mjpegtools >= 1.6.0
Requires: ImageMagick
Requires: ogmtools >= 1.0.2
Requires: lsdvd >= 0.15
# burning related tools
Requires: mkisofs
Requires: cdrecord
#Requires: dvdrecord
Requires: cdrdao
Requires: vcdimager
#Requires: fping
#Requires: rar
Requires: subtitleripper

# Automatically added by buildreq on Tue Jan 03 2006 (-bi)
BuildRequires: ImageMagick MPlayer cdrdao cdrecord fontconfig fping freetype2 lsdvd mjpegtools mkisofs ogmtools perl-Encode perl-Event-RPC perl-Glib perl-Gtk2-Ex-FormFactory perl-Log-Agent perl-Storable perl-devel perl-libintl subtitleripper transcode vcdimager perl-AnyEvent perl-Event-ExecFlow


%add_findreq_skiplist */Video/DVDRip/Term/*.pm

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
dvd::rip is a full featured DVD copy program written in Perl.
It provides an easy to use but feature-rich Gtk+ GUI to control almost
all aspects of the ripping and transcoding process. It uses the widely
known video processing swissknife transcode and many other Open Source
tools.

%prep
%setup -q
%patch -p1

%build
# SMP-incompatible build
%define __nprocs 1
%perl_vendor_build INSTALLMAN1DIR=%_man1dir SKIP_UNPACK_REQUIRED_MODULES=1

%install
%perl_vendor_install

install -pD -m644 %SOURCE1 %buildroot%_liconsdir/%name.png
# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=DVDRip
Comment=DVD ripping graphical tool
Icon=%name
Exec=%name
Terminal=false
Categories=AudioVideo;Video;AudioVideoEditing;
EOF

mkdir -p %buildroot%_datadir
mv %buildroot%perl_vendor_privlib/LocaleData %buildroot%_datadir/locale

%find_lang --output=%name.lang video.dvdrip

bzip2 -f9 Changes

%files -f %name.lang
%_bindir/*
%dir %perl_vendor_privlib/%module_dir
%perl_vendor_privlib/%module_dir/*
%_man1dir/*
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%doc Changes* Credits README TODO

%changelog
* Fri Jan 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.98.11-alt1.qa3
- Updated build dependencies.
- Added desktop file.

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.98.11-alt1.qa2
- NMU: converted menu to desktop file

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.98.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed May 19 2010 Ilya Mashkin <oddity@altlinux.ru> 0.98.11-alt1
- 0.98.11

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 0.98.10-alt1
- 0.98.10

* Tue May 27 2008 L.A. Kostis <lakostis@altlinux.ru> 0.98.8-alt1
- 0.98.8.

* Sun Feb 18 2007 L.A. Kostis <lakostis@altlinux.ru> 0.98.2-alt1
- compress Changes
- add missing dir
- remove man3pages (use perldoc instead).

* Fri Feb 16 2007 L.A. Kostis <lakostis@altlinux.ru> 0.98.2-alt0.2
- 0.98.2.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.97.13-alt1
- 0.97.13 release.

* Tue Jan 24 2006 LAKostis <lakostis@altlinux.org> 0.97.6-alt1
- change Packager (from orphaned) ;)

* Mon Jan 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.97.6-alt0.1
- new version

* Tue Jan 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.97.5-alt0.1
- change Packager (from orphaned)
- change name of package (close #4449)
- new (unstable) version

* Sun Apr 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.52.3-alt2
- build as arch dependant package (close #6501).
- requires perl-libintl >= 1.11-alt2 for working i18n.

* Mon Mar 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.52.3-alt1
- new version.

* Fri Jan 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.52.2-alt1.1
- fixed %%install.

* Sun Jan 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.52.2-alt1
- 0.52.2

* Thu Dec 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.51.4-alt1
- 0.51.4

* Mon Jun 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.50.18-alt1
- install icon (#close #4449)

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.50.18-alt0.5
- 0.50.18

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.16-alt0.5
- 0.50.16
- deparse patch by at@.

* Sat May 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.13-alt0.5
- 0.50.13 

* Thu May 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.12-alt0.5
- 0.50.12

* Sun Apr 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.11-alt0.5
- 0.50.11

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.9-alt0.5
- 0.50.9

* Wed Mar 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.7-alt0.5
- 0.50.7

* Mon Mar 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.5-alt0.5
- 0.50.5

* Thu Feb 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.4-alt0.5
- First build for Sisyphus.

