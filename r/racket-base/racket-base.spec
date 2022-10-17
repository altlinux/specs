%define _unpackaged_files_terminate_build 1

# FIXME: this macro doesn't work, but we need .rackboot section
# to make Racket work
# %%global _find_debuginfo_opts --keep-section .rackboot
# Temporary solution: strip files during building process, because
# inner strip doesn't remove .rackboot section.
%def_enable strip

# Disable static libs installation.
%def_disable libs

%add_optflags -ffat-lto-objects

%define zuo zuo -X /usr/share/zuo

Name: racket-base
Version: 8.6
Release: alt1

Summary: Racket is a general-purpose programming language (base package)
License: GPL-3.0 or LGPL-3.0 or Apache-2.0 or MIT
Group: Development/Scheme
Url: https://racket-lang.org/
Vcs: https://github.com/racket/racket

# racket: https://github.com/racket/racket/archive/refs/tags/v8.6.zip
# pb:     https://github.com/racket/pb/archive/refs/heads/v8.6.zip

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-racket
BuildRequires: /proc
BuildRequires: zuo

BuildRequires: liblz4-devel
BuildRequires: zlib-devel
BuildRequires: libncurses-devel
BuildRequires: libffi-devel

# ATTENTION!
# Building on ppc64le takes a very long time!
ExclusiveArch: %racket_arches

%description
%summary.

This package contain base which can install packages.

%prep
%setup

%build
mkdir -p racket/src/build && cd racket/src/build

# We can't use %%configure macro due to it uses ./configure, but
# we need ../configure.
export CFLAGS='%optflags'
../configure \
        --prefix=%_prefix \
        --bindir=%_bindir \
        --sysconfdir=%_sysconfdir \
        --datarootdir=%_datadir \
        --datadir=%_datadir \
        --includedir=%_includedir \
        --libdir=%_libdir \
        --mandir=%_mandir \
        --enable-pthread \
        %{subst_enable strip} \
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
mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/racket/LICENSE* %buildroot%_datadir/doc/%name-%version

%files
%doc LICENSE*
%_man1dir/*
%_sysconfdir/*
%_bindir/*
%racket_collectsdir/*
%racket_libdir/*.rktd
%racket_libdir/gracket
%racket_libdir/starter
# Exclude empty 'starter-sh' file.
%exclude %racket_libdir/starter-sh
%racket_compiled%racket_collectsdir/*

%if_disabled libs
# Do we really need C-headers without C-libraries? We don't, I think.
%exclude %_includedir/*
%endif

%changelog
* Sun Oct 16 2022 Anton Zhukharev <ancieg@altlinux.org> 8.6-alt1
- base Racket package
