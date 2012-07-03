Name: libzeitgeist
Version: 0.3.12
Release: alt1

Summary: Client library for applications that want to interact with the Zeitgeist daemon

Group: System/Libraries
License: LGPLv3 and GPLv3
Url: https://launchpad.net/libzeitgeist

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://launchpad.net/%name/0.3/%version/+download/%name-%version.tar

Patch: %name-log_fix.patch

# zeitgeist is just a runtime and the reason to install libzeitgeist
Requires: zeitgeist

# Automatically added by buildreq on Tue Jul 12 2011
# optimized out: glib2-devel pkg-config
BuildRequires: glibc-devel gtk-doc libgio-devel

%description
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1 -b .log

%build
%configure --disable-static
%make_build V=1

%check
make check

%install
%makeinstall_std INSTALL="install -p"
install -d -p -m 755 %buildroot%_datadir/vala/vapi
install -D -p -m 644 bindings/zeitgeist-1.0.{vapi,deps} %buildroot%_datadir/vala/vapi
find %buildroot -name '*.la' -exec rm -f {} ';'

# remove duplicate documentation
rm -fr %buildroot%_docdir/%name

%files
# documentation
%doc COPYING COPYING.GPL README

# essential
%_libdir/*.so.*

%files devel
# Documentation
%doc AUTHORS ChangeLog COPYING COPYING.GPL MAINTAINERS NEWS
%doc examples/*.vala examples/*.c
%_datadir/gtk-doc/html/zeitgeist-1.0/

# essential
%_includedir/zeitgeist-1.0/
%_pkgconfigdir/zeitgeist-1.0.pc
%_libdir/*.so

# extra
%_datadir/vala/vapi/

%changelog
* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3.12-alt1
- new version 0.3.12 (with rpmrb script)

* Tue Jul 12 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.10-alt1
- initial build for ALT Linux Sisyphus

* Wed Apr 06 2011 Renich Bon ciric <renich@woralelandia.com> - 0.3.10-1
- Updated to version 0.3.10
- Fixed bugs:
    https://bugs.launchpad.net/ubuntu/+source/libzeitgeist/+bug/742438
- Renamed log fix patch to something more appropriate

* Sat Apr 02 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-4
- Added -p to install statements (forgot some)
- Moved README to the main package from devel

* Fri Mar 25 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-3
- Removed Rubys geo2 dependency since is not needed; it's provided by glibc-devel

* Thu Mar 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-2
- Log test failure repaired by patch from Mamoru Tasaka

* Mon Mar 21 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-1
- Updated to 0.3.6
- Implemented the isa macro for the devel subpackage.
- Eliminated the doc macro from gtk-doc since it gets marked automatically

* Sat Mar 12 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-3
- Removed mistaken isa macro from zeitgeist require

* Thu Mar 10 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-2
- Cleaned up old stuff (BuildRoot, Clean and stuff of sorts)
    https://fedoraproject.org/wiki/Packaging/Guidelines#BuildRoot_tag
    https://fedoraproject.org/wiki/Packaging/Guidelines#.25clean
- Added glib2-devel and gtk-doc as a BuildRequires
- Added GPLv3 since it covers the documentation examples
- Updated Requires to use the new arch specification macro when accordingly
    https://fedoraproject.org/wiki/Packaging/Guidelines#Requires
- Configured install to preserve timestamps
- Added V=1 to the make flags for more verbosity on build
- Added a check section
- Removed disable-module from configure statement since it's not needed anymore:
    https://bugs.launchpad.net/libzeitgeist/+bug/683805

* Thu Feb 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-1
- updated to latest version

* Sun Feb 06 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-3
- got rid of INSTALL from docs
- got rid ot dorcdir and used doc to include html docs

* Sat Feb 05 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-2
- removed duplicate documentation
- added the use of macros for everything; including source and build dir.
- revised path syntax

* Thu Jan 27 2011 - Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-1
- First buildName: libzeitgeist
