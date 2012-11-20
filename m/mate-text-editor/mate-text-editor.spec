%filter_from_requires /^python....pluma./d
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/mateconftool-2 libICE-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtksourceview-2.0) pkgconfig(libsoup-2.4) pkgconfig(libxml-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
Summary:  Text editor for the MATE desktop
Name:     mate-text-editor
Version:  1.4.0
Release:  alt1_2
License:  GPLv2+
Group:    Editors
URL:      http://mate-desktop.org
Source0:  http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz


# mateconftool-2
Requires(pre):   mate-conf
Requires(post):  mate-conf
Requires(preun): mate-conf


BuildRequires: mate-common
BuildRequires: glib2-devel
BuildRequires: pango-devel
BuildRequires: gtk2-devel
BuildRequires: mate-conf-devel
BuildRequires: libSM-devel
BuildRequires: desktop-file-utils
BuildRequires: libenchant-devel
BuildRequires: iso-codes-devel
BuildRequires: libattr-devel
BuildRequires: libgail-devel
BuildRequires: libgtksourceview2-devel
BuildRequires: rarian-compat
BuildRequires: python-module-pygtk-devel
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-pygtksourceview-devel
BuildRequires: python-devel
BuildRequires: mate-doc-utils
BuildRequires: which
BuildRequires: /usr/bin/autopoint

Requires: pygtk2
Requires: python-module-pygobject
Requires: python-module-pygtksourceview
# the run-command plugin uses zenity
Requires: zenity
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
Requires: %{name} = %{version}-%{release}

%description devel
mate-text-editor is a small, but powerful text editor for the MATE desktop.
This package allows you to develop plugins that add new functionality
to mate-text-editor.

Install mate-text-editor-devel if you want to write plugins for mate-text-editor.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

# Fix debug permissions with messy hack 
find ./*/* -type f -exec chmod 644 {} \;
find ./*/*/* -type f -exec chmod 644 {} \;


%build
%configure \
        --disable-scrollkeeper \
        --disable-gtk-doc \
        --enable-python \
        --disable-schemas-install
make %{?_smp_mflags}

%install
export MATECONF_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_MAKEFILE_SCHEMA_INSTALLL

desktop-file-install --delete-original             \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

## clean up all the static libs for plugins
/bin/rm -f `find $RPM_BUILD_ROOT%{_libdir}/pluma/plugins -name "*.a"`
/bin/rm -f `find $RPM_BUILD_ROOT%{_libdir}/pluma/plugins -name "*.la"`
/bin/rm -f `find $RPM_BUILD_ROOT%{_libdir}/pluma/plugin-loaders -name "*.la"`


%find_lang pluma --with-gnome

%post
%mateconf_schema_upgrade pluma-file-browser pluma


%pre
%mateconf_schema_prepare pluma-file-browser pluma

%preun
%mateconf_schema_remove pluma-file-browser pluma

%files  -f pluma.lang
%doc README COPYING AUTHORS
%{_datadir}/pluma/
%{_datadir}/mate/help/pluma/
%{_datadir}/applications/pluma.desktop
%{_mandir}/man1/*
%{_libdir}/pluma/
%{_libexecdir}/pluma/
%{_bindir}/*
%{_sysconfdir}/mateconf/schemas/*


%files devel
%{_includedir}/pluma/
%{_libdir}/pkgconfig/pluma.pc



%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- added mate-desktop-1.5.0-alt-settings.patch - font settings

