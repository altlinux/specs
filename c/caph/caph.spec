Name: caph
Version: 1.1
Release: alt1
Group: Games/Puzzles
Summary: A sandbox game, based on physics
Source: %name-%version.tar.bz2
Url: http://caphgame.sourceforge.net/
License: GPLv3

# Automatically added by buildreq on Mon Oct 04 2010
BuildRequires: libGL-devel libSDL-devel libpng-devel

%description
It is a sandbox game, based on physics. The game aim is to make contact
red object with green object. You can use various objects, solid, wire
(rope), and bendable objects. Gravitation will help you.

%prep
%setup
sed -i '
/^#define SYS_DATA_DIR/c\
#define SYS_DATA_DIR "%_gamesdatadir/%name/"
' src/caph.c

cat > %name.sh <<@@@
#!/bin/sh

CAPHDIR="\$HOME/.%name"
SHAREDIR="%_gamesdatadir/%name"
test -d "\$CAPHDIR" && cd "\$CAPHDIR" || {
rm -rf "\$CAPHDIR"
mkdir -p "\$CAPHDIR"
cd "\$CAPHDIR"
cp \`find "\$SHAREDIR"/* -maxdepth 0 -type f\` .
for D in \`find "\$SHAREDIR"/* -maxdepth 0 -type d\`; do
  LD=\`basename \$D\`
  mkdir -p "\$LD"
  ln -s "\$D"/* "\$LD"/
done
}

exec "\$0.bin"
@@@

#mkdir bin

# TODO desktop

%build
cd src
./confg
./build

%install
mkdir -p "%buildroot%_gamesdatadir"
cp -r share/caph "%buildroot%_gamesdatadir/%name"
install -sD bin/%name %buildroot%_gamesbindir/%name.bin
install -m755 -D %name.sh %buildroot%_gamesbindir/%name

%files
%doc doc
%_gamesbindir/*
%_gamesdatadir/%name

%changelog
* Fri Dec 24 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Autobuild version bump to 1.1

* Mon Oct 04 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

