%define _name libquvi-scripts
%define ver_major 0.9
%define snapshot 20131130

# online tests
%def_without tests
%def_enable check

Name: %_name
Version: %ver_major.%snapshot
Release: alt4

Summary: Lua scripts for parsing the media details
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%_name/%ver_major/%_name-%version.tar.xz
Patch: libquvi-scripts-0.9.20130903-alt-pkgconfig.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1134853
Patch1: 0001-guardian.lua-Update-for-website-changes.patch

BuildArch: noarch

Conflicts: libquvi-scripts0.9 <= 0.9.20131130-alt3
Obsoletes: libquvi-scripts0.9 <= 0.9.20131130-alt3

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
Conflicts: libquvi-scripts0.9-devel <= 0.9.20131130-alt3
Obsoletes: libquvi-scripts0.9-devel <= 0.9.20131130-alt3

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
* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.20131130-alt4
- consolidated libquvi-scripts and libquvi-scripts0.9

* Wed Jun 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131130-alt3
- guardian.lua: applied fc fix  for website changes (RHBZ #1134853)
- updated dependencies

* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt2.1
- fixed file conflict with libquvi-scripts0.9 (ALT #31361)

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt2
- reqs: lua5 lua-module-luasocket (ALT #31354)

* Fri Oct 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt1
- 0.4.19

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.18-alt1
- 0.4.18

* Mon Jul 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.16-alt1
- 0.4.16

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.14-alt1
- 0.4.14

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.13-alt1
- 0.4.13

* Thu Nov 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.9-alt1
- 0.4.9

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus
