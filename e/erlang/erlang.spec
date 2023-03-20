%define _unpackaged_files_terminate_build 1

%def_with otp_debug
%def_with otp_native

%def_with ssl
%def_with termcap
%def_with gmp
%def_with java

%def_enable docs
%def_enable kernel_poll
%def_enable megaco_flex_scanner_lineno
%def_enable threads
%def_enable sctp
%def_disable lock_checking
%def_disable lock_counting

%def_disable strip_beam

%define subst_enable_to() %{expand:%%{?_enable_%1:--enable-%2}} %{expand:%%{?_disable_%1:--disable-%2}}
%define subst_with_to() %{expand:%%{?_with_%1:--with-%2}} %{expand:%%{?_without_%1:--without-%2}}

%define java_options -Xmx512m
%define fop_options -Xmx512m

#----------------------------------------------------------------------

%define Name Erlang
Name: erlang
Epoch: 1
Version: 25.3
Release: alt1
Summary: A programming language developed by Ericsson
License: Apache-2.0
Group: Development/Erlang
Url: http://www.erlang.org

Source: otp_src_OTP-%version.tar

Source5: epmd.service
Source6: epmd.socket
Source7: epmd@.service
Source8: epmd@.socket

Requires: %name-otp-modules = %version-%release
Provides: erlang_mod(demo) = %version

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-erlang
BuildRequires(pre): rpm-build-erlang

BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: /proc
BuildRequires: symlinks
BuildRequires: zlib-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libunixODBC-devel
BuildRequires: libGLU-devel
BuildRequires: libsystemd-devel

%{?_enable_sctp:BuildRequires: liblksctp-devel}
%{?_enable_docs:BuildRequires: xml-utils xsltproc %_bindir/fop}
%{?_with_java:BuildRequires: java-devel-default}
%{?_with_ssl:BuildRequires: libssl-devel openssl libkrb5-devel}
%{?_with_gmp:BuildRequires: libgmp-devel}
%{?_with_termcap:BuildRequires: libncurses-devel}

%description
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.


%package devel
Summary: Libs and headers for devel for Erlang
Group: Development/C
Requires: %name = %EVR

%description devel
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package contains Libs and headers for devel for Erlang.


%package full
Summary: Full Erlang/OTP package
Group: Development/Erlang
BuildArch: noarch
Requires: %name-otp-full = %EVR
Requires: %name-examples = %EVR
%{?_with_java:Requires: %name-jinterface = %EVR}

%description full
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package requires all standard Erlang/OTP subpackages.


%package otp-full
Summary: Full Erlang OTP package
Group: Development/Erlang
BuildArch: noarch
Requires: %name-otp = %EVR
Requires: %name-megaco = %EVR
Requires: %name-odbc = %EVR
Requires: %name-visual = %EVR
Requires: %name-common_test = %EVR

%description otp-full
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package requires all standard Erlang OTP subpackages.


%package otp
Summary: Standard Erlang OTP
BuildArch: noarch
Group: Development/Erlang
Provides: %name-otp-modules = %EVR
Provides: otp = %EVR
Requires: %name-otp-common = %EVR
Requires: %name-otp-bin = %EVR

%description otp
Standard Erlang OTP.


%package otp-common
Summary: Standard Erlang OTP - common files
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %EVR
Provides: otp-common = %EVR

%description otp-common
Standard Erlang OTP.
This package contains common Erlang OTP files.


%package otp-bin
Summary: Standard Erlang OTP - arch-depend binaries
Group: Development/Erlang
Provides: otp-bin = %EVR
Requires: %name-otp-common = %EVR

%description otp-bin
Standard Erlang OTP.
This package contains arch-depend binaries Erlang OTP files.


%package otp-devel
Summary: Headers for standard Erlang OTP
Group: Development/Erlang
BuildArch: noarch
Provides: otp-devel = %EVR
Requires: %name-otp-common = %EVR
Requires: %name-otp-modules = %EVR

%description otp-devel
Headers for standard Erlang OTP.


%package megaco
Summary: H.248 support for Erlang
Group: Development/Erlang
BuildArch: noarch
Provides: %name-megaco-modules = %EVR
Requires: %name-megaco-drivers = %EVR
Requires: %name-visual = %EVR

%description megaco
Megaco (aka H.248) is a signalling protocol used in VoIP networks.
This package contains modules for Erlang Megaco.


%package megaco-drivers
Summary: H.248 support for Erlang - drivers
Group: Development/Erlang
Requires: %name-megaco = %EVR

%description megaco-drivers
Megaco (aka H.248) is a signalling protocol used in VoIP networks.
This package contains drivers for Erlang/OTP Megaco files.


%package megaco-devel
Summary: Headers for Erlang megaco modules
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-megaco = %EVR

%description megaco-devel
Headers for Erlang megaco modules.


%package odbc
Summary: ODBC support for Erlang
Group: Development/Erlang
BuildArch: noarch
Provides: %name-odbc-modules = %EVR
Requires: %name-odbc-server = %EVR

%description odbc
ODBC support for Erlang programming language.


%package odbc-server
Summary: Server for Erlang/OTP ODBC driver
Group: Development/Erlang
Requires: %name-odbc = %EVR

%description odbc-server
ODBC support for Erlang programming language.
This package contains Server for Erlang/OTP ODBC driver.


%package odbc-devel
Summary: Headers for Erlang ODBC modules
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-odbc-modules = %EVR

%description odbc-devel
Headers for Erlang ODBC modules.


%package visual
Summary: Standart visual applications for Erlang
Group: Development/Erlang
BuildArch: noarch
Provides: %name-visual-modules = %EVR
Requires: %name-visual-common = %EVR

%description visual
Standard visual applications and modules for Erlang programming
language.


%package visual-common
Summary: Standart visual applications for Erlang - common files
Group: Development/Erlang
Requires: %name-otp = %EVR
Requires: tk

%description visual-common
Standard visual applications for Erlang programming language.
This package contains common files for Erlang visual applications.


%package visual-devel
Summary: Headers for standart visual Erlang modules
Group: Development/Erlang
BuildArch: noarch
Requires: %name-visual = %EVR

%description visual-devel
Headers for standart visual Erlang modules.


%package common_test
Summary: A portable framework for automatic testing Erlang applications
Group: Development/Erlang
BuildArch: noarch
Provides: %name-common_test-modules = %EVR
Requires: %name-common_test-common = %EVR

%description common_test
A portable framework for automatic testing Erlang applications.


%package common_test-common
Summary: A portable framework for automatic testing Erlang applications - common files
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %EVR

%description common_test-common
A portable framework for automatic testing Erlang applications.
This package contains common Erlang common_test files.


%package common_test-bin
Summary: A portable framework for automatic testing Erlang applications arch-depend binaries.
Group: Development/Erlang
Conflicts: speech-dispatcher
Requires: %name-common_test = %EVR

