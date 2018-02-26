%def_disable debug
%def_disable devel
%def_disable profile
%def_enable shared
%def_enable static
#----------------------------------------------------------------------

%define Name Tokyo Tyrant
%define sname ttserver
Name: tokyotyrant
%define lname lib%name
Summary: A network interface of Tokyo Cabinet
Version: 1.1.40
Release: alt1
License: %lgpl2plus
Group: System/Libraries
Group: Databases
URL: http://1978th.net/%name
Source0: %url/%name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Patch: %name-%version-alt.patch
Provides: %name-server = %version-%release
Provides: %sname = %version-%release
Requires: %lname = %version-%release
Requires: libtokyocabinet >= 1.4.35
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

BuildRequires: libtokyocabinet-devel >= 1.4.35
BuildRequires: zlib-devel

%description
%Name is a network interface for Tokyo Cabinet.
This package contains %Name server.


%package utils
Summary: Command line tools for managing %Name
Group: Databases
Requires: %lname = %version-%release

%description utils
%Name is a network interface for Tokyo Cabinet.
This package contains command line tools for managing %Name.


%if_enabled shared
%package -n %lname
Summary: %Name library
Group: System/Libraries

%description -n %lname
%Name is a network interface for Tokyo Cabinet.
This package contains %Name sharerd library.
%endif


%package -n %lname-devel
Summary: Headers for developing programs that will use %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is a network interface for Tokyo Cabinet.
This package contains the libraries and header files needed for
developing with %lname.


%if_enabled static
%package -n %lname-devel-static
Summary: Static version of %Name database library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is a network interface for Tokyo Cabinet.
This package contains static libraries for building statically linked
programs which use %Name.
%endif


%package doc
Summary: Documentation for %Name
Group: Documentation
BuildArch: noarch
Provides: %name-devel-man = %version-%release

%description doc
%Name is a network interface for Tokyo Cabinet.
This package contains documentation for developers.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%autoreconf
%configure \
    %{subst_enable debug} \
    %{subst_enable devel} \
    %{subst_enable profile} \
    %{subst_enable shared}
%make_build
bzip2 --best --keep --force -- ChangeLog


