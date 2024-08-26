# we are shipping the full contents of src in the data subpackage, which
# contains binary-like things (ELF data for tests, etc)
%global _unpackaged_files_terminate_build 1

%global go_arches %ix86 x86_64 aarch64 %arm mipsel ppc64le riscv64 loongarch64
%global go_root %_prefix/lib/golang
%global golibdir %_libdir/golang

%ifarch x86_64
%global go_hostarch  amd64
%endif
%ifarch %ix86
%global go_hostarch  386
%endif
%ifarch %arm
%global go_hostarch  arm
%endif
%ifarch aarch64
%global go_hostarch  arm64
%endif
%ifarch mipsel
%global go_hostarch  mipsle
%endif
%ifarch ppc64le
%global go_hostarch  ppc64le
%endif
%ifarch riscv64
%global go_hostarch  riscv64
%endif
%ifarch loongarch64
%global go_hostarch loong64
%endif

# Build golang shared objects for stdlib
%ifarch %ix86 x86_64 ppc64le %arm aarch64
%def_enable shared
%else
%def_disable shared
%endif

%ifarch %ix86 x86_64 ppc64le %arm aarch64 riscv64 loongarch64
%def_enable external_linker
%def_enable cgo
%else
%def_disable external_linker
%def_disable cgo
%endif

%def_enable check
%def_enable fail_on_tests

Name:    golang
Version: 1.23.0
Release: alt1
Summary: The Go Programming Language
Group:   Development/Other
License: BSD
URL:     http://golang.org/

Source0: golang-%version.tar
Source1: golang-gdbinit
Patch2:  golang-alt-certs-path.patch
Patch3:  go-never-download-newer-toolchains.patch
Patch101: 0001-avoid-requires-libselinux-utils.patch

ExclusiveArch: %go_arches

