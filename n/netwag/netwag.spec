Name: netwag
Version: 5.34.0
Release: alt1.qa4

Summary: GUI for netwox
License: GPL
Group: Networking/Other

Url: http://www.laurentconstantin.com/en/netw/netwag/
Source0: http://www.laurentconstantin.com/common/netw/netwag/download/v5/%name-%version-src.tgz
Source1: %name.desktop
Patch0: %name-config.patch
BuildArch: noarch

Requires: netwox
# Automatically added by buildreq on Thu Feb 16 2006
BuildRequires: netwox tk xterm
BuildRequires: desktop-file-utils

%description
GUI for Netwox (Netwox is a toolbox for network administrators and
network hackers).

%prep
%setup -q -n %name-%version-src
%patch0 -p1

%build
cd src
./genemake
sed -i -e 's,444,644,' -e 's,555,755,g' Makefile
%make

%install
install -d %buildroot{%_bindir,%_man1dir,%_desktopdir}

%make -C src install \
	INSTBIN=%buildroot%_bindir \
	INSTMAN1=%buildroot%_man1dir \
	INSTUSERGROUP="$(id -u):$(id -g)"

install %SOURCE1 %buildroot%_desktopdir
rm -f doc/gpl.txt
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Security \
	%buildroot%_desktopdir/netwag.desktop

%files
%doc doc/*.txt
%_bindir/*
%_man1dir/*
%_desktopdir/*

%changelog
* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 5.34.0-alt1.qa4
- NMU: fix desktop permissions

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 5.34.0-alt1.qa3
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for netwag

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.34.0-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for netwag
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 5.34.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for netwag

* Fri Apr 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.34.0-alt1
- new version (5.34.0)

* Mon Mar 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt2
- Added dependency on netwox (reported by Arioch)

* Thu Feb 16 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt1
- Initial build for Sisyphus (adopted spec from PLD)
