%define _unpackaged_files_terminate_build 1

%global llvm_version 15.0

Name: AFLplusplus
Version: 4.08c
Release: alt1

Summary: American Fuzzy Lop plus plus (AFL++)
License: Apache-2.0
Group: Development/Tools
VCS: https://github.com/AFLplusplus/AFLplusplus
Url: https://aflplus.plus

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Provides: afl++ = %EVR

Requires: clang%llvm_version lld%llvm_version

# Don't require afl-plot-ui to not depend on UI libs
%add_findreq_skiplist %_bindir/afl-plot

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++ gcc-plugin-devel
BuildRequires: llvm%llvm_version llvm%llvm_version-devel
BuildRequires: clang%llvm_version lld%llvm_version

%add_verify_elf_skiplist %_libexecdir/afl/*
%add_verify_elf_skiplist %_libexecdir/afl/custom_mutators/*
%add_verify_elf_skiplist %_datadir/afl/testcases/archives/common/ar/small_archive.a
%add_verify_elf_skiplist %_datadir/afl/testcases/others/elf/small_exec.elf

%description
The fuzzer afl++ is afl with community patches, qemu 5.1 upgrade,
collision-free coverage, enhanced laf-intel & redqueen, AFLfast++
power schedules, MOpt mutators, unicorn_mode, and a lot more!

Built without qemu_mode, unicorn_mode and nyx_mode

%package -n afl-plot-ui
Summary: GUI for afl-plot
Group: Development/Tools

BuildRequires: libgtk+3-devel

%description -n afl-plot-ui
afl-plot-ui is a helper utility for rendering the GNUplot graphs in a
GTK window. This allows to real time resizing, scrolling, and cursor
positioning features while viewing the graph. This utility also
provides options to hide graphs using check buttons.

%prep
%setup
%patch0 -p1

sed -i  "/^all:/i LDFLAGS += -ldl\n" ./utils/afl_network_proxy/GNUmakefile

# preserve utils for later installation
cp -r utils utils.orig
find ./utils.orig -type f -exec chmod -x {} \;

%build
export ALTWRAP_LLVM_VERSION=%llvm_version
export CC=clang
export CXX=clang++
export LD=ld.lld
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib

# Fix bad_elf_symbol _ZNK4llvm3cfg6UpdateIPNS_10BasicBlockEE4dumpEv
# from llvm-project/llvm/include/llvm/Support/CFGUpdate.h:51
export CPPFLAGS=-DNDEBUG

%make_build PREFIX=%prefix NO_NYX=1 -j $(nproc) source-only

# Build custom mutators
for mutator in atnwalk autotokens libfuzzer radamsa symcc symqemu; do
    %make_build -C custom_mutators/$mutator
done
%make_build CC=gcc -C custom_mutators/honggfuzz

# Build utils
for util in afl_network_proxy defork socket_fuzzing plot_ui; do
    %make_build -C utils/$util
done

%install
export ALTWRAP_LLVM_VERSION=%llvm_version
export CC=clang
export CXX=clang++
export LD=ld.lld
export CPPFLAGS=-DNDEBUG

%makeinstall_std PREFIX=%prefix

# Install custom mutators
mkdir %buildroot/%_libexecdir/afl/custom_mutators
install -m755 custom_mutators/atnwalk/atnwalk.so %buildroot/%_libexecdir/afl/custom_mutators/atnwalk-mutator.so
install -m755 custom_mutators/autotokens/autotokens.so %buildroot/%_libexecdir/afl/custom_mutators/autotokens-mutator.so
install -m755 custom_mutators/libfuzzer/libfuzzer-mutator.so -t %buildroot/%_libexecdir/afl/custom_mutators
install -m755 custom_mutators/radamsa/radamsa-mutator.so -t %buildroot/%_libexecdir/afl/custom_mutators
install -m755 custom_mutators/symcc/symcc-mutator.so -t %buildroot/%_libexecdir/afl/custom_mutators
install -m755 custom_mutators/symqemu/symqemu-mutator.so -t %buildroot/%_libexecdir/afl/custom_mutators

# Install utils
mkdir -pv %buildroot%_datadir/afl
mv utils.orig %buildroot%_datadir/afl/utils

for util in afl_network_proxy defork socket_fuzzing; do
    %makeinstall_std PREFIX=%prefix -C utils/$util
done
install -m755 utils/plot_ui/afl-plot-ui -t %buildroot%_bindir

%files
%_bindir/afl-*
%exclude %_bindir/afl-plot-ui
%_libexecdir/afl
%_datadir/afl
%_defaultdocdir/afl
%_man8dir/afl-*

%files -n afl-plot-ui
%_bindir/afl-plot-ui

%changelog
* Sun Sep 03 2023 Egor Ignatov <egori@altlinux.org> 4.08c-alt1
- First build for ALT
