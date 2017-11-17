Name: perl
Version: 5.24.3
Release: alt2
Epoch: 1

Summary: Practical Extraction and Report Language
License: GPL or Artistic
Group: Development/Perl
URL: http://www.perl.org
Packager: Perl Maintainers Team <cpan@altlinux.ru>

Source: perl-%version.tar

Patch01: perl-5.22.0-alt-644-at-ExtUtils-Install.patch
Patch02: perl-5.24.0-alt-644-at-installperl.patch
Patch03: perl-5.22.0-alt-644-viy-ExtUtils-Install-fix-test.patch
Patch04: perl-5.22.0-alt-at-MM_Unix-link-xs-with-libperl.patch
Patch05: perl-5.24.1-alt-at-MM_Unix-shabang.patch
Patch06: perl-5.24.1-alt-at-Storable-no-early-dep-on-Log-Agent.patch
Patch07: perl-5.24.0-alt-at-debian-Errno_pm.patch
Patch08: perl-5.24.1-alt-at-disable-Cpan-Meta-under-rpm.patch
Patch09: perl-5.24.0-alt-at-libperl-soname.patch
Patch10: perl-5.24.1-alt-at-no-rpath-for-std-libs.patch
Patch11: perl-5.20.1-alt-at-perl5db-findreq-cleanup.patch
Patch12: perl-5.20.1-alt-at-perlbug-findreq-cleanup.patch
Patch13: perl-5.20.1-alt-at-skip-deprecation-warning.patch
Patch14: perl-5.20.1-alt-crux-Cwd-use-realpath.patch
# or hsh with --mountpoints=/proc
Patch15: perl-5.20.1-alt-crux-fix-test-without-proc.patch
Patch16: perl-5.20.1-alt-ldv-support-for-alt-gcc-wrapper.patch
Patch17: perl-5.24.0-alt-viy-Unicode-Normalize-fix-deps.patch
# hack - sensitive test can fail transaction - see maintainers notes for 5.24.1
Patch18: perl-5.24.1-alt-viy-disable-Time-HiRes-itimer.t.patch
Patch19: perl-5.24.1-alt-viy-no-check-sums-in-customized.t.patch
# temporary quick hack; should be replaced by a proper surgery
# not installing version::regex will live perl.req's unmets
Patch20: perl-5.24.1-alt-viy-installperl-ExtUtils-MakeMaker-version.patch
# mail from Oleg Solovyov; see patch body
Patch21: perl-5.24.3-alt-solovyov.patch

# cpan update patches here. use format below:
#Patch50: cpan-update-Socket-2.013-to-Socket-2.016.diff
Patch51: cpan-update-Scalar-List-Utils-1.42-to-Scalar-List-Utils-1.46.diff

# ------ inserted with srpm-spec-inject-patches(1) -------
# BeginPatches(fedora)[shift=300]: -----------------------

# Document Math::BigInt::CalcEmu requires Math::BigInt, rhbz#959096,
# CPAN RT#85015
Patch322:        perl-5.18.1-Document-Math-BigInt-CalcEmu-requires-Math-BigInt.patch 

# Make *DBM_File desctructors thread-safe, bug #1107543, RT#61912
Patch326:        perl-5.18.2-Destroy-GDBM-NDBM-ODBM-SDBM-_File-objects-only-from-.patch

# Fix a memory leak when compiling a regular expression with a POSIX class,
# RT#128313, in upstream after 5.25.1
Patch331:        perl-5.24.0-Fix-a-memory-leak-in-strict-regex-posix-classes.patch

# Do not mangle errno from failed socket calls, RT#128316,
# in upstream after 5.25.1
Patch332:        perl-5.25.1-perl-128316-preserve-errno-from-failed-system-calls.patch

# Fix compiling regular expressions like /\X*(?0)/, RT#128109, in upstream
# after 5.25.1
Patch333:        perl-5.24.0-fix-128109-do-not-move-RExC_open_parens-0-in-reginse.patch

# Do not use unitialized memory in $h{\const} warnings, RT#128189,
# in upstream after 5.25.2
Patch334:        perl-5.25.2-uninit-warning-from-h-const-coredumped.patch

# Fix precedence in hv_ename_delete, RT#128086, in upstream after 5.25.0
Patch335:        perl-5.25.0-Fix-precedence-in-hv_ename_delete.patch

# Do not treat %: as a stash, RT#128238, in upstream after 5.25.2
Patch336:        perl-5.25.2-only-treat-stash-entries-with-.-as-sub-stashes.patch

# Do not crash when inserting a non-stash into a stash, RT#128238,
# in upstream after 5.25.2
Patch337:        perl-5.25.2-perl-128238-Crash-with-non-stash-in-stash.patch

# Fix line numbers with perl -x, RT#128508, in upstream after 5.25.2
Patch338:        perl-5.25.2-perl-128508-Fix-line-numbers-with-perl-x.patch

# Fix a crash when vivifying a stub in a deleted package, RT#128532,
# in upstream after 5.25.2
Patch340:        perl-5.25.2-perl-128532-Crash-vivifying-stub-in-deleted-pkg.patch

# Fix a crash in "Subroutine redefined" warning, RT#128257,
# in upstream after 5.25.2
Patch341:        perl-5.25.2-SEGV-in-Subroutine-redefined-warning.patch

# Fix a crash in lexical scope warnings, RT#128597, in upstream after 5.25.2
Patch342:        perl-5.25.2-perl-128597-Crash-from-gp_free-ckWARN_d.patch

# Fix handling \N{} in tr for characters in range 128--255, RT#128734,
# in upstream after 5.25.3
Patch343:        perl-5.24.0-PATCH-perl-128734-tr-N-.-failing-for-128-255.patch

