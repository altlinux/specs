# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-export-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
Group: File tools
%define _libexecdir %_prefix/libexec
Name:		mate-calc
Version:	1.5.1
Release:	alt1_2
Summary:	MATE Desktop calculator
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	mate-desktop-devel
BuildRequires:	desktop-file-utils
Source44: import.info
Patch33: mate-calc-1.5.1-alt-hack-yyscan-build.patch


%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
%setup -q -n %{name}-%{version}
#patch33 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-schemas-compile
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/applications/mate-calc.desktop
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/mate-calc/

%changelog
* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- converted for ALT Linux by srpmconvert tools

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- build fixed

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