%description common_test-bin
A portable framework for automatic testing Erlang applications arch-depend binaries.


%package common_test-devel
Summary: Headers for Erlang common_test modules
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-common_test-modules = %EVR

%description common_test-devel
Headers for Erlang common_test modules.


%package examples
Summary: OTP examples
Group: Development/Erlang
BuildArch: noarch
Requires: %name-megaco = %EVR
Requires: %name-visual = %EVR
AutoProv: no
AutoReq: no

%description examples
OTP examples.


%package emacs
Summary: Compiled elisp files for erlang-mode under GNU Emacs.
Group: Development/Erlang
BuildArch: noarch
Requires: %name-otp = %EVR

%description emacs
Compiled elisp files for erlang-mode under GNU Emacs.


%if_with java
%package jinterface
Summary: Erlang's level interface to Java
Group: Development/Erlang
BuildArch: noarch
Requires: %name-otp = %EVR

%description jinterface
Erlang's level interface to Java.


%package jinterface-debug
Summary: Erlang's level interface to Java - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Requires: %name-jinterface = %EVR

%description jinterface-debug
Erlang's level interface to Java modeles with debug information.


%package jinterface-native
Summary: Erlang's level interface to Java - modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Requires: %name-jinterface = %EVR

%description jinterface-native
Erlang's level interface to Java modules with native CPU code.
%endif


%if_with otp_debug
%package otp-debug
Summary: Standard Erlang OTP modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-otp-modules-debug = %EVR
Provides: otp-debug = %EVR
Requires: %name-otp-common = %EVR
Requires: %name-otp-bin = %EVR
Conflicts: %name-eunit-debug = 2.0

%description otp-debug
Standard Erlang OTP modules with debug information.


%package megaco-debug
Summary: H.248 support for Erlang - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-megaco-modules-debug = %EVR
Requires: %name-megaco-drivers = %EVR

%description megaco-debug
Megaco (aka H.248) is a signalling protocol used in VoIP networks.
This package contains modules for Erlang Megaco with debug information.


%package odbc-debug
Summary: ODBC support for Erlang - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-odbc-modules-debug = %EVR
Requires: %name-odbc-server = %EVR

%description odbc-debug
ODBC support for Erlang programming language.
This package contains modules for odbc with debug information.


%package visual-debug
Summary: Standart visual applications for Erlang - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-visual-modules-debug = %EVR
Requires: %name-otp-debug = %EVR
Requires: %name-visual-common = %EVR

%description visual-debug
Standard visual applications for Erlang programming language.
This package contains modules for visual applications with debug
information.


%package common_test-debug
Summary: A portable framework for automatic testing Erlang applications - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-common_test-modules-debug = %EVR
Requires: %name-common_test-common = %EVR

%description common_test-debug
A portable framework for automatic testing Erlang applications.
This package contains modules for common_test with debug information.
%endif


%if_with otp_native
%package otp-native
Summary: Standard Erlang OTP modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Provides: %name-otp-modules-native = %EVR
Provides: otp-native = %EVR
Requires: %name-otp-common = %EVR
Requires: %name-otp-bin = %EVR

%description otp-native
Standard Erlang OTP modules with native CPU code.


%package megaco-native
Summary: H.248 support for Erlang - modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Provides: %name-megaco-modules-native = %EVR
Requires: %name-megaco-drivers = %EVR

%description megaco-native
Megaco (aka H.248) is a signalling protocol used in VoIP networks.
This package contains modules for Erlang Megaco with native CPU code.


%package odbc-native
Summary: ODBC support for Erlang - modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Provides: %name-odbc-modules-native = %EVR
Requires: %name-odbc-server = %EVR

%description odbc-native
ODBC support for Erlang programming language.
This package contains modules for odbc with native CPU code.


%package visual-native
Summary: Standart visual applications for Erlang - modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Provides: %name-visual-modules-native = %EVR
Requires: %name-otp-native = %EVR
Requires: %name-visual-common = %EVR

%description visual-native
Standard visual applications for Erlang programming language.
This package contains modules for visual applications with native
CPU code.


%package common_test-native
Summary: A portable framework for automatic testing Erlang applications - modules with native CPU code
Group: Development/Erlang
BuildArch: noarch
Provides: %name-common_test-modules-native = %EVR
Requires: %name-common_test-common = %EVR

%description common_test-native
A portable framework for automatic testing Erlang applications.
This package contains modules for common_test with native CPU code.
%endif


%if_enabled docs
%package man
Summary: Man pages for Erlang/OTP
Group: Development/Documentation
BuildArch: noarch
AutoReq: no
AutoProv: no

%description man
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package contains man pages for Erlang.


%package doc
Summary: Documentation for Erlang/OTP.
License: EPL
Group: Development/Documentation
BuildArch: noarch
Requires: %name-doc-html = %EVR
Requires: %name-doc-pdf = %EVR
Requires: %name-doc-chunks = %EVR
AutoReq: no

%description doc
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This is Erlang/OTP documentation virtual package.


%package doc-html
Summary: Documentation for Erlang/OTP in HTML format
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-manual < R11B.4-alt0.1
Requires: %name-visual-common = %EVR
Requires: %name-doc-pdf = %EVR
Provides: %name-manual = %EVR
AutoReq: no
AutoProv: no

%description doc-html
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package contains documentation for Erlang/OTP in HTML format.


%package doc-pdf
Summary: Documentation for Erlang/OTP in PDF format
Group: Development/Documentation
BuildArch: noarch
Requires:  %name-visual-common = %EVR
Requires:  %name-common_test = %EVR
Requires:  %name-devel = %EVR
Requires:  %name-megaco = %EVR
Requires:  %name-odbc = %EVR
%if_with java
Requires:  %name-jinterface = %EVR
%endif
AutoReq: no
AutoProv: no

%description doc-pdf
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package contains documentation for Erlang/OTP in PDF format.


%package doc-chunks
Summary: Documentation for Erlang/OTP in chunk format
Group: Development/Documentation
BuildArch: noarch
Requires:  %name-visual-common = %EVR
Requires:  %name-common_test = %EVR
Requires:  %name-devel = %EVR
Requires:  %name-megaco = %EVR
Requires:  %name-odbc = %EVR
%if_with java
Requires:  %name-jinterface = %EVR
%endif
AutoReq: no
AutoProv: no

%description doc-chunks
Erlang is a programming language developed at Ericsson Computer Science
Laboratory. Erlang provides many features which are more commonly
associated with an operating system: concurrent processes, scheduling,
memory management, distribution, networking, etc.
This package contains documentation for Erlang/OTP in chunk format.
%endif


%prep
%setup -n otp_src_OTP-%version

#sed -i 's,armv7hl,armh,' erts/aclocal.m4

%ifarch %e2k
# beam/erl_bif_lists.c:779: non-void subtract_continue() w/o return
sed -i '/-Werror=return-type/d' erts/configure.in
# lcc: error: unrecognized command line option "-MG"
sed -i 's/MG_FLAG=-MG/MG_FLAG=/' erts/emulator/Makefile.in
# slow feature for LCC
%add_optflags -DNO_JUMP_TABLE
%endif

%build
%{?_with_java:%{?java_options:export _JAVA_OPTIONS="%java_options"}}
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

#24.1.2: Failed to create scheduler thread, error = 11
# each Erlang process can use ncpu*3+1 threads
# if you get this error, you need to increase the limit returned by "ulimit -u"
# which is 512 in the default ALT Linux configuration
export NPROCS=16

%configure \
	--libdir=%_libexecdir \
	%{subst_with ssl} \
	%{subst_with termcap} \
	%{subst_with gmp} \
	%{subst_with_to java javac} \
	%{subst_enable threads} \
	%{subst_enable sctp} \
	%{subst_enable kernel_poll kernel-poll} \
	%{subst_enable_to lock_checking lock-checking} \
	%{subst_enable_to lock_counting lock-counting} \
	%{subst_enable_to megaco_flex_scanner_lineno megaco-flex-scanner-lineno} \
%if_with java
	\
%else
	--without-jinterface \
%endif
	--enable-systemd \
	--enable-dynamic-ssl-lib \
	--with-ssl-rpath=no \
	--enable-shared-zlib

export ERL_LIBS=%buildroot%_otplibdir

%make_build

%if_enabled docs
%{?fop_options:export FOP_OPTS="%fop_options"}
export PATH="$PWD/bin:$PATH"
%make_build docs
%endif

%install
%{?_with_java:%{?java_options:export _JAVA_OPTIONS="%java_options"}}

%make_install DESTDIR=%buildroot install

%if_enabled docs
export ERL_LIBS=%buildroot%_otplibdir

%make_install PATH="$PWD/bin:$PATH" DESTDIR=%buildroot install-docs

install -d -m 0755 %buildroot{%_man1dir,%_man3dir,%_man4dir,%_man6dir,%_man7dir,%_docdir/%name-%version/{pdf,html/lib}}
xz -9f %buildroot%_erlmandir/man?/*
mv %buildroot%_otpdir/{COPYRIGHT,PR.template,README.md} %buildroot%_docdir/%name-%version

ln -sf %buildroot{%_otpdir/{doc,erts-*/doc,lib/*/doc}/pdf/*.pdf,%_docdir/%name-%version/pdf/}
ln -sf %buildroot%_erldocdir/* %buildroot%_docdir/%name-%version/html/
ln -sf %buildroot%_otpdir/erts-*/doc/html %buildroot%_docdir/%name-%version/html/erts

for d in %buildroot%_otplibdir/*; do
	install -d -m 0755 %buildroot%_docdir/%name-%version/html/lib/$(basename $d)/doc
	ln -sf $d/doc/html %buildroot%_docdir/%name-%version/html/lib/$(basename $d)/doc/html
	ln -sf $d/doc/pdf %buildroot%_docdir/%name-%version/html/lib/$(basename $d)/doc/pdf
done

ln -sf %buildroot%_docdir/%name-%version/html/lib  %buildroot%_docdir/%name-%version/lib
ln -sf %buildroot%_erldocdir/  %buildroot%_docdir/%name-%version/doc

for m in %buildroot%_erlmandir/man3/*; do
	ln -sf $m %buildroot%_man3dir/$(basename $m .xz)erl.xz
done
for n in 1 4 6 7; do
	ln -sf %buildroot{%_erlmandir/man$n/*,%_mandir/man$n/}
done

%define _compress_method xz
%endif #docs

install -d -m 0755 %buildroot{%_otpdir/usr/include,%_includedir}
ln -sf %buildroot%_otpdir/{erts-*/include/*.h,usr/include/}
ln -sf %buildroot%_otpdir/{lib/erl_interface-*/include/*.h,usr/include}
ln -sf %buildroot{%_otpdir/usr/include,%_includedir/%name}

#Save %%_otplibdir/*/*.hrl to %%_otplibdir/*/include and remove sources
for l in $(ls -d %buildroot%_otplibdir/* | grep -v '^%buildroot%_otplibdir/erl_interface-.*'); do
    if [ -d $l/src ]; then
	H=$(find $l/src -type f -name '*.hrl' | grep -v '.*_internal\.hrl$') ||:
	if [ -n "$H" ]; then
	    [ -d $l/include ] || install -d -m 0755 $l/include
	    for f in $H; do
		I=$(echo $l/include/$(basename $f))
		if [ ! -f "$I" ]; then
		    mv $f $l/include/
		    ln -sf $I $f
		fi
	    done
	    find $l/src/* -not -type l -not -type d -delete
	else
	    rm -rf $l/src
	fi
    fi
done
rm -f %buildroot%_otplibdir/erl_interface-*/src/{INSTALL,Makefile*,*.mk,*/*.c}
rm -rf %buildroot%_otpdir/{lib/*/{{c,java}_src,*.mk,priv/obj},erts-*/src}
rm -f %buildroot%_otplibdir/*/*/*.{asn1,erl}
rm -f %buildroot%_otplibdir/*/priv/bin/*.bat
rm -f %buildroot%_otplibdir/*/priv/*.in
rm -f %buildroot%_otplibdir/*/info
rm -f %buildroot%_otpdir/erts-*/info
find %buildroot -type f -name '*.src' -delete
find %buildroot -empty -delete


install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 AUTHORS LICENSE.txt README.md %buildroot%_docdir/%name-%version/

install -d -m 0755 %buildroot%_otpdir/usr/make
install -m 0644 make/*.mk %buildroot%_otpdir/usr/make/
install -m 0755 make/{make_emakefile,save_args} %buildroot%_otpdir/usr/make/
for f in make/*/*.mk; do
	install -D -m 0644 $f %buildroot%_otpdir/usr/$f
	ln -s ${f#make/} %buildroot%_otpdir/usr/make/$(basename $f)
done

rm -rf %buildroot%_otpdir/{Install,misc,usr/lib}

#subst 's|%buildroot||' %buildroot%_otpdir/{{,erts-*/}bin/{erl,start},releases/RELEASES}

sed 's|^[ \t]*ROOTDIR=|&%buildroot|' %buildroot%_otpdir/bin/erl > erl.buildroot
chmod 755 erl.buildroot

%define __erlang %_builddir/%buildsubdir/erl.buildroot
%define __erlc env ERLC_EMULATOR=%__erlang %buildroot%_otpdir/bin/erlc

install -d -m 0755 %buildroot%_bindir

install_ebin()
{
    local d f
    f=$1
    shift
    for d in %buildroot%_otplibdir/*/ebin; do
		install -d -m 0755 $d.$f
		done
    cat > %buildroot%_otpdir/bin/erl.$f <<__EOF__
#!/bin/sh
exec %_otpdir/bin/erl -pa \$(ls -d %_otplibdir/*/ebin.$f) \$@
__EOF__
    chmod 755 %buildroot%_otpdir/bin/erl.$f
    ln -sf %buildroot{%_otpdir/bin,%_bindir}/erl.$f
}

