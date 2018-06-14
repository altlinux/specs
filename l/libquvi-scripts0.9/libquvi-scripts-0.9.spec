%define _name libquvi-scripts
%define ver_major 0.9
%define snapshot 20131130

# online tests
%def_without tests
%def_enable check

Name: %_name%ver_major
Version: %ver_major.%snapshot
Release: alt3

Summary: Lua scripts for parsing the media details
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%_name/%ver_major/%_name-%version.tar.xz
Patch: libquvi-scripts-0.9.20130903-alt-pkgconfig.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1134853
Patch1: 0001-guardian.lua-Update-for-website-changes.patch

BuildArch: noarch

Requires: lua5 lua-module-luasocket lua-module-luaexpat lua-module-luajson

#BuildRequires asciidoc-a2x
%{?_with_tests:BuildRequires: glib2-devel libquvi%ver_major-devel libcurl-devel}

%description
%name contains the embedded lua scripts that libquvi uses for parsing
the media details. Some additional utility scripts are also included.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name

%prep
%setup -n %_name-%version
%patch
%patch1 -p1
#subst 's@\(^pkgconfigdir[[:space:]]=[[:space:]]\$(\)libdir\()/pkgconfig\)@\1datadir\2@' Makefile.*

%build
%autoreconf
%configure {?_with_tests:--with-tests}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_datadir/%_name/
%_man7dir/%_name.*
%_man7dir/quvi-modules-3rdparty.7.*
%_man7dir/quvi-modules.7.*
%doc NEWS README AUTHORS

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131130-alt3
- guardian.lua: applied fc fix  for website changes (RHBZ #1134853)
- updated dependencies

* Tue Sep 08 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131130-alt2
- reqs: lua5 lua-module-luasocket

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131130-alt1
- new official snapshot

* Fri Oct 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131012-alt1
- official snapshot

* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.20130903-alt1
- first build for Sisyphus

