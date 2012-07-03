%define _name geolocation
%define _name2 geolocation_plugin

Name: claws-mail-plugin-%_name
Version: 0.0.8
Release: alt1

Summary: Geolocation functionality for Claws Mail
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name2-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: glib2-devel >= 2.6
BuildPreReq: libgtk+2-devel >= 2.6
BuildPreReq: libsoup-devel >= 2.4
BuildPreReq: libchamplain-gtk-devel >= 0.8.0

%description
This Claws Mail plugin provides GeoLocation functionality.

%prep
%setup -n %_name2-%version

%build
%autoreconf
%configure \
	--disable-static
%make

%install
%makeinstall_std
%find_lang %_name2

%files -f %_name2.lang
%_libdir/claws-mail/plugins/%_name2.so

%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.0.8-alt1
- Updated to 0.0.8.

* Fri Mar 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.0.7-alt1.1
- rebuilt against newest clutter

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1
- Updated to 0.0.7.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1
- Drop obsoleted configure-libchamplain-fix.patch.
- Updated to 0.0.6.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.0.5-alt1
- Minor spec cleanup, sources: tar.gz -> tar.
- Updated to 0.0.5.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.0.4-alt2
- rebuild for claws-mail 3.7.8

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.0.4-alt1
- Updated to 0.0.4.

* Mon Oct 11 2010 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt2
- use autoreconf
- fix configure for libchamplain-gtk-0.8.0
- rebuild with libchamplain-gtk-0.8.0

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1
- 0.0.3

* Mon Jan 11 2010 Alexey Rusakov <ktirf@altlinux.org> 0.0.2-alt1
- Initial Sisyphus build

