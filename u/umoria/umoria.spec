Name: umoria
Version: 5.7.15
Release: alt1
License: GPLv3+
Group: Games/Adventure
Url: https://umoria.org/
Source: %name-%version.tar.gz
Summary: A single player dungeon simulation

Patch0: 0001-No-privilege-drop.patch
Patch1: 0002-Initialize-a-variable.patch

# Automatically added by buildreq on Sat Mar 11 2023
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libncurses-devel libsasl2-3 libstdc++-devel libtinfo-devel pkg-config python3 python3-base python3-dev sh4
BuildRequires: cmake gcc-c++ libssl-devel libncursesw-devel

%description
The Dungeons of Moria is a single player dungeon simulation originally
written by Robert Alan Koeneke, with its first public release in 1983.
The game was originally developed using VMS Pascal before being ported to the
C language by James E. Wilson in 1988, and released a Umoria.

%prep
%setup
%patch0 -p1
%patch1 -p1

cat > %name << "@@@"
#!/bin/sh
UMORIA=${UMORIA:-%_bindir/%name.bin}
UMODATA=${UMODATA:-%_datadir/%name}
UMOSCORE="%_localstatedir/%name/scores.dat"
UMOHOME="$HOME/.umoria"
UMOHDATA="$UMOHOME/data"
UMOHSCORE="$UMOHOME/scores.dat"

mkdir -p "$UMOHOME"
test -r "$UMOHSCORE" || ln -s "$UMOSCORE" "$UMOHSCORE"
test -r "$UMOHDATA" || ln -s "$UMODATA" "$UMOHDATA"
cd "$UMOHOME"
exec "$UMORIA"
@@@

%define CMHOME %_cmake__builddir/%name
%build
%cmake
%cmake_build

%install
install -D %name %buildroot%_bindir/%name
install -D %CMHOME/%name %buildroot%_bindir/%name.bin
mkdir -p %buildroot%_datadir/%name
install %CMHOME/data/* %buildroot%_datadir/%name/
install -D %CMHOME/scores.dat %buildroot%_localstatedir/%name/scores.dat

%files
%attr(2711,root,games) %_bindir/%name.bin
%_bindir/%name
%_datadir/%name
%dir %attr(775,root,games) %_localstatedir/%name
%attr(664,root,games) %_localstatedir/%name/scores.dat

%changelog
* Wed Mar 15 2023 Fr. Br. George <george@altlinux.org> 5.7.15-alt1
- Autobuild version bump to 5.7.15
- Fix build on ppc64le

* Sat Mar 11 2023 Fr. Br. George <george@altlinux.ru> 5.7.14-alt1
- Initial build for ALT
