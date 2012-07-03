Name: xclipboard
Version: 1.1.2
Release: alt1
Summary: X clipboard client
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel libXt-devel xorg-util-macros

%description
The xclipboard program is used to collect and display text selections
that are sent to the clipboard by other clients. It is typically used to
save clipboard selections for later use. It stores each clipboard
selection as a separate string, each of which can be selected. Each time
clipboard is asserted by another application, xclipboard transfers the
contents of that selection to a new buffer and displays it in the text
window.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%doc README
%_bindir/xclipboard
%_bindir/xcutsel
%_x11appconfdir/XClipboard
%_mandir/man1/xclipboard.1.gz
%_mandir/man1/xcutsel.1.gz

%changelog
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1.1
- Recalculate buildreq

* Sun Nov 14 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Sun Sep 26 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Fri Nov 21 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Sync with upstream up to aw7 downgrade patch

* Sat Oct 21 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- __autoreconf added to correct manpage extension

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:49:44 (59454)
- rebuild to fix libXaw.so.8 dependency

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:34:29 (31748)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
