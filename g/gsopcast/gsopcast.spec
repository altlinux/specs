Name: gsopcast
Version: 0.4.0
Release: alt3.qa1

Summary: A GTK based GUI front-end for p2p TV sopcast

License: GPL
Group: Video

Url: http://code.google.com/p/gsopcast/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://gsopcast.googlecode.com/files/%name-%version.tar.bz2
Patch: %name-gcc43.patch

# Automatically added by buildreq on Sun Mar 09 2008
BuildRequires: gcc-c++ libalsa-devel libgtk+2-devel perl-XML-Parser
BuildRequires: desktop-file-utils

#Requires: sp-sc >= 1.1.1

%description
A GTK based GUI front-end for p2p TV sopcast.

%prep
%setup -q
%patch

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Multimedia \
	--remove-category=Application \
	--add-category=Video \
	--add-category=TV \
	%buildroot%_desktopdir/gsopcast.desktop

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/%name
%_desktopdir/*
%_pixmapsdir/*

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gsopcast

* Wed Sep 30 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- remove sp-sc requires due sp-sc missed on x86_64

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt2
- add sp-sc requires
- fix build with gcc 4.3

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gsopcast

* Sun Mar 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

