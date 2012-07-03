Name: giver
Url: http://code.google.com/p/giver/
Version: 0.1.8
Release: alt2
License: X11/MIT
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.bz2
Patch: bnc-326064.txt
Group: Networking/File transfer
Summary: A simple file sharing desktop application

# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: GConf gcc-c++ 
BuildRequires: libavahi-sharp-devel libgnome-sharp-devel libnotify-sharp-devel
BuildRequires: mono-devel mono-mcs perl-XML-Parser

%description
Giver is a simple desktop file sharing application based that uses
Avahi and http to advertise and transfer files.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang giver

%files -f giver.lang
%dir %_libdir/giver
%_libdir/giver/*
%_bindir/giver
%dir %_datadir/giver
%_datadir/giver/*
%_niconsdir/*
%_liconsdir/*
%_miconsdir/*
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 0.1.8-alt2
- fix buildreq

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 0.1.8-alt1
- initial build from SuSe

* Fri Sep 21 2007 - mauro@suse.de
- Added bnc-326064.txt to fix bnc #326064
* Sun Sep 02 2007 - ro@suse.de
- remove lib64 usage as package is noarch
* Fri Aug 03 2007 - cgaisford@suse.de
- Updated to 0.1.8 which has a new license
* Fri Jul 27 2007 - maw@suse.de
- Realize mindblowing space savings by bzipping the source tarball
- Add some %%fdupes goodness
- Add some %%find_lang goodness
- Don't attempt to package directories that are owned by other
  packages
- Build as noarch.
* Thu Jul 26 2007 - mauro@suse.de
- Version 0.1.7 just added to autobuild
