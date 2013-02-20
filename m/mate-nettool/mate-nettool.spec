# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/mateconftool-2 pkgconfig(gmodule-export-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libgtop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: 		Network information tool for MATE
Name: 			mate-nettool
Version: 		1.4.0
Release: 		alt1_0101
URL: 			https://github.com/NiceandGently/mate-nettool
Source0: 		https://github.com/NiceandGently/mate-nettool/archive/%{name}-%{version}.tar.xz
License: 		GPLv2+
Group: 			Graphical desktop/MATE

BuildRequires: 	gtk2-devel
BuildRequires: 	mate-conf-devel
BuildRequires: 	libgtop2-devel
BuildRequires: 	desktop-file-utils
BuildRequires: 	mate-doc-utils
BuildRequires:  mate-common

Requires:		bind-utils
Requires:		whois
Source44: import.info

%description
MATE Nettool is a front-end to various networking command line
tools, like ping, netstat, ifconfig, whois, traceroute, finger.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static          \
	--disable-scrollkeeper \
	--with-gtk=2.0

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original                   \
  --remove-category="MATE"                                           \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications				\
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-nettool.desktop

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/mate-nettool/
%{_datadir}/icons/hicolor/*/apps/mate-nettool.png
%{_datadir}/icons/hicolor/scalable/apps/mate-nettool.svg
%{_datadir}/applications/mate-nettool.desktop
%{_datadir}/mate/help/mate-nettool/
%{_datadir}/omf/mate-nettool/


%changelog
* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_0101
- initial import

