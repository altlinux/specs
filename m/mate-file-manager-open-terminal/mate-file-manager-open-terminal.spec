Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/pkg-config libgio-devel pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:		mate-file-manager-open-terminal
Version:	1.5.0
Release:	alt1_2
Summary:	Mate-file-manager extension for an open terminal shortcut

License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:	mate-common
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	gsettings-desktop-schemas-devel
Requires:	gsettings-desktop-schemas
Source44: import.info

%description
The mate-file-manager-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure				\
	--disable-static		\
	--disable-schemas-compile	\
	--with-gnu-ld			

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/caja/extensions-2.0/*.la

%find_lang caja-open-terminal

%files -f caja-open-terminal.lang
%doc AUTHORS ChangeLog README COPYING
%{_datadir}/glib-2.0/schemas/org.mate.apps.caja-open-terminal.gschema.xml
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so

%changelog
* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Fri Dec 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

