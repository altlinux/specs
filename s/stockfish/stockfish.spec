%global nnuehash 5af11540bbfe

Name: stockfish
Version: 16
Release: alt2
Group: Games/Boards

Summary: Powerful open source chess engine
# CC0 is for the NNUE network file (see https://tests.stockfishchess.org/nns)
License: GPLv3+ and CC0
Url: http://stockfishchess.org
Packager: Leonid Znamenok <respublica@altlinux.org>

# Main source
# https://github.com/official-%name/Stockfish/archive/sf_%version.tar.gz
Source0: %name-%version.tar

# the NN file
Source1: https://tests.stockfishchess.org/api/nn/nn-%nnuehash.nnue

# steal some documentation
Source10: https://raw.githubusercontent.com/frankkopp/FrankyUCIChessEngine/master/engine-interface.txt
# polyglot support
Source20: https://raw.githubusercontent.com/spinkham/stockfish/master/polyglot.ini

# Patch removes check for the existence of curl or wget in the makefile
Patch0: stockfish-16-alt-remove-nnue-downloading-makefile.patch
Patch3500: stockfish-loongarch64.patch

BuildRequires: gcc-c++
BuildRequires: make

%description
Stockfish is a free UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard with
PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in
order to be used comfortably. Read the documentation for your GUI of choice for
information about how to use Stockfish with your GUI.

%prep
# verify the NNUE net checksum early to catch maintainer error
test %nnuehash = "$(sha256sum %SOURCE1 | cut -c1-12)"

%setup

%patch0 -p1
%patch3500 -p1
%ifarch %e2k
# SSSE3 is available on e2k, but assembly is different
sed -i '/#define USE_INLINE_ASM/d' src/nnue/layers/simd.h
%endif

cp %SOURCE10 ./
cp %SOURCE1 ./src/

# W: wrong-file-end-of-line-encoding
sed -i 's,\r$,,' engine-interface.txt

# polyglot of installed binary and disable log
sed -e 's,\(EngineDir = \).*,\1%_bindir,' \
-e 's,\(EngineCommand = \).*,\1%name,' \
-e 's,\(LogFile = \).*,\1~/,' -e 's,\(LogFile = \).*,\1false,' \
%SOURCE20 >polyglot.ini

%build
# default to general-64, which also works for s390x
%global sfarch general-64

%ifarch x86_64
%global sfarch x86-64
%endif

%ifarch %ix86
%global sfarch x86-32
%endif

%ifarch ppc64le
%global sfarch ppc-64
%endif

%ifarch aarch64
%global sfarch armv8
%endif

%ifarch armh
%global sfarch armv7
%endif

%ifarch %e2k
%global sfarch e2k
%endif

%ifarch loongarch64
%global sfarch loongarch64
%endif

%make_build -C src build ARCH=%sfarch

%install
mkdir -p %buildroot%_bindir
install -m 755 -p src/%name %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir/%name
cp -p polyglot.ini %buildroot%_sysconfdir/%name

%check
# run bench as a sanity check
./src/%name bench

%files
%doc Copying.txt AUTHORS engine-interface.txt README.md
%_bindir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/polyglot.ini

%changelog
* Fri Oct 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 16-alt2
- NMU: fixed FTBFS on LoongArch

* Wed Jul 19 2023 Leonid Znamenok <respublica@altlinux.org> 16-alt1
- New version

* Mon May 15 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 15.1-alt1.1
- Fixed build for Elbrus.

* Mon Jan 16 2023 Leonid Znamenok <respublica@altlinux.org> 15.1-alt1
- Rebuild for ALT Linux, thanks Fedora!
- Build support for the e2k architecture has been added.
- Outdated documentation has been removed.
- Links have been updated.
