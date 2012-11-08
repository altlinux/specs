# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define name 	matchbox-desktop
%define version 2.0
%define release %mkrel 5

Summary: 	Desktop for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	alt1_5
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2
BuildRequires:	libmatchbox-devel
BuildRequires:	libstartup-notification-devel
BuildRequires:	gtk+2-devel
Requires:	matchbox-panel
Requires:	matchbox-window-manager
Requires:	matchbox-common
Obsoletes:	matchbox-desktop-devel < %{version}-%{release}
Source44: import.info
Patch33: matchbox-desktop-2.0-alt-link.patch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the main desktop from Matchbox.

%prep
%setup -q
%patch33 -p1

%build
%configure --enable-dnotify --enable-startup-notification
%make

%install
%makeinstall_std

# wmsession config
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/X11/wmsession.d
cat > $RPM_BUILD_ROOT/%_sysconfdir/X11/wmsession.d/22Matchbox <<EOF
NAME=Matchbox
ICON=/usr/share/pixmaps/mbdesktop.png
EXEC=/usr/bin/matchbox-session
DESC=Matchbox
SCRIPT:
exec /usr/bin/matchbox-session
EOF

%files
%doc AUTHORS README ChangeLog
%_bindir/%name
%config(noreplace) %_sysconfdir/X11/wmsession.d/*




%changelog
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_5
- mageia import

