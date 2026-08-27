Name: ttf-promtfont
Version: 1.2.2
Release: alt1
Source: %name-%version.tar
License: OFL-1.0 
Group: System/Fonts/True type
Summary: A font for button prompts and glyphs in games and game-related applications.
Url: https://shinmera.com/promptfont
BuildArch: noarch

%description
%summary

%prep
%setup

%install
install -Dm644 *.ttf -t "%buildroot%_datadir/fonts/ttf/%name/"
install -Dm644 *.otf -t "%buildroot%_datadir/fonts/otf/%name/"
install -Dm644 LICENSE.txt README.md index.html promptfont.css index.css tags.txt preview.png -t "%buildroot%_docdir/%name/"
install -Dm644 glyphs.json tags.txt promptfont.txt promptfont.css promptfont.h promptfont.cs promptfont.py promptfont.lisp promptfont.lua promptfont.rs promptfont.gd promptfont.gml atlas*.png -t "%buildroot%_datadir/%name/"

%files
%_datadir/fonts/ttf/%name/*
%_datadir/fonts/otf/%name/*
%_docdir/%name/
%_datadir/%name

%changelog
* Tue Aug 25 2026 Artyom Bystrov <arbars@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus