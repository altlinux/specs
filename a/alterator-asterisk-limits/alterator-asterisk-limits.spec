Name: alterator-asterisk-limits
Version: 0.0.2
Release: alt1
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Summary: Alterator module for control Asterisk limits
License: GPL
Group: System/Configuration/Other

Requires: gettext
Requires: alterator >= 3.3-alt8
Requires: alterator-sh-functions
Requires: alterator-fbi >= 5.9-alt3
Requires: asterisk-initscript

BuildPreReq: alterator-fbi >= 0.15-alt2
BuildRequires: alterator >= 3.3-alt8

%description
%summary

%prep
%setup -q

%build
%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_libexecdir/alterator/backend3/*

%changelog
* Thu Nov 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.0.2-alt1
- use libshell (shell-config) for backend
- rename type 'uint' to 'asterisk-uint'
- use workflow 'none'

* Tue Oct 13 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