%set_verify_elf_method skip
%add_debuginfo_skiplist %go_root
%brp_strip_none %go_root/bin/*
%brp_strip_none %go_root/pkg/*

AutoReq: nocpp

Requires: %name-src = %version-%release
Requires: /proc

BuildRequires(pre): rpm-build-golang rpm-build-python3
BuildRequires: golang
BuildRequires: libselinux-utils
BuildRequires: libpcre2-devel
BuildRequires: glibc-devel-static
BuildRequires: /proc
# for tests
BuildRequires: /dev/pts

Provides: go = %version-%release

Provides:  golang-godoc = %version-%release
Obsoletes: golang-godoc < %version-%release

# Due to vet, cover utilities.
Conflicts: golang-tools <= 0-alt1.git7e09e072
# /usr/bin/cover
Conflicts: perl-Devel-Cover

%description
Go is expressive, concise, clean, and efficient. Its concurrency mechanisms
make it easy to write programs that get the most out of multicore and
networked machines, while its novel type system enables flexible and
modular program construction.


%package gdb
Summary:   The Go Runtime support for GDB
Group:     Development/Other
BuildArch: noarch
Requires:  %name = %version-%release
Requires:  gdb
AutoReq: nopython
%add_python3_path %go_root/src/runtime
%add_python3_compile_exclude %go_root/src/runtime
%add_python3_req_skip gdb

%description gdb
The Go Runtime support for GDB.


%package shared
Summary: Golang shared object libraries
Group:   Development/Other

%description shared
%summary.


%package docs
Summary:   Go sources and documentation
Group:     Documentation
BuildArch: noarch
Requires:  %name = %version-%release

%description docs
Go sources and documentation.

%package misc
Summary:   Golang compiler miscellaneous sources
Group:     Development/Other
BuildArch: noarch
Requires:  %name = %version-%release
AutoReqProv: no

%description misc
%summary.

%package tests
Summary:   Golang compiler tests for stdlib
Group:     Development/Other
BuildArch: noarch
Requires:  %name = %version-%release
AutoReqProv: no

%description tests
%summary.

%package src
Summary:   Golang compiler source tree
Group:     Development/Other
BuildArch: noarch
AutoReq: noshell, noshebang

%description src
%summary.

%prep
%setup -q

%patch2 -p1
%patch3 -p1
%patch101 -p1

%build
# go1.5 bootstrapping. The compiler is written in golang.
export GOROOT_BOOTSTRAP=%go_root

# set up final install location
export GOROOT_FINAL=%go_root

export GOHOSTOS=linux
export GOHOSTARCH=%go_hostarch

export GOOS=linux
export GOARCH=%go_hostarch

# use our gcc options for this build, but store gcc as default for compiler
export CC="gcc"
export CC_FOR_TARGET="gcc"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
%if_disabled external_linker
export GO_LDFLAGS="-linkmode internal"
%endif
%if_disabled cgo
export CGO_ENABLED=0
%endif

# build
cd src
./make.bash --no-clean -v
cd ..

%if_enabled shared
GOROOT=$PWD PATH="$GOROOT/bin:$PATH" go install -v -buildmode=shared -v -x std
%endif

%check
export GOROOT=$PWD
export PATH="$GOROOT/bin:$PATH"
export CC="gcc"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

%if_disabled external_linker
export GO_LDFLAGS="-linkmode internal"
%endif
%if_disabled cgo
export CGO_ENABLED=0
%endif
export GO_TEST_TIMEOUT_SCALE=2

cd src
%if_enabled fail_on_tests
./run.bash --no-rebuild -v -v -v -k
%else
./run.bash --no-rebuild -v -v -v -k ||:
%endif
cd ..

%install
# remove GC build cache
rm -rf pkg/obj/go-build/*

# create the top level directories
mkdir -p -- \
	%buildroot%_bindir \
	%buildroot%go_root \
	%buildroot%_datadir/%name

cp -apfv api bin doc lib pkg src misc test go.env VERSION \
	%buildroot%go_root/

find %buildroot%go_root -exec touch -r $PWD/VERSION "{}" \;


# remove bootstrap files
rm -rfv -- %buildroot%go_root/pkg/bootstrap

# remove the doc Makefile
rm -rfv -- %buildroot%go_root/doc/Makefile

# remove the unnecessary zoneinfo file (Go will always use the system one first)
rm -rfv -- \
	%buildroot%go_root/lib/time

%if_enabled shared
mkdir -p %buildroot%golibdir
for file in $(find %buildroot%go_root/pkg/linux_%{go_hostarch}_dynlink  -iname "*.so" ); do
	mv  $file %buildroot%golibdir
	pushd $(dirname $file)
	ln -fs %golibdir/$(basename $file) $(basename $file)
	popd
done
%endif

# add symlinks for binaries.
for z in %buildroot%go_root/bin/*; do
	[ -x "$z" ] || continue

	n="${z##*/}"
	path="$(relative "$z" "%buildroot%_bindir/$n")"

	ln -sv -- "$path" %buildroot%_bindir/$n
done

# https://golang.org/doc/go1.5#moving
# Because the go/types package has now moved into the main repository (see below),
# the vet and cover tools have also been moved. They are no longer maintained in
# the external golang.org/x/tools repository, although (deprecated) source still
# resides there for compatibility with old releases.
for z in cover vet; do
	z="%buildroot%go_root/pkg/tool/linux_%{go_hostarch}/$z"
	[ -x "$z" ] || continue

	n="${z##*/}"
	path="$(relative "$z" "%buildroot%_bindir/$n")"

	ln -sv -- "$path" %buildroot%_bindir/$n
done

# restore the gdb debugging script, needed at runtime by gdb
mkdir -p -- %buildroot%_datadir/%name/gdb
sed \
	-e 's,@GOROOT@,%go_root,g' \
	%SOURCE1 > %buildroot%_datadir/%name/gdb/golang-gdbinit

mkdir -p -- %buildroot%_datadir/%name/src
for n in syscall regexp; do
	mkdir -- %buildroot%_datadir/%name/src/$n

	find %buildroot%go_root/src/$n \
		\( \
			\( -type f -name '*.sh' \) -o \
			\( -type f -name '*.pl' \)    \
		\) \
			-print0 |
		xargs -0 mv -fvt %buildroot%_datadir/%name/src/$n --
