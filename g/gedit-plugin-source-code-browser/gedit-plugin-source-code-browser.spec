Name: gedit-plugin-source-code-browser
Version: 3.0.3
Release: alt5.git.9.g7d83d2b
Summary: source code class and function browser plugin for Gedit 3
License: BSD
Group: Editors
Url: https://github.com/toobaz/gedit-source-code-browser/

# GIT https://github.com/toobaz/gedit-source-code-browser/
Source: %name-%version.tar
Source44: %name.watch

Obsoletes: gedit-source-code-browser < %EVR
Provides: gedit-source-code-browser

# Automatically added by buildreq on ...
BuildRequires: rpm-build-python3 time

Requires: gedit /usr/bin/ctags

%define gedit_pluginsdir %_libdir/gedit/plugins
%add_python3_path %gedit_pluginsdir

%description
This plugin will add a new tab to the side pane in the Gedit text editor which
shows symbols (functions, classes, variables, etc.) for the active document.
Clicking a symbol in the list wil jump to the line on which that symbol is
defined.

See the [ctags supported languages](http://ctags.sourceforge.net/languages.html)
for a list of the 41 programming languages supported by this plugin.

%prep
%setup
find -type d -name __pycache__ -exec rm -rf {} \;

%install
mkdir -p %buildroot%gedit_pluginsdir \
	%buildroot%_datadir/glib-2.0/schemas
cp -r sourcecodebrowser* %buildroot%gedit_pluginsdir/
install -m644 sourcecodebrowser/data/*.gschema.xml \
	%buildroot%_datadir/glib-2.0/schemas/

%files
%doc README*
%gedit_pluginsdir/*
%_datadir/glib-2.0/schemas/*

%changelog
* Mon May 01 2023 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt5.git.9.g7d83d2b
- change package name from `gedit-source-code-browser` to `gedit-plugin-source-code-browser`
- change upstream once again to https://github.com/Supreeeme/gedit-source-code-browser

* Tue May 04 2021 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt4.git.11.g56d9ae0
- fix BR, move to py3

* Mon Dec 14 2020 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt3.git.11.g56d9ae0
- fix ctags dep to allow working with universal-ctags

* Wed Nov 04 2020 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt2.git.11.g56d9ae0
- fix "Breaks with gedit 3.36.1"

* Mon Jan 09 2017 Ildar Mulyukov <ildar@altlinux.ru> 3.0.3-alt1.git.8.g2eae5cd
- initial build for ALT Linux Sisyphus