%{?_with_otp_debug:install_ebin debug -A -r CInf -c}

%{?_with_otp_native:install_ebin native -s -c}

for f in ct_run dialyzer erl erlc escript run_erl start to_erl typer; do
    ln -sf %buildroot%_otpdir{/erts-*,}/bin/$f
    ln -sf %buildroot{%_otpdir/bin,%_bindir}/$f
done

symlinks -scdr %buildroot

%{?_enable_strip_beam:%__erlang -noshell -run beam_lib strip_release %buildroot%_otpdir -run erlang halt}

%add_findreq_skiplist %_otplibdir/megaco-*/examples/meas/*.sh.skel
%add_findreq_skiplist %_otplibdir/*/contribs/ebin/* %_otplibdir/*/examples/ebin/* %_otplibdir/*/examples/*/ebin/*

# systemd-related stuff
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/epmd.service
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/epmd.socket
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/epmd@.service
install -D -p -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/epmd@.socket

%check
export TARGET="$(make -sk target_configured 2>/dev/null | grep -v make)"
export ERL_TOP="$(pwd)"
export PATH="$ERL_TOP/bin:$PATH"
ERL_TOP=${ERL_TOP} make TARGET=${TARGET} release_tests

cat >> release/tests/emulator_test/emulator.spec <<-EOF
{skip_cases,"../emulator_test",time_SUITE,
    [univ_to_local,local_to_univ],"Depends on CET timezone"}.
EOF
sed -i '/disksup_SUITE/d' release/tests/os_mon_test/os_mon_smoke.spec

pushd release/tests/test_server

# Workarount to use correct target triplet in ts:install
sed -i 's/-pc-linux-/-alt-linux-/g' config.guess

$ERL_TOP/bin/erl -noshell -s ts install -s ts smoke_test batch -s init stop
#$ERL_TOP/bin/erl -noshell -s ts install -s ts run emulator batch -s init stop

if grep -q '=failed *[1-9]' ct_run.test_server@*/*/run.*/suite.log; then
    echo "One or more tests failed."
fi

rm -rf ct_run.test_server@*

popd

%pre
getent group epmd >/dev/null || groupadd -r epmd
getent passwd epmd >/dev/null || \
useradd -r -g epmd -d /tmp -s /sbin/nologin \
-c "Erlang Port Mapper Daemon" epmd 2>/dev/null || :


%files
%_bindir/*
%exclude %_bindir/ct_run
%dir %_otpdir
%dir %_otpdir/bin
%dir %_otplibdir
%_otpdir/bin/*
%_otpdir/releases
%dir %_otplibdir/erts-*
%dir %_otpdir/erts-*
%_otpdir/erts-*/bin
%_unitdir/*

%dir %_docdir/%name-%version
%_docdir/%name-%version/AUTHORS
%_docdir/%name-%version/LICENSE.txt
%_docdir/%name-%version/README.md
%if_enabled docs
%_docdir/%name-%version/COPYRIGHT
%_docdir/%name-%version/PR.template
%dir %_erldocdir
%endif

%exclude %_otpdir/bin/typer*
%exclude %_bindir/typer*
%exclude %_otpdir/erts-*/bin/typer
%exclude %_otpdir/bin/ct_run
%exclude %_otpdir/erts-*/bin/ct_run

%if_with otp_debug
%exclude %_otpdir/bin/*.debug
%exclude %_bindir/*.debug
%endif

%if_with otp_native
%exclude %_otpdir/bin/*.native
%exclude %_bindir/*.native
%endif


%files devel
%_otpdir/erts-*/lib
%_otpdir/erts-*/include
%_otpdir/usr
%dir %_otplibdir/erl_interface-*
%_otplibdir/erl_interface-*/bin
%_otplibdir/erl_interface-*/include
%_otplibdir/erl_interface-*/lib
%_otplibdir/erl_interface-*/src
%_includedir/%name


%files otp-bin
%_otplibdir/asn1-*/priv
%_otplibdir/crypto-*/priv
%_otplibdir/diameter-*/bin
%_otplibdir/os_mon-*/priv/bin
%_otplibdir/runtime_tools-*/priv
%_otplibdir/edoc-*/bin


%files emacs
%_otplibdir/tools-*/emacs


%files otp-common
%dir %_otplibdir/asn1-*
%dir %_otplibdir/compiler-*
%dir %_otplibdir/crypto-*
%dir %_otplibdir/diameter-*
%dir %_otplibdir/dialyzer-*
%dir %_otplibdir/edoc-*
%dir %_otplibdir/eldap-*
%_otplibdir/edoc-*/priv
%dir %_otplibdir/erl_docgen-*
%_otplibdir/erl_docgen-*/priv
%dir %_otplibdir/eunit-*
%dir %_otplibdir/inets-*

%_otplibdir/inets-*/priv
%dir %_otplibdir/kernel-*
%dir %_otplibdir/mnesia-*
%dir %_otplibdir/os_mon-*
%dir %_otplibdir/os_mon-*/priv
%dir %_otplibdir/observer-*
%dir %_otplibdir/observer-*/ebin
%dir %_otplibdir/parsetools-*
%dir %_otplibdir/public_key-*
%dir %_otplibdir/runtime_tools-*
%dir %_otplibdir/sasl-*
%dir %_otplibdir/snmp-*
%_otplibdir/snmp-*/bin
%_otplibdir/snmp-*/mibs
%_otplibdir/snmp-*/priv
%dir %_otplibdir/ssh-*
%dir %_otplibdir/ssl-*
%dir %_otplibdir/stdlib-*
%dir %_otplibdir/syntax_tools-*
%dir %_otplibdir/tools-*
%_otplibdir/tools-*/priv
%dir %_otplibdir/xmerl-*
%dir %_otplibdir/erl_interface-*
%dir %_otplibdir/ftp-*
%dir %_otplibdir/tftp-*


