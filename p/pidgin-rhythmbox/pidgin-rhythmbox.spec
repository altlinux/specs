Name: pidgin-rhythmbox
Version: 2.0
Release: alt2

Summary: Pidgin-Rhythmbox
Group: Sound
License: GPL
Url: http://jon.oberheide.org/projects/pidgin-rhythmbox/

Source0: http://jon.oberheide.org/projects/pidgin-rhythmbox/downloads/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: pidgin
Requires: rhythmbox

# Automatically added by buildreq on Sun Jul 27 2008
BuildRequires: gcc-c++ libdbus-glib-devel pidgin-devel

%description
The Pidgin-Rhythmbox plugin will automatically update your Pidgin user info
and status message with the currently playing music in Rhythmbox. If the
artist and title are known, it will also attempt to create a link to the
song's lyrics by using Google's "I'm Feeling Lucky" feature.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/pidgin/%name.*

%changelog
* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 2.0-alt2
- don't use obsolete macros

* Wed Jun 13 2007 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- build for Sisyphus


