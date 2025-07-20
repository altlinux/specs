#
# Written 22-09-2004 <phil@firestorm.cx>
#

# git  commit 3c0d4ba89ccd371a0f83683216fb179292e328c8
Summary: Tiny and flexible webcam program
Name: fswebcam
Version: 20200725
Release: alt1.git_1_3c0d4b

License: GPL-2
Group: Video

Source: fswebcam-%version.tar

Url: https://www.sanslogic.co.uk/fswebcam/
Vcs: https://github.com/fsphil/fswebcam


%def_enable 32bit


# Automatically added by buildreq on Sun Jul 20 2025
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error perl sh5
BuildRequires: libgd-devel perl-parent


%description
A tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
%setup

%build
%autoreconf
autoupdate

%configure  \
%if_enabled 32bit
    --enable-32bit-buffer
%endif

%make_build

%install
%makeinstall

%files
%doc README CHANGELOG LICENSE example.conf
%_bindir/fswebcam
%_mandir/man1/fswebcam.1.*

%changelog
* Sun Jul 20 2025 Hihin Ruslan <ruslandh@altlinux.ru> 20200725-alt1.git_1_3c0d4b
- New version

* Sun Jul 20 2025 Hihin Ruslan <ruslandh@altlinux.ru> 20170115-alt1.1
- Fix Buildreq
- Fix License, Fix Url and Vcs

* Tue Apr 18 2017 Hihin Ruslan <ruslandh@altlinux.ru> 20170115-alt1
- New version

* Sun Jan 24 2016 Hihin Ruslan <ruslandh@altlinux.ru> 20160111-alt1
- New version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20070108-alt1.qa1
- NMU: rebuilt for debuginfo.

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