%files otp-devel
%_otplibdir/asn1-*/include
%_otplibdir/asn1-*/src
%_otplibdir/compiler-*/include
%_otplibdir/compiler-*/src
%_otplibdir/diameter-*/include
%_otplibdir/diameter-*/src
%_otplibdir/edoc-*/include
%_otplibdir/edoc-*/src
%_otplibdir/eldap-*/include
%_otplibdir/eunit-*/include
%_otplibdir/inets-*/include
%_otplibdir/tftp-*/include
%_otplibdir/tftp-*/src
%_otplibdir/kernel-*/include
%_otplibdir/kernel-*/src
%_otplibdir/mnesia-*/include
%_otplibdir/mnesia-*/src
%_otplibdir/os_mon-*/include
%_otplibdir/os_mon-*/src
%_otplibdir/parsetools-*/include
%_otplibdir/public_key-*/asn1
%_otplibdir/public_key-*/include
%_otplibdir/public_key-*/src
%_otplibdir/runtime_tools-*/include
%_otplibdir/sasl-*/include
%_otplibdir/sasl-*/src
%_otplibdir/snmp-*/include
%_otplibdir/snmp-*/src
%_otplibdir/ssh-*/include
%_otplibdir/ssh-*/src
%_otplibdir/ssl-*/include
%_otplibdir/ssl-*/src
%_otplibdir/stdlib-*/include
%_otplibdir/stdlib-*/src
%_otplibdir/syntax_tools-*/include
%_otplibdir/tools-*/include
%_otplibdir/tools-*/src
%_otplibdir/xmerl-*/include
%_otplibdir/xmerl-*/src


%files otp
%_otplibdir/asn1-*/ebin
%_otplibdir/compiler-*/ebin
%_otplibdir/crypto-*/ebin
%_otplibdir/diameter-*/ebin
%_otplibdir/edoc-*/ebin
%_otplibdir/erl_docgen-*/ebin
%_otplibdir/erts-*/ebin
%_otplibdir/eunit-*/ebin
%_otplibdir/eldap-*/ebin
%_otplibdir/inets-*/ebin
%_otplibdir/tftp-*/ebin
%_otplibdir/ftp-*/ebin
%_otplibdir/kernel-*/ebin
%_otplibdir/mnesia-*/ebin
%_otplibdir/observer-*/ebin/ttb.*
%_otplibdir/os_mon-*/ebin
%_otplibdir/parsetools-*/ebin
%_otplibdir/public_key-*/ebin
%_otplibdir/runtime_tools-*/ebin
%_otplibdir/sasl-*/ebin
%_otplibdir/snmp-*/ebin
%_otplibdir/ssh-*/ebin
%_otplibdir/ssl-*/ebin
%_otplibdir/stdlib-*/ebin
%_otplibdir/syntax_tools-*/ebin
%_otplibdir/tools-*/ebin
%_otplibdir/xmerl-*/ebin
%_otplibdir/erl_interface-*/ebin


%files megaco-drivers
%_otplibdir/megaco-*/priv


%files megaco-devel
%_otplibdir/megaco-*/include
%_otplibdir/megaco-*/src


%files megaco
%dir %_otplibdir/megaco-*
%_otplibdir/megaco-*/ebin


%files visual-common
%_otpdir/erts-*/bin/typer
%_otpdir/bin/typer*
%_bindir/typer*
%dir %_otplibdir/debugger-*
%_otplibdir/debugger-*/priv
%dir %_otplibdir/et-*
%dir %_otplibdir/observer-*
%_otplibdir/observer-*/priv
%dir %_otplibdir/reltool-*
%dir %_otplibdir/wx-*
%ifnarch %e2k
# error: File not found by glob: /usr/src/tmp/erlang-buildroot/usr/lib/erlang/lib/wx-*/priv
%_otplibdir/wx-*/priv
%endif

%files visual-devel
%_otplibdir/debugger-*/src
%_otplibdir/debugger-*/include
%_otplibdir/dialyzer-*/include
%_otplibdir/dialyzer-*/src
%_otplibdir/et-*/include
%_otplibdir/observer-*/include
%_otplibdir/observer-*/src
%_otplibdir/reltool-*/src
%_otplibdir/reltool-*/include
%_otplibdir/wx-*/include
%_otplibdir/wx-*/src


%files visual
%_otplibdir/debugger-*/ebin
%_otplibdir/dialyzer-*/ebin
%_otplibdir/et-*/ebin
%_otplibdir/observer-*/ebin
%exclude %_otplibdir/observer-*/ebin/ttb.*
%_otplibdir/reltool-*/ebin
%_otplibdir/wx-*/ebin


%files odbc-server
%_otplibdir/odbc-*/priv


%files odbc-devel
%_otplibdir/odbc-*/include


%files odbc
%dir %_otplibdir/odbc-*
%_otplibdir/odbc-*/ebin


%files common_test-common
%dir %_otplibdir/common_test-*
%_otplibdir/common_test-*/priv


%files common_test-devel
%_otplibdir/common_test-*/include
%_otplibdir/common_test-*/src


%files common_test-bin
%_otpdir/erts-*/bin/ct_run
%_otpdir/bin/ct_run
%_bindir/ct_run

%files common_test
%_otplibdir/common_test-*/ebin


%files examples
%_otplibdir/*/examples


%files otp-full


%files full


%if_with otp_debug
%files otp-debug
%_otplibdir/*/ebin.debug
%exclude %_otplibdir/megaco-*
%exclude %_otplibdir/common_test-*
%exclude %_otplibdir/debugger-*
%exclude %_otplibdir/et-*
%exclude %_otplibdir/observer-*
%exclude %_otplibdir/odbc-*
%exclude %_otplibdir/reltool-*
%exclude %_otplibdir/wx-*
%exclude %_otplibdir/jinterface-*
%_otpdir/bin/*.debug
%dir %_otplibdir/observer-*/ebin.debug
%_bindir/*.debug


%files megaco-debug
%_otplibdir/megaco-*/ebin.debug


%files visual-debug
%_otplibdir/debugger-*/ebin.debug
%_otplibdir/et-*/ebin.debug
%_otplibdir/observer-*/ebin.debug
%_otplibdir/reltool-*/ebin.debug
%_otplibdir/wx-*/ebin.debug

%files odbc-debug
%_otplibdir/odbc-*/ebin.debug


%files common_test-debug
%_otplibdir/common_test-*/ebin.debug
%endif

%if_with otp_native
%files otp-native
%_otplibdir/*/ebin.native
%exclude %_otplibdir/megaco-*
%exclude %_otplibdir/common_test-*
%exclude %_otplibdir/debugger-*
%exclude %_otplibdir/et-*
%exclude %_otplibdir/observer-*
%exclude %_otplibdir/reltool-*
%exclude %_otplibdir/wx-*
%exclude %_otplibdir/odbc-*
%exclude %_otplibdir/jinterface-*
%_otpdir/bin/*.native
%dir %_otplibdir/observer-*/ebin.native
%_bindir/*.native


%files megaco-native
%_otplibdir/megaco-*/ebin.native


%files visual-native
%_otplibdir/debugger-*/ebin.native
%_otplibdir/et-*/ebin.native
%_otplibdir/observer-*/ebin.native
%_otplibdir/reltool-*/ebin.native
%_otplibdir/wx-*/ebin.native


%files odbc-native
%_otplibdir/odbc-*/ebin.native


