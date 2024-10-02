%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libuxre
Version: 070715
Release: alt1

Summary: POSIX compatible regular expression library
License: LGPLv2
Group: System/Libraries

Url: https://sourceforge.net/projects/heirloom/
Source: heirloom-%version.tar
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: mk-configure >= 0.34.2-alt4
BuildRequires: rpm-macros-mk-configure

%description
libuxre is a POSIX-compatible regexp engine
based on the code released as Open Source by Caldera.

%package devel
Summary: Development files of libuxre
Group: Development/C
Requires: %name = %EVR

%description devel
Development files of %name

%prep
%setup -Dn heirloom-%version/%name

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

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Oct 1 2024 Aleksey Cheusov <cheusov@altlinux.org> 070715-alt1
- Initial version
