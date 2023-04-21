Name: xfce4-mailwatch-plugin
Version: 1.3.1
Release: alt1

Summary: The Xfce4 Mailwatch Plugin is a multi-protocol, multi-mailbox mail watcher
Summary(ru_RU.UTF8): Многопротокольный апплет для проверки нескольких почтовых ящиков для Xfce4
License: GPL-2.0-only
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-mailwatch-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-mailwatch-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel libexo-gtk3-devel
BuildRequires: libgnutls-devel libgcrypt-devel

%define _unpackaged_files_terminate_build 1

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
%patch -p1

%build
%xfce4reconf
%configure \
    --enable-ssl \
    --enable-ipv6 \
    --enable-debug=mimimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%_liconsdir/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri Apr 21 2023 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Mon Nov 09 2020 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Use _unpackaged_files_terminate_build.
- Enabled debug (minimum level).
- Updated BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Updated to 1.3.0.

* Fri Dec 04 2015 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt5
- Rebuild with libgnutls30.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt4
- Rebuild with libxfce4util-4.12.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3
- Rebuild with libgnutls28.

* Thu Jan 30 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- imap: Quote mailbox name (closes: #29776).
- Fix Xfce name (XFCE -> Xfce).

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
