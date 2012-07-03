#
# Written 22-09-2004 <phil@firestorm.cx>
#

Summary: Tiny and flexible webcam program
Name: fswebcam
Version: 20070108
Release: alt1
License: GPL
Group: Video

Source: http://www.firestorm.cx/fswebcam/files/fswebcam-%version.tar.gz
Patch: fswebcam-20070108-as_need.patch

Url: http://www.firestorm.cx/fswebcam/
# Automatically added by buildreq on Mon Oct 29 2007
BuildRequires: libgd2-devel



%description
A tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
%setup -q
%patch0 -p1

%build
%__autoreconf
%configure
%make_build

%install
%makeinstall


%files
%doc README CHANGELOG LICENSE example.conf
%_bindir/fswebcam
%_mandir/man1/fswebcam.1.gz

%changelog
* Mon Oct 29 2007 Hihin Ruslan <ruslandh@altlinux.ru> 20070108-alt1
-- First build for ALT Linux.
 
* Tue Jan 09 2007 Philip Heron <phil@sanslogic.co.uk> - 20070108-1
- Updated for latest release.

* Sun Dec 10 2006 Philip Heron <phil@firestorm.cx> - 20061210-1
- Added example configuration.

* Fri Apr 28 2006 Philip Heron <phil@firestorm.cx> - 20060424-1
- Updated package description, and group.

* Wed Feb 22 2006 Philip Heron <phil@firestorm.cx>
- Updated spec to use configure script and cleaned up.
