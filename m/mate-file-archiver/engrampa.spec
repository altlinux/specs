%define _libexecdir %_prefix/libexec
%define oldname engrampa
%define glib2_version 2.16.0
%define pango_version 1.8.0
%define libmateui_version 1.1.2
%define libmateprint_version 1.1.0
%define libmateprintui_version 1.1.0
%define desktop_file_utils_version 0.9
%define caja_version 1.1.0
%define mate_doc_utils_version 1.1.0

Summary:        Tool for viewing and creating archives
Name:           mate-file-archiver
Version:        1.4.0
Release:        alt2_1.1
License:        GPLv2+
Group:          Archiving/Other
URL:            http://pub.mate-desktop.org
Source:         http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: mate-file-manager-devel >= %{caja_version}
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libSM-devel
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: mate-doc-utils >= %{mate_doc_utils_version}
BuildRequires: intltool
BuildRequires: mate-conf-devel
BuildRequires: mate-common

Requires(pre): mate-conf
Requires(post): mate-conf
Requires(preun): mate-conf
Patch33: file-roller-2.28.2-alt-7z.patch
Source44: import.info

%description
engrampa is an application for creating and viewing archives files,
such as tar or zip files.

%prep
%setup -q -n %{oldname}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p0

%build

%configure \
	--disable-scrollkeeper \
	--disable-static \
	--with-gtk=2.0 \
	--enable-caja-actions

export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export tagname=CC
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%find_lang %{oldname} --all-name

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/engrampa.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/engrampa.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/mateconf/schemas/engrampa.schemas \
    > /dev/null || :
fi

%files -f %{oldname}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/engrampa
%{_datadir}/engrampa
%{_datadir}/applications/engrampa.desktop
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so
%{_libexecdir}/engrampa
%{_datadir}/icons/hicolor/*/apps/engrampa.png
%{_datadir}/icons/hicolor/scalable/apps/engrampa.svg
%{_sysconfdir}/mateconf/schemas/engrampa.schemas
%{_datadir}/mate/help/engrampa/*
%{_datadir}/omf/*


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

