# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 10

Name: yara
Version: 4.3.0
Release: alt1
License: BSD-3-Clause and Apache-2.0
Group: Development/Tools
Summary: The pattern matching swiss knife for malware researchers (and everyone else)
Url: http://virustotal.github.io/yara/
Vcs: https://github.com/virustotal/yara
# Docs: https://yara.readthedocs.io/

Source: %name-%version.tar
BuildRequires: flex
BuildRequires: libjansson-devel
BuildRequires: libmagic-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: libssl-devel
BuildRequires: protobuf-compiler

%description
YARA is a tool aimed at (but not limited to) helping malware researchers to
identify and classify malware samples. With YARA you can create descriptions of
malware families (or whatever you want to describe) based on textual or binary
patterns. Each description, a.k.a rule, consists of a set of strings and a
boolean expression which determine its logic.

%package -n libyara%sover
Summary: YARA dynamic libraries (pattern matcher)
Group: System/Libraries

%description -n libyara%sover
Dynamic library for YARA.

%package -n libyara-devel
Summary: YARA development files (pattern matcher)
Group: Development/C
Requires: libyara%sover = %EVR
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
	--enable-macho	\
	--enable-dex	\
	--enable-pb-tests
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/libyara.a

%check
# Parallel make -j check does not work anymore:
# https://github.com/VirusTotal/yara/issues/1667
%make check VERBOSE=1
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
yara --version
cat > main.rule <<'EOF'
rule MAIN {
  strings:   $my = /Name:/
  condition: $my
}
EOF
yarac main.rule /tmp/a
yara main.rule -r . | grep MAIN.*yara.spec

%files
%doc AUTHORS CONTRIBUTORS README.md COPYING
%_bindir/yara*
%_man1dir/yara*.1*

%files -n libyara%sover
%_libdir/libyara.so.%sover
%_libdir/libyara.so.%sover.*

%files -n libyara-devel
%_libdir/libyara.so
%_includedir/yara*
%_pkgconfigdir/yara.pc

%changelog
* Sat Mar 25 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.0-alt1
- Update to v4.3.0 (2023-03-22).

* Sat Jan 28 2023 Vitaly Chikunov <vt@altlinux.org> 4.2.3-alt2
- Fix ALT beekeeper rebuild by updating test-magic for libmagic 5.44.

* Wed Aug 10 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.3-alt1
- Update to v4.2.3 (2022-08-08).

* Tue Jul 05 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.2-alt1
- Update to v4.2.2 (2022-06-30).

* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.1-alt1
- Update to v4.2.1 (2022-04-26).

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.0-alt1
- Update to v4.2.0 (2022-03-09). (Fixes: CVE-2021-45429).

* Tue Oct 26 2021 Vitaly Chikunov <vt@altlinux.org> 4.1.3-alt1
- Update to v4.1.3 (2021-10-21).

* Sun Aug 29 2021 Vitaly Chikunov <vt@altlinux.org> 4.1.2-alt1
- Update to v4.1.2 (2021-08-23).

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
