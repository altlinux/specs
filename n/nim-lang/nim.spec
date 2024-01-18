%def_with check
%def_without badtests
%def_without nimdoc
Name: nim-lang
Version: 2.0.2
Release: alt1
License: MIT
Summary: A statically typed compiled systems programming language
Source: nim-%version.tar.xz
Patch: nim-1.6.12-alt-install.patch
Patch1: nim-1.6.12-alt-testament-all-propagate-keys.patch
Patch2: nim-1.6.12-alt-Unparallel.patch
Patch3: nim-1.6.12-alt-32badtest.patch
Url: https://nim-lang.org
Group: Development/Other

BuildRequires(pre): /proc /dev/pts
# Automatically added by buildreq on Fri Jul 03 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python2-base sh4
BuildRequires: parallel gcc-c++ node git-core
BuildRequires: rpm-build-python3
%if_with check
BuildRequires: libgc libsqlite3 valgrind libpcre3
%endif

%description
Nim is a statically typed compiled systems programming language. It
combines successful concepts from mature languages like Python, Ada and
Modula.

%prep
%setup -n nim-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

for N in `grep -rl '#!.usr/bin/env python3' *`; do sed -i 's@.usr/bin/env python3@/usr/bin/python3@' $N; done
echo 'will cite' | parallel --citation > /dev/null 2>&1 ||:

# Hack out network example
sed -i '/runnableExamples:/,/Pizza/s/^/  ##/' lib/pure/httpclient.nim

# Wait for ld
echo 'sem --wait --id $$' >> build.sh

%build
sh build.sh --parallel %__nprocs
./bin/nim c koch
./koch boot -d:release
./koch toolsNoExternal
%if_with nimdoc
./koch docs
%endif