done

# ensure these exist and are owned
mkdir -p -- \
	%buildroot%go_path/src/github.com \
	%buildroot%go_path/src/bitbucket.org \
	%buildroot%go_path/src/code.google.com/p \
	%buildroot%go_path/src/golang.org/x \
#

# cleanup
find \
	%buildroot%go_root/src \
	\( \
		\( -type f -name '.gitignore' \) -o \
		\( -type f -name '*.orig'     \) \
	\) \
		-print0 |
	xargs -0 rm -rfv --


# find test files
cwd=$(pwd)
src_list=$cwd/go-src.list
tests_list=$cwd/go-tests.list
rm -f $src_list $tests_list
touch $src_list $tests_list
pushd %buildroot%go_root
find src/ -type d -a \( ! -name testdata -a ! -ipath '*/testdata/*' \) -printf '%%%%dir %go_root/%%p\n' >> $src_list
find src/ ! -type d -a \( ! -ipath '*/testdata/*' -a ! -name '*_test.go' \) -printf '%go_root/%%p\n' >> $src_list
find src/ -type d -a \( -name testdata -o -ipath '*/testdata/*' \) -printf '%%%%dir %go_root/%%p\n' >> $tests_list
find src/ ! -type d -a \( -ipath '*/testdata/*' -o -name '*_test.go' \) -printf '%go_root/%%p\n' >> $tests_list
popd

