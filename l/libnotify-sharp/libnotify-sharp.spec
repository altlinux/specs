%define oname notify-sharp
Name: libnotify-sharp
Version: 0.4.0
Release: alt4.svn3037

License: X11/MIT
Url: http://trac.galago-project.org/wiki/DesktopNotifications
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

Source: %oname-%version.tar.gz
Group: Development/Other
Summary: notify-sharp is a C# client implementation for Desktop Notifications

BuildRequires: libgcc libgtk-sharp2-devel mono-mcs ndesk-dbus-glib-devel monodoc-devel

BuildPreReq: rpm-build-mono
BuildRequires: /proc

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%package monodoc
Summary: Development documentation for %name
Group: Development/Other
BuildArch: noarch

%description monodoc
This package contains the API documentation for %name in Monodoc format.

%prep
%setup -n %oname-%version
%__subst "s|\$(DESTDIR)\$(libdir)|\$(DESTDIR)%_monodir/..|" src/Makefile.*

%build
%autoreconf
%configure --disable-static
%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_monogacdir/*
%_monodir/notify-sharp

%files devel
%_pkgconfigdir/*

%files monodoc
%_monodocdir/%oname-docs.*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt4.svn3037
- svn version r3037
- update buildreq
- change Packager

* Fri Dec 19 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt3
- fix build with new %%_monodocdir macros

* Sat Nov 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt2
- fix build on x86_64 (fix bug #17959)
- add doc files, add monodoc subpackage (thanks Alexey Shabalin)

* Sun Oct 26 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Mar 25 2008 ro@suse.de
- added ndesk-dbus-glib-devel to buildreq
* Fri Nov 09 2007 mauro@suse.de
- Added a Requires notification-daemon to fix bnc #328526.
* Mon Aug 06 2007 ro@suse.de
- fix build on lib64 (mono is in /usr/lib regardless)
* Mon Jul 23 2007 mauro@suse.de
- Package added to pdb.
- Initial submit to factory.
- Docs disabled in this version in order to get the build done.
* Thu Jun 21 2007 maw@suse.de
- Don't build as root.
  Mon Jun 11 2007 12:00:00 EST 2007 - calvinrg@gmail.com
- Initial package, version 0.4.0
