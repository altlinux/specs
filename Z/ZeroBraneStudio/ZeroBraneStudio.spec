%define lua lua5.1

Name: ZeroBraneStudio
Version: 2.01
Release: alt1
Summary: lightweight cross-platform Lua IDE
License: MIT
Group: Development/Other
Url: http://studio.zerobrane.com/
BuildArch: noarch
Vcs: https://github.com/pkulchenko/ZeroBraneStudio

Source: https://github.com/pkulchenko/ZeroBraneStudio/archive/%version.tar.gz#/%name-%version.tar.gz
Source88: %name.watch

Requires: wxlua lua5.1(socket) lua5.1(lfs) lua5.1(lpeg)
#Requires: luarocks(git)
# Requires: luarocks(copas) luarocks(mobdebug) luarocks(lua-parser-loose)
Requires: %lua

BuildRequires: desktop-file-utils

%description
ZeroBrane Studio is a lightweight cross-platform Lua IDE with code completion,
syntax highlighting, remote debugger, code analyzer, live coding, and debugging
support for several Lua engines (LuaJIT, Love 2D, Moai, Gideros, Corona,
Marmalade Quick, Cocos2d-x, GSL-shell, Adobe Lightroom, OpenResty/Nginx and
others). It originated from the Estrela Editor.

%prep
%setup
rm -rf bin \
	*.exe \
	zbstudio/ZeroBraneStudio.app \
	lualibs/{socket{,.lua},mime.lua} \
	lualibs/re.lua \

%install
sed -r -i "/ide.config.stylesoutshell/ i ide.config.path.lua = '%_bindir/%lua'" src/main.lua

mkdir -p %buildroot%_desktopdir %buildroot%_iconsdir
cp -a . %buildroot%_datadir/%name
cp -a zbstudio/res/icons %buildroot%_iconsdir/hicolor

desktop-file-install \
	--set-key=Exec --set-value='sh -c "cd %_datadir/%name ; exec %lua src/main.lua"' \
	--dir=%buildroot%_desktopdir zbstudio/res/zbstudio.desktop

%add_findreq_skiplist %_datadir/%name/zbstudio.sh
%add_findreq_skiplist %_datadir/%name/build/*
%add_findreq_skiplist %_datadir/%name/lualibs/*.lua
%add_findreq_skiplist %_datadir/%name/lualibs/*/*.lua
%add_findreq_skiplist %_datadir/%name/lualibs/*/*/*.lua

%files
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Sat Dec 09 2023 Ildar Mulyukov <ildar@altlinux.ru> 2.01-alt1
- new version

* Tue Aug 22 2023 Ildar Mulyukov <ildar@altlinux.ru> 1.90-alt2
- fix build with newer autodep system

* Mon Mar 02 2020 Ildar Mulyukov <ildar@altlinux.ru> 1.90-alt1
- new version

* Thu Jun 06 2019 Ildar Mulyukov <ildar@altlinux.ru> 1.80-alt1
- new version
- fix lua-5.1 as the interpreter

* Tue Nov 10 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.20-alt1
- new version

* Fri Sep 11 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.10-alt1
- new version
- luadist integration should fail

* Tue Oct 28 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.80-alt1
- initial build for ALT Linux Sisyphus
