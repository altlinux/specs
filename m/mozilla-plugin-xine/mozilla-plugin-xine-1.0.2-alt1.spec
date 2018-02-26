%define pname xine-plugin
Name: mozilla-plugin-xine
Version: 1.0.2
Release: alt1.1
Summary: Media plugin for mozilla compatible browsers using libxine backend
Group: Video
License: %gpl2plus
URL: http://xinehq.de/
Source: %pname-%version.tar

# Automatically added by buildreq on Mon Aug 11 2008
BuildRequires: gcc-c++ libX11-devel libxine-devel xorg-cf-files
BuildRequires: browser-plugins-npapi-devel libnspr-devel
BuildRequires: rpm-build-licenses

%description
This is a very simple netscape/mozilla browser plugin using the xine
engine to display multimedia streams.
Features:
- embedded display on browser window
- streaming playback directly from xine engine
- playback control using keyboard
- relative paths supported
- on screen display of buffering and stream information
- playlists and references support
- loop and repeat mode
- multiple instances within the same page
- javascript support


%prep
%setup -n %pname-%version


%build
%configure --with-plugindir=%browser_plugins_path
%make_build
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot%browser_plugins_path/*.la


%files
%doc AUTHORS ChangeLog.* README TODO
%browser_plugins_path/*


%changelog
* Fri Oct 02 2009 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Mon Aug 11 2008 Led <led@altlinux.ru> 1.0.2-alt1
- 1.0.2
- cleaned up spec

* Sun Jun 22 2008 Martin Stransky <stransky@redhat.com> - 1.0.1-4
- rebuild against new xulrunner

* Sun Jun 01 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-3
- require mozilla-filesystem instead of xulrunner on >= F9

* Wed Apr 23 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-2
- remove the dropped patch from spec file completely

* Tue Apr 22 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0.1-1
- new upstream release
- drop the xine-lib version patch - fixed in upstream

* Sat Feb 09 2008 Martin Sourada <martin.sourada@gmail.com> - 1.0-6
- rebuild for gcc 4.3
- add patch for x.y.z.w format xine-lib version string

* Tue Aug 21 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-5
- rebuild 

* Thu Aug 09 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-4
- update License: field to GPLv2+

* Wed Mar 14 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-3
- fix rpmlint warning

* Tue Mar 13 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-2
- add BR: xorg-x11-proto-devel, libX11-devel

* Sun Feb 04 2007 Martin Sourada <martin.sourada@seznam.cz> - 1.0-1
- Initial package
