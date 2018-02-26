Name: perl
Version: 5.14.2
Release: alt4
Epoch: 1

Summary: Practical Extraction and Report Language
License: GPL or Artistic
Group: Development/Perl
URL: http://www.perl.org
Packager: Alexey Tourbin <at@altlinux.ru>

Source: perl-%version.tar
Patch: perl-%version-%release.patch

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

# do not provide auxiliary unicore libraries
%add_findprov_skiplist */unicore/*/*

BuildRequires: /proc
BuildRequires: libdb4-devel libgdbm-devel

%package base
Summary: Pathologically Eclectic Rubbish Lister
Group: System/Base
Provides: perl = %epoch:%version
Obsoletes: perl < %epoch:%version
Provides: perl-version = 0.88
Obsoletes: perl-version < 0.88
Provides: perl-PerlIO = %epoch:%version perl-Storable = %epoch:%version
Obsoletes: perl-PerlIO < %epoch:%version perl-Storable < %epoch:%version
Provides: perl-Digest-MD5 perl-Time-HiRes perl-MIME-Base64
Obsoletes: perl-Digest-MD5 perl-Time-HiRes perl-MIME-Base64

%package devel
Summary: Perl header files and development modules
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release

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
%patch -p1

%build
%define ver %(v=%version IFS=.; set $v; echo $1.$2)
%define privlib /usr/share/perl5
%define archlib %_libdir/perl5
%define autolib %archlib/auto
%define site_prefix %_prefix/local
%define site_privlib %site_prefix/share/perl/%ver
%define site_archlib %site_prefix/%_lib/perl/%ver

sh Configure -ders \
	-Dusethreads -Duseithreads -Duselargefiles \
	-Duseshrplib -Dlibperl=libperl-%ver.so \
	-Dcc=gcc -Doptimize="%optflags" -DDEBUGGING=maybe \
	-Dprefix=%_prefix -Dprivlib=%privlib -Darchlib=%archlib \
	-Dvendorprefix=%_prefix -Dvendorlib=%privlib -Dvendorarch=%archlib \
	-Dsiteprefix=%site_prefix -Dsitelib=%site_privlib -Dsitearch=%site_archlib \
	-Dotherlibdirs=/etc/perl5:/usr/lib/perl5/vendor_perl \
	-Dinc_version_list=none \
	-Dpager='%_bindir/less -isR' \
	-Dman1dir=none -Dman3dir=none \
	-Dcf_by='%vendor' -Dcf_email='%packager' \
	-Dmyhostname=localhost -Dperladmin=root@localhost

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
ln -snf psed %buildroot%_bindir/s2p

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
rm %buildroot%privlib/Archive/Extract.pm
rm -r %buildroot%privlib/Archive/Tar* %buildroot%_bindir/ptar*
rm -r %buildroot%privlib/autodie* %buildroot%privlib/Fatal.pm
rm -r %buildroot%privlib/Attribute/Handlers*
rm %buildroot%privlib/B/Debug.pm
rm -r %buildroot%privlib/B/Lint*
rm -r %buildroot%privlib/CGI*
rm -r %buildroot%privlib/CPAN* %buildroot%privlib/App/Cpan.pm %buildroot%_bindir/cpan*
rm -r %buildroot{%privlib,%archlib,%autolib}/Compress
rm -r %buildroot{%archlib,%autolib}/Devel/DProf* %buildroot%_bindir/dprofpp
rm %buildroot%privlib/Devel/SelfStubber.pm
rm -r %buildroot{%archlib,%autolib}/Digest/SHA* %buildroot%_bindir/shasum
rm -r %buildroot{%privlib,%archlib,%autolib}/Encode*
rm %buildroot%archlib/encoding.pm %buildroot%_bindir/{enc2xs,piconv}
rm %buildroot%privlib/encoding/warnings.pm
rm -r %buildroot%privlib/ExtUtils/CBuilder*
rm -r %buildroot%privlib/Filter*
rm %buildroot%privlib/File/CheckTree.pm
rm %buildroot%privlib/File/Fetch.pm
rm -r %buildroot{%archlib,%autolib}/Filter*
rm %buildroot%privlib/HTTP/Tiny.pm
rm -r %buildroot%privlib/JSON* %buildroot%_bindir/json*
rm -r %buildroot%privlib/I18N/LangTags*
rm %buildroot%privlib/I18N/Collate.pm
rm -r %buildroot%privlib/IO/{Compress,Uncompress} %buildroot%privlib/File/GlobMapper.pm
rm -r %buildroot%privlib/IO/Zlib.pm
rm %buildroot%privlib/IPC/Cmd.pm
rm -r %buildroot{%archlib,%autolib}/IPC/SysV* %buildroot%archlib/IPC/{Msg,Semaphore,SharedMem}.pm
find %buildroot%privlib/Net/* -not -name '*ent.*' -print -delete
rm %buildroot%_bindir/libnetcfg
rm -r %buildroot%privlib/Locale
rm -r %buildroot%privlib/Log/Message*
rm -r %buildroot{%privlib,%archlib,%autolib}/Math/Big* %buildroot%privlib/big*.pm
rm -r %buildroot%privlib/Math/{Complex,Trig}.pm
rm -r %buildroot%privlib/Memoize*
rm -r %buildroot%privlib/Module/Build* %buildroot%privlib/inc %buildroot%_bindir/config_data
rm -r %buildroot%privlib/Module/Load*
rm -r %buildroot%privlib/Module/Pluggable* %buildroot%privlib/Devel/InnerPackage.pm
rm %buildroot%privlib/Module/CoreList.pm %buildroot%_bindir/corelist
rm %buildroot%privlib/Module/Metadata.pm
rm %buildroot%privlib/NEXT.pm
rm %buildroot%privlib/Object/Accessor.pm
rm %buildroot%privlib/Package/Constants.pm
rm %buildroot%privlib/Params/Check.pm
rm %buildroot%privlib/parent.pm
rm %buildroot%privlib/Parse/CPAN/Meta.pm
rm %buildroot%privlib/Perl/OSType.pm
rm %buildroot%privlib/Pod/Escapes.pm
rm %buildroot%privlib/Pod/LaTeX.pm %buildroot%_bindir/pod2latex
rm %buildroot%privlib/Pod/{Checker,Find,InputObjects,ParseUtils,Parser,PlainText,Select,Usage}.pm
rm %buildroot%_bindir/{pod2usage,podchecker,podselect}
rm -r %buildroot%privlib/Pod/{Man,ParseLink,Text}*
rm %buildroot%_bindir/{pod2man,pod2text}
rm -r %buildroot%privlib/Pod/Perldoc* %buildroot%_bindir/perldoc
rm -r %buildroot%privlib/Pod/Simple*
rm %buildroot%privlib/Shell.pm
rm %buildroot%privlib/Term/ANSIColor.pm
rm %buildroot%privlib/Term/Cap.pm
rm %buildroot%privlib/Term/ReadLine.pm
rm -r %buildroot%privlib/Term/UI*
rm -r %buildroot%privlib/Text/Balanced*
rm -r %buildroot{%archlib,%autolib}/Text/Soundex*
rm %buildroot%privlib/Tie/File.pm
rm %buildroot%privlib/Tie/RefHash.pm
rm -r %buildroot{%archlib,%autolib}/Time/Piece* %buildroot%archlib/Time/Seconds.pm
rm -r %buildroot{%privlib,%archlib,%autolib}/Unicode/Collate*
rm %buildroot%privlib/Version/Requirements.pm

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
# pragma
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
# initial unicode support
%dir	%privlib/unicore
	%privlib/unicore/Heavy.pl
%dir	%privlib/unicore/To
	%privlib/unicore/To/Digit.pl
	%privlib/unicore/To/Fold.pl
	%privlib/unicore/To/Lower.pl
	%privlib/unicore/To/Title.pl
	%privlib/unicore/To/Upper.pl
%dir	%privlib/unicore/lib
%dir	%privlib/unicore/lib/Alpha
	%privlib/unicore/lib/Alpha/Y.pl
%dir	%privlib/unicore/lib/Blk
	%privlib/unicore/lib/Blk/ASCII.pl
%dir	%privlib/unicore/lib/Cased
	%privlib/unicore/lib/Cased/Y.pl
%dir	%privlib/unicore/lib/Gc
	%privlib/unicore/lib/Gc/Cc.pl
	%privlib/unicore/lib/Gc/P.pl
%dir	%privlib/unicore/lib/Hex
	%privlib/unicore/lib/Hex/Y.pl
%dir	%privlib/unicore/lib/Lower
	%privlib/unicore/lib/Lower/Y.pl
%dir	%privlib/unicore/lib/Nt
	%privlib/unicore/lib/Nt/De.pl
%dir	%privlib/unicore/lib/Perl
	%privlib/unicore/lib/Perl/Alnum.pl
	%privlib/unicore/lib/Perl/Blank.pl
	%privlib/unicore/lib/Perl/Graph.pl
	%privlib/unicore/lib/Perl/Print.pl
	%privlib/unicore/lib/Perl/SpacePer.pl
	%privlib/unicore/lib/Perl/Word.pl
%dir	%privlib/unicore/lib/Space
	%privlib/unicore/lib/Space/Y.pl
%dir	%privlib/unicore/lib/Upper
	%privlib/unicore/lib/Upper/Y.pl
# modules
	%privlib/Carp*
	%archlib/Config.pm
	%archlib/Config_heavy.pl
	%archlib/Config_git.pl
%dir	%privlib/Config
	%privlib/Config/Extensions.pm
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
	%privlib/File/DosGlob.pm
	%privlib/File/Find.pm
	%privlib/File/Path.pm
	%privlib/File/stat.pm
	%privlib/File/Temp.pm
	%privlib/FileHandle.pm
%dir	%archlib/File
	%archlib/File/Glob.pm
%dir	%autolib/File
	%autolib/File/Glob
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

%files	devel
	%_bindir/a2p
	%_bindir/find2perl
	%_bindir/h2xs
	%_bindir/instmodsh
	%_bindir/perlbug
	%_bindir/perlthanks
	%_bindir/prove
	%_bindir/psed
	%_bindir/s2p
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
	%autolib/Devel/PPPort
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
	%privlib/ExtUtils/ParseXS.pm
	%privlib/ExtUtils/testlib.pm
	%privlib/ExtUtils/typemap
	%privlib/ExtUtils/xsubpp
%dir	%privlib/Pod
	%privlib/Pod/Html.pm
	%_bindir/pod2html
	%privlib/Test.pm
%dir	%privlib/Test
	%privlib/Test/Builder*
	%privlib/Test/Harness.pm
	%privlib/Test/More.pm
	%privlib/Test/Simple.pm
%doc	%privlib/Test/Tutorial.pod
%dir	%privlib/pod
%doc	%privlib/pod/a2p.pod
# perldiag.pod is NOT a doc; it used by diagnostics.pm
	%privlib/pod/perldiag.pod
# Test-Harness pieces
%dir	%privlib/App
	%privlib/App/Prove*
	%privlib/TAP

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
%dir	%privlib/Unicode
	%privlib/Unicode/UCD.pm
%dir	%privlib/unicore
	%privlib/unicore/version
	%privlib/unicore/Name.pl
	%privlib/unicore/lib/
%exclude %privlib/unicore/lib/Alpha/Y.pl
%exclude %privlib/unicore/lib/Blk/ASCII.pl
%exclude %privlib/unicore/lib/Cased/Y.pl
%exclude %privlib/unicore/lib/Gc/Cc.pl
%exclude %privlib/unicore/lib/Gc/P.pl
%exclude %privlib/unicore/lib/Hex/Y.pl
%exclude %privlib/unicore/lib/Lower/Y.pl
%exclude %privlib/unicore/lib/Nt/De.pl
%exclude %privlib/unicore/lib/Perl/Alnum.pl
%exclude %privlib/unicore/lib/Perl/Blank.pl
%exclude %privlib/unicore/lib/Perl/Graph.pl
%exclude %privlib/unicore/lib/Perl/Print.pl
%exclude %privlib/unicore/lib/Perl/SpacePer.pl
%exclude %privlib/unicore/lib/Perl/Word.pl
%exclude %privlib/unicore/lib/Space/Y.pl
%exclude %privlib/unicore/lib/Upper/Y.pl
	%privlib/unicore/To/
%exclude %privlib/unicore/To/Digit.pl
%exclude %privlib/unicore/To/Fold.pl
%exclude %privlib/unicore/To/Lower.pl
%exclude %privlib/unicore/To/Title.pl
%exclude %privlib/unicore/To/Upper.pl
# required for Unicode::Normalize
	%privlib/unicore/CombiningClass.pl
	%privlib/unicore/Decomposition.pl
	%privlib/unicore/CompositionExclusions.txt
# required for Unicode::UCD
	%privlib/unicore/Blocks.txt
	%privlib/unicore/CaseFolding.txt
	%privlib/unicore/SpecialCasing.txt

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
	%autolib/sdbm
	%privlib/DBM_Filter*
%dir	%privlib/pod
%doc	%privlib/pod/perldbmfilter.pod

%files	Unicode-Normalize
%dir	%archlib/Unicode
	%archlib/Unicode/Normalize.pm
%dir	%autolib/Unicode
	%autolib/Unicode/Normalize

%changelog
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
