# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/pkg-config
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-actions
Summary:	Caja extension for customizing the context menu
Name:		mate-file-manager-actions
Version:	1.5.0
Release:	alt2_0101
Group:		Graphical desktop/MATE
License:	GPLv2+ and LGPLv2+
URL:		https://github.com/NiceandGently/caja-actions
Source0:	https://github.com/downloads/NiceandGently/caja-actions/%{oldname}-%{version}.tar.xz

BuildRequires:	mate-file-manager-devel
BuildRequires:	libuuid-devel
BuildRequires:	libSM-devel
BuildRequires:	libunique-devel
BuildRequires:	mate-common
BuildRequires:	libxml2-devel
BuildRequires:	mate-doc-utils
BuildRequires:	libgtop2-devel
#BuildRequires:	mate-conf-devel
Source44: import.info
Patch33: caja-actions-1.5.0-alt-no-mateconf.patch

%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Nautilus interface

%package	devel
Summary:	Development tools for the caja-actions
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
%setup -n %{oldname}-%{version} -q
sed -i -e 's,Encoding=UTF-8,,g' src/cact/cact.desktop.in src/cact/cact.desktop.in
%patch33 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-schemas-install \
	--with-gtk=2 \
    --enable-mateconf=no \
    --disable-scrollkeeper \
    --enable-html-manuals=gdt \
    --with-default-io-provider=na-desktop

make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

rm $RPM_BUILD_ROOT%{_datadir}/doc/caja-actions-1.5.0/INSTALL

%find_lang %{oldname}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop


%files -f %{oldname}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/na-print-schemas
%{_libexecdir}/caja-actions/na-set-conf
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop
%{_datadir}/gtk-doc/html/caja-actions-3/
%{_datadir}/mate/help/caja-actions-config-tool/
%{_datadir}/omf/caja-actions-config-tool/

%files devel
%{_includedir}/caja-actions/

%changelog
* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0101
dropped obsolete mate-conf BR:

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0101
- initial import

