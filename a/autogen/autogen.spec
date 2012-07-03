Name: autogen
Version: 5.9.9
Release: alt1.1

Summary: AutoGen - The Automated Program Generator
License: %gpl2plus
Group: Development/Other
Url: http://autogen.sourceforge.net/

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch: autogen-5.8-fix-linking.patch
Patch2: %name-5.9.6-fix-libtool.patch
Packager: Alexey Rusakov <ktirf@altlinux.org>

BuildPreReq: rpm-build-licenses rpm-build-compat

BuildPreReq: texi2html guile18-devel libxml2-devel

%description
AutoGen is a tool designed to simplify the creation and maintenance of programs that contain large amounts of repetitious text. It is especially valuable in programs that have several blocks of text that must be kept synchronized.

AutoGen can now accept XML files as definition input, in addition to CGI data (for producing dynamic HTML) and traditional AutoGen definitions.

A common example where this would be useful is in creating and maintaining the code required for processing program options. Processing options requires multiple constructs to be maintained in parallel in different places in your program. Options maintenance needs to be done countless times. So, AutoGen comes with an add-on package named AutoOpts that simplifies the maintenance and documentation of program options.

The Copyright itself is privately held by Bruce Korb.

%package -n libopts
Summary: Command line option parser based on AutoGen
Group: Development/Other
License: %lgpl3plus, %bsd

%description -n libopts
AutoOpts is a very powerful command line option parser consisting of a set of AutoGen templates and a run time library that nearly eliminates the hassle of parsing and documenting command line options. This package allows you to specify several program attributes, up to 100 option types and many attributes for each option.

%package -n libopts-devel
Summary: AutoGen development files and libraries
Group: Development/Other
License: %lgpl3plus, %bsd
Requires: libopts = %version-%release
Obsoletes: autogen-devel = %version-%release
Provides: autogen-devel = %version-%release

%description -n libopts-devel
AutoOpts is a very powerful command line option parser consisting of a set
of AutoGen templates and a run time library that nearly eliminates the
hassle of parsing and documenting command line options. This package allows
you to specify several program attributes, up to 100 option types and many
attributes for each option.

This package is needed to write programs that use AutoOpts API.

%prep
%setup -q
%patch -b .fix-linking
# The libtool.m4 that is bundled with Autogen uses capitalized ECHO
# variable. System-wide libtool mentions lowercase echo variable. This
# leads to the messed libtool script.
%patch2 -b .fix-libtool

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS TODO COPYING NEWS NOTES THANKS README VERSION
%_bindir/autogen
%_bindir/columns
%_bindir/getdefs
%_bindir/xml2ag
%dir %_datadir/%name
%_datadir/%name/*
%_infodir/%{name}*
%_man1dir/autogen.1.*
%_man1dir/columns.1.*
%_man1dir/getdefs.1.*
%_man1dir/xml2ag.1.*

%files -n libopts
%_libdir/libopts.so.*
%_libdir/libguileopts.so.*

%files -n libopts-devel
%_bindir/autoopts-config
%dir %_includedir/autoopts
%_includedir/autoopts/*
%_libdir/pkgconfig/autoopts.pc
%_libdir/*.so
%_datadir/aclocal/autoopts.m4
%_datadir/aclocal/liboptschk.m4
%_man1dir/autoopts-config.1.*
%_man3dir/*.3.*

%exclude %_libdir/*.a

%changelog
* Tue Nov 03 2009 Alexey Rusakov <ktirf@altlinux.org> 5.9.9-alt1.1
- Build with guile18 (thanks to boyarsh@ for a nudge).

* Sat Aug 22 2009 Alexey Rusakov <ktirf@altlinux.org> 5.9.9-alt1
- New version (5.9.9).
- Removed obsolete *install_info calls in %%post/%%preun.

* Fri Dec 05 2008 Alexey Rusakov <ktirf@altlinux.org> 5.9.6-alt1
- New version (5.9.6).
- Specfile cleaned up (removed %%__ macros, enabled SMP build, and others).
- Repocop warnings fixed:
  + removed deprecated ldconfig call;
  + fixed info files (un)installation;
  + added Packager tag.

* Wed Dec 26 2007 Alexey Rusakov <ktirf@altlinux.org> 5.9.4-alt1
- New version (5.9.4).
- Separated libopts sub-package from autogen, and renamed autogen-devel to
  libopts-devel.
- Brought licensing into order (libopts has %lgpl3plus/%bsd licensing, and
  autogen is distributed under %gpl2plus license).
- Use license macros.
- Reduced buildreqs.

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 5.8.9-alt1
- make the patch for under-linking actually work (yeah, do autoreconf).
- requires Autoconf >= 2.59b

* Mon Apr 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.4-alt1
- new version 5.8.4
- fixed linking problems

* Mon Mar 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.3-alt1
- new version (5.8.3)
- spec cleanup

* Sun Oct 09 2005 Alexey Rusakov <ktirf@altlinux.ru> 5.7.3-alt1
- New version.
- Removed excess buildreqs.

* Fri Feb 18 2005 Vladimir Lettiev <crux@altlinux.ru> 5.6.6-alt1
- Initial build for ALTLinux Sisyphus

