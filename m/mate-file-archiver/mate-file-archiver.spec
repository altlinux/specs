# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums pkgconfig(gio-unix-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
Group: Archiving/Other
%define _libexecdir %_prefix/libexec
%define oldname mate-file-archiver
Name:           mate-file-archiver
Version:        1.5.1
Release:        alt1_3
Summary:        MATE Desktop file archiver

License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz


BuildRequires:  mate-common
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(mate-doc-utils)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(sm)

Requires:   gsettings-desktop-schemas
Patch33: file-roller-2.28.2-alt-7z.patch
Source44: import.info

%description
Mate File Archiver is an application for creating and viewing archives files,
such as tar or zip files.


%package -n mate-file-manager-archiver
Group: Archiving/Other
Summary: File Roller extension for mate-file-manager
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n mate-file-manager-archiver
This package contains the Mate File archiver extension for Mate file manger.
It adds an item to the mate-file-manager contexst menu that lets you compress files
or directories.


%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p0


%build
%configure                 \
   --disable-scrollkeeper  \
   --disable-static        \
   --with-gtk=2.0          \
   --enable-caja-actions

make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original          \
  --remove-category=MATE                        \
  --add-category=X-Mate                         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/engrampa.desktop

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'


%find_lang engrampa --with-gnome

%post
/bin/touch --no-create %{_datadir}/icons/mate &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/mate &>/dev/null
fi

%files -f engrampa.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/engrampa
%{_libexecdir}/engrampa/
%{_datadir}/engrampa/
%{_datadir}/mate/help/engrampa/
%{_datadir}/applications/engrampa.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/MateConf/gsettings/engrampa.convert
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml

%files -n mate-file-manager-archiver
%{_libdir}/caja/extensions-2.0/libcaja-engrampa.so



%changelog
* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_3
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

