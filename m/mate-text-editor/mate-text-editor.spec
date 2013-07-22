# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize libICE-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(libxml-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
%add_python_req_skip pluma
%define _libexecdir %_prefix/libexec
Summary:  Text editor for the MATE desktop
Name:     mate-text-editor
Version:  1.6.0
Release:  alt1_2
License:  GPLv2+
Group:    Editors
URL:      http://mate-desktop.org
Source0:  http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz


BuildRequires: desktop-file-utils
BuildRequires: libenchant-devel
BuildRequires: libsoup-devel
BuildRequires: gtk2-devel
BuildRequires: libgtksourceview-devel
BuildRequires: iso-codes-devel
BuildRequires: libSM-devel
BuildRequires: mate-common
BuildRequires: mate-doc-utils
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-pygtk-devel
BuildRequires: python-module-pygtksourceview-devel
BuildRequires: python-devel
BuildRequires: rarian-compat

Requires: pygtk2
Requires: mate-desktop
# the run-command plugin uses mate-dialogs
Requires: mate-dialogs
Source44: import.info

%description
mate-text-editor is a small, but powerful text editor designed specifically for
the MATE desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

mate-text-editor is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels.

%package devel
Summary: Support for developing plugins for the mate-text-editor text editor
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-text-editor

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;


%build
%configure \
        --disable-static          \
        --disable-scrollkeeper    \
        --enable-gtk-doc-html     \
        --enable-gvfs-metadata    \
        --enable-python           \
        --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install

desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/*.desktop

## clean up all the static libs for plugins
/bin/rm -f `find %{buildroot}%{_libdir}/pluma/plugins -name "*.a"`
/bin/rm -f `find %{buildroot}%{_libdir}/pluma/plugins -name "*.la"`
/bin/rm -f `find %{buildroot}%{_libdir}/pluma/plugin-loaders -name "*.la"`

# remove needless gsettings convert file to avoid slow session start
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/pluma.convert


%find_lang pluma --with-gnome
%files  -f pluma.lang
%doc README COPYING AUTHORS
%{_datadir}/pluma
%{_datadir}/mate/help/pluma
%{_datadir}/applications/pluma.desktop
%{_mandir}/man1/*
%{_libdir}/pluma
%{_libexecdir}/pluma
%{_bindir}/pluma
%{_bindir}/mate-text-editor
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml

%files devel
%{_includedir}/pluma
%{_libdir}/pkgconfig/pluma.pc



%changelog
* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
dropped obsolete mate-conf BR:

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- added mate-desktop-1.5.0-alt-settings.patch - font settings

