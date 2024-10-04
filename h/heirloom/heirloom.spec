%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: heirloom
Version: 070715
Release: alt3
Summary: Collection of standard Unix utilities by Caldera
Group: Development/Other

License: LGPLv2

Url: https://sourceforge.net/projects/heirloom/
Source: %name-%version.tar
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: mk-configure >= 0.34.2-alt4
BuildRequires: rpm-macros-mk-configure

%description
The Heirloom Project provides traditional implementations
of standard Unix utilities. In many cases, they have been
derived from original Unix material released as Open Source by
Caldera and Sun.

%package -n libuxre
Summary: POSIX compatible regular expression library
Group: System/Libraries

%description -n libuxre
libuxre is a POSIX-compatible regexp engine
based on the code released as Open Source by Caldera.

%package -n libuxre-devel
Summary: Development files of libuxre
Group: Development/C
Requires: libuxre = %EVR

%description -n libuxre-devel
Development files of %name

%prep
%setup -Dn %name-%version/libuxre

%define _mkc_env \
	export MKSTATICLIB=no \
	%mkc_env

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%_mkc_env
%mkcmake_configure
%mkcmake_build

%install
%_mkc_env
%mkcmake_install

%files -n libuxre
%_libdir/*.so.*

%files -n libuxre-devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Oct 1 2024 Aleksey Cheusov <cheusov@altlinux.org> 070715-alt3
- Reworked from scratch
