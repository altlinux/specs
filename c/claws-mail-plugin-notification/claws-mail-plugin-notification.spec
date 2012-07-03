%define _name notification
%define _name2 notification_plugin

%def_disable lcdproc
%def_disable indicator
%def_enable hotkeys

Name: claws-mail-plugin-%_name
Version: 0.30
Release: alt1

Summary: Various ways to notify the user of new and unread email. 
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name2-%version.tar
Patch1: %_name2-0.28-fix-ru.po.patch

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: claws-mail-devel >= 3.7.3.22
BuildPreReq: glib2-devel >= 2.6.0
# Trayicon module needs 2.10.0, others go well with 2.6.0
BuildPreReq: libgtk+2-devel >= 2.10.0
BuildPreReq: libnotify-devel
BuildPreReq: libcanberra-devel >= 0.6
%{?_enable_indicator:BuildPreReq: libindicate-devel >=  0.3.0}
%{?_enable_hotkeys:BuildPreReq: libgio-devel >= 2.15.6}

%description
The Notification plugin provides various ways to notify the user of new and
possibly unread mail. Currently, the following modules are implemented:

    * A mail banner (stocks ticker-like widget)
    * A popup window
    * A command to be issued on new mail arrival

All modules can be activated or deactivated at compilation time, and are
highly configurable at run time. It is possible to include only selected
folders in any module. In general, the notification is executed after
filtering, so it is possible to exclude spam or other unwanted messages
from notification.

%prep
%setup -q -n %_name2-%version
%patch1 -p1

%build
%autoreconf
%configure \
    --disable-static \
    --enable-popup \
    --enable-banner \
    --enable-command \
    --enable-trayicon \
    --enable-libnotify \
    %{subst_enable lcdproc} \
    %{subst_enable indicator} \
    %{subst_enable hotkeys} \

# Rebuild ru.gmo to apply changes from claws-mail-0.24-fix-ru.po.patch
cd po; make ru.gmo; cd -

%make

%install
%makeinstall_std
%find_lang %_name2

%files -f %_name2.lang
%_libdir/claws-mail/plugins/%_name2.so

%exclude %_libdir/*/*/*.la
# XXX: It's hard to believe so far that someone uses development files to
# extend the hotkeys feature of this plugin. So we just skip them
%exclude %_includedir/claws-mail/plugins/%_name2

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.30-alt1
- Updated to 0.30.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.29-alt1
- Updated to 0.29.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.28-alt1
- Drop obsoleted alt-libnotify07.patch.
- Updated fix-ru.po.patch.
- Updated to 0.28.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.27-alt1
- Updated fix-ru.po.patch.
- Minor spec cleanup, sources: tar.gz -> tar.
- Build with libnotify-0.7.
- Updated to 0.27.

* Wed Mar 09 2011 Mikhail Efremov <sem@altlinux.org> 0.26-alt3
- Disable libindicate support.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.26-alt2
- rebuild for claws-mail 3.7.8

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.26-alt1
- Updated to 0.26.

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.25-alt1
- Rebuild ru.gmo to apply changes from claws-mail-0.24-fix-ru.po.patch
- New version.

* Fri Aug 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.24-alt1.1
- rebuilt with new libindicate
- fix build requires

* Sat Jan 16 2010 Alexey Rusakov <ktirf@altlinux.org> 0.24-alt1
- New version.
- Two new features enabled: global hotkeys and indicator applet.

* Thu Jul 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.22-alt1
- New version (0.22).
- Added a dependency on libcanberra-gtk in order to make use of fd.o sound
  themes for notifications.

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.21-alt1
- New version (0.21).
- Removed no more necessary libgnutls-devel buildreq, it is installed as
  a dependency of claws-mail-devel from now on.

* Thu Oct 16 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt1
- New version (0.19).
- Updated buildreqs (C-Mail uses gnutls instead of openssl from now on).

* Mon May 26 2008 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt2
- Rebuild for the updated Claws Mail.

* Tue Apr 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- new version (0.19)

* Sat Apr 12 2008 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt2
- Build with updated Claws Mail.

* Mon Mar 24 2008 Alexey Rusakov <ktirf@altlinux.org> 0.15-alt1
- New version (0.15).
- Updated buildreqs.

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.14-alt1
- new version (0.14)

* Tue Nov 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.13-alt1
- new version (0.13)
- Require exact version of Claws Mail the plugin was built with (yes this
  is terrible, but Claws Mail refuses to load plugins built with older
  version anyway).

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12.1-alt1.2
- rebuilt with new Claws Mail

* Tue Oct 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12.1-alt1.1
- rebuilt with Claws Mail 3.0.2

* Sun Sep 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12.1-alt1
- new version (0.12.1)

* Tue Sep 04 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12-alt1
- new version (0.12), for Claws Mail 3.0.0
- the license has changed to %gpl3plus
- a new trayicon module is unconditionally compiled
- a new lcdproc module is compiled if enabled (disabled by default, since
  external LCD displays are not very popular here in Russia, it seems)

* Wed Aug 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.11-alt1
- new version (0.11), for Claws Mail 2.10.0

* Mon May 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.10-alt2
- rebuilt with new ClawsMail.

* Sat Apr 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.10-alt1
- new version (0.10)
- added limitation of claws-mail's major version to requirements.

* Sun Apr 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt1
- Initial Sisyphus version.

