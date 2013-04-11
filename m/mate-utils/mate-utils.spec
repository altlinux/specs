Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/scrollkeeper-config gcc-c++ libICE-devel libSM-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gthread-2.0) pkgconfig(libcanberra-gtk) pkgconfig(xext) zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-utils
Version:        1.6.0
Release:        alt1
Summary:        MATE utility programs

License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

# 1 = build, undef = dont build
%define gdict_applet 1

BuildRequires:  desktop-file-utils
BuildRequires:  hardlink
BuildRequires:  mate-common
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libgtop-2.0)
%if 0%{?gdict_applet:1}
BuildRequires:  mate-panel-devel
%endif
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-doc-utils
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  popt-devel
BuildRequires:  rarian-compat
BuildRequires:  consolehelper
BuildRequires:  gsettings-desktop-schemas-devel
Source44: import.info
Obsoletes: Obsoletes: mate-utils-libs < 1.5.0-alt2_1
Conflicts: mate-utils-libs < 1.5.0-alt2_1

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screenshot tool and others.

%package devel
Group: Development/C
Summary: Development files for mate-utils
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package -n mate-system-log
Group: File tools
Summary: A log file viewer for the MATE desktop
Requires: consolehelper
%description -n mate-system-log
The mate-system-log package contains an application that lets you
view various system log files.


%prep
%setup -q
#%if 0%{?gdict_applet:1}
#sed -i -e 's@libmatepanelapplet-2.0@libmatepanelapplet-4.0@g' configure.ac
#%endif
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
        --disable-static \
        --disable-scrollkeeper \
        --disable-schemas-compile \
        --enable-gdict-applet%{!?gdict_applet:=no}

#sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make V=1 %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install 

# make mate-system-log use consolehelper until it starts using polkit
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth      include      config-util
account      include      config-util
session      include      config-util
EOF

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=/usr/sbin/mate-system-log
SESSION=true
FALLBACK=true
EOF

mkdir -p  %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_sbindir}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/mate-system-log

rm -fv $RPM_BUILD_ROOT%{_libdir}/*.la

desktop-file-install --vendor ""                     \
  --delete-original                                  \
  --remove-category="MATE"                           \
  --add-category="X-Mate"                            \
  --dir %{buildroot}%{_datadir}/applications      \
  %{buildroot}%{_datadir}/applications/*

# save space by linking identical images in translated docs
hardlink -c -v %{buildroot}%{_datadir}/mate/help

%find_lang %{name} --with-gnome
%find_lang mate-disk-usage-analyzer --with-gnome
%find_lang mate-dictionary --with-gnome
%find_lang mate-search-tool --with-gnome
%find_lang mate-system-log --with-gnome

cat mate-disk-usage-analyzer.lang >> %{name}.lang
cat mate-dictionary.lang >> %{name}.lang
cat mate-search-tool.lang >> %{name}.lang

%files -f %{name}.lang
%doc COPYING NEWS README
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README
%doc baobab/AUTHORS
%doc baobab/README
%{_bindir}/mate-dictionary
%{_bindir}/mate-panel-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-search-tool
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/applications/mate-dictionary.desktop
%{_datadir}/applications/mate-screenshot.desktop
%{_datadir}/applications/mate-search-tool.desktop
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_datadir}/mate-dict/
%{_datadir}/mate-dictionary/
%{_datadir}/mate-screenshot/
%{_datadir}/mate-disk-usage-analyzer/
%{_datadir}/pixmaps/mate-search-tool/
%{_libdir}/libmatedict.so.*
%if 0%{?gdict_applet}
%{_libexecdir}/mate-dictionary-applet
%endif
%{_mandir}/man1/mate-dictionary.1*
%{_mandir}/man1/mate-search-tool.1*
%{_mandir}/man1/mate-screenshot.1*
%{_mandir}/man1/mate-disk-usage-analyzer.1*
%{_datadir}/icons/mate/*/apps/baobab.*
%{_datadir}/mate/help/mate-dictionary/
%{_datadir}/mate/help/mate-disk-usage-analyzer/
%{_datadir}/mate/help/mate-search-tool/
%{_datadir}/MateConf/gsettings/mate-dictionary.convert
%{_datadir}/MateConf/gsettings/mate-disk-usage-analyzer.convert
%{_datadir}/MateConf/gsettings/mate-screenshot.convert
%{_datadir}/MateConf/gsettings/mate-search-tool.convert
%{_datadir}/MateConf/gsettings/mate-system-log.convert
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet


%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict/


%files -n mate-system-log -f mate-system-log.lang
%doc COPYING
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/mate-utils/
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_datadir}/mate/help/mate-system-log/
%{_mandir}/man1/mate-system-log.1.*


%changelog
* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- new fc release

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
- restored libs subpackage

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_6
- new fc release

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

