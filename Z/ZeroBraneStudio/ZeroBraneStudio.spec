%define lua lua5.1

Name: ZeroBraneStudio
Version: 1.80
Release: alt1
Summary: lightweight cross-platform Lua IDE
License: MIT
Group: Development/Other
Url: http://studio.zerobrane.com/
BuildArch: noarch

# https://github.com/pkulchenko/ZeroBraneStudio
Source: https://github.com/pkulchenko/ZeroBraneStudio/archive/%version.tar.gz
Source88: %name.watch
Patch: zbs-1.8.0.patch

Requires: wxlua luarocks5.1(luasocket) >= 3.0 luarocks5.1(luafilesystem) luarocks5.1(lpeg)
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
%patch0 -p1
rm -rf bin \
	*.exe \
	zbstudio/ZeroBraneStudio.app \
	lualibs/{socket{,.lua},mime.lua} \
	lualibs/re.lua \
; echo FIXME: Leaving \
	lualibs/{copas,coxpcall} \
	lualibs/mobdebug \
	lualibs/lua_{lexer,parser}_loose.lua \

%install
sed -r -i "/ide.config.stylesoutshell/ i ide.config.path.lua = '%_bindir/%lua'" src/main.lua

mkdir -p %buildroot%_desktopdir %buildroot%_iconsdir
cp -a . %buildroot%_datadir/%name
cp -a zbstudio/res/icons %buildroot%_iconsdir/hicolor

desktop-file-install \
	--set-key=Exec --set-value='sh -c "cd %_datadir/%name ; exec %lua src/main.lua"' \
	--dir=%buildroot%_desktopdir zbstudio/res/zbstudio.desktop

#
%add_findreq_skiplist %_datadir/%name/zbstudio.sh
%add_findreq_skiplist %_datadir/%name/build/*

%files
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
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
