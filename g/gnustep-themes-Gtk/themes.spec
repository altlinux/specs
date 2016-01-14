Name: gnustep-themes-Gtk
Version: 1.0
Release: alt6.svn20140115.1
Summary: Gnome Theme for GNUstep
License: LGPLv2.1+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/plugins/themes/Gtk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel
BuildPreReq: glib2-devel libgtk+2-devel libGConf-devel
BuildPreReq: /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Gnome is a theme engine for GNUstep which
uses the current Gtk+-Theme selected in Gnome
for drawing its widgets.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_libdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt6.svn20140115.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt6.svn20140115
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.svn20140115
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.svn20140115
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.svn20120521
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3.svn20120521
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.svn20120521
- Built with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20120521
- Initial build for Sisyphus

