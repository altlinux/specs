%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

# We need to save '.rackboot' section in these binaries to make them work.
%brp_strip_debug %_bindir/*
%brp_strip_debug %racket_libdir/*

# Disable static libs installation.
%def_disable libs

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
%add_optflags -ffat-lto-objects

%define zuo zuo -X /usr/share/zuo

Name: racket-core
Version: 8.8
Release: alt2

Summary: Racket, the programming language (base package)
License: Apache-2.0 or MIT
Group: Development/Scheme
Url: https://racket-lang.org/
Vcs: https://github.com/racket/racket

# racket: https://github.com/racket/racket/archive/refs/tags/v8.6.zip
# pb:     https://github.com/racket/pb/archive/refs/heads/v8.6.zip

Source0: %name-%version.tar
Source1: update-launchers.rkt
Source2: update-mans.rkt

BuildRequires(pre): rpm-macros-racket
BuildRequires: /proc
BuildRequires: zuo

BuildRequires: liblz4-devel
BuildRequires: zlib-devel
BuildRequires: libncurses-devel
BuildRequires: libffi-devel

# ATTENTION!
# Building on ppc64le takes a very long time (2-2.5 hours)!
# It is related to usage of portable bytecode.
ExclusiveArch: %racket_arches

%description
%summary.

This package contains minimal Racket which can install packages for itself.

%prep
%setup

sed -i 's|@RACKETLIBDIR@|%racket_libdir|' %SOURCE1
sed -i 's|@RACKETLIBDIR@|%racket_libdir|' %SOURCE2

%build
mkdir -p racket/src/build && cd racket/src/build

# We can't use %%configure macro because it uses ./configure, but
# we need ../configure.
export CFLAGS='%optflags'
../configure \
        --prefix=%prefix \
        --bindir=%_bindir \
        --sysconfdir=%_sysconfdir \
        --datarootdir=%_datadir \
        --datadir=%_datadir \
        --includedir=%_includedir \
        --libdir=%_libdir \
        --mandir=%_mandir \
        --enable-pthread \
	--enable-sharezo \
        --disable-strip \
        %{subst_enable libs} \
	--docdir=%racket_docdir \
	--collectsdir=%racket_collectsdir \
	--pkgsdir=%racket_pkgsdir \
	--enable-ffi \
%ifarch ppc64le
	--enable-pb --enable-mach=tpb64l \
%endif
        %nil

%zuo . cs JOBS=%__nprocs

%install
cd racket/src/build
%zuo . install-cs DESTDIR=%buildroot JOBS=%__nprocs

# Move Racket licenses files to our docs location.
# Also remove unused licenses (we build CS variant, so need MIT and Apache2.0
# only - others should be removed).
mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/racket/LICENSE* %buildroot%_datadir/doc/%name-%version
rm %buildroot%_datadir/doc/%name-%version/LICENSE-{GPL,LGPL,libscheme}.txt

mkdir -p %buildroot%racket_libdir/launchers.d
mkdir -p %buildroot%racket_libdir/mans.d

mv %buildroot%racket_libdir/launchers.{rktd,d/%name.rktd}
mv %buildroot%racket_libdir/mans.{rktd,d/%name.rktd}

mkdir -p %buildroot%racket_sharedir
install -pD -m0644 %SOURCE1 %buildroot%racket_sharedir/update-launchers.rkt
install -pD -m0644 %SOURCE2 %buildroot%racket_sharedir/update-mans.rkt

mkdir -p %buildroot%_rpmlibdir

cat << EOF >> %buildroot%_rpmlibdir/racket-update-launchers.filetrigger
#!/bin/sh -e
if grep -qs -E '%racket_libdir/launchers.d'; then
    %_bindir/racket -f %racket_sharedir/update-launchers.rkt ||:
fi
EOF
chmod 0755 %buildroot/%_rpmlibdir/racket-update-launchers.filetrigger

cat << EOF >> %buildroot%_rpmlibdir/racket-update-mans.filetrigger
#!/bin/sh -e
if grep -qs -E '%racket_libdir/mans.d'; then
    %_bindir/racket -f %racket_sharedir/update-mans.rkt ||:
fi
EOF
chmod 0755 %buildroot%_rpmlibdir/racket-update-mans.filetrigger

%files
%doc LICENSE*
%_man1dir/*
%_sysconfdir/*
%_bindir/*
%racket_collectsdir/*
%racket_libdir/*.rktd
%racket_libdir/*.d
%racket_libdir/gracket
%racket_libdir/starter*
%racket_sharedir/*.rkt
%_rpmlibdir/*.filetrigger

%if_disabled libs
# Do we really need C-headers without C-libraries? We don't, I think.
%exclude %_includedir/*
%endif

%changelog
* Sat Mar 25 2023 Anton Zhukharev <ancieg@altlinux.org> 8.8-alt2
- Fixed paths for filetriggers.

* Sun Mar 12 2023 Anton Zhukharev <ancieg@altlinux.org> 8.8-alt1
- 8.6 -> 8.8.

* Sun Jan 08 2023 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt4
- add launchers.d and mans.d and filetriggers for them

* Mon Oct 24 2022 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt3
- rename from racket-base to racket-core

* Tue Oct 18 2022 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt2
- clean up spec
- do not remove 'starter-sh' file
- save needed section in binaries
- update license
- ship only used licenses
- save .zo files in /usr/lib
- set strict elf verifying method

* Sun Oct 16 2022 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt1
- base Racket package