%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%_datadir/%name/COPYING
install -d -m 0755 %buildroot{%_docdir,%_sysconfdir/sysconfig,%_initdir,%_localstatedir/%name,%_logdir/%sname}
mv %buildroot{%_datadir/%name,%_docdir/%name-%version}
mv %buildroot{%_sbindir/*,%_docdir/%name-%version/}
install -m 0755 %SOURCE1 %buildroot%_initdir/%name
install -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name


%pre
%_sbindir/groupadd -r -f _tyrant &>/dev/null ||:
%_sbindir/useradd -r -n -M -s /dev/null -d %_localstatedir/%name -g _tyrant \
    -c "Server of Tokyo Tyrant (%sname)" _tyrant &>/dev/null ||:


%post
%post_service %name ||:

%preun
%preun_service %name ||:


%files
%_bindir/%sname
%_man1dir/%sname.*
%_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%attr(770,root,_tyrant) %dir %_localstatedir/%name
%attr(770,root,_tyrant) %dir %_logdir/%sname


%files utils
%_bindir/*
%_man1dir/*
%exclude %_bindir/%sname
%exclude %_man1dir/%sname.*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files doc
%_docdir/%name-%version
%_man3dir/*


%changelog
* Thu Jan 21 2010 Led <led@altlinux.ru> 1.1.40-alt1
- 1.1.40

* Wed Dec 09 2009 Led <led@altlinux.ru> 1.1.39-alt1
- 1.1.39:
  + ttservstart: error handler for the accept call was added
- 1.1.38:
  + new functions: do_mc_append, do_mc_prepend

* Wed Nov 11 2009 Led <led@altlinux.ru> 1.1.37-alt2
- rebuild with libtokyocabinet.so.9

* Tue Nov 10 2009 Led <led@altlinux.ru> 1.1.37-alt1
- 1.1.37

* Mon Oct 19 2009 Led <led@altlinux.ru> 1.1.36-alt1
- 1.1.36:
  + new function: serv_strstr
  + "-mul" option was added

* Tue Oct 06 2009 Led <led@altlinux.ru> 1.1.35-alt1
- 1.1.35:
  + new functions: tculogadbputshl, tculogadbputshlproc,
    tcrdbparasearch, tcrdbparasearchworker
  + "tcadbmisc" is now supported

* Sun Sep 27 2009 Led <led@altlinux.ru> 1.1.34-alt1
- 1.1.34
- changed URL

* Thu Jul 23 2009 Led <led@altlinux.ru> 1.1.33-alt1
- 1.1.33:
  + new functions: tcrdbqryhint, tcrdbmetasearch, serv_bit

* Thu Jul 16 2009 Led <led@altlinux.ru> 1.1.32-alt1
- 1.1.32:
  + new functions: runtypical, proctypical, threadtypical

* Mon Jul 13 2009 Led <led@altlinux.ru> 1.1.31-alt1
- 1.1.31

* Sat Jul 11 2009 Led <led@altlinux.ru> 1.1.30-alt1
- 1.1.30:
  + new function: scrextkill

* Sat Jun 27 2009 Led <led@altlinux.ru> 1.1.29-alt1
- 1.1.29:
  + new function: do_http_options
- fixed Requires

* Sun May 31 2009 Led <led@altlinux.ru> 1.1.28-alt1
- 1.1.28:
  + new functions: serv_fwmkeys, serv_regex

* Sun May 24 2009 Led <led@altlinux.ru> 1.1.27-alt1
- 1.1.27
- fixed init-script (close #20160)

* Sat May 09 2009 Led <led@altlinux.ru> 1.1.26-alt1
- 1.1.26:
  + new functions: ttservsettermhandler, do_term
- 1.1.25:
  + new function: ttcmdidtostr

* Thu May 07 2009 Led <led@altlinux.ru> 1.1.24-alt1
- 1.1.24:
  + new functions: tcrdbsetecode, tcrdblockmethod, tcrdbunlockmethod,
    tcrdbopen2, tcrdbsetmst2, tcrdbtune, ttbreakservexpr

* Tue Apr 07 2009 Led <led@altlinux.ru> 1.1.23-alt1
- 1.1.23:
  + new function: serv_eval

* Mon Apr 06 2009 Led <led@altlinux.ru> 1.1.22-alt1
- 1.1.22:
  + serv_mapreduce): the parameter for the target keys became an option
- 1.1.21:
  + serv_mapreduce: the parameter for the session ID was abolished
- 1.1.20:
  + new functions: serv_stashputkeep, serv_stashputcat, serv_mapreduce,
    serv_mapreducemapemit
  + do_put, do_out, do_get: parameter validation was enhanced

* Thu Apr 02 2009 Led <led@altlinux.ru> 1.1.19-alt1
- 1.1.19:
  + new function: tcrdbqrysearchcount
  + tcreplread: timeout mechanism was added
  + do_repl: performance was improved
  + tcrdbqrysearchget: the option for no update log was added

* Wed Mar 25 2009 Led <led@altlinux.ru> 1.1.18-alt1
- 1.1.18:
  + performance was improved

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.1.17-alt1
- 1.1.17:
  + new function tcrdbqrysetlimit instead of tcrdbqrysetmax

* Thu Feb 19 2009 Led <led@altlinux.ru> 1.1.16-alt1
- 1.1.16

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.1.15-alt1
- 1.1.15:
  + new function: ttsockgets2

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.1.14-alt1
- 1.1.14:
  + new function: do_extpc
- 1.1.13:
  + new function: tcrdbqrysearchget
- 1.1.12:
  + new functions: tcrdbtblput, tcrdbtblout, tcrdbtblget,
    tcrdbtblsetindex, tcrdbtblgenuid, tcrdbqrysearch

* Wed Jan 07 2009 Led <led@altlinux.ru> 1.1.11-alt1
- 1.1.11:
  + new function: serv_misc

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.1.10-alt1
- 1.1.10:
  + new functions: tculogadbmisc, do_misc, serv_foreach,
    serv_stashvanish, serv_stashforeach, tcsocksetlife

* Mon Dec 15 2008 Led <led@altlinux.ru> 1.1.9-alt2
- rebuild with libtokyocabinet.so.7

* Sun Dec 14 2008 Led <led@altlinux.ru> 1.1.9-alt1
- 1.1.9:
  + new functions: tcrdbputshl, serv_isect, serv_union
- 1.1.8:
  + new functions: serv_lock, serv_unlock
- cleaned up spec

* Thu Oct 30 2008 Led <led@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Mon Sep 29 2008 Led <led@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Wed Sep 24 2008 Led <led@altlinux.ru> 1.1.2-alt1
- 1.1.2
- updated %name-1.1.2-alt.patch

* Tue Sep 09 2008 Led <led@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Aug 13 2008 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
