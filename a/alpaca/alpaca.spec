%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id com.jeffser.Alpaca

Name: alpaca
Version: 3.5.0
Release: alt1

Summary: Chat with local AI models
License: GPL-3.0-or-later
Group: Office

Url: https://github.com/Jeffser/Alpaca
Vcs: https://github.com/Jeffser/Alpaca
Source: %name-%version.tar

%add_python3_path %_datadir/Alpaca

Requires: typelib(GtkSource) = 5

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/glib-compile-resources 
BuildRequires: /usr/bin/gtk4-update-icon-cache
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

ExclusiveArch: aarch64 x86_64

%description
An Ollama client

Features
* Built in Ollama instance
* Talk to multiple models in the same conversation
* Pull and delete models from the app
* Have multiple conversations
* Image recognition (Only available with compatible models)
* Plain text documents recognition
* Import and export chats
* Append YouTube transcripts to the prompt
* Append text from a website to the prompt
* PDF recognition

Disclaimer
This project is not affiliated at all with Ollama. I'm not responsible for
any damages to your device or software caused by running code given
by any models.

%package local
Summary: Chat with local AI models on your computer
Group: Office
Requires: %name = %EVR
Requires: ollama
Requires: numactl

%description local
An Ollama client with support local AI Models in your computer

Features
* Built in Ollama instance
* Talk to multiple models in the same conversation
* Pull and delete models from the app
* Have multiple conversations
* Image recognition (Only available with compatible models)
* Plain text documents recognition
* Import and export chats
* Append YouTube transcripts to the prompt
* Append text from a website to the prompt
* PDF recognition

Disclaimer
This project is not affiliated at all with Ollama. I'm not responsible for
any damages to your device or software caused by running code given
by any models.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_bindir/alpaca_search_provider
%_datadir/Alpaca/
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.*
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.SearchProvider.service
%_datadir/gnome-shell/search-providers/%app_id.search-provider.ini
%_desktopdir/%app_id.SearchProvider.desktop
%doc README.md

%files local

%changelog
* Fri Jan 24 2025 Semen Fomchenkov <armatik@altlinux.org> 3.5.0-alt1
- Initial build.
