Name: linscope
Version: 0.3.2
Release: alt4.qa1

Summary: Network scanner for network shares (SMB)
License: GPL
Group: Networking/Other
Url: http://sourceforge.net/projects/%name
Source0: %name-%version.tar
Source1: README.ALT
Source2: %name.desktop

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

BuildRequires(pre): rpm-macros-qt3
# Automatically added by buildreq on Mon Oct 27 2008
BuildRequires: gcc-c++ kdelibs-devel qt3-designer
BuildRequires: desktop-file-utils

%description
LinScope is GUI, port scanner with enumerating windows network shares (SMB).
LinScope can save favorites list. You can add different ip address ranges
and scan them apart or together. Linscope searches FTP and HTTP services too.
It works in large networks and internet, where broadcast traffic is disabled
(uses direct ip address and rpcclient from samba). User could manually assign
command s for opening shares, apart for ftp,http and smb.

%prep
%setup -n Linscope

%build
cd linscope
PATH=$PATH:%_qt3dir/bin
qmake
sed -i -e "s,^UIC \(.*\),UIC\1 -nounload," Makefile
%make

%install
install -D %name/lrpcscanip %buildroot%_bindir/lrpcscanip
install %name/%name %buildroot%_bindir/%name
install -pD -m0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -d %buildroot%_datadir/%name
install -pD -m0644 %name/linscope_*.qm %buildroot%_datadir/%name
install -pD -m0644 %SOURCE1 README.ALT
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Security \
	%buildroot%_desktopdir/linscope.desktop

%files
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name/*
%dir %_datadir/%name
%doc CHANGES.TXT README.TXT TODO.TXT README.ALT

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.2-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for linscope

* Tue Mar 16 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.2-alt4
- Fix building.

* Wed Dec 03 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.2-alt3
- Remove obsolete %%clean_menus/%%update_menus calls.

* Mon Oct 27 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.2-alt2
- Fix build with gcc4.3.
- Fix repocop warnings for desktop-file.
- Update buildreqs.

* Tue Feb 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3.2-alt1
- Initial build for Sisyphus (adopted spec from Dries Verachtert
  <dries@ulyssis.org>).
- Added linscope-0.3.2-alt-translation.patch for correct path to
  .qm-files.
