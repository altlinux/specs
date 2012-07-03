#
# spec file for package vdfuse (Version 8.2a)
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: vdfuse
Version: 8.2a
Release: alt1

Summary: Application for mounting vdi images
License: GPLv3
Group: System/Kernel and hardware

%define virtualbox_version 4.1.8

# yes, only forum
Url: http://forums.virtualbox.org/viewtopic.php?f=7&t=17574

# we need includes from virtualbox
Source: VirtualBox-%virtualbox_version-include-only.tar.bz2
# and of cource source code :)
Source1: vdfuse-v82a.c
# script to extract includes from virtualbox sources
Source99: virtualbox-patch-source

Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libfuse-devel
BuildRequires: virtualbox

%description
This program presents a virtual disk as a Filesystem in User
Space (FUSE).  The separate partitions appear as block files
Partition1, ... under the mount point.  You can then mount any or
all of the partitions as a Loop Device. If you use the readonly
flag then these files are readonly and the partitions themselves
can only be mounted readonly.

NB: you will need to add "user_allow_other" to /etc/fuse.conf

%prep
%setup -n VirtualBox-%{virtualbox_version}_OSE

%build
export LD_LIBRARY_PATH=%_libdir/virtualbox/
${CC:-gcc} %SOURCE1 -o %name \
    `pkg-config --cflags --libs fuse` \
    -I./include \
    -Wl,-rpath,%_libdir/virtualbox/ \
    -l:%_libdir/virtualbox/VBoxDD.so \
    -l:%_libdir/virtualbox/VBoxDD2.so \
    -l:%_libdir/virtualbox/VBoxDDU.so \
    -Wall %optflags

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 8.2a-alt1
- initial build for ALT Linux Sisyphus (based on opensuse package)

* Fri Jan 20 2012 tejas.guruswamy@opensuse.org
- Update VirtualBox sources to 4.1.8
* Sun Jun  5 2011 tejas.guruswamy@opensuse.org
- Update VirtualBox sources to 4.0.8
- Update source file to v82a
* Sat Feb 26 2011 tejas.guruswamy@opensuse.org
- Update VirtualBox sources to 4.0.4
* Tue Jan  4 2011 tejas.guruswamy@opensuse.org
- Update to v82
- Add patch for Virtualbox 4.0.0 compatibility
* Sun Apr 25 2010 masterpatricko@gmail.com
- Build against VirtualBox OSE 3.1.6
* Fri Feb 26 2010 masterpatricko@gmail.com
- Update to v70
  * minor compile-time bug fix: VBOX_SUCCESS was removed from the trunk source; replace with RT_SUCCESS
* Fri Aug 21 2009 mseben@novell.com
- initial openSUSE package
