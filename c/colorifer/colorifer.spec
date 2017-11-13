Name: colorifer
Version: 1.0.1
Release: alt16

Summary: Simple program output colorifer
License: GPLv2+
Group: Text tools

Packager: Stanislav Ievlev <inger@altlinux.ru>

Url: http://colorifer.sourceforge.net/
Source: %name-%{version}rc6.tar.bz2

Patch1: %name-alt-compat1.patch

Requires: lib%name = %version-%release

#BuildPreReq: libncursesw

# Automatically added by buildreq on Mon Mar 22 2004 (-bi)
BuildRequires: boost-devel gcc-c++ help2man libncurses-devel libncursesxx-devel libpcre-devel

%description
This package contains simple wrapper to colorize output from any programs.

%package -n csed
Summary: Color stream substitution filter
Group: Editors
Requires: lib%name = %version-%release

%description -n csed
Color stream substitution filter

%package -n lib%name
Summary: shared library between colorifer tools
Group: System/Libraries

%description -n lib%name
Shared library between colorifer tools

%prep
%setup -n %name-%{version}rc6
%patch1 -p2

%build
%add_optflags -DCONFIGDIR=\\\"%_datadir/%name/\\\"
%make_build DEBUG_LDGLAGS= DEBUG_LDGLAGS_UTILS=

%install
%makeinstall
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name
mkdir -p %buildroot%_datadir/%name/

%files
#_doc ChangeLog TODO NEWS
%doc TODO NEWS
%_sysconfdir/buildreqs/packages/ignore.d/*
%_bindir/%name
%_bindir/pcolorize*
%_man1dir/pcolorize.*
%dir %_datadir/%name

%files -n csed
%_bindir/csed
%_man1dir/csed.*

%files -n lib%name
%_libdir/*.so.*

%changelog
* Mon Nov 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt16
- Fixed build with current boost and gcc.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.1-alt15.qa1
- NMU: rebuilt for updated dependencies.

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt15
- Fixed build with new gcc and ld.

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt14.1
- rebuild (with the help of girar-nmu utility)

* Thu Dec 04 2008 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt14
- fixed build

* Sun Nov 30 2008 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt13
- rebuild with gcc 4.1

* Sun Jun 17 2007 Slava Semushin <php-coder@altlinux.ru> 1.0.1-alt12.1
- NMU
- Catalog /usr/share/colorifer now belongs to package (#8050)
- Spec cleanup:
  + Replaced tabs to one space
  + s/Copyright/License/
  + s/URL/Url/
  + s/%%setup -q/%%setup/
  + s/$RPM_BUILD_ROOT/%%buildroot/
  + Removed superfluous libtinfo-devel from BuildRequires
  + Small tweak %%description of libcolorifer package
  + Don't use macros for install command

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt12
- fixed libdir

* Thu Mar 09 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt11
- fixed linkage

* Tue Jan 18 2005 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt10
- rebuild with gcc3.4

* Wed Jan 12 2005 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt9
- rebuild with new libncursesxx
- prepare for gcc3.4

* Tue May 11 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt8
- rc6:
    - rename 'C' command to 'p'.
    - separate subsitution command 's/regex/color/' (currently works like s/regex/color/g)
    - support for '!' in sed style addresses.

* Wed Apr 14 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt7
- rc5:
   - all sed address forms are supported now
   - added pcolorize script to easy setup of colorifer wrapper
   - more config samples (to colorize syslog messages)

* Tue Mar 30 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt6
- rc4

* Thu Mar 25 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt5
- ignore colorifer on buildreqs

* Thu Mar 25 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt4
- rc3:
    fix strange getopt usage

* Wed Mar 24 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- rc2: 
   enable locale support
   fix ncurses error handling

* Mon Mar 22 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- rc1

* Fri Mar 19 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- new ideas, new version

* Thu Nov 13 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt0.2.rc1
- added libpcre3 to ignore list

* Wed Nov 12 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt0.1.rc1
- Daedalus release

* Tue Nov 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt11
- little improvements

* Mon Nov 10 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt10
- ported to the new config class

* Wed Nov 05 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt9
- fix setting attributes (was problems on rxvt)

* Tue Nov 04 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt8
- fix terminal reset

* Tue Nov 04 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt7
- integrate with new libing features
- added colorstreams library subpackages

* Tue Oct 28 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt6
- fix race

* Mon Oct 27 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt5
- minor fixes, project moved to sourceforge

* Thu Oct 23 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt4
- fix ignore.d content (s,libing,libing2,)

* Thu Oct 23 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt3
- fix segfault on incorrect regexps

* Wed Oct 22 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt2
- improvements main algorithm

* Tue Oct 21 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.1-alt2
- cvs snapshot: more documentation, minor code improvements

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.1-alt1
- new release

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt2
- fix bug with processing return code of subprocess

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt1
- minor features, bugfixes

* Mon Mar 24 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.3-alt2
- fine sources

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.3-alt1
- 0.5.3
  minor fixes

* Tue Mar 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt3
- fine sources

* Wed Feb 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt2
- daedalus release

* Tue Feb 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt1
- minor cleanups

* Mon Jan 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.1-alt1
- minor changes

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt1
- daedalus release

* Wed Jan 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt2
- sync with latest libing changes

* Mon Dec 30 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt1
- ported to libing

* Thu Nov 28 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Added support for gcc_common >= 1.2:
  pass program name to redirected children.

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- real split stdout and stderr

* Mon Sep 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt1
- move to xinclude in config
- rebuild with  gcc 3.2

* Thu Aug 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt3
- new buildreq files layout

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt2
- minor improvements

* Tue Jun 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt1
- reduce depenencies on libraries (only libtinfo now)
- now compatible with g++3 (tested on 3.0.4)

* Mon Jun 17 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt2
- added ignore.d files for buildreq

* Fri Jun 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- bugfix: added multiplextor for stdout stderr channels

* Tue Jun 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt2
- fixes and features

* Mon Jun 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt1
- Initial release for ALT