%files common_test-native
%_otplibdir/common_test-*/ebin.native
%endif

%if_with java
%files jinterface
%dir %_otplibdir/jinterface-*
%_otplibdir/jinterface-*/ebin
%_otplibdir/jinterface-*/priv

%files jinterface-native
%_otplibdir/jinterface-*/ebin.native

%files jinterface-debug
%_otplibdir/jinterface-*/ebin.debug
%endif


%if_enabled docs
%files doc

%files man
%dir %_erldir
%_erlmandir
%_man1dir/*
%_man3dir/*
%_man4dir/*
%_man6dir/*
%_man7dir/*

%files doc-pdf
%_otpdir/doc/pdf
%dir %_otpdir/erts-*/doc
%_otpdir/erts-*/doc/pdf
%_docdir/%name-%version/pdf
%dir %_otplibdir/*/doc
%_otplibdir/*/doc/pdf


%files doc-html
%_otpdir/doc/*
%exclude %_otpdir/doc/pdf
%_otpdir/erts-*/doc/html
%_otplibdir/*/doc/html
%_docdir/%name-%version/lib
%_docdir/%name-%version/doc
%_docdir/%name-%version/html

%files doc-chunks
%_otplibdir/*/doc/chunks

%endif


%changelog
* Mon Mar 20 2023 Egor Ignatov <egori@altlinux.org> 1:25.3-alt1
- new version 25.3

* Thu Dec 15 2022 Egor Ignatov <egori@altlinux.org> 1:25.2-alt1
- new version 25.2

* Fri Oct 28 2022 Egor Ignatov <egori@altlinux.org> 1:25.1.2-alt1
- new version 25.1.2

* Sun Oct 23 2022 Egor Ignatov <egori@altlinux.org> 1:25.1.1-alt1
- new version 25.1.1

* Wed Mar 30 2022 Egor Ignatov <egori@altlinux.org> 1:24.3.3-alt1
- new version 24.3.3

* Mon Mar 21 2022 Egor Ignatov <egori@altlinux.org> 1:24.3.2-alt1
- new version 24.3.2

* Sat Nov 20 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:24.1.3-alt2
- E2K: removed unsupported -MG option
- E2K: disabled use of Labels as Values
- commented on the issue with pthread_create fail

* Wed Oct 27 2021 Egor Ignatov <egori@altlinux.org> 1:24.1.3-alt1
- new version 24.1.3

* Wed Oct 27 2021 Egor Ignatov <egori@altlinux.org> 1:24.1.2-alt2
- enable tests
- fix man symlinks

* Thu Oct 07 2021 Egor Ignatov <egori@altlinux.org> 1:24.1.2-alt1
- new version 24.1.2

* Wed Apr 14 2021 Grigory Ustinov <grenka@altlinux.org> 1:21.3.6-alt4
- Fixed FTBFS with -fcommon.

* Wed Jun 24 2020 Michael Shigorin <mike@altlinux.org> 1:21.3.6-alt3
- E2K: ftbfs workaround
- fixed docs knob

* Mon Jun 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:21.3.6-alt2
- fixed packaging on so-called armh

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 1:21.3.6-alt1
- new version 21.3.6

* Fri Apr 12 2019 Alexey Shabalin <shaba@altlinux.org> 1:21.3.3-alt1
- new version

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 1:21.3.2-alt1
- new version

* Tue Feb 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:21.2.4-alt3
- Fixed build on other architectures without hipe support.

* Tue Feb 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1:21.2.4-alt2
- Use pre BuildRequires for macros
- Remove unnecessary BuildRequires

* Fri Jan 25 2019 Alexey Shabalin <shaba@altlinux.org> 1:21.2.4-alt1
- new version

* Thu Oct 11 2018 Denis Medvedev <nbr@altlinux.org> 1:21.0.9-alt1
- new version

* Sat Sep 22 2018 Anton Midyukov <antohami@altlinux.org> 1:20.1.3-alt4
- Rebuilt with libwxGTK3.0

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 1:20.1.3-alt3.1
- NMU: rebuild with new openssl.

* Mon Aug 13 2018 Denis Medvedev <nbr@altlinux.org>  1:20.1.3-alt4
- rebuilding with wxGTK rebuild task.

* Fri Jun 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:20.1.3-alt3
- Rebuilt with %%ubt macro support, disabled parallel docs build.

* Fri May 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:20.1.3-alt2
- fixed build on arm arches

* Thu Oct 26 2017 Denis Medvedev <nbr@altlinux.org> 1:20.1.3-alt1
- new version

* Wed Apr 05 2017 Denis Medvedev <nbr@altlinux.org> 1:19.0.7-alt2
- recompilation with updated rpm-build-erlang

* Tue Sep 20 2016 Denis Medvedev <nbr@altlinux.org> 1:19.0.7-alt1
- new version

* Thu Apr 07 2016 Denis Medvedev <nbr@altlinux.org> 1:18.3-alt2
- With wxGTK3.1

* Mon Apr 04 2016 Denis Medvedev <nbr@altlinux.org> 1:18.3-alt1
- New version OTP-18.3

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> R15B.2-alt3.1
- Rebuilt with wxGTK 2.8.12

* Tue Oct 23 2012 Pavel Shilovsky <piastry@altlinux.org> R15B.2-alt2
* Tue Apr 23 2013 Dmitry V. Levin <ldv@altlinux.org> R15B.2-alt3
- Disabled pdf_opt because ghostscript no longer provides pdfopt.

* Tue Oct 23 2012 Pavel Shilovsky <piastry@altlinux.org> R15B.2-alt2
- Not include deleted win32reg into stdlib

* Sun Sep 30 2012 Sergey Shilov <hsv@altlinux.org> R15B.2-alt1
- R15B01 upstream release

