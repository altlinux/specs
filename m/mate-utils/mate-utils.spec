BuildRequires: chrpath
Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize gcc-c++ libICE-devel libSM-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libgtop-2.0) pkgconfig(xext) zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-utils
Version:        1.8.0
Release:        alt2_1
Summary:        MATE utility programs

License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  e2fsprogs-devel
BuildRequires:  hardlink
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-panel-devel
BuildRequires:  libGL-devel
BuildRequires:  popt-devel
BuildRequires:  consolehelper
BuildRequires:  yelp-tools

Requires: mate-dictionary = %{version}-%{release}
Requires: mate-screenshot = %{version}-%{release}
Requires: mate-search-tool = %{version}-%{release}
Requires: mate-system-log = %{version}-%{release}
Requires: mate-disk-usage-analyzer = %{version}-%{release}
Source44: import.info
Obsoletes: Obsoletes: mate-utils-libs < 1.5.0-alt2_1
Conflicts: mate-utils-libs < 1.5.0-alt2_1
Obsoletes: Obsoletes: mate-utils-libs < 1.5.0-alt2_1
Conflicts: mate-utils-libs < 1.5.0-alt2_1

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

%package common
Group: File tools
Summary: Common files for %{name}
BuildArch: noarch
%description common
%{summary}.

%package devel
Group: Development/C
Summary: Development files for mate-utils
# short-lived mate-dictionary-devel subpkg
Obsoletes: mate-dictionary-devel < 1.6.0-8
#Provides:  mate-dictionary-devel = %{version}-%{release}
Requires:  mate-dictionary%{?_isa} = %{version}-%{release}
%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package -n mate-system-log
Group: File tools
Summary: A log file viewer for the MATE desktop
Requires: %{name}-common = %{version}-%{release}
Requires: consolehelper
# rhbz (#1016935)
Requires: libmate-desktop
%description -n mate-system-log
An application that lets you view various system log files.

%package -n mate-screenshot
Group: File tools
Summary: A utility to take a screen-shot of the desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

%package -n mate-dictionary
Group: File tools
Summary: A dictionary for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop.

%package -n mate-search-tool
Group: File tools
Summary: A file searching tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
Requires: libmate-desktop
%description -n mate-search-tool
An application to search for files on your computer.

%package -n mate-disk-usage-analyzer
Group: File tools
Summary: A disk usage analyzing tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-usage-analyzer
An application to help analyze disk usage.

%prep
%setup -q

%build
%configure \
    --disable-static            \
    --disable-schemas-compile   \
    --enable-gdict-applet       \
    --enable-gtk-doc-html       \
    --enable-ipv6=yes           \
    --enable-maintainer-flags=no  \
    --with-gtk=2.0              \
    --with-x

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

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

rm -fv %{buildroot}%{_libdir}/*.la
rm -fv %{buildroot}%{_datadir}/MateConf/gsettings/*.convert

desktop-file-install                          \
  --delete-original                           \
  --dir %{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome --all-name
%find_lang mate-disk-usage-analyzer --with-gnome --all-name
%find_lang mate-dictionary --with-gnome --all-name
%find_lang mate-search-tool --with-gnome --all-name
%find_lang mate-system-log --with-gnome --all-name
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%files
# empty

%files common -f %{name}.lang
%doc COPYING COPYING.libs
%doc NEWS README

%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict/
%{_datadir}/gtk-doc/html/mate-dict/

%files -n mate-system-log -f mate-system-log.lang
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/mate-utils/
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_mandir}/man1/mate-system-log.1*

%files -n mate-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-panel-screenshot
%{_datadir}/applications/mate-screenshot.desktop
%{_datadir}/mate-screenshot
%{_mandir}/man1/mate-screenshot.1*
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml

%files -n mate-dictionary -f mate-dictionary.lang
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README
%{_bindir}/mate-dictionary
%{_datadir}/applications/mate-dictionary.desktop
%{_datadir}/mate-dict/
%{_datadir}/mate-dictionary/
%{_libexecdir}/mate-dictionary-applet
%{_libdir}/libmatedict.so.*
%{_mandir}/man1/mate-dictionary.1*
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service

%files -n mate-search-tool -f mate-search-tool.lang
%{_bindir}/mate-search-tool
%{_datadir}/applications/mate-search-tool.desktop
%{_mandir}/man1/mate-search-tool.1*
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/pixmaps/mate-search-tool/

%files -n mate-disk-usage-analyzer -f mate-disk-usage-analyzer.lang
%doc baobab/AUTHORS
%doc baobab/README
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_datadir}/mate-disk-usage-analyzer
%{_mandir}/man1/mate-disk-usage-analyzer.1*
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/mate-disk-usage-analyzer.*


%changelog
* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with libgtop

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_7
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_6
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

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

