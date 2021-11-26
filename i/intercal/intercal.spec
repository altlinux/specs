Name: intercal
Version: 0.31
Release: alt2

Summary: A compiler for the INTERCAL language
License: GPL-2.0-or-later and GFDL-1.2-or-later
Group: Development/Other
Url: http://www.catb.org/~esr/intercal/

# https://gitlab.com/esr/intercal
# git://git.altlinux.org/gears/i/intercal.git
Source: %name-%version-%release.tar

BuildRequires: flex makeinfo

%description
INTERCAL is the original esoteric language, a farrago of features
that will test the mettle of any programmer and bend the minds of
most.  The INTERCAL suite includes not just a compiler and debugger
for the language but most of the code ever written for it as well.

%prep
%setup -n %name-%version-%release
cp -a pit examples
rm -r examples/{lib,Makefile}

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build -k fuzz

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files
%_bindir/*
%_libdir/*.a
%_includedir/*
%_datadir/ick*
%_infodir/*
%_mandir/man?/*
%doc BUGS NEWS README HISTORY examples/ etc/%name.el

%changelog
* Thu Aug 26 2021 Dmitry V. Levin <ldv@altlinux.org> 0.31-alt2
- Added -ffat-lto-objects to %%optflags_lto.

* Sun Dec 27 2020 Dmitry V. Levin <ldv@altlinux.org> 0.31-alt1
- 0.30 -> 0.31.
- Fixed build with gcc-10.
- Enabled LFS on 32-bit systems.

* Mon Mar 04 2019 Dmitry V. Levin <ldv@altlinux.org> 0.30-alt1
- Updated to 0.30.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1.git20140828.1
- NMU: added BR: texinfo

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20140828
- Version 0.29

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.24-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 26 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.24-alt1
- initial build
