# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/mateconftool-2 pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
Summary: Editor/admin tool for mate-conf
Name: mate-conf-editor
Version:  1.4.0
Release:  alt1_2
License:  GPLv2+
Group: File tools
URL:      http://mate-desktop.org
Source0:  http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

# mateconftool-2
Requires(pre):   mate-conf
Requires(post):  mate-conf
Requires(preun): mate-conf

BuildRequires: mate-conf-devel
BuildRequires: gtk2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: rarian-compat
BuildRequires: gettext
BuildRequires: mate-doc-utils
BuildRequires: mate-common
Source44: import.info

%description
mate-conf-editor allows you to browse and modify MateConf configuration
sources.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-scrollkeeper \
        --disable-schemas-install
make %{?_smp_mflags}

%install
export MATECONF_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_MAKEFILE_SCHEMA_INSTALLL


desktop-file-install --vendor "" --delete-original       \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%post
%mateconf_schema_upgrade mateconf-editor

%pre
%mateconf_schema_prepare mateconf-editor

%preun
%mateconf_schema_remove mateconf-editor

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mateconf-editor
%{_datadir}/icons/hicolor/*/apps/mateconf-editor.png
%{_datadir}/mateconf-editor/
%{_datadir}/mate/help/mateconf-editor/
%{_datadir}/applications/mateconf-editor.desktop
%{_mandir}/man1/mateconf-editor.1.*
%{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas
%{_datadir}/omf/mateconf-editor/

%changelog
* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

