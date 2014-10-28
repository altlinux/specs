Name: ZeroBraneStudio
Version: 0.80
Release: alt1
Summary: lightweight cross-platform Lua IDE
License: MIT
Group: Development/Other
Url: http://studio.zerobrane.com/
BuildArch: noarch

# https://github.com/pkulchenko/ZeroBraneStudio
Source: %name-%version.tar

Requires: wxlua luarocks(luasocket) >= 3.0 luarocks(copas) luarocks(mobdebug) luarocks(lua-parser-loose)
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
rm -rf bin lualibs

%install
sed -r -i "/ide.config.stylesoutshell/ i ide.config.path.lua = '/usr/bin/lua'" src/main.lua

mkdir -p %buildroot%_desktopdir %buildroot/usr/share/icons
cp -a . %buildroot/usr/share/%name
cp -a zbstudio/res/icons %buildroot/usr/share/icons/hicolor

desktop-file-install \
	--set-key=Exec --set-value='sh -c "cd /usr/share/%name ; exec lua src/main.lua"' \
	 --dir=%buildroot%_desktopdir zbstudio/res/zbstudio.desktop

%files
%doc CHANGELOG.md LICENSE README*
/usr/share/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*.desktop

%changelog
* Tue Oct 28 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.80-alt1
- initial build for ALT Linux Sisyphus
