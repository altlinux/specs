Name: xfce4-mailwatch-plugin
Version: 1.2.0
Release: alt1

Summary: The Xfce4 Mailwatch Plugin is a multi-protocol, multi-mailbox mail watcher
Summary(ru_RU.UTF8): Многопротокольный апплет для проверки нескольких почтовых ящиков для Xfce4
License: %gpl2only
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/xfce4-mailwatch-plugin
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel libexo-devel
# Automatically added by buildreq on Thu Nov 09 2006
BuildRequires: libSM-devel libgnutls-devel xorg-cf-files libgcrypt-devel

%description
The Xfce4 Mailwatch Plugin is a multi-protocol, multi-mailbox mail watcher.
Currently, the protocols supported are:
  * IMAP (SSL/TLS and cleartext)
  * POP3 (SSL/TLS and cleartext)
  * Mbox mail spool (local)
  * Maildir mail spool (local)
  * MH-Maildir mail spool (local)
  * Google Mail (GMail) mailbox (remote) (requires gnutls)

%prep
%setup

%build
%xfce4reconf
%configure \
    --enable-ssl \
    --enable-ipv6 \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_liconsdir/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Oct 28 2013 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Drop obsoleted patches.
- Updated Url.
- Updated to 1.2.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt7
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt6
- Rebuild with xfce4-panel-4.9.

* Sun Feb 06 2011 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt5
- Add patches from Debian:
    + fix high CPU usage
    + link against libxfcegui4
    + fix mbox refresh interval
    + Link against libgcrypt
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated.
- Fix License.

* Mon Nov 24 2009 Dmitriy Kruglikov <dkr@altlinux.ru> 1.1.0-alt4
- Added icons

* Mon Nov 22 2009 Dmitriy Kruglikov <dkr@altlinux.ru> 1.1.0-alt3
- Updated to spec. New BuildRequires:

* Sat Nov 21 2009 Dmitriy Kruglikov <dkr@altlinux.ru> 1.1.0-alt1
- Updated to current (1.1.0) stable version. Tested IMAP(s) and Gmail.
- New translations.

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.0.1-alt1
- First version of RPM package for Sisyphus.
