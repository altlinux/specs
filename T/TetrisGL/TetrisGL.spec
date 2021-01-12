Name: TetrisGL
Version: 1.0.2
Release: alt1

Summary: Just another tetris game with OpenGL graphics
License: GPLv3
Group: Games/Arcade

Url: http://github.com/BaZzz01010101/TetrisGL
Source: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libGLEW-devel
BuildRequires: libglfw3-devel
BuildRequires: libglm-devel
BuildRequires: rapidjson
BuildRequires: libfreetype-devel
BuildRequires: libstb-devel

%description
This project has developed for training purposes only.
It has been written in C++ and uses OpenGL to render all graphics.

Ported to Linux/e2k online: http://youtu.be/761Ab1SDZsQ

NB: users must be in `games' group to play!

%prep
%setup

%build
%cmake_insource
# libglfw.so -> libglfw.so.3
sed -i 's,glfw3,glfw,' CMakeFiles/TetrisGL.dir/link.txt
%make_build # VERBOSE=1

%install
cat > %name << EOF
#!/bin/sh
exec %_libexecdir/%name/%name
EOF

rm -f bin/*.{exe,dll}

mkdir -p %buildroot%_libexecdir/%name
cp -a bin/* %buildroot%_libexecdir/%name

install -D /dev/null %buildroot%_localstatedir/games/%name.scores
ln -srf %buildroot{%_localstatedir/games/%name.scores,%_libexecdir/%name/leaderboard.dat}

install -D bin/settings.dat %buildroot%_localstatedir/games/%name.settings
ln -srf %buildroot{%_localstatedir/games/%name.settings,%_libexecdir/%name/settings.dat}

install -pDm755 ../bin/%name %buildroot%_libexecdir/%name/%name
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_libexecdir/%name
%attr(0755,root,root)  %_bindir/%name
%attr(2711,root,games) %_libexecdir/%name/%name
%attr(0664,root,games) %_localstatedir/games/%name.scores
%attr(0664,root,games) %_localstatedir/games/%name.settings

%changelog
* Tue Jan 12 2021 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- initial package

