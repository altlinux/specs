Name:		nmapsi4
Version:	0.2.1
Release:	alt1.1
Summary:	NmapSI4 is a qt4 interface for nmap scanner
License:	GPLv2
Group:		Security/Networking
Url:		http://nmapsi4.netsons.org/
Source0:	http://nmapsi4.googlecode.com/files/%name-%version.tar.gz
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildRequires: cmake gcc-c++ libqt4-devel

Requires:	nmap

%description
NmapSi4 is a complete Qt4-based Gui with the design goals
to provide a complete nmap interface for Users, in order
to menagement all option of this power security net scanner!

%prep
%setup -q

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
%make DESTDIR=%buildroot install
chmod +x %buildroot%_bindir/*

%files
%doc AUTHORS NEWS README TODO
%_bindir/*
%_datadir/%name
%_datadir/icons/*/*/apps/%name.png
%_desktopdir/kde/*.desktop

%changelog
* Mon Feb 07 2011 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1.1
- fix build (rules)

* Mon Feb 07 2011 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sun Dec 21 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1
- 0.1.1 released
- changed group from Monitoring to %group

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt2.rc1
- delete post/postun scripts (new rpm)

* Sun Jan 13 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.rc1
- new release candidate - rc1
- use cmake
- exclude COPYING from packaging
- refresh buildrequires with buildreq -bi

* Thu Dec 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.beta3
- new beta3 version
- build for Sisyphus
- remove external desktop-files (use patch for original desktops)

* Thu Nov 01 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt0.beta1
- initial build for ALT Linux
