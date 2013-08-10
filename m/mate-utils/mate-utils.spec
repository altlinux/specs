Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/scrollkeeper-config gcc-c++ libICE-devel libSM-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libgtop-2.0) pkgconfig(xext) zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-utils
Version:        1.6.0
Release:        alt1_6
Summary:        MATE utility programs

License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

# upstream patch
# https://github.com/mate-desktop/mate-utils/commit/a59fda7d006b856ac5982750f2ffdefd24191be0
# fix rhbz #975199
Patch0:         mate-utils_fix-save-path-selection_screenshot.patch

BuildRequires:  desktop-file-utils
BuildRequires: e2fsprogs-devel libe2fs-devel
BuildRequires:  hardlink
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-doc-utils
BuildRequires:  mate-panel-devel
BuildRequires:  libGL-devel
BuildRequires:  popt-devel
BuildRequires:  rarian-compat
BuildRequires:  consolehelper
Source44: import.info
Obsoletes: Obsoletes: mate-utils-libs < 1.5.0-alt2_1
Conflicts: mate-utils-libs < 1.5.0-alt2_1

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

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
An application that lets you view various system log files.

%package -n mate-screenshot
Group: File tools
Summary: A utility to take a screen-shot of the desktop
Requires: consolehelper
%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

%package -n mate-dictionary
Group: File tools
Summary: A dictionary for MATE Desktop
Requires: consolehelper
%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop.

%package -n mate-dictionary-devel
Group: File tools
Summary: Development files for mate-utils
Requires:  mate-dictionary%{?_isa} = %{version}-%{release}
%description -n mate-dictionary-devel
The mate-dictionary-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-dictionary.

%package -n mate-search-tool
Group: File tools
Summary: A file searching tool for MATE Desktop
%description -n mate-search-tool
An application to search for files on your computer.

%package -n mate-disk-usage-analyzer
Group: File tools
Summary: A disk usage analyzing tool for MATE Desktop
%description -n mate-disk-usage-analyzer
An application to help analyze disk usage.

%prep
%setup -q
%patch0 -p1 -b .save-path-selection
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
    --disable-static            \
    --disable-scrollkeeper      \
    --disable-schemas-compile   \
    --enable-gdict-applet       \
    --enable-gtk-doc-html       \
    --enable-ipv6=yes           \
    --disable-schemas-compile   \
    --with-x

make %{?_smp_mflags} V=1

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
rm -fv $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/*.convert

desktop-file-install                          \
  --remove-category="MATE"                    \
  --add-category="X-Mate"                     \
  --delete-original                           \
  --dir %{buildroot}%{_datadir}/applications  \
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
%{_datadir}/mate-dict
%{_datadir}/mate-dictionary
%{_datadir}/mate-screenshot
%{_datadir}/mate-disk-usage-analyzer
%{_datadir}/pixmaps/mate-search-tool
%{_libdir}/libmatedict.so.*
%{_libexecdir}/mate-dictionary-applet
%{_mandir}/man1/mate-dictionary.1*
%{_mandir}/man1/mate-search-tool.1*
%{_mandir}/man1/mate-screenshot.1*
%{_mandir}/man1/mate-disk-usage-analyzer.1*
%{_datadir}/mate/help/mate-dictionary
%{_datadir}/mate/help/mate-disk-usage-analyzer
%{_datadir}/mate/help/mate-search-tool
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%{_datadir}/icons/mate/*/apps/baobab.*


%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict


%files -n mate-system-log -f mate-system-log.lang
%doc COPYING
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/mate-utils/
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_datadir}/mate/help/mate-system-log
%{_mandir}/man1/mate-system-log.1.*

%files -n mate-screenshot -f %{name}.lang
%doc COPYING
%{_bindir}/mate-screenshot
%{_bindir}/mate-panel-screenshot
%{_datadir}/applications/mate-screenshot.desktop
%{_datadir}/mate-screenshot
%{_mandir}/man1/mate-screenshot.1.*
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml

%files -n mate-dictionary -f mate-dictionary.lang
%doc COPYING
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README
%{_bindir}/mate-dictionary
%{_datadir}/mate-dict
%{_datadir}/mate-dictionary
%{_libexecdir}/mate-dictionary-applet
%{_libdir}/libmatedict.so.*
%{_mandir}/man1/mate-dictionary.1.*
%{_datadir}/mate/help/mate-dictionary
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service

%files -n mate-dictionary-devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict

%files -n mate-search-tool -f mate-search-tool.lang
%doc COPYING
%{_bindir}/mate-search-tool
%{_datadir}/applications/mate-search-tool.desktop
%{_mandir}/man1/mate-search-tool.1.*
%{_datadir}/mate/help/mate-search-tool
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml

%files -n mate-disk-usage-analyzer -f mate-disk-usage-analyzer.lang
%doc COPYING
%doc baobab/AUTHORS
%doc baobab/README
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_datadir}/mate-disk-usage-analyzer
%{_mandir}/man1/mate-disk-usage-analyzer.1.*
%{_datadir}/mate/help/mate-disk-usage-analyzer
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/icons/mate/*/apps/baobab.*


%changelog
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

