Name: autogen
Version: 5.18.12
Release: alt2

Summary: AutoGen - The Automated Program Generator
License: %gpl3plus
Group: Development/Other
Url: http://www.gnu.org/software/autogen/
Packager: Mikhail Efremov <sem@altlinux.org>

Source: %name-%version.tar
Patch1: autogen-5.18.4-masquerade-deps.patch

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Dec 10 2017
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 guile22 libgc-devel libgmp-devel perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl pkg-config python-base
BuildRequires: guile22-devel libxml2-devel makeinfo texi2html

%define _unpackaged_files_terminate_build 1

%description
AutoGen is a tool designed to simplify the creation and maintenance
of programs that contain large amounts of repetitious text.
It is especially valuable in programs that have several blocks of text
that must be kept synchronized.

AutoGen can now accept XML files as definition input, in addition to CGI
data (for producing dynamic HTML) and traditional AutoGen definitions.

A common example where this would be useful is in creating and
maintaining the code required for processing program options. Processing
options requires multiple constructs to be maintained in parallel
in different places in your program. Options maintenance needs to be
done countless times. So, AutoGen comes with an add-on package named
AutoOpts that simplifies the maintenance and documentation of program
options.

%package -n libopts
Summary: Command line option parser based on AutoGen
Group: Development/Other
License: %lgpl3plus, %bsd

%description -n libopts
AutoOpts is a very powerful command line option parser consisting of
a set of AutoGen templates and a run time library that nearly eliminates
the hassle of parsing and documenting command line options.
This package allows you to specify several program attributes, up to 100
option types and many attributes for each option.

%package -n libopts-devel
Summary: AutoGen development files and libraries
Group: Development/Other
License: %lgpl3plus, %bsd
Requires: libopts = %version-%release
Obsoletes: autogen-devel = %version-%release
Provides: autogen-devel = %version-%release

%description -n libopts-devel
AutoOpts is a very powerful command line option parser consisting of
a set of AutoGen templates and a run time library that nearly eliminates
the hassle of parsing and documenting command line options. This package
allows you to specify several program attributes, up to 100 option types
and many attributes for each option.

This package is needed to write programs that use AutoOpts API.

%prep
%setup
%patch1 -p1
rm doc/autogen.info*

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS TODO COPYING NEWS THANKS README VERSION
%_bindir/autogen
%_bindir/columns
%_bindir/getdefs
%_bindir/xml2ag
%_libdir/%name/
%dir %_datadir/%name
%_datadir/%name/*
%_infodir/%{name}*
%_man1dir/autogen.1*
%_man1dir/columns.1*
%_man1dir/getdefs.1*
%_man1dir/xml2ag.1*

%files -n libopts
%_libdir/libopts.so.*

%files -n libopts-devel
%_bindir/autoopts-config
%dir %_includedir/autoopts
%_includedir/autoopts/*
%_pkgconfigdir/autoopts.pc
%_libdir/*.so
%_datadir/aclocal/autoopts.m4
%_man1dir/autoopts-config.1.*
%_man3dir/*.3.*

%changelog
* Sun Dec 10 2017 Dmitry V. Levin <ldv@altlinux.org> 5.18.12-alt2
- Regenerated texinfo documentation.

* Mon Sep 04 2017 Mikhail Efremov <sem@altlinux.org> 5.18.12-alt1
- Updated to 5.18.12.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 5.18.4-alt1.1
- NMU: added BR: texinfo

* Thu Oct 16 2014 Mikhail Efremov <sem@altlinux.org> 5.18.4-alt1
- Don't require /usr/xpg4/bin/sh.
- Minor spec cleanup.
- Fix pkgfile placement.
- Updated License.
- Updated Url.
- Drop old patches.
- Source archive: tar.gz -> tar.
- Updated to 5.18.4.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.9.9-alt1.1.qa1
- NMU: rebuilt for debuginfo.

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