* Mon Aug 06 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt7
- fix ( thanks for the patch led@ )  strip of chunk Attr (ALT #27603)

* Fri Apr 13 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt6
- revert upstream source to OTP_R15B01 tag (ALT #27216).

* Sat Apr 07 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt5
- fix erlang-doc-pdf post-install unowned files.

* Wed Apr 04 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt4
- R15B01 upstream release
- remove hipe_crash_with_on_load patch

* Mon Feb 20 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt3
- fix repocop warnings
- fix build with %def_disable docs
- remove support to build with icc

* Sat Feb 18 2012 Sergey Shilov <hsv@altlinux.org> R15B.1-alt2
- fix extra reqs during update (ALT #26845)
- add alt-arm patch (thanks Sergey Bolshakov)

* Sat Dec 24 2011 Sergey Shilov <hsv@altlinux.org> R15B.1-alt1
- R15B-1
  + Line number and filename information are now included in exception backtraces.
    This information will be pretty-printed in the shell and used in crash reports etc.
  + The driver interface has been changed to enable 64-bit aware drivers.
  + CommonTest hooks are now in a final supported version.
  + There is a new GUI tool in the observer application which integrates
    pman, etop, appmon and tv into one tool.
    The tool does also contain functions for activating tracing in an easy way.
  + The Erlang distribution can now be run over the new SSL implementation.
  You can find the README file for the release at
  http://erlang.org/download/otp_src_R15B.readme

* Fri Oct 07 2011 Sergey Shilov <hsv@altlinux.org> R14B.4-alt1
- R14B-4
  You can find the README file for the release at
  http://www.erlang.org/download/otp_src_R14B04.readme

* Fri Sep 16 2011 Sergey Shilov <hsv@altlinux.org> R14B.3-alt3
- build without libperfctr.

* Tue Aug 02 2011 Sergey Shilov <hsv@altlinux.org> R14B.3-alt2
- fix Erlang VM ethreads pre-pentium4 compatibility.

* Thu Jul 28 2011 Sergey Shilov <hsv@altlinux.org> R14B.3-alt1
- R14B-3
  You can find the README file for the release at
  http://www.erlang.org/download/otp_src_R14B03.readme
- new spec based on Clustrx package ( many thanks to led@ )
- man pages and documentation build from upstream sources
- added:
  + R14B-3a-hipe_crash_with_on_load.patch
- cleaned up:
  + otp-R14B-2a-mnesiaex.patch
  + otp-R14B-2a-tuples.patch
  + otp-R14B-2a-opt.patch
- fixed
  + R14B-3a-beam_lib.patch


* Sun Mar 27 2011 Sergey Shilov <hsv@altlinux.org> R14B.2-alt2
- fix sisyphus_check: forbidden requires: xorg-devel
  check-deps ERROR: package dependencies violation
- move elisp files for erlang-mode under GNU Emacs to erlang-emacs package (close #24670).

* Wed Mar 16 2011 Sergey Shilov <hsv@altlinux.org> R14B.2-alt1
- R14B-2
  You can find the README file for the release at
  http://www.erlang.org/download/otp_src_R14B02.readme


* Sun Mar 13 2011 Sergey Shilov <hsv@altlinux.org> R14B.1-alt2
- fix packager (#25219);
- fix Repocops rpm-filesystem-conflict-symlink-file warning.

* Fri Jan 14 2011 Sergey Shilov <hsv@altlinux.org> R14B.1-alt1
- R14B.1-alt1

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> R12B.5-alt11.2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> R12B.5-alt11.2
- NMU.
- Build with new libffi.

* Fri Sep 04 2009 Dmitry V. Levin <ldv@altlinux.org> R12B.5-alt11.1
- NMU.
- Fixed buggy find(1) expression in %%install script.
- lib/erl_interface/src/prog/erl_start.c (get_addr): Fixed buffer overflow.

* Thu Apr 02 2009 Led <led@altlinux.ru> R12B.5-alt11
- ffi: added 'time_t' type

* Thu Feb 19 2009 Led <led@altlinux.ru> R12B.5-alt10
- fixed parallel build for any __nprocs
- removed unneeded Provides

* Thu Feb 19 2009 Led <led@altlinux.ru> R12B.5-alt9
- fixed parallel build for __nprocs >= 8
- fixed spec

* Mon Feb 16 2009 Led <led@altlinux.ru> R12B.5-alt8
- fix build ffi on big-endian arches (thanx sbolshakov@)

* Thu Feb 12 2009 Led <led@altlinux.ru> R12B.5-alt7
- extended beam_lib (stdlib)
- added getopt, beam_strip (stdlib)
- applied upstream's otp_src_R12B-5_OTP-7738.patch
- remade %%build
- strip modules
- compress modules with native code and with debug info

* Thu Jan 15 2009 Led <led@altlinux.ru> R12B.5-alt6
- cleaned up asm insertions
- renamed new BIFs and moved to separate module 'tuples': append/2,
  delete/2, delete/3, flatsize/1, flatten/1, insert/3, insert_elements/3
- added functions to module 'tuples': append_element/2, element/2,
  make/2, set_element/3, from_list/1, to_list/1, size/1

* Tue Jan 13 2009 Led <led@altlinux.ru> R12B.5-alt5
- added BIFs:
  + erlang:concat/2
  + erlang:delete_elements/3
  + erlang:flatten/1
  + erlang:insert_elements/3
  + erlang:tuple_flatsize/1

* Sat Jan 10 2009 Led <led@altlinux.ru> R12B.5-alt4
- optimized some BIFs for x86/x86_64

* Tue Dec 30 2008 Led <led@altlinux.ru> R12B.5-alt3
- fixed spec
- added BIFs erlang:delete_element/2, erlang:insert_element/3

* Fri Dec 26 2008 Led <led@altlinux.ru> R12B.5-alt2
- non-parallel build eunit
- cleaned up spec

* Sun Nov 16 2008 Led <led@altlinux.ru> R12B.5-alt1
- R12B-5

* Mon Oct 20 2008 Led <led@altlinux.ru> R12B.4-alt4
- configure.in: make dirs from mkdir.list

* Fri Oct 17 2008 Led <led@altlinux.ru> R12B.4-alt3
- updated ffi support

* Sun Sep 21 2008 Led <led@altlinux.ru> R12B.4-alt2
- rebuild with rpm-build-%name >= 0.6.2

* Fri Sep 05 2008 Led <led@altlinux.ru> R12B.4-alt1
- R12B-4
- updated:
  + otp_src_R12B-4-ffi.patch
  + otp_src_R12B-4-mnesiaex.patch

* Wed Sep 03 2008 Led <led@altlinux.ru> R12B.3-alt4
- added "BuildRequires: /proc" for native (HIPE'ed) modules

* Thu Aug 28 2008 Led <led@altlinux.ru> R12B.3-alt3
- with native (HIPE'ed) modules

* Tue Aug 19 2008 Led <led@altlinux.ru> R12B.3-alt2
- fixed BuildArch and unmets (#16741)

* Fri Aug 15 2008 Led <led@altlinux.ru> R12B.3-alt1
- added otp_src_R12B-3-alt-configure.patch
- fixed %name-otp-devel
- added otp_src_R12B-3-mnesiaex.patch

* Mon Jun 23 2008 Led <led@altlinux.ru> R12B.3-alt0.7
- fixed spec (%%files otp)

* Fri Jun 20 2008 Led <led@altlinux.ru> R12B.3-alt0.6
- moved common_test to separate packages %name-common_test*

* Thu Jun 19 2008 Led <led@altlinux.ru> R12B.3-alt0.5
- rebuild with rpm-build-%name-0.3.1

* Thu Jun 19 2008 Led <led@altlinux.ru> R12B.3-alt0.4
- rebuild with rpm-build-%name-0.3

* Thu Jun 19 2008 Led <led@altlinux.ru> R12B.3-alt0.3
- moved to *-visual* packages:
  + dialyzer
  + typer
  + observer/etop*
  + observer/ttb_et*
  + hipe/hipe_tool*
  + common_test
- moved jinterface to separate package

* Wed Jun 18 2008 Led <led@altlinux.ru> R12B.3-alt0.2
- moved observer to *-visual* packages

* Wed Jun 18 2008 Led <led@altlinux.ru> R12B.3-alt0.1
- R12B-3

* Sun Feb 24 2008 Led <led@altlinux.ru> R12B.1-alt0.4
- build with rpm-build-%name

* Sat Feb 16 2008 Led <led@altlinux.ru> R12B.1-alt0.3
- reverted system headers (links) to %_libexecdir/%name%_includedir

* Fri Feb 15 2008 Led <led@altlinux.ru> R12B.1-alt0.2
- link system header to %_includedir/%name

* Mon Feb 11 2008 Led <led@altlinux.ru> R12B.1-alt0.1
- R12B-1
- removed otp_src_R12B-0-osp1.patch (fixed in upstream)
- updated:
  + otp_src_R12B-1-alt-arch.patch
  + otp_src_R12B-1-ffi.patch

* Mon Jan 28 2008 Led <led@altlinux.ru> R12B.0-alt0.6
- updated spec for build with opt_otp only on i586/x86_64/arm
- fixed post-scripts

* Thu Jan 24 2008 Led <led@altlinux.ru> R12B.0-alt0.5
- fixed spec
- added:
  + otp_src_R12B-0-alt-arch.patch
  + otp_src_R12B-0-ffi.patch
- cleaned up:
  + otp-R12B-0-alt-include.patch
  + otp-R12B-0-configure.patch
  + otp_src_R12B-0-osp1.patch

* Sun Dec 23 2007 Led <led@altlinux.ru> R12B.0-alt0.4
- cleaned up spec
- added subpackages

* Sun Dec 23 2007 Led <led@altlinux.ru> R12B.0-alt0.3
- fixed upgrading packages

* Sat Dec 22 2007 Led <led@altlinux.ru> R12B.0-alt0.2
- moved optimized modules to %_libexecdir/%name/lib/*/ebin.opt/

* Fri Dec 21 2007 Led <led@altlinux.ru> R12B.0-alt0.1
- R12B-0
- add support to build with icc
- removed:
  + otp-R11B-5-odbcserver.patch (fixed in upstream)
- added:
  + otp-R12B-0-configure.patch
  + otp-R12B-0-link.patch
  + otp_src_R11B-5-libadd.patch
  + otp_src_R12B-0-osp1.patch
- added subpackages %name-examples, %name-otp-opt

* Sun Nov 11 2007 Mikhail Yakshin <greycat@altlinux.org> R11B.5-alt1
- tested with ejabberd and built for Sisyphus

* Tue Oct 09 2007 Led <led@altlinux.ru> R11B.5-alt0.9
- cleaned up and fixed spec
- fixed BuildRequires

* Mon Sep 10 2007 Led <led@altlinux.ru> R11B.5-alt0.8
- added new rpm macros

* Fri Sep 07 2007 Led <led@altlinux.ru> R11B.5-alt0.7
- reverted non-internal headers to %_libexecdir/%name/lib/*/ as symlinks

* Thu Sep 06 2007 Led <led@altlinux.ru> R11B.5-alt0.6
- added additional *.hrl files

* Wed Sep 05 2007 Led <led@altlinux.ru> R11B.5-alt0.5
- cleaned up sources in packages

* Tue Aug 28 2007 Led <led@altlinux.ru> R11B.5-alt0.4
- added rpm macros

* Mon Aug 27 2007 Led <led@altlinux.ru> R11B.5-alt0.3
- moved libs from %%_libdir to %%_libexecdir

* Fri Aug 17 2007 Led <led@altlinux.ru> R11B.5-alt0.2
- added otp-R11B-5-odbcserver.patch (fixed #12576)

* Tue Jun 26 2007 Led <led@altlinux.ru> R11B.5-alt0.1
- R11B-5
- added %name-docbuilder subpackage

* Tue Jun 05 2007 Led <led@altlinux.ru> R11B.4-alt0.1
- R11B-4
- cleaned up spec
- removed docs
- removed emacs-mode-%name
- added patches from FC7
- used gcj

* Tue Feb 20 2007 Mikhail Yakshin <greycat@altlinux.ru> R11B-alt2
- Fixed x86_64 build

* Sat Feb 10 2007 Mikhail Yakshin <greycat@altlinux.org> R11B-alt1
- R11B-3

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> R10B.10-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Oct 12 2006 Alex V. Myltsev <avm@altlinux.ru> R10B.10-alt2
- Merged with alb's version from backports.
- Applied the 'new glibc' patch.
- Moved zlib.3.gz to erl_zlib.3.gz.
- Moved Megaco to a separate package..

* Thu Sep 07 2006 Alexey Borovskoy <alb@altlinux.ru> R11B.1-alt0.M24.1
- New release (R11B-1).

* Wed Mar 22 2006 Alexey Borovskoy <alb@altlinux.ru> R10B.10-alt0.M24.1
- New release (R10B-10).

* Mon Dec 19 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.9-alt0.M24.1
- New release (R10B-9).

* Sun Oct 30 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.8-alt0.M24.2
- Add ODBC support.

* Fri Oct 28 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.8-alt0.M24.1
- New release (R10B-8).
- Add patch for disable static linking with zlib. Does not work and disabled.
- Add zlib-devel buildtime dependency. But dymamic linking with zlib not
  supported in erts/emulator/dirvers/common/gzio.c due using private zutil.h.
- Remove --enable-threads due erl segfault.

* Thu Sep 08 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.7-alt0.M24.1
- New release (R10B-7)

* Wed Aug 10 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.6-alt0.M24.1
- New release (R10B-6)

* Wed May 11 2005 Alexey Borovskoy <alb@altlinux.ru> R10B.4-alt0.M24.1
- New release (R10B-4)
- Split to subpackages:
  + manual
    For manual in HTML
  + manpages
    For manpages
  + visual
    For visual apps that requires tk/tcl
  + emacs-mode-erlang
    For Emacs mode

* Tue Nov 02 2004 Plugnikov A. Mike <amike@altlinux.ru> R10B.0-alt1
- New version (R10B)
- Merged upstream patches:
  patch-lib_stdlib_src_dets__v9
  erlang_ssl_broker
- Fix spec

* Sat May 15 2004 Ott Alex <ott@altlinux.ru> R9C.0-alt3
- Fix build process

* Sun Feb 22 2004 Ott Alex <ott@altlinux.ru> R9C.0-alt2
- Added some fixes from freebsd ports (thanks to Ermine!)
- Build without tcl/tk & java

* Wed Dec 10 2003 Ott Alex <ott@altlinux.ru> R9C.0-alt1
- Initial build for ALTLinux
