Name: gpsman
Version: 6.4.3
Release: alt1
Summary: A GPS manager

Group: Networking/Other
License: GPLv2+
Url: http://gpsman.sourceforge.net/
Source0: %name-%version.tgz
#man files for the utils, stolen from debian
Source1: mou2gmn.1
Source2: mb2gmn.1
Source3: gpsman.desktop
Source4: gpsman-icon.png
#fix location of files in executable
Patch0: gpsman-6.3.2-sourcedir.patch

BuildArch: noarch

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: desktop-file-utils
Requires: tk
Requires: tcl-img

%description
GPS Manager (GPSMan) is a graphical manager of GPS data that makes possible
the preparation, inspection and edition of GPS data in a friendly environment.

GPSMan supports communication and real-time logging with both Garmin and
Lowrance receivers and accepts real-time logging information in NMEA 0183
from any GPS receiver.

%prep
%setup -q
%patch0 -p1

#make sure all files are utf-8
recode()
{
  iconv -f "$2" -t utf-8 < "$1" > "${1}_"
  mv -f "${1}_" "$1"
}
for f in `find manual/html -name *.html`
 do recode $f iso-8859-15
done
recode manual/html/info/WPs.txt iso-8859-15

%build
#no build needed

%install
#manual install
install -D -m 0755 gpsman.tcl $RPM_BUILD_ROOT%_bindir/gpsman
install -Dd gmsrc $RPM_BUILD_ROOT%_datadir/gpsman
for f in `find gmsrc/ -type f -maxdepth 1`
 do install -D -m 0644 $f $RPM_BUILD_ROOT%_datadir/gpsman/`echo $f | cut -d '/' -f2`
done
install -Dd gmsrc/gmicons $RPM_BUILD_ROOT%_datadir/gpsman/gmicons
for f in `find gmsrc/gmicons/ -type f -name *.gif`
 do install -D -m 0644 $f $RPM_BUILD_ROOT%_datadir/gpsman/gmicons/`echo $f | cut -d '/' -f3`
done
install -D -m 0644 man/man1/gpsman.1 $RPM_BUILD_ROOT%_mandir/man1/gpsman.1
#utils
install -D -m 0755 util/mb2gmn.tcl $RPM_BUILD_ROOT%_bindir/mb2gmn
install -D -m 0755 util/mou2gmn.tcl $RPM_BUILD_ROOT%_bindir/mou2gmn
#man files
install -D -m 0644 %SOURCE1 $RPM_BUILD_ROOT%_mandir/man1/mb2gmn.1
install -D -m 0644 %SOURCE2 $RPM_BUILD_ROOT%_mandir/man1/mou2gmn.1
# desktop file and icon
mkdir -p   $RPM_BUILD_ROOT%_datadir/pixmaps/
install -m 644 %SOURCE4 \
  $RPM_BUILD_ROOT%_datadir/pixmaps/
desktop-file-install --vendor="" \
  --dir=$RPM_BUILD_ROOT%_datadir/applications \
  %SOURCE3


%files
%doc LICENSE
%doc manual/GPSMandoc.pdf manual/html
%_bindir/*
%_datadir/gpsman
%_mandir/man?/*
%attr(0644,root,root) %_datadir/applications/%name.desktop
%attr(0644,root,root) %_datadir/pixmaps/*

%changelog
* Tue May 01 2012 Ilya Mashkin <oddity@altlinux.ru> 6.4.3-alt1
- 6.4.3

* Sun Apr 22 2012 Ilya Mashkin <oddity@altlinux.ru> 6.4.2-alt1
- 6.4.2
- changed url

* Sat Jan 16 2010 Ilya Mashkin <oddity@altlinux.ru> 6.4.1-alt1
- 6.4.1

* Mon Dec 22 2008 Ilya Mashkin <oddity@altlinux.ru> 6.4-alt3
- remove deprecated macros from spec

* Sun Nov 02 2008 Ilya Mashkin <oddity@altlinux.ru> 6.4-alt2
- fix menu and requires

* Sat Nov 01 2008 Ilya Mashkin <oddity@altlinux.ru> 6.4-alt1
- 6.4

* Fri Oct 31 2008 Ilya Mashkin <oddity@altlinux.ru> 6.3.2-alt1
- build for ALT Linux

* Thu Aug 14 2008 Lucian Langa <cooly@gnome.eu.org> - 6.3.2-4
- fix reuirements
- misc cleanups

* Tue Feb 26 2008 Steve Conklin <sconklin at redhat dot com> - 6.3.2-3
- rpmlint clean up

* Sun Dec 09 2007 Robert 'Bob' Jensen <bob@bobjensen.com> - 6.3.2-2
- rpmlint clean up

* Sun Dec 09 2007 Sindre Pedersen Bjørdal - 6.3.2-1
- Initial build
