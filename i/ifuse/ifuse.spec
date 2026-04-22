# no git-version-gen in tarball
%def_enable snapshot

Name: ifuse
Version: 1.2.1
Release: alt1

Summary: Filesystem access for the iPhone and iPod Touch
Group: Communications
License: LGPL-2.1
Url: http://www.libimobiledevice.org/

Vcs: https://github.com/libimobiledevice/ifuse

%if_disabled snapshot
#Source: %url/downloads/%name-%version.tar.bz2
Source: https://github.com/libimobiledevice/ifuse/releases/download/%version/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif

%define fuse_ver 3.0
%define plist_ver 2.2.0
%define imobiledevice_ver 1.4.0

Requires: fuse3 >= %fuse_ver

BuildRequires: libfuse3-devel >= %fuse_ver
BuildRequires: libplist-devel >= %plist_ver
BuildRequires: libimobiledevice-devel >= %imobiledevice_ver

%description
iFuse is a FUSE filesystem driver which uses libiphone to connect to devices
without the need for a jailbreak.
It is using the native Apple "AFC" protocol, over the normal USB cable in order
to access the iPhone's or iPod Touch's media files under Linux.

%prep
%setup
echo %version > .tarball-version

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/ifuse
%_man1dir/ifuse.1*
%doc AUTHORS README*

%changelog
* Wed Apr 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Oct 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jun 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt2
- updated to 1.1.4-9-gbbf2838

* Tue Jun 16 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Thu Dec 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt5
- updated to 1.1.3-6-ge75d32c

* Mon Feb 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt4
- rebuilt against libimobiledevice.so.6

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt3
- rebuilt against libimobiledevice.so.5/libplist.so.3

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt2
- rebuilt against libplist.so.2

* Thu Mar 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt2
- rebuilt against libimobiledevice.so.4

* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt3
- rebuild against libimobiledevice-1.1.3

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt2
- rebuild against libimobiledevice-1.1.1

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 0.9.7-alt1
- 0.9.6 -> 0.9.7

* Tue Jan 26 2010 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt1
- 0.9.5 -> 0.9.6

* Wed Dec 23 2009 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- build for Sisyphus

