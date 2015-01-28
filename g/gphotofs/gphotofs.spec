#
# spec file for package gphotofs
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name: gphotofs
Version: 0.5
Release: alt2

Summary: User Level File System for gphoto-Based Cameras
License: GPL-2.0+
Group: System/Kernel and hardware

Url: http://gphoto.sourceforge.net
Source: gphotofs-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: glib2-devel
BuildRequires: libfuse-devel
BuildRequires: libgphoto2-devel
BuildRequires: libjpeg-devel

Requires: fuse

%description
This package provides a fuse module to make digital cameras supported
by libgphoto2 visible as a file system.

%prep
%setup

%build
%configure
make

%install
%makeinstall_std mandir=%_mandir

%files
%doc AUTHORS NEWS README
%_bindir/gphotofs

%changelog
* Fri Jan 30 2015 Michael Shigorin <mike@altlinux.org> 0.5-alt2
- rebuilt against current libgphoto2

* Sun Jun 08 2014 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE package)

* Thu Sep 13 2012 meissner@suse.com
- updated to 0.5.0 upstream release
  - adpated to libgphoto2 2.5.0
* Mon Jun 27 2011 ke@suse.de
- Install AUTHORS COPYING NEWS README
* Fri Oct 31 2008 meissner@suse.de
- fixed implicit get*id and a typo in return handling bnc#439324
* Fri Aug 10 2007 bk@suse.de
- Add "Requires: fuse" to ensure that fuse is present (285101#c29)
* Mon Jul 30 2007 meissner@suse.de
- sync to upstream 0.4.0
  - ported code to work with fuse 2.5 too.
  - some small bugfixes
* Mon Jan 15 2007 meissner@suse.de
- upgraded to current trunk.
  - write support, mkdir, rmdir added
* Sun Oct 22 2006 meissner@suse.de
- buildrequires libgphoto2-devel
* Mon Sep  4 2006 meissner@suse.de
- upstream 0.3:
  - Command line options to select a specific camera, like gphoto2.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan  9 2006 meissner@suse.de
- initial gphotofs import.
