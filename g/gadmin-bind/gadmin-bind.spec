Name: gadmin-bind
Version: 0.2.3
Release: alt3

Summary: Gadmin-bind -- A GTK+ administation tool for ISC bind
Group: System/Configuration/Other
Source: %name-%version.tar.gz
Source1: %name.pam
Patch1: alt-%name-desktop.patch
Patch: alt-chroot-path.patch
License: GPL

# Automatically added by buildreq on Mon Apr 30 2007
BuildRequires: libgtk+2-devel ImageMagick
Obsoletes: gbindadmin < 2.0
Provides: gbindadmin

%description
GBINDADMIN is a fast and easy to use GTK+ administration tool for ISC BIND.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%configure SYSINIT_START_CMD="chkconfig bind on" SYSINIT_STOP_CMD="chkconfig bind off" --localstatedir=%_var

%make_build

%install
%make DESTDIR=%buildroot install
rm -r %buildroot%_docdir/%name
install -d %buildroot%_bindir
# pam auth
install -d %buildroot%_sysconfdir/pam.d/
install -d %buildroot%_sysconfdir/security/console.apps
install -m 644 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -m 644 etc/security/console.apps/%name %buildroot%_sysconfdir/security/console.apps/%name

# desktop entry
install -d %buildroot%_desktopdir
install -m 644 desktop/%name.desktop %buildroot%_desktopdir/%name.desktop

ln -s consolehelper %buildroot%_bindir/%name
for size in 16x16 32x32 48x48 ; do
    mkdir -p %buildroot%_iconsdir/hicolor/$size/apps
    convert %buildroot%_pixmapsdir/%name.png -size $size %buildroot%_iconsdir/hicolor/$size/apps/%name.png
done

%find_lang %name

%files -f %name.lang
%doc README AUTHORS ChangeLog COPYING
%_bindir/%name

%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*

%_desktopdir/*.desktop

%_sbindir/%name
%_pixmapsdir/%name.png
%dir %_pixmapsdir/%name
%_pixmapsdir/%name/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt3
- Fixed localstatedir location.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.3-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Mar 12 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.3-alt2
- fix desktop file (tnx repocop)
- fix icons (tnx repocop)

* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.3-alt1
- new version
- rename with upstream

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.1.5-alt0.1
- first build

