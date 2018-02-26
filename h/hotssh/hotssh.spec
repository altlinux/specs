BuildRequires: desktop-file-utils
%define ver_major 0.2

Name: hotssh
Version: %ver_major.7
Release: alt1.qa1.1

Summary: Secure Shell Client
Group: Networking/Remote access
License: GPLv2+
Url: http://www.gnome.org/projects/hotssh

Source: http://ftp.gnome.org/pub/GNOME/sources/%name/%ver_major/%name-%version.tar.bz2

BuildArch: noarch

BuildRequires: intltool python-devel python-module-dbus-devel python-module-pygtk-devel

%description
HotSSH is an interface to Secure Shell, for GNOME and OpenSSH. It
intends to be a better experience than simply invoking "ssh" from an
existing terminal window.

%prep
%setup -q

%build
./waf configure --prefix=%prefix
./waf

%install
./waf install --destdir=%buildroot

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/hotssh.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_iconsdir/hicolor/*/*/*
%python_sitelibdir/hotssh/
%exclude %_docdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.7-alt1.qa1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.7-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hotssh

* Sat Feb 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- first build for Sisyphus

