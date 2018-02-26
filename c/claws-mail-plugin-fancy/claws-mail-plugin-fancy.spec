%define _name fancy

Name: claws-mail-plugin-%_name
Version: 0.9.16
Release: alt1

Summary: The Fancy plugin renders html email using the GTK+ port of WebKit library.
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libwebkitgtk2-devel libsoup-gnome-devel

BuildRequires: libcurl-devel

%description
The Fancy plugin renders html email using the GTK+ port of WebKit library.

%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static
%make

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/claws-mail/plugins/%_name.so

%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.9.16-alt1
- Updated to 0.9.16.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.9.15-alt1
- Updated to 0.9.15.

* Tue Nov 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.14-alt3
- Fix bug webkit_web_view_get_selected_text undefined

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.14-alt2
- rebuild with new libwebkitgtk

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.9.14-alt1
- 0.9.14.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.9.13-alt1
- Minor spec cleanup, sources: tar.gz -> tar.
- 0.9.13.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.9.12-alt1
- 0.9.12

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.9.11-alt1
- 0.9.11

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt3
- realy rebuild with new libwebkitgtk

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt2
- rebuild with new libwebkitgtk

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.9.10-alt1
- 0.9.10

* Sat Jan 30 2010 Alexey Rusakov <ktirf@altlinux.org> 0.9.9-alt1
- 0.9.9

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- initial build
