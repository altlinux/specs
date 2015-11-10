Name: ZeroBraneStudio
Version: 1.20
Release: alt1
Summary: lightweight cross-platform Lua IDE
License: MIT
Group: Development/Other
Url: http://studio.zerobrane.com/
BuildArch: noarch

# https://github.com/pkulchenko/ZeroBraneStudio
Source: %name-%version.tar

Requires: wxlua luarocks(luasocket) >= 3.0
# Requires: luarocks(copas) luarocks(mobdebug) luarocks(lua-parser-loose)
Requires: lua5

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
	zbstudio/ZeroBraneStudio.app \
	lualibs/{socket{,.lua},mime.lua} \
; echo FIXME: Leaving \
	lualibs/{copas,coxpcall} \
	lualibs/mobdebug \
	lualibs/lua_{lexer,parser}_loose.lua \

%install
sed -r -i "/ide.config.stylesoutshell/ i ide.config.path.lua = '%_bindir/lua'" src/main.lua

mkdir -p %buildroot%_desktopdir %buildroot%_iconsdir
cp -a . %buildroot%_datadir/%name
cp -a zbstudio/res/icons %buildroot%_iconsdir/hicolor

desktop-file-install \
	--set-key=Exec --set-value='sh -c "cd %_datadir/%name ; exec lua src/main.lua"' \
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
* Tue Nov 10 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.20-alt1
- new version

* Fri Sep 11 2015 Ildar Mulyukov <ildar@altlinux.ru> 1.10-alt1
- new version
- luadist integration should fail

* Tue Oct 28 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.80-alt1
- initial build for ALT Linux Sisyphus
