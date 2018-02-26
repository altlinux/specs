#
# spec file for package libx86emu (Version 1.1)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Steffen Winterfeldt
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


ExclusiveArch:  %ix86 x86_64

Name:           libx86emu
License:        BSD 3-Clause
Group:          System/Libraries
Summary:        A small x86 emulation library.
Version:        1.1
Release:        alt1
Url:            http://download.opensuse.org/source/factory/repo/oss/suse/src/
Source:         %name-%version.tar
Packager:       Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description
Small x86 emulation library with focus of easy usage and extended
execution logging functions.



Authors:
--------
    Steffen Winterfeldt

%package        devel
License:        BSD 3-Clause
Summary:        A small x86 emulation library.
Group:          System/Libraries
Requires:       %name = %version-%release

%description    devel
Small x86 emulation library with focus of easy usage and extended
execution logging functions.



Authors:
--------
    Steffen Winterfeldt

%prep
%setup

%build
%make_build LIBDIR=%_libdir

%install
install -d -m 755 %buildroot%_libdir
%makeinstall_std LIBDIR=%_libdir

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/x86emu.h
%doc README LICENSE

%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

* Wed Jun 10 2009 snwint@suse.de
- avoid that error in future
* Tue Jun  9 2009 coolo@novell.com
- fix typo
* Tue Jun  9 2009 snwint@suse.de
- export only API functions in shared lib
* Wed Apr  8 2009 snwint@suse.de
- upgraded to version 1.0
- align to package conventions
