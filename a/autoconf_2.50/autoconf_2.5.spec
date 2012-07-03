%define realname autoconf
%define dialect _2.50
%define suff -2.5

Name: %realname%dialect
Version: 2.59
Release: alt10
Epoch: 2

Summary: A GNU tool for automatically configuring source code
License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/%realname/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

%set_compress_method gzip
%define srcname %realname-%version
%define __spec_autodep_custom_pre export autom4te_perllibdir=%buildroot%_datadir/%realname%suff

Source: ftp://ftp.gnu.org/gnu/autoconf/%srcname.tar
Patch1: autoconf-2.58-alt-texinfo.patch
Patch2: autoconf-2.59-alt-datadir.patch
Patch3: autoconf-2.59-alt-warnings.patch
Patch4: autoconf-2.59-alt-_AC_PATH_X_XMKMF.patch
Patch5: autoconf-2.59-alt-AC_PROG_CXXCPP.patch
Patch6: autoconf-2.59-alt-AC_LANG_FUNC_LINK_TRY_GCC_BUILTIN.patch
Patch7: autoconf-2.59-rh-_AC_PATH_X_DIRECT.patch
Patch8: autoconf-2.59-owl-tmp.patch
Patch9: autoconf-2.59-alt-intltool.patch
Patch10: autoconf-2.59-alt-stubs.patch

Provides: %realname = %epoch:%version-%release
Obsoletes: %realname
Provides: %{realname}_2.5 = %epoch:%version-%release
Obsoletes: %{realname}_2.5

PreReq: autoconf-common, alternatives >= 0:0.4
Requires: m4 >= 1.4, mktemp >= 1:1.3.1

BuildRequires: help2man, alternatives >= 0:0.4

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages.  If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q -n %srcname
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

find -type f -name \*.orig -delete -print

find -type f -print0 |
	xargs -r0 grep -FZl 'mawk gawk' -- |
	xargs -r0 %__subst 's/mawk gawk/gawk mawk/g' --

# patch texinfo file
%__subst '/@direntry/,/@end direntry/ { s/(%realname)/(%realname%suff)/g;s/\(\* [[:alnum:].]*\):/\1%suff:/g }' doc/%realname.texi

%build
export ac_cv_prog_EMACS=no
%configure --program-suffix=%suff
%make_build

%install
%makeinstall

# We don't want to include the standards.info stuff in the package,
# since it comes from binutils.
rm -f %buildroot%_infodir/standards*

# Some more helpful scripts.
rm -f %buildroot%_datadir/%realname/INSTALL
mv %buildroot%_datadir/%realname %buildroot%_datadir/%realname%suff

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mv %buildroot%_infodir/%realname.info %buildroot%_infodir/%realname%suff.info

for f in %buildroot%_bindir/*%suff; do
	ln -s "${f##*/}" "${f%%%suff}%dialect"
done

%define _perl_lib_path %perl_vendor_privlib:%_datadir/%realname%suff

mkdir -p %buildroot%_altdir

cat >%buildroot%_altdir/%name <<EOF
%_bindir/%realname-default	%_bindir/%realname%suff	30
%_datadir/%realname	%_datadir/%realname%suff	%_bindir/%realname%suff
%_infodir/%realname.info.gz	%_infodir/%realname%suff.info.gz	%_bindir/%realname%suff
EOF

for i in autoheader autom4te autoreconf autoscan autoupdate ifnames; do
cat >>%buildroot%_altdir/%name <<EOF
%_bindir/$i-default	%_bindir/$i%suff	%_bindir/%realname%suff
EOF
done

