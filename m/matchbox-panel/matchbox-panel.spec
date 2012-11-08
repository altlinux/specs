# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/msgfmt /usr/bin/msgmerge /usr/bin/xgettext
# END SourceDeps(oneline)
%define name 	matchbox-panel
%define version 0.9.3
%define release %mkrel 4

Summary: 	Panel for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	alt1_4
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%name/0.9/%name-%version.tar.bz2

BuildRequires:	libmatchbox-devel libapm-devel libstartup-notification-devel libwireless-devel
Source44: import.info
Patch33: matchbox-panel-0.9.3-alt-xvt.patch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the panel from Matchbox.

%prep
%setup -q
%patch33 -p1

%build
%configure --enable-nls --enable-dnotify --enable-startup-notification
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/pixmaps/*
%_datadir/applications/*





%changelog
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4
- mageia import

