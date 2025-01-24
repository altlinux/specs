#
# spec file for package libcerror
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: libcerror
Version: 20240413
Release: alt1

Summary: Library for cross-platform C error functions
License: LGPLv3+
Group: Development/C

#DL-URL: https://github.com/libyal/libcerror/releases/download/20240413/libcerror-beta-20240413.tar.gz
Url: https://github.com/libyal/libcerror
Source: %name-alpha-%version.tar.gz

BuildRequires: pkg-config

%description
A library for cross-platform C error functions.

This package is part of the libyal library collection
and is used by other libraries in the collection.

%package devel
Summary: Development files for libcerror, a cross-platform C error library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C error functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%setup

%build
./autogen.sh
%configure \
	--disable-static \
	--enable-wide-character-type
%make_build

%install
%makeinstall_std

%check
./runtests.sh

%files
%_libdir/%name.so.*

%files devel
%doc AUTHORS ChangeLog COPYING* NEWS README
%_includedir/%name.h
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%changelog
* Thu Dec 26 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 20240413-alt1
- New version 20240413.

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130904-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct  2 2013 Greg.Freemyer@gmail.com
- update to v20130904
  * bug fix for issue under memory limitations
  * code clean up
- make %%description fields slightly more robust
* Sun Jul 28 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * fix in .pc.in
  * updated common files
  * additional bounds checking
  * added FORMAT_MESSAGE_IGNORE_INSERTS to FormatMessage calls
  * textual changes
  * updated dependencies
  * 2013 update
- switch to gz compression to eliminate download / conversion process
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121222) for build.opensuse.org
