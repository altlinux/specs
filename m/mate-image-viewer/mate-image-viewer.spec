Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dbus-binding-tool /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize libICE-devel libSM-devel libexif-devel libgio-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-unix-print-2.0) pkgconfig(shared-mime-info) pkgconfig(x11) python-devel python-module-pygobject-devel xorg-xproto-devel zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:          mate-image-viewer
Version:       1.5.0
Release:       alt1_3
Summary:       Eye of MATE image viewer

License:       GPLv2+ and LGPLv2+ 
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Patch0:        schema.patch

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(libart-2.0)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(mate-desktop-2.0)
BuildRequires: pkgconfig(lcms)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(mate-icon-theme)
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: libjpeg-devel
BuildRequires: intltool
BuildRequires: rarian-compat
BuildRequires: desktop-file-utils
BuildRequires: mate-common

Requires:      gsettings-desktop-schemas
Source44: import.info

%description
This is the Eye of MATE, an image viewer program.  It is meant to be
a fast and functional image viewer.

Eye of MATE is a fork of Eye of GNOME.

%package devel
Summary:  Support for developing plugins for the eom image viewer
Group:    Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
The Eye of MATE image viewer (eom) is the official image viewer for the
MATE desktop. This package allows you to develop plugins that add new
functionality to eog.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
   --disable-scrollkeeper \
   --disable-schemas-install 
           
make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor "" --delete-original \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/eom.desktop

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

%find_lang eom --with-gnome

# save space by linking identical images in translated docs
helpdir=$RPM_BUILD_ROOT%{_datadir}/mate/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
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


%files -f eom.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/eom
%{_libdir}/eom/plugins/
%{_datadir}/applications/eom.desktop
%{_datadir}/eom/
%{_datadir}/mate/help/eom/
%{_datadir}/icons/hicolor/*/apps/eom.*
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml

%files devel
%{_libdir}/pkgconfig/eom.pc
%{_includedir}/eom-2.20/

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- added mate-desktop-1.5.0-alt-settings.patch - font settings

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

