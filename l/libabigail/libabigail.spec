%define soversion 7

Name: libabigail
Version: 2.8
Release: alt1
Summary: ABI Generic Analysis and Instrumentation Library and tools
Group: Development/Other

License: Apache-2.0 WITH LLVM-exception
Url: https://sourceware.org/libabigail/
Source0: %name-%version.tar

# Automatically added by buildreq on Wed Oct 22 2025 (-bi)
# optimized out: bashrc cpio debugedit elfutils glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libctf-nobfd0 libelf-devel libgpg-error libstdc++-devel openssl-config perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent perl-unicore pkg-config python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-charset-normalizer python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-requests python3-module-roman_numerals python3-module-six python3-module-snowballstemmer python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml python3-module-urllib3 rpm-build-file sh5 termutils xz zlib-devel
BuildRequires: binutils-devel doxygen gcc-c++ libbpf-devel libdw-devel liblzma-devel libxml2-devel libxxhash-devel makeinfo python3-module-sphinx

%description
This package contains %summary.

%package -n libabigail%soversion
Summary: ABI Generic Analysis and Instrumentation Library runtime
Group: System/Libraries
Conflicts: libabigail < %version

%description -n libabigail%soversion
This package contains %summary.

%package devel
Summary: ABI Generic Analysis and Instrumentation Library development files
Group: Development/C
Requires: libabigail%soversion = %EVR

%description devel
This package contains %summary.

%package -n abigail-tools
Summary: ABI Generic Analysis and Instrumentation Library tools
Group: Development/Other
Requires: libabigail%soversion = %EVR
Provides: libabigail = %version
Obsoletes: libabigail < %version, libabigail-doc < %version

%description -n abigail-tools
This package contains %summary:
abidiff, kmidiff, abipkgdiff, abicompat, abidw, and abilint.

The abidiff command line tool compares the ABI of two ELF shared
libraries and emits meaningful textual reports about changes impacting
exported functions, variables and their types.  Simarly, the kmidiff
compares the kernel module interface of two Linux kernels, abipkgdiff
compares the ABIs of ELF binaries contained in two packages, abicompat
checks if a subsequent version of a shared library is still compatible
with an application that is linked against it, abidw emits an XML
representation of the ABI of a given ELF shared library, abilint
checks that a given XML representation of the ABI of a shared library
is correct.

%prep
%setup

%build
%autoreconf
# Workaround autoconf bug that breaks AC_SYS_LARGEFILE for C++ projects.
%if 0%{?_is_ilp32}
export ac_cv_sys_largefile_opts='-D_FILE_OFFSET_BITS=64'
%endif
%configure \
	--disable-silent-rules \
	--disable-static \
	#
%make_build
%make_build -C doc/manuals man info

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

# Install man and texinfo files as they are not installed by the
# default 'install' target of the makefile.
make -C doc/manuals install-man-and-info-doc DESTDIR=%buildroot

%check
%make_build -k check check-self-compare

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files -n libabigail%soversion
%_libdir/libabigail/
%_libdir/libabigail.so.%{soversion}*

%files devel
%_includedir/*
%_libdir/libabigail.so
%_pkgconfigdir/libabigail.pc
%_aclocaldir/abigail.m4

%files -n abigail-tools
%_bindir/*
%_mandir/man?/*
%_infodir/abigail.info*

%changelog
* Wed Oct 22 2025 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.8-alt1
- 1.8.2 -> 2.8.
- Updated package license: LGPLv3+ -> Apache-2.0 WITH LLVM-exception.

* Thu Feb 25 2021 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt1
- 1.8 -> 1.8.2.

* Mon Nov 30 2020 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt1
- 1.7 -> 1.8.

* Wed Feb 26 2020 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt1
- 1.6 -> 1.7.

* Wed Mar 27 2019 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt1
- 1.2 -> 1.6.

* Wed Mar 28 2018 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- 1.0.rc2 -> 1.2.
- Renamed libabigail to abigail-tools, dropped doc subpackage.

* Fri Feb 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.2.rc2
- Updated to 1.0.rc2.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2.rc0.1
- NMU: added BR: texinfo

* Thu Nov 19 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.2.rc0
- Updated to 1.0.rc0.

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.1.git088f077
- Initial build.
