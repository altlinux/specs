%global	main_version	2.1.6
Name: xfe
Version: 2.1.6
Release: alt1

Summary: MS-Explorer or Commander like file manager for X
License: GPLv2+
Group: File tools

Url: http://roland65.free.fr/xfe/
Source: %name-%version.tar.xz
Patch0:	xfe-2.0-use-system-libsn.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Mon Oct 09 2017
# optimized out: fontconfig fontconfig-devel glibc-kernheaders-x86 gnu-config libX11-devel libXrender-devel libfreetype-devel libstdc++-devel perl perl-Encode perl-XML-Parser pkg-config python-base tzdata xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-kernheaders-generic imake intltool libXft-devel libfox-devel libpng-devel xorg-cf-files

BuildRequires: desktop-file-utils

BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libstartup-notification-devel
BuildRequires:	/usr/bin/pkexec
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(x11-xcb)

BuildRequires:	autoconf
BuildRequires:	automake


%description
X File Explorer (Xfe) is a filemanager for X. It is based on the popular
X Win Commander, which is discontinued. Xfe is desktop independent and
is written with the C++ Fox Toolkit. It has Windows Commander or
MS-Explorer look and is very fast and simple. The main features are:
file associations, mount/umount devices, directory tree for quick cd,
change file attributes, auto save registry, compressed archives
view/creation/extraction and much more.

%prep
%setup -q -n %{name}-%{main_version}
%patch -p1

for f in \
	ChangeLog
do
	mv $f{,.iso}
	iconv -f ISO-8859-1 -t UTF-8 -o $f{,.iso}
	touch -r $f{.iso,}
	rm -f $f.iso
done

# Fix libreoffice related command name (bug 1788292)
sed -i.oo xferc.in \
	-e 's|lobase|oobase|g' \
	-e 's|localc|oocalc|g' \
	-e 's|lodraw|oodraw|g' \
	-e 's|loimpress|ooimpress|g' \
	-e 's|lomath|oomath|g' \
	-e 's|lowriter|oowriter|g' \
	%{nil}

# Patch0
autoreconf -fi
rm -rf libsn

%build
%configure --enable-release
%make_build


%install
%makeinstall_std
%find_lang %name


# Tweak too generic and short names
mkdir -p %{buildroot}%{_datadir}/%{name}/pixmaps
mkdir -p %{buildroot}%{_bindir}
for suffix in \
	a i e p w
do
	cat > %{buildroot}%{_bindir}/xfe-xf${suffix} <<EOF
#!/bin/sh
export PATH=%{_libexecdir}/%{name}:\$PATH
exec xf${suffix} \$@
EOF
	chmod 0755 %{buildroot}%{_bindir}/xfe-xf${suffix}

	mv %{buildroot}%{_datadir}/applications/{,xfe-}xf${suffix}.desktop
	# Modify desktop file
	sed -i \
		-e "\@^Exec=@s|xf${suffix}|xfe-xf${suffix}|" \
		%{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop
	desktop-file-validate %{buildroot}%{_datadir}/applications/xfe-xf${suffix}.desktop

	mv %{buildroot}%{_mandir}/man1/{,xfe-}xf${suffix}.1
done

# Move configuration files
mkdir %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/xferc \
	%{buildroot}%{_sysconfdir}
ln -sf ../../../%{_sysconfdir}/xferc %{buildroot}%{_datadir}/%{name}/xferc


%files -f %name.lang

%doc AUTHORS COPYING README TODO BUGS
%config(noreplace)	%{_sysconfdir}/xferc
%_bindir/*
%_datadir/xfe/
%_desktopdir/xf*.desktop
%dir	%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/icons/default-theme/
%{_datadir}/%{name}/icons/gnome*-theme/
%{_datadir}/%{name}/pixmaps/

%{_datadir}/icons/hicolor/*/apps/xf*.*

%{_datadir}/polkit-1/actions/org.xfe.root.policy

#_pixmapsdir/*
%_man1dir/*


%changelog
* Sun Mar 29 2026 Ilya Mashkin <oddity@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Tue Mar 03 2026 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Feb 22 2026 Ilya Mashkin <oddity@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Jan 22 2026 Ilya Mashkin <oddity@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri Jan 09 2026 Ilya Mashkin <oddity@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Thu Sep 25 2025 Ilya Mashkin <oddity@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Mike Radyuk <torabora@altlinux.org> 1.42-alt1
- New version (closes: #25570, #27616)

* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.32.3-alt1.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.32.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xfe

* Tue Apr 12 2011 Mike Radyuk <torabora@altlinux.org> 1.32.3-alt1
- initial build for ALT Linux Sisyphus (closes: #23321)
