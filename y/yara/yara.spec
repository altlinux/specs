# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: yara
Version: 4.1.1
Release: alt2
License: BSD-3-Clause and Apache-2.0
Group: Development/Tools
Summary: The pattern matching swiss knife for malware researchers (and everyone else)
Url: http://virustotal.github.io/yara/
Vcs: https://github.com/virustotal/yara
# Docs: https://yara.readthedocs.io/

Source: %name-%version.tar
BuildRequires: flex
BuildRequires: libssl-devel
BuildRequires: libjansson-devel
BuildRequires: libmagic-devel
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-c-devel

%description
YARA is a tool aimed at (but not limited to) helping malware researchers to
identify and classify malware samples. With YARA you can create descriptions of
malware families (or whatever you want to describe) based on textual or binary
patterns. Each description, a.k.a rule, consists of a set of strings and a
boolean expression which determine its logic.

%package -n libyara4
Summary: YARA dynamic libraries (pattern matcher)
Group: System/Libraries

%description -n libyara4
Dynamic library for YARA.

%package -n libyara-devel
Summary: YARA development files (pattern matcher)
Group: Development/C
Requires: libyara4 = %EVR
AutoReqProv: nocpp

%description -n libyara-devel
Development files for YARA.

%prep
%setup

%build
%autoreconf
#	--disable-static
# make[2]: *** No rule to make target 'libyara/.libs/libyara.a', needed by 'test-arena'.  Stop.
%configure \
	--with-crypto	\
	--enable-cuckoo	\
	--enable-magic	\
	--enable-dotnet	\
	--enable-macho	\
	--enable-dex	\
	--enable-pb-tests
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/libyara.a

%check
LD_LIBRARY_PATH=%buildroot%_libdir %buildroot%_bindir/yara --version
%make_build check

%files
%doc AUTHORS CONTRIBUTORS README.md COPYING
%_bindir/yara*
%_man1dir/yara*.1*

%files -n libyara4
%_libdir/libyara.so.*

%files -n libyara-devel
%_libdir/libyara.so
%_includedir/yara*
%_pkgconfigdir/yara.pc

%changelog
* Sun Aug 01 2021 Vitaly Chikunov <vt@altlinux.org> 4.1.1-alt2
- Build on all architectures.

* Mon Jun 14 2021 Vitaly Chikunov <vt@altlinux.org> 4.1.1-alt1
- Update to v4.1.1 (2021-05-24).

* Wed May 12 2021 Vitaly Chikunov <vt@altlinux.org> 4.1.0-alt1
- Update to v4.1.0 (2021-04-19).

* Sun Feb 07 2021 Vitaly Chikunov <vt@altlinux.org> 4.0.5-alt1
- Update to v4.0.5 (2021-02-05).

* Thu Jan 28 2021 Vitaly Chikunov <vt@altlinux.org> 4.0.4-alt1
- Update to v4.0.4 (2021-01-27), security fixes.

* Wed Dec 30 2020 Vitaly Chikunov <vt@altlinux.org> 4.0.2-alt1
- Import v4.0.2 (2020-06-26).
