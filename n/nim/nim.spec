%define _unpackaged_files_terminate_build 1

%def_with bootstrap
%def_with check

Name: nim
Version: 2.2.10
Release: alt1

Summary: Statically typed compiled systems programming language
License: MIT
Group: Development/Other
Url: https://nim-lang.org
Vcs: https://github.com/nim-lang/Nim

Source0: %name-%version.tar
# Bootstrap C sources: https://github.com/nim-lang/csources_v3/archive/master.tar.gz
# csources_v3 is a fixed snapshot used to bootstrap the Nim compiler
Source1: csources_v3-master.tar.gz
# https://github.com/nim-lang/checksums/archive/0b8e46379c5bc1bf73d8b3011908389c60fb9b98.tar.gz
# commit 0b8e46379c5bc1bf73d8b3011908389c60fb9b98 (2.0.1)
Source2: checksums-master.tar.gz
Patch: %name-%version-alt.patch

%if_with bootstrap
# Bootstrap: build from C sources
BuildRequires: glibc-devel
%else
# Normal build: use existing nim from repo
BuildRequires: nim
%endif
%if_with check
BuildRequires: libssl-devel
%endif

%description
Nim is a statically typed compiled systems programming language.
It combines successful concepts from mature languages like Python, Ada
and Modula. Its design focuses on efficiency, expressiveness, and
elegance (in that order of priority).

Nim compiles to C, C++, and JavaScript and produces native binaries
with no runtime dependency on a Nim-specific runtime library.

%package -n nimgrep
Summary: Search and replace tool for Nim source code
Group: Development/Other
Requires: %name = %EVR

%description -n nimgrep
nimgrep is a command-line tool for searching and replacing patterns
in Nim source code, with awareness of Nim syntax.

%package -n nimpretty
Summary: Source code formatter for Nim
Group: Development/Other
Requires: %name = %EVR

%description -n nimpretty
nimpretty is the official source code formatter for Nim.
It formats Nim code according to the official style guide.

%package -n nimsuggest
Summary: IDE support tool for Nim (language server)
Group: Development/Other
Requires: %name = %EVR

%description -n nimsuggest
nimsuggest is a tool that helps IDE/editor plugins provide
features such as code completion, jump to definition, find usages
and other IDE-like features for the Nim programming language.

%package -n nim-debug
Summary: Debugging tools for Nim
Group: Development/Other
Requires: %name = %EVR
Requires: gdb

%description -n nim-debug
Debugging tools for the Nim programming language:
nim-gdb is a GDB helper script for debugging Nim programs with GDB
Python support. nim_dbg is a debug build of the Nim compiler itself.

%prep
%setup -a1 -a2
%autopatch -p1
mv csources_v3-master csources_v3
mkdir -p dist
mv checksums-master dist/checksums

%build
%if_with bootstrap
cd csources_v3
%make -j$(nproc)
cd ..
bin/nim c --noNimblePath --skipUserCfg --skipParentCfg --hints:off koch
%else
ln -sf $(which nim) bin/nim
%endif
./koch boot -d:release --skipUserCfg --skipParentCfg --hints:off
./koch toolsnoexternal --skipUserCfg --skipParentCfg --hints:off

%install
install -Dm755 bin/nim %buildroot%_bindir/nim
for tool in nimgrep nimpretty nimsuggest nim-gdb nim_dbg; do
    [ -f bin/$tool ] && install -Dm755 bin/$tool %buildroot%_bindir/$tool || true
done

# Install stdlib to /usr/lib/nim/lib/ — compiler looks for system.nim at
# $libpath/system.nim where libpath = getPrefixDir()/lib = /usr/lib/nim/lib
install -d %buildroot%_target_libdir_noarch/nim/lib
cp -r lib/. %buildroot%_target_libdir_noarch/nim/lib/
rm %buildroot%_target_libdir_noarch/nim/lib/pure/unidecode/gen.py

# Install nim.cfg to /etc/nim/ — compiler searches /etc/nim/nim.cfg
install -d %buildroot%_sysconfdir/nim
install -Dm644 config/nim.cfg %buildroot%_sysconfdir/nim/nim.cfg
install -Dm644 config/nimdoc.cfg %buildroot%_sysconfdir/nim/nimdoc.cfg

# Install nim-gdb Python module
install -Dm644 tools/debug/nim-gdb.py %buildroot%_datadir/nim/debug/nim-gdb.py

%check
export PATH="$PWD/bin:$PATH"
testament --targets:c pat tests/stdlib/tos.nim

%files
%doc readme.md copying.txt
%_bindir/nim
%_target_libdir_noarch/nim/
%dir %_sysconfdir/nim
%config(noreplace) %_sysconfdir/nim/nim.cfg
%config(noreplace) %_sysconfdir/nim/nimdoc.cfg

%files -n nimgrep
%_bindir/nimgrep

%files -n nimpretty
%_bindir/nimpretty

%files -n nimsuggest
%_bindir/nimsuggest

%files -n nim-debug
%_bindir/nim-gdb
%_bindir/nim_dbg
%_datadir/nim/debug/nim-gdb.py

%changelog
* Tue May 26 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.2.10-alt1
- Initial build for ALT Sisyphus.
