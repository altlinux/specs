%define _name rssyl

Name: claws-mail-plugin-%_name
Version: 0.33
Release: alt1

Summary: RSS feed aggregator for Claws Mail
License: %gpl2plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libcurl-devel libxml2-devel

%description
The RSSyl plugin is an RSS feed aggregator for Claws Mail. It has the following
features:

    * Handling of RSS 1.0, RSS 2.0, and Atom feeds
    * Fetching and threaded display of comment feeds
    * Customisable refresh interval for each feed
    * Customisable number of feed items to keep for each feed

Navigating in your feeds and posts is done in the same way as you would for
emails, which makes feed-reading really fast and enjoyable if Claws Mail's
shortcuts are hardwired into your fingers.
Also, the RSSyl plugin unleashes its full potential when used with an HTML
viewer plugin like Dillo or Gtkhtml2Viewer, as this allows fetching a post's
images and font styles.

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
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.33-alt1
- Updated to 0.33.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.32-alt1
- Updated to 0.32.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.31-alt1
- Updated to 0.31.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.30-alt1
- Updated to 0.30.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.29-alt1
- Updated to 0.29.

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.28-alt1
- Updated to 0.28.

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.27-alt1
- New version.

* Sun Jan 17 2010 Alexey Rusakov <ktirf@altlinux.org> 0.26-alt1
- New version.

* Thu Jul 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.25-alt1
- New version (0.25).

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.24-alt1
- New version (0.24).
- Removed no more necessary libgnutls-devel buildreq, it is installed as
  a dependency of claws-mail-devel from now on.

* Thu Oct 16 2008 Alexey Rusakov <ktirf@altlinux.org> 0.22-alt1
- New version (0.22).
- Updated buildreqs (Claws Mail now uses gnutls instead of openssl).

* Mon May 26 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt2
- Rebuild for the updated Claws Mail.

* Tue Apr 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt1
- new version (0.19)

* Sat Apr 12 2008 Alexey Rusakov <ktirf@altlinux.org> 0.18-alt2
- Build with updated Claws Mail.

* Mon Mar 24 2008 Alexey Rusakov <ktirf@altlinux.org> 0.18-alt1
- New version (0.18).

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- New version (0.17).
- Removed a workaround for gettext version.

* Tue Nov 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- new version (0.16)
- Require exact version of Claws Mail the plugin was built with (yes this
  is terrible, but Claws Mail refuses to load plugins built with older
  version anyway).

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt1.2
- rebuilt with new Claws Mail

* Tue Oct 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt1.1
- rebuilt with Claws Mail 3.0.2

* Tue Sep 04 2007 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt1
- new version (0.15), for Claws Mail 3.0.0

* Wed Aug 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14-alt1
- new version (0.14), for Claws Mail 2.10.0

* Mon May 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.13-alt1
- new version (0.13)

* Sat Apr 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12-alt1
- new version (0.12)
- added limitation of claws-mail's major version to requirements.

* Sun Apr 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.11-alt1
- new version 0.11 (with rpmrb script)

* Thu Feb 08 2007 Alexey Rusakov <ktirf@altlinux.org> 0.10-alt1
- Initial Sisyphus version.