# Fix crash in "evalbytes S", RT#129196, in upstream after 5.25.4
Patch345:        perl-5.25.4-perl-129196-Crash-bad-read-with-evalbytes-S.patch
Patch346:        perl-5.24.0-Regression-test-for-RT-129196.patch
Patch347:        perl-5.25.4-toke.c-fix-mswin32-builds.patch

# Fix crash in splice, RT#129164, RT#129166, RT#129167, in upstream after 5.25.4
Patch348:        perl-5.24.0-perl-129164-Crash-with-splice.patch

# Fix string overrun in Perl_gv_fetchmethod_pvn_flags, RT#129267,
# in upstream after 5.25.4
Patch349:        perl-5.24.0-clean-up-gv_fetchmethod_pvn_flags-introduce-name_end.patch
Patch350:        perl-5.25.4-clean-up-gv_fetchmethod_pvn_flags-move-origname-init.patch
Patch351:        perl-5.25.4-clean-up-gv_fetchmethod_pvn_flags-rename-nsplit-to-l.patch
Patch352:        perl-5.25.4-fix-129267-rework-gv_fetchmethod_pvn_flags-separator.patch
Patch353:        perl-5.25.4-perl-129267-Test-for-gv_fetchmethod-buffer-overrun.patch

# Fix crash when matching UTF-8 string with non-UTF-8 substrings, RT#129350,
# in upstream after 5.25.5
Patch354:        perl-5.24.0-perl-129350-anchored-floating-substrings-must-be-utf.patch

# Fix parsing perl options in shell bang line, RT#129336,
# in upstream after 5.25.5
Patch355:        perl-5.24.0-rt-129336-perl-i-u-erroneously-interpreted-as-u.patch

# Fix firstchar bitmap under UTF-8 with prefix optimization, RT#129950,
# in upstream after 5.25.6
Patch356:        perl-5.24.0-regcomp.c-fix-perl-129950-fix-firstchar-bitmap-under.patch

# Avoid infinite loop in h2xs tool if enum and type have the same name,
# RT#130001, in upstream after 5.25.6
Patch357:        perl-5.25.6-perl-130001-h2xs-avoid-infinite-loop-for-enums.patch

# Fix stack handling when calling chdir without an argument, RT#129130,
# in upstream after 5.25.6
Patch358:        perl-5.24.0-perl-129130-make-chdir-allocate-the-stack-it-needs.patch

# Fix crash in Storable when deserializing malformed code reference, RT#68348,
# RT130098
Patch359:        perl-5.25.7-Fix-Storable-segfaults.patch

# Fix assigning split() return values to an array, in upstream after 5.25.7
Patch361:        perl-5.24.0-split-was-leaving-PL_sv_undef-in-unused-ary-slots.patch

# Fix const correctness in hv_func.h, bug #1242980, RT#130169,
# in upstream after 5.25.7
Patch362:        perl-5.25.7-Fix-const-correctness-in-hv_func.h.patch

# Fix a crash in optimized evaluation of "or ((0) x 0))", RT#130247,
# in upsream after 5.25.7
Patch363:        perl-5.24.0-assertion-failure-in-.-or-0-x-0.patch

# Fix a memory leak in IO::Poll, RT#129788, in upstream after 5.25.7
Patch364:        perl-5.24.0-perl-129788-IO-Poll-fix-memory-leak.patch

# Fix regular expression matching, RT#130307, in upstream after 5.25.7
Patch365:        perl-5.25.7-perl-130307-Correctly-unwind-on-cache-hit.patch

# Fix a buffer overflow in split in scalar context, RT#130262,
# in upstream after 5.25.8
Patch366:        perl-5.24.1-perl-130262-split-scalar-context-stack-overflow-fix.patch

# Fix a heap overflow with pack "W", RT129149, in upstream after 5.25.8
Patch367:        perl-5.25.8-perl-129149-avoid-a-heap-buffer-overflow-with-pack-W.patch
Patch368:        perl-5.25.8-perl-129149-fix-the-test-so-skip-has-a-SKIP-to-work-.patch

# Fix a use-after-free when processing scalar variables in forms, RT#129125,
# in upstream after 5.25.8
Patch369:        perl-5.24.1-perl-129125-copy-form-data-if-it-might-be-freed.patch

# Fix a heap overflow if invalid octal or hexadecimal number is used in
# transliteration expression, RT#129342, in upstream after 5.25.8
Patch370:        perl-5.24.1-perl-129342-ensure-range-start-is-set-after-error-in.patch

# Fix out-of-bound read in case of unmatched regexp backreference, RT#129377,
# in upstream after 5.25.8
Patch371:        perl-5.24.1-perl-129377-don-t-read-past-start-of-string-for-unma.patch
# EndPatches(fedora): --------------------------------------

# there's a problem with strict.pm
%add_findreq_skiplist */strict.pm
# the failure for bytes_heavy.pl is normal, it's not self-contained
%add_findreq_skiplist */bytes_heavy.pl
# skip Compress::Zlib and Encode dependencies
%add_findreq_skiplist */DBM_Filter/*.pm
# Data::Dumper uses B::Deparse (on demand) to store coderefs
%add_findreq_skiplist */Data/Dumper.pm
# open.pm requires Encode in certain cases
%add_findreq_skiplist */open.pm
# Pod::Html requires Pod::Simple
%add_findreq_skiplist */Pod/Html.pm
%add_findreq_skiplist */pod2html
# It requires Encode which we split out
%add_findreq_skiplist */ExtUtils/MakeMaker.pm
%add_findreq_skiplist */ExtUtils/MakeMaker/Locale.pm
# It requires Term::Readline which is moved to Term-Readline-Gnu
%add_findreq_skiplist */perl5db.pl

