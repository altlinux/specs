# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define mate_conf_version 1.1.0

Summary: 	Editor/admin tool for MateConf
Name: 		mate-conf-editor
Version: 	1.4.0
Release: 	alt1_1.1
URL: 		http://pub.mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 	GPLv2+ and GFDL
Group: 		File tools

Requires(pre): mate-conf >= %{mate_conf_version}
Requires(post): mate-conf >= %{mate_conf_version}
Requires(preun): mate-conf >= %{mate_conf_version}

BuildRequires: mate-conf-devel
BuildRequires: gtk2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: scrollkeeper
BuildRequires: gettext
BuildRequires: mate-doc-utils
BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: autoconf automake libtool

%description
mate-conf-editor allows you to browse and modify MateConf configuration
sources.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
    --disable-scrollkeeper

make %{?_smp_mflags}

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# stuff we don't want
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

%find_lang mateconf-editor --all-name

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule %{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas > /dev/null || :


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas > /dev/null || :
fi

%files -f mateconf-editor.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mateconf-editor
%{_datadir}/icons/hicolor/*/apps/mateconf-editor.png
%{_datadir}/mateconf-editor
%{_datadir}/applications/mateconf-editor.desktop
%{_mandir}/man1/mateconf-editor.1.*
%{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas
%dir %{_datadir}/omf/mateconf-editor
%{_datadir}/mate/help/mateconf-editor/*
%{_datadir}/omf/mateconf-editor/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

