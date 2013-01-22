%define base_name mdm

%define _libexecdir %_libdir/%base_name
%define authentication_scheme pam
%def_disable static
%def_enable ipv6
%def_with xinerama
%def_with xdmcp
%def_with tcp_wrappers
%def_without selinux
%def_with consolekit
%def_with libaudit
%def_disable polkit

Name: mint-display-manager
Version: 1.0.8
Release: alt1

Summary: The Mint Display Manager
License: %gpl2plus
Group: Graphical desktop/Other

Url: https://github.com/linuxmint/mdm
Source: %name-%version.tar
Source1: mdm_xdmcp.control
Source2: mdm-termok-command

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: desktop-file-utils intltool gnome-common gnome-doc-utils libglade-devel libxml2-devel

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: docbook-dtds gcc-c++ gnome-doc-utils-xslt imake intltool libSM-devel libXau-devel libXdmcp-devel libXext-devel libXi-devel libXinerama-devel libdbus-glib-devel libdmx-devel libgnomecanvas-devel libpam-devel libpopt-devel librsvg-devel libwrap-devel xorg-cf-files xsltproc zenity xorg-server

Requires: coreutils consolehelper zenity xinitrc

Conflicts: gdm2.20

#Provides: gdm = %version
#Conflicts: gdm < %version
#Conflicts: gdm > %version

%description
Mdm (the Mint Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Mdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.
Its code based on GDM 2.20. It provides graphical configuration tools,
themeability, remote, automatic and timed login, event scripting,
language selection and it comes with more features than any other
Display Manager currently available.

%package help
Summary: User documentation for Mdm
Group: Graphical desktop/Other
BuildArch: noarch

%description help
This package contains user documentation for Mint Display Manager.

%prep
%setup
%patch -p1

%build
export ac_cv_path_CONSOLE_HELPER=%_bindir/consolehelper
gnome-doc-prepare --force
%autoreconf
%configure \
		--with-sysconfsubdir=X11/mdm \
		--enable-console-helper \
		--enable-authentication-scheme=%authentication_scheme \
		--with-pam-prefix=%_sysconfdir \
		%{?_with_consolekit:--with-console-kit=yes} \
		%{subst_with selinux} \
		%{?_with_libaudit:--with-libaudit=yes} \
		--enable-secureremote=yes \
		--disable-scrollkeeper \
		%{subst_enable static} \
		--disable-dependency-tracking

%make_build
gzip -9nf ChangeLog

%install
mkdir -p %buildroot%_datadir/mdm/autostart/LoginWindow

%make DESTDIR=%buildroot logdir=/var/log/mdm install

mkdir -p %buildroot%_sysconfdir/X11/sessions

ln -s consolehelper %buildroot%_bindir/mdmsetup

# fix custom.conf
subst 's,/usr/lib/mdm,%_libexecdir,g' \
       %buildroot%_sysconfdir/X11/%base_name/custom.conf

# control mdm/xdmcp
install -pDm755 %SOURCE1 %buildroot%_controldir/mdm_xdmcp

# install mdm-termok-command
install -pDm755 %SOURCE2 %buildroot%_sbindir/mdm-termok-command

%find_lang %base_name
%find_lang --output=%base_name-help.lang --without-mo --with-gnome %base_name

%pre
groupadd -r -f %base_name >/dev/null 2>&1
useradd -r -N -c 'MDM' -g %base_name -d /var/lib/mdm -s /dev/null %base_name >/dev/null 2>&1 ||:
%pre_control mdm_xdmcp

%post
%post_control -s disabled mdm_xdmcp

%files -f %base_name.lang
%_bindir/*
%_sbindir/*
%_libexecdir/*
%_libdir/gtk-2.0/modules/lib*.so
%_datadir/%base_name
%_pixmapsdir/*
%_datadir/icons/*/*/*/*.*
%_datadir/xsessions/ssh.desktop

%dir %_sysconfdir/X11/sessions

%config %_controldir/mdm_xdmcp
%config %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/X11/%base_name
%config(noreplace) %_sysconfdir/security/console.apps/*

%_man1dir/*
%doc AUTHORS ChangeLog* NEWS README TODO

%dir %_var/log/mdm
%attr(750, mdm, mdm) %dir %_localstatedir/mdm

%files help -f %base_name-help.lang

%exclude %_libdir/gtk-2.0/modules/lib*.la
%exclude %_datadir/xsessions/gnome.desktop

%changelog
* Tue Jan 22 2013 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Fix LocaleFile path in the mdm.conf.in.
- Masquerade Xreset dependence.
- Pathes from gdm2.20 applied.
- Initial build (spec based on gdm2.20.spec).
