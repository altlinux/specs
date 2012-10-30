# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-calc
Version:        1.4.0
Release:        alt2
Summary:        A desktop calculator

Group:          File tools
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch:	alt-hack-yyscan-build.patch

BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: libsoup-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-doc-utils
BuildRequires: gettext
BuildRequires: flex
BuildRequires: bison
BuildRequires: intltool
BuildRequires: mate-common

Requires(post): glib2
Requires(postun): glib2

%description
mate-calc is a powerful graphical calculator with financial, logical and
scientific modes. It uses a multiple precision package to do its arithmetic
to give a high degree of accuracy.

%prep
%setup -q
%patch0 -p2
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-scrollkeeper 

make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang mate-calc --all-name


%files -f mate-calc.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/applications/mate-calc.desktop
%{_datadir}/glib-2.0/schemas/org.mate.mate-calc.gschema.xml
%{_datadir}/mate-calc
%doc %{_mandir}/man1/mate-calc.1.gz
%{_datadir}/mate/help/mate-calc/*

%changelog
* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- build fixed

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

