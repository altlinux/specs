# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: yara
Version: 4.0.2
Release: alt1
License: BSD-3-Clause and Apache-2.0
Group: Development/Tools
Summary: The pattern matching swiss knife for malware researchers (and everyone else)
Url: http://virustotal.github.io/yara/
Vcs: https://github.com/virustotal/yara
# Docs: https://yara.readthedocs.io/
Requires: libyara4 = %EVR
ExclusiveArch: %ix86 x86_64

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
%make_build check
%buildroot%_bindir/yara --version

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
* Wed Dec 30 2020 Vitaly Chikunov <vt@altlinux.org> 4.0.2-alt1
- Import v4.0.2 (2020-06-26).
