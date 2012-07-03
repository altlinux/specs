%define _name gtkhtml2
%define _name2 gtkhtml2_viewer
%def_disable debug

Name: claws-mail-plugin-%_name
Version: 0.33
Release: alt1

Summary: HTML renderer plugin for Claws Mail
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name2-%version.tar
Patch1: %name-0.18-alt-static-libgtkhtml.patch

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

BuildPreReq: gettext-tools >= 0.15
BuildPreReq: glib2-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libgtkhtml2-devel libcurl-devel

%description
The Gtkhtml2Viewer plugin is an HTML renderer plugin for Claws Mail. It
features:

    * Basic rendering of HTML message parts
    * Displaying of attached images
    * Optional fetching and displaying of remote images
    * Remote image caching
    * The ability to Reply to the message, quoting the selected text

%prep
%setup -q -n %_name2-%version
%patch1 -R -p1

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
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.33-alt1
- Updated to 0.33.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.32-alt1
- Updated to 0.32.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.31-alt1
- Updated to 0.31.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.30-alt1
- Minor spec cleanup, sources: tar.gz -> tar.
- Updated to 0.30.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.29-alt1
- Updated to 0.29.

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.28-alt1
- Drop cvs build requires.
- Updated to 0.28.

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.27-alt1
- New version.

* Sat Jan 16 2010 Alexey Rusakov <ktirf@altlinux.org> 0.26-alt1
- New version.

* Wed Jul 08 2009 Alexey Rusakov <ktirf@altlinux.org> 0.24-alt1
- New version 0.24 (with rpmrb script).

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.23-alt1
- New version (0.23).
- Don't pass parameters to %%autoreconf the second time.
- Removed no more necessary libgnutls-devel buildreq, it is installed as
  a dependency of claws-mail-devel from now on.

* Thu Oct 16 2008 Alexey Rusakov <ktirf@altlinux.org> 0.21-alt1
- New version (0.21).
- Updated the patch for system libgtkhtml2.
- Updated buildreqs (Claws Mail now uses gnutls instead of openssl).

* Mon May 26 2008 Alexey Rusakov <ktirf@altlinux.org> 0.18-alt2
- Rebuild for the updated Claws Mail.

* Tue Apr 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.18-alt1
- New version (0.18).
- Added a patch that switches off static libgtkhtml2 building/linking.
- Added a strange buildreq of cvs, needed by autopoint for some reason.

* Sat Apr 12 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17.2-alt2
- Build with updated Claws Mail.

* Mon Mar 24 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17.2-alt1
- New version (0.17.2).

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- New version (0.17).
- Removed workarounds.

* Tue Nov 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- new version (0.16)
- Require exact version of Claws Mail the plugin was built with (yes this
  is terrible, but Claws Mail refuses to load plugins built with older
  version anyway).

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.2-alt1.2
- rebuilt with new Claws Mail

* Tue Oct 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.2-alt1.1
- rebuild with Claws Mail 3.0.2

* Tue Sep 04 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.2-alt1
- new version (0.15.2), for Claws Mail 3.0.0
- the license has changed to %gpl3plus

* Wed Aug 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15.1-alt1
- new version (0.15.1), for Claws Mail 2.10.0

* Sun May 20 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt2
- rebuilt with new ClawsMail (should I restrain the limitation to the minor
  version too?).

* Sat Apr 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt1
- new version (0.15)
- added limitation of claws-mail's major version to requirements.

* Sun Apr 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Thu Feb 08 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14.1-alt1
- Initial Sisyphus version.

