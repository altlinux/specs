Name: gnustep-themes-Gtk
Version: 1.0
Release: alt1.svn20120521
Summary: Gnome Theme for GNUstep
License: LGPLv2.1+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gui/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel
BuildPreReq: glib2-devel libgtk+2-devel libGConf-devel

%description
Gnome is a theme engine for GNUstep which
uses the current Gtk+-Theme selected in Gnome
for drawing its widgets.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_libdir/GNUstep

%changelog
* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20120521
- Initial build for Sisyphus