%install
mkdir -p %buildroot%prefix
sh ./install.sh %buildroot/usr
install koch %buildroot/%_bindir
install bin/* %buildroot/%_bindir/
install -D tools/nim.bash-completion %buildroot%_datadir/bash-completion/completions/nim
install -D tools/nim.zsh-completion %buildroot%_datadir/zsh/site-functions/_nim

%check
sed -i '/jester/d' tests/cpp/tasync_cpp.nim
sed -i '/Megatest/d' tests/misc/tjoinable.nim tests/testament/tjoinable.nim

# vim: map <F11> <CR>/^FAIL:<CR>$F/ "eyw<C-W><C-W><C-W>_1G/aarch64<CR>:execute '/' . @e<CR>
# vim: map <F10> <CR>$F/"3yw<C-W><C-W><C-W>_1G:execute '/' . @e<CR>
# XXX Some bad tests
%if_without badtests
echo \
               tests/niminaction/Chapter8/sfml/sfml_test.nim \
               tests/manyloc/nake/nakefile.nim \
        %ifarch %ix86
               tests/stdlib/tcasts.nim \
               tests/misc/trunner.nim \
        %endif
        %ifarch ppc64le
               tests/misc/trunner.nim \
               tests/arc/t14472.nim \
               tests/arc/tasyncleak3.nim \
               tests/arc/tasyncleak4.nim \
               tests/arc/tasyncorc.nim \
               tests/arc/tcaseobj.nim \
               tests/arc/tcaseobjcopy.nim \
               tests/arc/tcustomtrace.nim \
               tests/arc/tfuncobj.nim \
               tests/arc/thard_alignment.nim \
               tests/arc/thavlak_orc_stress.nim \
               tests/arc/torc_selfcycles.nim \
               tests/arc/tunref_cycle.nim \
               tests/destructor/tnewruntime_strutils.nim \
               tests/destructor/tv2_raise.nim \
               tests/dll/nimhcr_unit.nim \
               tests/misc/tsizeof4.nim \
               tests/range/tcompiletime_range_checks.nim \
               tests/valgrind/tbasic_valgrind.nim \
               tests/valgrind/tleak_arc.nim \
               tests/views/tsplit_into_openarray.nim \
               tests/dll/nimhcr_basic.nim \
               tests/compiler/tasm.nim \
               tests/objects/tunsafenew2.nim \
        %endif
        %ifarch aarch64
               tests/range/tcompiletime_range_checks.nim \
               tests/dll/nimhcr_unit.nim \
               tests/arc/tasyncorc.nim \
               tests/threads/threadex.nim \
               tests/threads/t7172.nim \
               tests/threads/t8535.nim \
               tests/threads/tonthreadcreation.nim \
               tests/threads/tmanyjoin.nim \
               tests/threads/tthreadvars.nim \
               tests/threads/tracy_allocator.nim \
               tests/threads/treusetvar.nim \
               tests/dll/nimhcr_basic.nim \
               tests/compiler/tasm.nim \
               tests/misc/ttlsemulation.nim \
        %endif
        %ifarch %arm
               tests/misc/trunner.nim \
               tests/arc/thard_alignment.nim \
               tests/destructor/topttree.nim \
               tests/tuples/t12892.nim \
               tests/dll/nimhcr_unit.nim \
               tests/stdlib/tarithmetics.nim \
               tests/misc/tsizeof4.nim \
               tests/enum/tenum.nim \
               tests/threads/threadex.nim \
               tests/threads/tmanyjoin.nim \
               tests/threads/tonthreadcreation.nim \
               tests/threads/t7172.nim \
               tests/threads/t8535.nim \
               tests/threads/tracy_allocator.nim \
               tests/threads/treusetvar.nim \
               tests/threads/tthreadvars.nim \
               tests/stdlib/tcasts.nim \
               tests/dll/nimhcr_basic.nim \
               tests/dll/client.nim \
               tests/compiler/tasm.nim \
               tests/misc/ttlsemulation.nim \
        %endif
| tr ' ' '\n' > badtests.txt
## do
##        echo "#" > "$badtest"
## done

mkdir -p badtests
for baddir in tests/manyloc/keineschweine
do
        test -d "$baddir" && mv "$baddir" badtests
done
%endif

PATH=`pwd`/bin:$PATH ./koch tests --colors:off --megatest:off --nim:bin/nim --skipFrom:badtests.txt all
# XXX Unparallel patch: these must not be executed in parallel with any other suite
PATH=`pwd`/bin:$PATH ./koch tests --colors:off --megatest:off --nim:bin/nim --skipFrom:badtests.txt c ic
PATH=`pwd`/bin:$PATH ./koch tests --colors:off --megatest:off --nim:bin/nim --skipFrom:badtests.txt c navigator

%files
%doc %_datadir/nim/doc
%if_with nimdoc
%doc doc/html
%endif
%_bindir/*
%_localstatedir/nimble/pkgs
%prefix/lib/nim
%_sysconfdir/nim
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*

%changelog
* Fri Jan 12 2024 Fr. Br. George <george@altlinux.org> 2.0.2-alt1
- Autobuild version bump to 2.0.2
- Update bad tests
- Disable nimdoc until it ceases to download modules

* Mon Jun 05 2023 Fr. Br. George <george@altlinux.ru> 1.6.12-alt3
- Fix nimble paths (again)

* Sat Jun 03 2023 Fr. Br. George <george@altlinux.org> 1.6.12-alt2
- Fix nimble paths

* Sat Jun 03 2023 Fr. Br. George <george@altlinux.org> 1.6.12-alt1
- Autobuild version bump to 1.6.12
- Introduce check section (not all tests are passed though)

* Fri May 07 2021 Fr. Br. George <george@altlinux.ru> 1.4.6-alt1
- Autobuild version bump to 1.4.6

* Sun Oct 18 2020 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0
- Build Nimble separately

* Fri Jul 03 2020 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Autobuild version bump to 1.2.4
- Package tools

* Tue Sep 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build for ALT