for i in %realname autoheader autom4te autoreconf autoscan autoupdate config.guess config.sub ifnames; do
cat >>%buildroot%_altdir/%name <<EOF
%_man1dir/$i.1.gz	%_man1dir/$i%suff.1.gz	%_bindir/%realname%suff
EOF
done

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%_altdir/*
%_bindir/*
%_datadir/%realname%suff
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS NEWS README TODO

%changelog
* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt10
- Removed obsolete %%install_info/%%uninstall_info calls.
- Switched to alternatives-0.4.

* Tue Dec 25 2007 Alex V. Myltsev <avm@altlinux.ru> 2:2.59-alt9
- Changed the %%subst to rewrite direntries instead of deleting.

* Sun Dec 23 2007 Alex V. Myltsev <avm@altlinux.ru> 2:2.59-alt8
- Changed dialect to "_2.50" (2.5 is now smaller than 2.13).
- Removed conflicting texinfo dir entries.

* Fri Nov 02 2007 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt7
- Patched AC_LANG_FUNC_LINK_TRY to ask GNU C headers to include stubs.
  This is required for better glibc-devel >= 2.5-alt5 support.

* Thu Oct 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2:2.59-alt6
- Added intltool support to autoreconf.

* Tue Jun 20 2006 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt5
- Merged all warning fixes to single patch.
- Applied Owl patch to use mktemp in a fail-close way.
- Applied RH patch to _AC_PATH_X_DIRECT macro:
  + check for Xlib.h instead of Intrinsic.h to find X11 headers location;
  + try to link with libX11 instead of libXt to find X11 libraries location.

* Thu Feb 24 2005 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt4
- Converted alternatives config file to new format (0.2.0).

* Fri May 14 2004 Alexey Voinov <voins@altlinux.ru> 2:2.59-alt3
- Some more fixes for "-Wall -Werror"

* Tue Jan 06 2004 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt2
- Changed AC_PROG_CXXCPP so it won't fail when no c++
  preprocessor available.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt1
- Updated to 2.59.

* Sun Nov 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.58-alt1
- Updated to 2.58.
- Removed alt-dnet patch (no longer needed).

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.57-alt2
- Updated package dependencies.
- Corrected ac_extension order.
- Partially fixed "-Wall -Werror" support (voins, #2913).

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 2:2.57-alt1.1
- move to new alternatives scheme

* Sat Dec 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.57-alt1
- Updated to 2.57

* Sun Nov 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.56-alt1
- 2.56

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.54-alt2
- Removed libdnet checks.
- Explicitly disabled build of autoconf mode for emacs.
- Changed suffix, compatibility symlinks added (#0001192).
- Added autoconf-common support.
- Raised alternatives priority.

* Tue Sep 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.54-alt1
- 2.54

* Sat May 18 2002 Dmitry V. Levin <ldv@altlinux.org> 2.53-alt4
- Fixed typo in provides.

* Wed May 15 2002 Alexey Voinov <voins@altlinux.ru> 2.53-alt3
- Use configure --program-suffix to add suffixes to (almost) all files.
- .alt-datadir patch fixes Makefile.ins to use /usr/share/autoconf_2.5
- Simplified %install section.

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.53-alt2
- Set compress method to "gzip".
- Set dircategory to "Development/Other".
- Added more files to alternatives support.

* Sat Apr 06 2002 Alexey Voinov <voins@voins.program.ru> 2.53-alt1
- fork from 2:2.13-alt4
- new version (2.53)
- URL corrected
- support for *.info and man pages (update-)alternatives.

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt4
- Renamed to autoconf_2.13
- Added update-alternatives support (voins).

* Wed Feb 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt3
- Fixed acspecific to avoid -lelf usage for getloadavg.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt2
- Rebuilt.

* Thu Aug 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt1
- Revert back to stable version.
- Reworked tmp files handling.
- Merged RH patches:
  + acgeneral.m4: fixed exit status;
  + autoscan.pl: patched to get a better choice of init file (#42071),
    to test for CPP after CC (#42072) and to detect C++ source and g++ (#42073).
  + acspecific.m4: include various standard C headers as needed
    by various autoconf tests (#19114);
  + acgeneral.m4, acspecific.m4: back-ported _AC_PROG_CXX_EXIT_DECLARATION
    from version 2.50 to make detection of C++ exit() declaration prototype
    platform independent. The check is done in AC_PROG_CXX with the result
    stored in "confdefs.h". The exit() prototype in AC_TRY_RUN_NATIVE is no
    longer needed.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52b-alt1
- 2.52b

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52-alt1
- 2.52
- Added manpages from debian.

* Sun Dec 24 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl5mdk
- Fixed exit function prototype for gcc >= 2.96.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl4mdk
- RE adaptions.

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-4mdk
- macros for install-info

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-3mdk
- cleanup and macros

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-2mdk
- new groups

* Mon Mar  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.13-1mdk
- Back to last 2.13 and stable version, add a serial.

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge change of Jeff package.

* Thu May 13 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- 2.14.1

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to help autoconf clean after itself and not leave /tmp clobbered
  with acin.* and acout.* files (can you say annoying?)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)
- use gawk, not mawk

* Thu Mar 18 1999 Preston Brown <pbrown@redhat.com>
- moved /usr/lib/autoconf to /usr/share/autoconf (with automake)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.13.

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires perl

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc

