Summary: Electronic strongbox
Name: gringotts
Version: 1.2.10
Release: alt1.qa1
License: GPL
Group: Editors
URL: http://devel.pluto.linux.it/projects/Gringotts/

Source: http://devel.pluto.linux.it/projects/Gringotts/current/gringotts-%{version}.tar.bz2
Patch: gringotts-1.2.8-gtk24.patch

# Automatically added by buildreq on Tue Jun 22 2010 (-bb)
BuildRequires: imake libICE-devel libgringotts-devel libgtk+2-devel libmcrypt-devel libpopt-devel xorg-cf-files

BuildRequires: gtk2-devel libpopt-devel libgringotts-devel pkgconfig desktop-file-utils

%description
Gringotts is a small but (hopely ;) useful utility that stores sensitive
data (passwords, credit card numbers, friends' addresses) in an organized,
optimized and most of all very secure form.
It uses libGringotts to provide a strong level of encryption, just aiming
to be as trustworthy as possible.

%prep
%setup
%patch0

### FIXME: Include improved desktop-file. (Please fix upstream)
cat <<EOF >gringotts.desktop.in
[Desktop Entry]
Name=Gringotts Data Protection
Comment=Store sensitive data securely
Icon=gringotts
Exec=gringotts
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Utility;
EOF

%build
%configure
%make_build

%install
%makeinstall
%find_lang %{name}
install -d -m0755 %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/gnome/apps/Utilities/gringotts.desktop %{buildroot}%{_datadir}/applications
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=Settings \
	--add-category=X-PersonalSettings \
	%buildroot%_desktopdir/gringotts.desktop

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog FAQ NEWS README TODO
%{_bindir}/gringotts
%{_datadir}/pixmaps/gringotts*.xpm
%{_datadir}/applications/gringotts.desktop

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.10-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gringotts
  * postclean-03-private-rpm-macros for the spec file

* Tue Jun 22 2010 Mykola Grechukh <gns@altlinux.ru> 1.2.10-alt1
- first build for altlinux

* Wed Jun 29 2004 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Fix for gtk 2.4. (Rok Mandeljc)

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Add improved desktop file.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Updated to release 1.2.8.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.2.7-0
- Updated to release 1.2.7.

* Thu Apr 18 2003 Dag Wieers <dag@wieers.com> - 1.2.6-0
- Updated to release 1.2.6.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Initial package. (using DAR)
