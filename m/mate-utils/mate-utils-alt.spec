# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/mateconftool-2 /usr/bin/scrollkeeper-config gcc-c++ libICE-devel libSM-devel pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libgtop-2.0) pkgconfig(mateconf-2.0) pkgconfig(xext) zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define glib2_version 2.13.3
%define gtk2_version 2.10.0
%define desktop_file_utils_version 0.9
%define mate_doc_utils_version 1.0.0
%define libmate_version 1.1.2
%define libmateui_version 1.1.2
%define mate_desktop_version 1.1.0
%define mate_panel_version 1.1.0

Name:           mate-utils
Version:        1.4.0
Release:        alt1_1.1
Summary:        MATE utility programs

Group:          File tools
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:  mate-doc-utils >= %{mate_doc_utils_version}
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk2-devel >= %{gtk2_version}
BuildRequires:  mate-desktop-devel >= %{mate_desktop_version}
BuildRequires:  mate-panel-devel >= %{mate_panel_version}
BuildRequires:  libcanberra-devel
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
BuildRequires:  libgtop2-devel
BuildRequires:  e2fsprogs-devel libe2fs-devel
BuildRequires:  consolehelper
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  mate-common
BuildRequires:  automake autoconf libtool
BuildRequires:  scrollkeeper
BuildRequires:  mate-common

Requires(post): desktop-file-utils >= %{desktop_file_utils_version}
Requires(post): mate-conf >= 1.1.0
Requires(preun): mate-conf >= 1.1.0
Requires(pre): mate-conf >= 1.1.0
Requires(postun): desktop-file-utils >= %{desktop_file_utils_version}

# obsolete the standalone baobab package from Extras
Obsoletes: baobab < %{version}-%{release}
Provides: baobab = %{version}-%{release}

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screenshot tool and others.

%package devel
Summary: Development files for mate-utils
Group: Development/C
Requires:  mate-utils = %{version}-%{release}

%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package libs
Summary: mate-utils libraries
Group: Development/C

%description libs
This package contains libraries provided by mate-utils (such as libmatedict)

%package mate-system-log
Summary: A log file viewer for the MATE desktop
Group: File tools
Requires: mate-utils = %{version}-%{release}
Requires: consolehelper

%description mate-system-log
The mate-system-log package contains an application that lets you
view various system log files.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--disable-scrollkeeper \
	--enable-console-helper

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p mate-utils.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

# make mate-system-log use consolehelper until it starts using polkit
./mkinstalldirs $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
cat <<EOF >$RPM_BUILD_ROOT%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth      include      config-util
account      include      config-util
session      include      config-util
EOF

./mkinstalldirs $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps
cat <<EOF >$RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=/usr/sbin/mate-system-log
SESSION=true
FALLBACK=true
EOF

./mkinstalldirs $RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT%{_bindir}/mate-system-log $RPM_BUILD_ROOT%{_sbindir}
ln -s /usr/bin/consolehelper $RPM_BUILD_ROOT%{_bindir}/mate-system-log


# save space by linking identical images in translated docs
for n in baobab mate-dictionary mate-search-tool mate-system-log; do
  helpdir=$RPM_BUILD_ROOT%{_datadir}/mate/help/$n
  for f in $helpdir/C/figures/*.png; do
    for d in $helpdir/*; do
      if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
        g="$d/figures/$b"
        if [ -f "$g" ]; then
          if cmp -s $f $g; then
            rm "$g"; ln -s "../../C/figures/$b" "$g"
          fi
        fi
      fi
    done
  done
done


%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule \
   %{_sysconfdir}/mateconf/schemas/mate-dictionary.schemas \
   %{_sysconfdir}/mateconf/schemas/mate-search-tool.schemas \
   %{_sysconfdir}/mateconf/schemas/mate-screenshot.schemas \
   %{_sysconfdir}/mateonf/schemas/baobab.schemas \
      >& /dev/null || :
touch --no-create %{_datadir}/icons/mate >&/dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  for f in mate-dictionary.schemas mate-search-tool.schemas mate-screenshot.schemas baobab.schemas; do
    if [ -f %{_sysconfdir}/mateconf/schemas/$f ]; then
      mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/$f >& /dev/null || :
    fi
  done
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  for f in mate-dictionary.schemas mate-search-tool.schemas mate-screenshot.schemas baobab.schemas; do
    if [ -f %{_sysconfdir}/mateconf/schemas/$f ]; then
      mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/$f >& /dev/null || :
    fi
  done
fi

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate >&/dev/null || :
fi

%post mate-system-log
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule \
   %{_sysconfdir}/mateconf/schemas/mate-system-log.schemas \
      >& /dev/null || :

%pre mate-system-log
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mate-system-log.schemas >& /dev/null || :
fi

%preun mate-system-log
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mate-system-log.schemas >& /dev/null || :
fi


%files
%doc COPYING NEWS README
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README
%doc baobab/AUTHORS
%doc baobab/README
%{_sysconfdir}/mateconf/schemas/mate-dictionary.schemas
%{_sysconfdir}/mateconf/schemas/mate-screenshot.schemas
%{_sysconfdir}/mateconf/schemas/mate-search-tool.schemas
%{_sysconfdir}/mateconf/schemas/baobab.schemas
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
%{_libexecdir}/mate-dictionary-applet
%{_datadir}/mate-2.0/ui/MATE_DictionaryApplet.xml
%{_libdir}/matecomponent/servers/MATE_DictionaryApplet.server
%{_mandir}/man1/mate-dictionary.1*
%{_mandir}/man1/mate-search-tool.1*
%{_mandir}/man1/mate-screenshot.1*
%{_mandir}/man1/mate-disk-usage-analyzer.1*
%{_datadir}/icons/mate/
%{_datadir}/mate/help/
%{_datadir}/omf/
%_datadir/locale/*/*

%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict/

%files libs
%{_libdir}/libmatedict.so.*

%files mate-system-log
%{_bindir}/mate-system-log
%{_sbindir}/mate-system-log
%{_datadir}/mate-utils/
%{_sysconfdir}/mateconf/schemas/mate-system-log.schemas
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/applications/mate-system-log.desktop
%{_mandir}/man1/mate-system-log.1.*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