%files
%_bindir/*
%go_root
%go_path
%exclude %go_root/doc
%exclude %go_root/misc
%exclude %go_root/src
%exclude %go_root/test

%if_enabled shared
%exclude %go_root/pkg/linux_%{go_hostarch}_dynlink
%exclude %golibdir/*.so

%files shared
%go_root/pkg/linux_%{go_hostarch}_dynlink
%golibdir/*.so
%endif

%files gdb
%_datadir/%name/gdb
%go_root/src/runtime/runtime-gdb.py

%files docs
%doc LICENSE PATENTS VERSION
%dir %_datadir/%name
%_datadir/%name/src
%go_root/doc

%files misc
%go_root/misc

%files tests -f go-tests.list
%go_root/test

%files src -f go-src.list
%exclude %go_root/src/runtime/runtime-gdb.py

%changelog
* Mon Aug 26 2024 Alexey Shabalin <shaba@altlinux.org> 1.23.0-alt1
- New version (1.23.0).

* Wed Aug 07 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.6-alt1
- New version (1.22.6).

* Wed Jul 03 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.5-alt1
- New version (1.22.5) (Fixes: CVE-2024-24791).

* Fri Jun 07 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.4-alt1
- New version (1.22.4) (Fixes: CVE-2024-24789, CVE-2024-24790).

* Tue May 07 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.3-alt1
- New version (1.22.3) (Fixes: CVE-2024-24787, CVE-2024-24788).

* Wed Apr 03 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.2-alt1
- New version (1.22.2) (Fixes: CVE-2023-45288).

* Tue Mar 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.1-alt1
- New version (1.22.1) (Fixes: CVE-2024-24783, CVE-2023-45289, CVE-2023-45290).

* Fri Feb 16 2024 Alexey Shabalin <shaba@altlinux.org> 1.22.0-alt1
- New version (1.22.0).

* Thu Feb 08 2024 Alexey Shabalin <shaba@altlinux.org> 1.21.7-alt2
- Update files in tests package (ALT#48016).

* Wed Feb 07 2024 Alexey Shabalin <shaba@altlinux.org> 1.21.7-alt1
- New version (1.21.7).

* Tue Jan 09 2024 Alexey Shabalin <shaba@altlinux.org> 1.21.6-alt1
- New version (1.21.6).

* Tue Dec 05 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.5-alt1
- New version (1.21.5) (Fixes: CVE-2023-39326, CVE-2023-45285, CVE-2023-45283).

* Wed Nov 08 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.4-alt1
- New version (1.21.4) (Fixes: CVE-2023-45283, CVE-2023-45284).

* Wed Oct 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.3-alt1
- New version (1.21.3) (Fixes: CVE-2023-39325).

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.2-alt1
- New version (1.21.2) (Fixes: CVE-2023-39323).

* Fri Sep 15 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt2
- Don't use -buildmode=shared on loongarch64 and riscv64 (thx to iv@) (ALT#47559).

* Wed Sep 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt1
- New version (1.21.1) (Fixes: CVE-2023-39318, CVE-2023-39319, CVE-2023-39320, CVE-2023-39321, CVE-2023-39322).

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.0-alt3
- Add go.env to package.
- Disable download toolchains in go.env.

* Thu Aug 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.0-alt2
- Add loongarch64 to %%go_arches.
- Enable external_linker and cgo for riscv64 and loongarch64.
- Add Requires: /proc.
- Enable %%check.

* Wed Aug 09 2023 Alexey Shabalin <shaba@altlinux.org> 1.21.0-alt1
- New version (1.21.0).

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.7-alt1
- New version (1.20.7) (Fixes: CVE-2023-29409).

* Wed Jul 12 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.6-alt1
- New version (1.20.6) (Fixes: CVE-2023-29406).

* Tue Jun 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.5-alt1
- New version (1.20.5) (Fixes: CVE-2023-29402, CVE-2023-29403, CVE-2023-29404, CVE-2023-29405).

* Tue May 02 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.4-alt1
- New version (1.20.4) (Fixes: CVE-2023-24539, CVE-2023-24540, CVE-2023-29400)

* Tue Apr 04 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.3-alt1
- New version (1.20.3) (Fixes: CVE-2023-24534, CVE-2023-24536, CVE-2023-24537, CVE-2023-24538).

* Thu Mar 16 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.2-alt2
- Disable shell autoreq for golang-src (ALT#45547).

* Thu Mar 09 2023 Alexey Shabalin <shaba@altlinux.org> 1.20.2-alt1
- New version (1.20.2).

* Tue Mar 07 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.7-alt1
- New version (1.19.7) (Fixes: CVE-2023-24532).

* Thu Feb 16 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.6-alt1
- New version (1.19.6) (Fixes: CVE-2022-41725, CVE-2022-41724, CVE-2022-41723, CVE-2022-41722).

* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.5-alt1
- New version (1.19.5).

* Wed Dec 07 2022 Alexey Shabalin <shaba@altlinux.org> 1.19.4-alt1
- New version (1.19.4) (Fixes: CVE-2022-41717, CVE-2022-41720).

* Thu Nov 03 2022 Alexey Shabalin <shaba@altlinux.org> 1.19.3-alt1
- New version (1.19.3) (Fixes: CVE-2022-41716).

* Sat Oct 08 2022 Alexey Shabalin <shaba@altlinux.org> 1.19.2-alt1
- New version (1.19.2).
- Remove tzdata patch.

* Thu Oct 06 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.7-alt1
- New version (1.18.7) (Fixes: CVE-2022-2879, CVE-2022-2880, CVE-2022-41715).

* Wed Sep 14 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.6-alt1
- New version (1.18.6) (Fixes: CVE-2022-27664).

* Tue Aug 02 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.5-alt1
- New version (1.18.5) (Fixes: CVE-2022-32189).

* Thu Jul 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.4-alt1
- New version (1.18.4).
- Fixes:
  + CVE-2022-1705
  + CVE-2022-32148
  + CVE-2022-30631
  + CVE-2022-30633
  + CVE-2022-28131
  + CVE-2022-30635
  + CVE-2022-30632
  + CVE-2022-30630
  + CVE-2022-1962

* Sun Jun 12 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.3-alt1
- New version (1.18.3) (Fixes: CVE-2022-30580, CVE-2022-30634, CVE-2022-30629, CVE-2022-29804).

* Fri May 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.2-alt1
- New version (1.18.2).

* Fri Apr 15 2022 Alexey Shabalin <shaba@altlinux.org> 1.18.1-alt1
- New version (1.18.1).

* Wed Apr 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.9-alt1
- New version (1.17.9) (Fixes: CVE-2022-24675, CVE-2022-28327, CVE-2022-27536).

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.8-alt1
- New version (1.17.8) (Fixes: CVE-2022-24921).

* Fri Feb 11 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.7-alt1
- New version (1.17.7) (Fixes: CVE-2022-23806, CVE-2022-23772, CVE-2022-23773).

* Fri Jan 07 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.6-alt1
- New version (1.17.6).

* Thu Dec 09 2021 Alexey Shabalin <shaba@altlinux.org> 1.17.5-alt1
- New version (1.17.5) (Fixes: CVE-2021-44716, CVE-2021-44717).

* Thu Nov 04 2021 Alexey Shabalin <shaba@altlinux.org> 1.17.3-alt1
- New version (1.17.3) (Fixes: CVE-2021-41771, CVE-2021-41772).

* Mon Oct 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.17.2-alt1
- New version (1.17.2).
- Fixes:
  + CVE-2021-38297

* Thu Sep 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.17.1-alt3
- Remove workaround patch for building golang itself

* Wed Sep 22 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.17.1-alt2
- Fix golang build

* Mon Sep 13 2021 Alexey Shabalin <shaba@altlinux.org> 1.17.1-alt1
- New version (1.17.1).
- Fixes:
  + CVE-2021-39293

* Mon Aug 09 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.7-alt1
- New version (1.16.7).
- Fixes:
  + CVE-2021-36221

* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.6-alt1
- New version (1.16.6).
- Fixes:
  + CVE-2021-34558

* Sat Jun 05 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.5-alt1
- New version (1.16.5).
- Fixes:
  + CVE-2021-33195
  + CVE-2021-33196
  + CVE-2021-33197
  + CVE-2021-33198

* Thu May 06 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.4-alt1
- New version (1.16.4).
- Fixes:
  + CVE-2021-31525

* Tue Apr 20 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.3-alt1
- New version (1.16.3).

* Fri Mar 12 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.2-alt1
- New version (1.16.2).

* Thu Mar 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- New version (1.16.1).
- Fixes:
  + CVE-2021-27918
  + CVE-2021-27919
- Remove test for other platform scripts.

* Fri Feb 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.16-alt1
- New version (1.16).
- Build shared package for x86, x86_64, ppc64le, arm, aarch64.
- find debuginfo files for shared for shared libs.

* Fri Feb 05 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.8-alt1
- New version (1.15.8).

* Wed Jan 20 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.7-alt1
- New version (1.15.7).
- Fixes:
  + CVE-2021-3114
  + CVE-2021-3115

* Tue Dec 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.6-alt2
- Disable AutoReqProv for misc package

* Fri Dec 04 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.6-alt1
- New version (1.15.6).

* Sat Nov 14 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.5-alt1
- New version (1.15.5).
- Fixes:
  + CVE-2020-28362
  + CVE-2020-28366
  + CVE-2020-28367

* Tue Oct 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.3-alt1
- New version (1.15.3).

* Fri Sep 11 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.2-alt1
- New version (1.15.2). (Fixes: CVE-2020-24553)

* Tue Aug 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.15-alt1
- New version (1.15).
- Set a standard go_root as /usr/lib/golang, regardless of arch
- Add misc, tests, src packages

* Mon Aug 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.7-alt1
- New version (1.14.7). (Fixes: CVE-2020-16845)

* Thu Jul 23 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.6-alt1
- New version (1.14.6). (Fixes: CVE-2020-15586, CVE-2020-14039)

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.4-alt1
- New version (1.14.4).

* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt2
- merge chanlog with p9

* Sat May 16 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- New version (1.14.3).

* Sat May 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.2-alt2
- avoid requires libselinux-utils.

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.2-alt1
- 1.14.2

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Feb 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.14-alt1
- 1.14
- Build on riscv64

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.8-alt1
- 1.13.8

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.17-alt1
- 1.12.17

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.6-alt1
- 1.13.6

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.15-alt1
- 1.12.15

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.5-alt1
- 1.13.5

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.4-alt1
- 1.13.4 (Fixes: CVE-2019-17596)

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.13-alt1
- New version (1.12.13).

* Wed Nov 06 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.11-alt1
- New version (1.12.11). (Fixes: CVE-2019-17596)

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.1-alt1
- 1.13.1

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.10-alt1
- New version (1.12.10). (Fixes: CVE-2019-16276)

* Thu Sep 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.13-alt1
- 1.13

* Mon Aug 19 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.9-alt1
- 1.12.9 (Fixes: CVE-2019-14809, CVE-2019-9512, CVE-2019-9514)

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.7-alt1
- New version (1.12.7).

* Tue Jun 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.6-alt1
- New version (1.12.6).

* Fri Apr 12 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed Mar 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- New version (1.12.1).
- Apply timezone patch, avoid using bundled data

* Thu Jan 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.5-alt1
- 1.11.5
- fixed CPU DoS vulnerability affecting P-521 and P-384 (Fixes: CVE-2019-6486)
- add ppc64le to go_arches

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.4-alt1
- New version (1.11.4).

* Thu Jan 17 2019 Ivan A. Melnikov <iv@altlinux.org> 1.11.2-alt1.0.mips1
- Build on mipsel.

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- New version (1.11.2).

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- New version (1.11.1).

* Fri Sep 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.11-alt1
- New version (1.11).

* Fri Jun 22 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.3-alt1
- New version (1.10.3).
- backport patches from upstream for aarch64

* Thu May 03 2018 Alexey Gladkov <legion@altlinux.ru> 1.10.2-alt1
- New version (1.10.2).

* Wed Jan 10 2018 Alexey Gladkov <legion@altlinux.ru> 1.9.2-alt1
- New version (1.9.2).

* Tue Aug 29 2017 Alexey Gladkov <legion@altlinux.ru> 1.9-alt2
- Enable build for aarch64.

* Mon Aug 28 2017 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1
- New version (1.9).

* Fri Apr 07 2017 Alexey Gladkov <legion@altlinux.ru> 1.8.1-alt1
- New version (1.8.1).

* Tue Aug 16 2016 Alexey Gladkov <legion@altlinux.ru> 1.7-alt1
- New version (1.7).

* Mon Feb 29 2016 Alexey Gladkov <legion@altlinux.ru> 1.6-alt1
- New version (1.6).

* Fri Jan 22 2016 Alexey Gladkov <legion@altlinux.ru> 1.5.3-alt1
- New version (1.5.3).

* Tue Sep 22 2015 Alexey Gladkov <legion@altlinux.ru> 1.5.1-alt1
- New version (1.5.1).
- The vet and cover tools have been moved to this package.

* Sun May 03 2015 Alexey Gladkov <legion@altlinux.ru> 1.4.2-alt1
- New version (1.4.2).
- Disable tests.

* Fri Dec 12 2014 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4).
- Drop vim subpackage.

* Mon Jun 23 2014 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- New version (1.3).

* Tue Dec 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.2-alt1
- New version (1.2).

* Mon Oct 28 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt2
- Add gdb and vim plugins.
- Fix rebuild command (ALT#29508).

* Thu Oct 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt1
- New version (1.1.2).
- Fix ssl certs search path (ALT#29449).

* Fri Jun 14 2013 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1
- First build for ALTLinux.

* Sat May 25 2013 Dan Horák <dan[at]danny.cz> - 1.1-3
- set ExclusiveArch

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-2
- Fix noarch package discrepancies

* Fri May 24 2013 Adam Goode <adam@spicenitz.org> - 1.1-1
- Initial Fedora release.
- Update to 1.1

* Thu May  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.3.rc3
- Update to rc3

* Thu Apr 11 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.2.beta2
- Update to beta2

* Tue Apr  9 2013 Adam Goode <adam@spicenitz.org> - 1.1-0.1.beta1
- Initial packaging.
