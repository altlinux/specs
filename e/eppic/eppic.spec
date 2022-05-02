# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    eppic
# git tag 4.0 c2a25643ea2d479a450fc54339adba57b54516b9
# git describe origin/master --tags
# 4.0-13-gdc60e00
Version: 4.0.0.13.gdc60e00
Release: alt3
Summary: Eppic is a C interpreter
Group:   Development/C
License: GPL-2.0-or-later
Url:     https://code.google.com/archive/p/eppic/
Vcs:     https://github.com/lucchouina/eppic.git
# Wiki:  https://code.google.com/archive/p/eppic/wikis/README.wiki

Source: %name-%version.tar

BuildRequires: flex
BuildRequires: ncurses-devel

%description
Eppic is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces.

%package -n libeppic-devel
Summary: Eppic (is a C interpreter) development libraries
Group:   Development/C

%description -n libeppic-devel
Eppic is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

%prep
%setup
# Fix for binutils 2.37 (remove previously unused modifier 'l')
sed -i '/\$(AR)/s/l//' libeppic/Makefile

%build
cd libeppic
%add_optflags %optflags_shared -ffat-lto-objects %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags"

%install
cd libeppic
mkdir -p %buildroot%_libdir %buildroot%_includedir
make ROOT=%buildroot LIBDIR=%_libdir install

%files -n libeppic-devel
%doc libeppic/README
%_includedir/eppic.h
%_includedir/eppic_api.h
%_libdir/libeppic.a

%changelog
* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 4.0.0.13.gdc60e00-alt3
- Fix multiple definitions of 'lastv'.
- Enabled LFS support.

* Wed Sep 22 2021 Vitaly Chikunov <vt@altlinux.org> 4.0.0.13.gdc60e00-alt2
- Fix build with binutils 2.37.

* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 4.0.0.13.gdc60e00-alt1
- First import of 4.0-13-gdc60e00 (2019-03-29).