# do not provide auxiliary unicore libraries
%add_findprov_skiplist */unicore/*/*

BuildRequires: /proc
BuildRequires: libdb4-devel libgdbm-devel

%package base
Summary: Pathologically Eclectic Rubbish Lister
Group: System/Base
Provides: perl = %epoch:%version
Obsoletes: perl < %epoch:%version
Provides: perl-version = 0.99
Obsoletes: perl-version < 0.99
Provides: perl-PerlIO = %epoch:%version perl-Storable = %epoch:%version
Obsoletes: perl-PerlIO < %epoch:%version perl-Storable < %epoch:%version
Provides: perl-Digest-MD5 perl-Time-HiRes perl-MIME-Base64
Obsoletes: perl-Digest-MD5 perl-Time-HiRes perl-MIME-Base64

%package devel
Summary: Perl header files and development modules
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release
Provides: perl-Test-Tester = 0.114
Obsoletes: perl-Test-Tester < 0.114
Conflicts: perl-Test-Tester < 0.114
Provides: perl-Test-use-ok = 0.12
Obsoletes: perl-Test-use-ok < 0.12
Conflicts: perl-Test-use-ok < 0.12

%package pod
Summary: Perl documentation
Group: Development/Documentation
Requires: perl-base = %epoch:%version
Provides: perl-doc = %epoch:%version
BuildArch: noarch

%package threads
Summary: Perl thread modules
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release

%package unicore
Summary: Perl Unicode library
Group: Development/Perl
Requires: perl-Unicode-Normalize = %epoch:%version-%release
BuildArch: noarch

%package DBM
Summary: Perl modules for accessing DBM databases
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release
Provides:  perl-DB_File
Obsoletes: perl-DB_File

%package Unicode-Normalize
Summary: Unicode normalization forms
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release

%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications (and what it excels
at) are probably system administration utilities and web programming.
A large proportion of the CGI scripts on the web are written in Perl.

%description base
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications (and what it excels
at) are probably system administration utilities and web programming.
A large proportion of the CGI scripts on the web are written in Perl.

This package provides Perl interpreter and a subset of the standard
library required to perform basic tasks.

%description devel
This package contains Perl header files and development modules.
Most perl packages will need to install perl-devel to build.

%description pod
This package provides standard Perl documentation in Pod format.

%description threads
This package provides Perl modules for thread programming.  The threads
module provides interface to interpreter-based threading implementation
(ithreads).  The threads::shared module enables data sharing between
threads.  Thread::Queue and Thread::Semaphore provide thread-safe
synchronization primitives.

%description unicore
This package provides extended Unicode support for Perl (full support
for Unicode properties in regular expressions, Unicode Character Database,
the Unicode::UCD module, and the charnames pragma).

%description DBM
This package provides Perl modules for accessing DBM databases.
AnyDBM_File provides a framework for multiple DBM implementations
(DB_File, NDBM_File, GDBM_File, and SDBM_File). DBM_Filter allows
filtering DBM keys/values by user-defined code.

%description Unicode-Normalize
This module provides support for normalized forms of Unicode text,
as described in Unicode Standard Annex #15.  With these forms,
equivalent text will have identical binary representations.

%prep
%setup -q
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch51 -p1

# ------ inserted with srpm-spec-inject-patches(1) -------
# BeginPatches(fedora): ------------------------------------
%patch322 -p1
%patch326 -p1
#patch331 -p1
#patch332 -p1
#patch333 -p1
%patch334 -p1
#patch335 -p1
%patch336 -p1
%patch337 -p1
#patch338 -p1
%patch340 -p1
%patch341 -p1
#patch342 -p1
#patch343 -p1
#patch345 -p1
#patch346 -p1
#patch347 -p1
%patch348 -p1
%patch349 -p1
%patch350 -p1
%patch351 -p1
%patch352 -p1
%patch353 -p1
%patch354 -p1
#patch355 -p1
%patch356 -p1
%patch357 -p1
%patch358 -p1
%patch359 -p1
%patch361 -p1
%patch362 -p1
%patch363 -p1
%patch364 -p1
%patch365 -p1
%patch366 -p1
%patch367 -p1
%patch368 -p1
%patch369 -p1
%patch370 -p1
%patch371 -p1
# EndPatches(fedora): --------------------------------------

# .orig files can break some test
# at least t/porting/readme.t :
# Failed test 39 - Maintainers.pl.orig is mentioned in Porting/README.pod at porting/readme.t line 36
find -name '*.orig' -delete

%build
%define ver %(v=%version IFS=.; set $v; echo $1.$2)
%define privlib /usr/share/perl5
%define archlib %_libdir/perl5
%define autolib %archlib/auto
%define site_prefix %_prefix/local
%define site_privlib %site_prefix/share/perl/%ver
%define site_archlib %site_prefix/%_lib/perl/%ver

%ifarch e2k
# mcst#2279
%add_optflags -D_FORTIFY_SOURCE=0
%endif

sh Configure -ders \
%ifarch %{ix86}
	-Duse64bitint \
%endif
	-Dusethreads -Duseithreads -Duselargefiles \
	-Duseshrplib -Dlibperl=libperl-%ver.so \
	-Dcc=gcc -Doptimize="%optflags" -DDEBUGGING=maybe \
	-Dprefix=%_prefix -Dprivlib=%privlib -Darchlib=%archlib \
	-Dvendorprefix=%_prefix -Dvendorlib=%privlib -Dvendorarch=%archlib \
	-Dsiteprefix=%site_prefix -Dsitelib=%site_privlib -Dsitearch=%site_archlib \
	-Dotherlibdirs=/etc/perl5:/usr/lib/perl5/vendor_perl \
	-Dinc_version_list=none \
	-Dpager='%_bindir/less -isR' \
	-Dman1dir=%_man1dir -Dman3dir=none \
	-Dcf_by='%vendor' -Dcf_email='%packager' \
	-Dmyhostname=localhost -Dperladmin=root@localhost

%ifarch e2k
# till apx. lcc-1.23
echo '-lcxa' >> ./ext.libs
%endif

# kill rpath
sed -i 's@ -Wl,-rpath,%archlib/CORE@@g' config.sh [Mm]akefile myconfig

# fixup man1ext and man3ext
sed -i '/man1ext/{s/0/1/}' config.sh [Mm]akefile
sed -i '/man3ext/{s/0/3pm/}' config.sh [Mm]akefile

# make -lperl symlink
ln -snf libperl-%ver.so libperl.so

# build the rest (SMP incompatible)
make

%check
export LD_LIBRARY_PATH=$PWD LD_BIND_NOW=1 PERL_DL_NONLAZY=1
make test

%install
%make_install install.perl DESTDIR=%buildroot

# use symlinks instead of hardlinks
ln -snf perl%version %buildroot%_bindir/perl
ln -snf perl%version %buildroot%_bindir/perl5
ln -snf c2ph %buildroot%_bindir/pstruct

# skeleton
mkdir -p %buildroot%privlib/auto
mkdir -p %buildroot/etc/perl5
mkdir -p %buildroot/usr/lib/perl5/vendor_perl

# relocate libperl
mv %buildroot%archlib/CORE/libperl-%ver.so %buildroot%_libdir/
ln -snf `relative %_libdir/libperl-%ver.so %archlib/CORE/libperl.so` %buildroot%archlib/CORE/libperl.so
ln -snf `relative %_libdir/libperl-%ver.so %archlib/CORE/libperl-%ver.so` %buildroot%archlib/CORE/libperl-%ver.so

# relocate Config.pod and POSIX.pod
mv %buildroot{%archlib,%privlib}/Config.pod
mv %buildroot{%archlib,%privlib}/POSIX.pod

# cleanup modules which we package separately
rm -r %buildroot%privlib/Archive/Tar* %buildroot%_bindir/ptar*
rm -r %buildroot%privlib/autodie* %buildroot%privlib/Fatal.pm
rm -r %buildroot%privlib/Attribute/Handlers*
rm %buildroot%privlib/B/Debug.pm
rm -r %buildroot%privlib/CPAN* %buildroot%privlib/App/Cpan.pm %buildroot%_bindir/cpan*
rm -r %buildroot{%privlib,%archlib,%autolib}/Compress
rm %buildroot%privlib/Devel/SelfStubber.pm
rm -r %buildroot{%archlib,%autolib}/Digest/SHA* %buildroot%_bindir/shasum
rm -r %buildroot{%privlib,%archlib,%autolib}/Encode*
rm %buildroot%archlib/encoding.pm %buildroot%_bindir/{enc2xs,encguess,piconv}
rm %buildroot%privlib/encoding/warnings.pm
rm %buildroot%privlib/experimental.pm
rm -r %buildroot%privlib/ExtUtils/CBuilder*
rm -r %buildroot%privlib/Filter*
rm %buildroot%privlib/File/Fetch.pm
rm -r %buildroot{%archlib,%autolib}/Filter*
rm %buildroot%privlib/HTTP/Tiny.pm
rm -r %buildroot%privlib/JSON* %buildroot%_bindir/json*
rm -r %buildroot%privlib/I18N/LangTags*
rm %buildroot%privlib/I18N/Collate.pm
rm -r %buildroot%privlib/IO/{Compress,Uncompress} %buildroot%privlib/File/GlobMapper.pm
rm %buildroot%privlib/IO/Socket/IP.pm
rm -r %buildroot%privlib/IO/Zlib.pm
rm %buildroot%privlib/IPC/Cmd.pm
rm -r %buildroot{%archlib,%autolib}/IPC/SysV* %buildroot%archlib/IPC/{Msg,Semaphore,SharedMem}.pm
find %buildroot%privlib/Net/* -not -name '*ent.*' -print -delete
rm %buildroot%_bindir/libnetcfg
rm -r %buildroot%privlib/Locale
rm -r %buildroot{%privlib,%archlib,%autolib}/Math/Big* %buildroot%privlib/big*.pm
rm -r %buildroot%privlib/Math/{Complex,Trig}.pm
rm -r %buildroot%privlib/Memoize*
rm -r %buildroot%privlib/Module/Load*
rm -r %buildroot%privlib/Module/CoreList* %buildroot%_bindir/corelist
rm %buildroot%privlib/Module/Metadata.pm
rm %buildroot%privlib/NEXT.pm
rm %buildroot%privlib/Params/Check.pm
rm %buildroot%privlib/Parse/CPAN/Meta.pm
rm %buildroot%privlib/Perl/OSType.pm
rm %buildroot%privlib/Pod/Escapes.pm
rm %buildroot%privlib/Pod/{Checker,Find,InputObjects,ParseUtils,Parser,PlainText,Select,Usage}.pm
rm %buildroot%_bindir/{pod2usage,podchecker,podselect}
rm -r %buildroot%privlib/Pod/{Man,ParseLink,Text}*
rm %buildroot%_bindir/{pod2man,pod2text}
rm -r %buildroot%privlib/Pod/Perldoc* %buildroot%_bindir/perldoc
rm -r %buildroot%privlib/Pod/Simple*
rm %buildroot%privlib/Term/ANSIColor.pm
rm %buildroot%privlib/Term/Cap.pm
rm %buildroot%privlib/Term/ReadLine.pm
rm -r %buildroot%privlib/Text/Balanced*
rm %buildroot%privlib/Tie/File.pm
rm %buildroot%privlib/Tie/RefHash.pm
rm -r %buildroot{%archlib,%autolib}/Time/Piece* %buildroot%archlib/Time/Seconds.pm
rm -r %buildroot{%privlib,%archlib,%autolib}/Unicode/Collate*

rm %buildroot%_bindir/zipdetails
rm %buildroot%privlib/perlfaq.pm

# cleanup Perl4-CoreLibs
grep -lZ '^warn "Legacy library' %buildroot%privlib/*.pl |xargs -r0 rm -fv --

# further cleanup
rm %buildroot%archlib/File/Spec/{Cygwin,Epoc,Mac,OS2,VMS,Win32}.pm
rm %buildroot%privlib/ExtUtils/MM_{AIX,BeOS,Cygwin,Darwin,DOS,MacOS,NW5,OS2,QNX,UWIN,VMS,VOS,Win32,Win95}.pm
rm %buildroot%_bindir/perlivp

mkdir -p %buildroot%_rpmlibdir
cat <<EOF >%buildroot%_rpmlibdir/perl-base-files.req.list
# perl-base dirlist for %_rpmlibdir/files.req
/usr/lib/perl5	perl-base
/usr/lib64/perl5	perl-base
/usr/share/perl5	perl-base
/etc/perl5	perl-base
/usr/lib/perl5/vendor_perl	perl-base
EOF

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d/
echo perl >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/perl-base

%files	base
%doc	Artistic AUTHORS README
	%_bindir/perl
	%_bindir/perl5*
	%_libdir/libperl-%ver.so
# skeleton
%dir	%privlib
%dir	%privlib/auto
%dir	%archlib
%dir	%autolib
%dir	/etc/perl5
%dir	/usr/lib/perl5/vendor_perl
%config %_rpmlibdir/perl-base-files.req.list
%config %_sysconfdir/buildreqs/packages/substitute.d/perl-base
# pragma
	%archlib/arybase.pm
	%autolib/arybase
	%archlib/attributes.pm
	%autolib/attributes
	%privlib/autouse.pm
	%privlib/base.pm
	%privlib/bytes*
	%privlib/constant.pm
	%privlib/deprecate.pm
	%privlib/feature.pm
	%privlib/fields.pm
	%privlib/filetest.pm
	%privlib/if.pm
	%privlib/integer.pm
	%privlib/less.pm
	%archlib/lib.pm
	%privlib/locale.pm
	%privlib/meta_notation.pm
	%archlib/mro.pm
	%autolib/mro
	%privlib/open.pm
	%archlib/ops.pm
	%privlib/overload*
	%archlib/re.pm
	%autolib/re
	%privlib/sigtrap.pm
	%privlib/sort.pm
	%privlib/strict.pm
	%privlib/subs.pm
	%privlib/utf8*
	%privlib/vars.pm
	%privlib/version.pm
%doc	%privlib/version.pod
%dir	%privlib/version
	%privlib/version/regex.pm
#	%privlib/version/vpp.pm
%doc	%privlib/version/Internals.pod
	%privlib/vmsish.pm
	%privlib/warnings*
# module loaders
	%privlib/AutoLoader.pm
	%archlib/DynaLoader.pm
	%privlib/SelfLoader.pm
	%privlib/XSLoader.pm
# data utils
%dir	%archlib/Hash
	%archlib/Hash/Util*
%dir	%autolib/Hash
	%autolib/Hash/Util*
%dir	%archlib/List
	%archlib/List/Util*
%dir	%autolib/List
	%autolib/List/Util*
%dir	%archlib/Scalar
	%archlib/Scalar/Util*
%dir	%archlib/Sub
	%archlib/Sub/Util*
# initial unicode support
%dir	%privlib/unicore
	%privlib/unicore/Heavy.pl
%dir	%privlib/unicore/To
	%privlib/unicore/To/Digit.pl
	%privlib/unicore/To/Fold.pl
	%privlib/unicore/To/Lower.pl
	%privlib/unicore/To/Title.pl
	%privlib/unicore/To/Upper.pl
	%privlib/unicore/To/Cf.pl
	%privlib/unicore/To/Lc.pl
	%privlib/unicore/To/Tc.pl
	%privlib/unicore/To/Uc.pl
%dir	%privlib/unicore/lib
%dir	%privlib/unicore/lib/Alpha
	%privlib/unicore/lib/Alpha/Y.pl
%dir	%privlib/unicore/lib/Cased
	%privlib/unicore/lib/Cased/Y.pl
%dir	%privlib/unicore/lib/Gc
	%privlib/unicore/lib/Gc/Nd.pl
	%privlib/unicore/lib/Gc/P.pl
%dir	%privlib/unicore/lib/Hex
	%privlib/unicore/lib/Hex/Y.pl
%dir	%privlib/unicore/lib/Lower
	%privlib/unicore/lib/Lower/Y.pl
%dir	%privlib/unicore/lib/Nt
	%privlib/unicore/lib/Nt/Di.pl
	%privlib/unicore/lib/Nt/Nu.pl
%dir	%privlib/unicore/lib/Perl
	%privlib/unicore/lib/Perl/_PerlIDS.pl
	%privlib/unicore/lib/Perl/Alnum.pl
	%privlib/unicore/lib/Perl/Blank.pl
	%privlib/unicore/lib/Perl/Graph.pl
	%privlib/unicore/lib/Perl/Print.pl
	%privlib/unicore/lib/Perl/Word.pl
%dir	%privlib/unicore/lib/Upper
	%privlib/unicore/lib/Upper/Y.pl
# modules
	%privlib/Carp*
	%archlib/Config.pm
	%archlib/Config_heavy.pl
	%archlib/Config_git.pl
%dir	%privlib/Config
	%privlib/Config/Extensions.pm
%dir	%privlib/Config/Perl
	%privlib/Config/Perl/V.pm
%dir	%privlib/Class
	%privlib/Class/Struct.pm
	%archlib/Cwd.pm
	%autolib/Cwd
%dir	%archlib/Data
	%archlib/Data/Dumper.pm
%dir	%autolib/Data
	%autolib/Data/Dumper
	%privlib/Digest.pm
%dir	%privlib/Digest
	%privlib/Digest/base.pm
	%privlib/Digest/file.pm
%dir	%archlib/Digest
	%archlib/Digest/MD5.pm
%dir	%autolib/Digest
	%autolib/Digest/MD5
	%privlib/English.pm
	%archlib/Errno.pm
	%privlib/Exporter*
	%archlib/Fcntl.pm
	%autolib/Fcntl
%dir	%privlib/File
	%privlib/File/Basename.pm
	%privlib/File/Compare.pm
	%privlib/File/Copy.pm
	%privlib/File/Find.pm
	%privlib/File/Path.pm
	%privlib/File/stat.pm
	%privlib/File/Temp.pm
	%privlib/FileHandle.pm
%dir	%archlib/File
	%archlib/File/Glob.pm
	%archlib/File/DosGlob.pm
%dir	%autolib/File
	%autolib/File/Glob
	%autolib/File/DosGlob
	%archlib/File/Spec*
	%privlib/FindBin.pm
%dir	%privlib/Getopt
	%privlib/Getopt/Long.pm
	%privlib/Getopt/Std.pm
	%archlib/IO.pm
%dir	%archlib/IO
	%archlib/IO/Dir.pm
	%archlib/IO/File.pm
	%archlib/IO/Handle.pm
	%archlib/IO/Pipe.pm
	%archlib/IO/Poll.pm
	%archlib/IO/Seekable.pm
	%archlib/IO/Select.pm
	%archlib/IO/Socket*
%dir	%autolib/IO
	%autolib/IO/IO.so
%dir	%privlib/IPC
	%privlib/IPC/Open2.pm
	%privlib/IPC/Open3.pm
%dir	%archlib/MIME
	%archlib/MIME/Base64.pm
	%archlib/MIME/QuotedPrint.pm
%dir	%autolib/MIME
	%autolib/MIME/Base64
	%privlib/PerlIO*
	%archlib/PerlIO*
	%autolib/PerlIO*
	%archlib/POSIX.pm
	%autolib/POSIX
	%privlib/SelectSaver.pm
	%archlib/Socket.pm
	%autolib/Socket
	%archlib/Storable.pm
	%autolib/Storable
	%privlib/Symbol.pm
%dir	%archlib/Sys
	%archlib/Sys/Hostname.pm
	%archlib/Sys/Syslog.pm
%dir	%autolib/Sys
	%autolib/Sys/Hostname
	%autolib/Sys/Syslog
%dir	%privlib/Text
	%privlib/Text/Abbrev.pm
	%privlib/Text/ParseWords.pm
	%privlib/Text/Tabs.pm
	%privlib/Text/Wrap.pm
%dir	%privlib/Tie
	%privlib/Tie/Array.pm
	%privlib/Tie/Handle.pm
	%privlib/Tie/Hash*
%dir	%archlib/Tie
	%archlib/Tie/Hash*
%dir	%autolib/Tie
	%autolib/Tie/Hash*
	%privlib/Tie/Memoize.pm
	%privlib/Tie/Scalar.pm
	%privlib/Tie/StdHandle.pm
	%privlib/Tie/SubstrHash.pm
%dir	%privlib/Time
	%privlib/Time/gmtime.pm
	%privlib/Time/localtime.pm
	%privlib/Time/tm.pm
	%privlib/Time/Local.pm
%dir	%archlib/Time
	%archlib/Time/HiRes.pm
%dir	%autolib/Time
	%autolib/Time/HiRes
	%privlib/UNIVERSAL.pm
# required for perl.req and perl.prov
	%archlib/B.pm
%dir	%autolib/B
	%autolib/B/B.so
	%archlib/O.pm
	%archlib/Opcode.pm
	%autolib/Opcode
	%privlib/Safe.pm
# rarely used but part of perl
	%privlib/Benchmark.pm
%doc	%privlib/CORE.pod
	%privlib/DirHandle.pm
	%privlib/Env.pm
	%privlib/FileCache.pm
%dir	%archlib/I18N
	%archlib/I18N/Langinfo.pm
%dir	%autolib/I18N
	%autolib/I18N/Langinfo
%dir	%privlib/Net
	%privlib/Net/*ent.pm
%dir	%privlib/Pod
	%privlib/Pod/Functions.pm
%dir	%privlib/Search
	%privlib/Search/Dict.pm
%dir	%privlib/Term
	%privlib/Term/Complete.pm
%dir	%privlib/User
	%privlib/User/*ent.pm
# in separate package perl-parent; required in buildroot for tests
%exclude %privlib/parent.pm

%files	devel
	%_bindir/h2xs
	%_bindir/instmodsh
	%_bindir/perlbug
	%_bindir/perlthanks
	%_bindir/prove
	%_bindir/splain
	%_bindir/xsubpp
# perl4-compat scripts
	%_bindir/h2ph
	%_bindir/pl2pm
	%_bindir/c2ph
	%_bindir/pstruct
	%privlib/blib.pm
	%privlib/diagnostics.pm
	%privlib/dumpvar.pl
	%privlib/perl5db.pl
	%privlib/Dumpvalue.pm
%dir	%archlib/CORE
	%archlib/CORE/*.h
	%archlib/CORE/libperl*.so
# perl-devel modules
	%privlib/AutoSplit.pm
	%privlib/B
	%archlib/B
	%autolib/B
%exclude %autolib/B/B.so
	%privlib/DB.pm
%dir	%archlib/Devel
	%archlib/Devel/Peek.pm
	%archlib/Devel/PPPort.pm
%dir	%autolib/Devel
	%autolib/Devel/Peek
	# explicitly ignored in installperl
	#%autolib/Devel/PPPort
%dir	%privlib/ExtUtils
	%privlib/ExtUtils/Command*
	%privlib/ExtUtils/Constant*
	%privlib/ExtUtils/Embed.pm
	%privlib/ExtUtils/Install.pm
	%privlib/ExtUtils/Installed.pm
	%privlib/ExtUtils/Liblist*
	%privlib/ExtUtils/MakeMaker.pm
%dir	%privlib/ExtUtils/MakeMaker
	%privlib/ExtUtils/MakeMaker/*.pm
	# explicitly ignored in installperl; returned by tmp hack (Patch18)
%dir	%privlib/ExtUtils/MakeMaker/version
	%privlib/ExtUtils/MakeMaker/version/*.pm
%doc	%privlib/ExtUtils/MakeMaker/*.pod
	%privlib/ExtUtils/MM.pm
	%privlib/ExtUtils/MM_Any.pm
	%privlib/ExtUtils/MM_Unix.pm
	%privlib/ExtUtils/MY.pm
	%privlib/ExtUtils/MANIFEST.SKIP
	%privlib/ExtUtils/Manifest.pm
	%privlib/ExtUtils/Miniperl.pm
	%privlib/ExtUtils/Mkbootstrap.pm
	%privlib/ExtUtils/Mksymlists.pm
	%privlib/ExtUtils/Packlist.pm
%dir	%privlib/ExtUtils/ParseXS
	%privlib/ExtUtils/ParseXS/*.pm
	%privlib/ExtUtils/ParseXS.pm
%doc	%privlib/ExtUtils/ParseXS.pod
%dir	%privlib/ExtUtils/Typemaps
	%privlib/ExtUtils/Typemaps/*.pm
	%privlib/ExtUtils/Typemaps.pm
	%privlib/ExtUtils/testlib.pm
	%privlib/ExtUtils/typemap
	%privlib/ExtUtils/xsubpp
%dir	%privlib/Pod
	%privlib/Pod/Html.pm
	%_bindir/pod2html
	%privlib/Test.pm
%dir	%privlib/Test
%doc	%privlib/Test/Tutorial.pod
%dir	%privlib/pod
# perldiag.pod is NOT a doc; it used by diagnostics.pm
	%privlib/pod/perldiag.pod
# Test-Simple pieces
	%privlib/ok.pm
	%privlib/Test/Builder*
	%privlib/Test/More.pm
	%privlib/Test/Simple.pm
%dir	%privlib/Test/use
	%privlib/Test/use/ok.pm
	%privlib/Test/Tester.pm
%dir	%privlib/Test/Tester
	%privlib/Test/Tester/Capture.pm
	%privlib/Test/Tester/CaptureRunner.pm
	%privlib/Test/Tester/Delegate.pm
# Test-Harness pieces
%dir	%privlib/App
	%privlib/App/Prove*
	%privlib/TAP
	%privlib/Test/Harness.pm

%files	pod
%dir	%privlib/pod
%doc	%privlib/pod/perl*.pod
%exclude %privlib/pod/perldiag.pod
%exclude %privlib/pod/perldbmfilter.pod
%doc	%privlib/Config.pod
%doc	%privlib/POSIX.pod

%files	threads
	%privlib/Thread*
	%archlib/threads*
	%autolib/threads

%files	unicore
	%privlib/charnames.pm
	%privlib/_charnames.pm
%dir	%privlib/Unicode
	%privlib/Unicode/UCD.pm
%dir	%privlib/unicore
	%privlib/unicore/version
	%privlib/unicore/Name.pm
	%privlib/unicore/Name.pl
	%privlib/unicore/UCD.pl
	%privlib/unicore/lib/

%exclude %privlib/unicore/lib/Alpha/Y.pl
%exclude %privlib/unicore/lib/Cased/Y.pl
%exclude %privlib/unicore/lib/Gc/Nd.pl
%exclude %privlib/unicore/lib/Gc/P.pl
%exclude %privlib/unicore/lib/Hex/Y.pl
%exclude %privlib/unicore/lib/Lower/Y.pl
%exclude %privlib/unicore/lib/Nt/Di.pl
%exclude %privlib/unicore/lib/Nt/Nu.pl
%exclude %privlib/unicore/lib/Perl/_PerlIDS.pl
%exclude %privlib/unicore/lib/Perl/Alnum.pl
%exclude %privlib/unicore/lib/Perl/Blank.pl
%exclude %privlib/unicore/lib/Perl/Graph.pl
%exclude %privlib/unicore/lib/Perl/Print.pl
%exclude %privlib/unicore/lib/Perl/Word.pl
%exclude %privlib/unicore/lib/Upper/Y.pl
	%privlib/unicore/To/
%exclude %privlib/unicore/To/Digit.pl
%exclude %privlib/unicore/To/Fold.pl
%exclude %privlib/unicore/To/Lower.pl
%exclude %privlib/unicore/To/Title.pl
%exclude %privlib/unicore/To/Upper.pl
%exclude %privlib/unicore/To/Cf.pl
%exclude %privlib/unicore/To/Lc.pl
%exclude %privlib/unicore/To/Tc.pl
%exclude %privlib/unicore/To/Uc.pl
# required to build Unicode::Normalize
	%privlib/unicore/CombiningClass.pl
	%privlib/unicore/Decomposition.pl
# required for Unicode::UCD
	%privlib/unicore/Blocks.txt
	%privlib/unicore/SpecialCasing.txt
# not required
	%privlib/unicore/NamedSequences.txt

%files	DBM
	%privlib/AnyDBM_File.pm
	%archlib/DB_File.pm
	%autolib/DB_File
	%archlib/NDBM_File.pm
	%autolib/NDBM_File
	%archlib/GDBM_File.pm
	%autolib/GDBM_File
	%archlib/SDBM_File.pm
	%autolib/SDBM_File
	%privlib/DBM_Filter*
%dir	%privlib/pod
%doc	%privlib/pod/perldbmfilter.pod

%files	Unicode-Normalize
%dir	%archlib/Unicode
	%archlib/Unicode/Normalize.pm
	%autolib/Unicode

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.3-alt2
- added patch21 from Oleg Solovyov

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.3-alt1
- 5.24.2 -> 5.24.3

* Wed Aug 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.2-alt1
- 5.24.1 -> 5.24.2 (CVE-2016-1238)

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.1-alt1
- 5.22.3 -> 5.24.1
- build with -Duse64bitint on %%{ix86}

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.22.3-alt1
- 5.22.2 -> 5.22.3

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.2-alt2
- cpan-update-Scalar-List-Utils-1.41-to-Scalar-List-Utils-1.41-1.46

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.2-alt1
- 5.22.1 -> 5.22.2

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.1-alt2
- added buildreqs substitute.d perl-base -> perl

* Wed Dec 16 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.1-alt1
- 5.22.0 -> 5.22.1

* Sun Nov 29 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.0-alt2
- added Provides/Conflicts on perl-Test-use-ok (now in perl-devel)

* Tue Nov 10 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.0-alt1
- 5.20.3 -> 5.22.0

* Wed Oct 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.20.3-alt1
- Updated to 5.20.3.

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.20.1-alt2
- cpan update: Socket-2.013 to Socket-2.016

* Fri Nov 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.20.1-alt1
- 5.18.2 -> 5.20.1

* Wed Jan 08 2014 Vladimir Lettiev <crux@altlinux.ru> 1:5.18.2-alt1
- 5.18.1 -> 5.18.2

* Tue Aug 20 2013 Vladimir Lettiev <crux@altlinux.ru> 1:5.18.1-alt1
- 5.16.3 -> 5.18.1
- Version::Requirements removed from core
- File::DosGlob moved to archlib
- Updated Text::Tabs to 2013.0523

* Tue Mar 12 2013 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.3-alt1
- 5.16.2 -> 5.16.3
- Fixed CVE-2013-1667: memory exhaustion with arbitrary hash keys

* Tue Nov 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.2-alt1
- 5.16.1 -> 5.16.2

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1:5.16.1-alt3
- Storable.pm: restored patch to avoid early dependency on Log::Agent
- ExtUtils/MM_Any.pm: disabled CPAN::Meta under rpm
- moved unicore/lib/Perl/_PerlIDS.pl to perl-base, for constant.pm
- moved unicore/To/Tc.pl to perl-base, required for ucfirst()

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.1-alt2
- unicore database files moved to perl-base:
  * unicore/To/Cf.pl (format control characters)
  * unicore/To/Lc.pl (lowercase)
  * unicore/To/Uc.pl (uppercase)

* Thu Aug 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.1-alt1
- 5.14.2 -> 5.16.1
- Devel::DProf, Shell moved from core
- added new arybase pragma

* Fri Jan 20 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.14.2-alt4
- updated Digest 1.16 -> 1.17 (fixed CVE-2011-3597)

* Sat Jan 14 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.14.2-alt3
- updated Safe.pm 2.29 -> 2.30 (closes: #26802)

* Wed Nov 02 2011 Alexey Tourbin <at@altlinux.ru> 1:5.14.2-alt2
- moved unicore/Cased/Y.pl to perl-base

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1:5.14.2-alt1
- 5.12.4 -> 5.14.2
- perl-pod: packaged OS-specific docs (e.g. perlaix.pod) as they are
  referenced in perl.pod and perltoc.pod
- packaged perl-Unicode-Normalize subpackage as it is now required in
  perl-unicore by Unicode::UCD
- perl4-compat is replaced by separate CPAN distribution Perl4-CoreLibs
- new modules packaged as separate CPAN distributions: HTTP-Tiny,
  Perl-OSType, Module-Metadata, Version-Requirements, JSON-PP
- older modules packaged as separate CPAN distributions: File-CheckTree,
  I18N-Collate, Devel-DProf, Devel-SelfStubber
- another coming of static_XS.patch

* Mon Sep 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.12.4-alt2
- Fixed regression on x86-64 introduced in 5.12.4 (closes: #26249).

* Sat Sep 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.4-alt1
- 5.12.3 -> 5.12.4
- Updated MIME::Base64 3.08 -> 3.13 (Closes: #25646)

* Mon Apr 18 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.12.3-alt4
- Reverted the change in XS functions prototypes introduced in previous
  release, due to massive build breakage (closes: #23793).

* Tue Apr 05 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt3
- overhauled static_XS.patch - all XS functions are now static by default
- updated ExtUtil-ParseXS to CPAN version 2.2206
- updated Test-Simple to CPAN version 0.98
- deprecate.pm: disabled warning for vendor directories

* Fri Feb 11 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt2
- rebuilt for debuginfo
- revived static_XS.patch - auto-generated XS functions static by default

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt1
- 5.12.2 -> 5.12.3
- merged perl-PerlIO and perl-Storable into perl-base
- moved some files from unicore library to perl-base (closes: #24733)
- moved Config.pod and POSIX.pod from perl-devel to perl-pod

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.2-alt02
- redefined default sitelib paths

* Sun Nov 14 2010 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.2-alt01
- re.so moved from perl-devel to perl-base (Closes: #24561)

* Thu Sep 16 2010 Alexey Tourbin <at@altlinux.ru> 1:5.12.2-alt00
- packaged from scratch
