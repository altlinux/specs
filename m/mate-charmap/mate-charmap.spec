# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/mateconftool-2 pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pygtk-2.0) python-devel
# END SourceDeps(oneline)
BuildRequires: libgtk+2-gir-devel
%define _libexecdir %_prefix/libexec
%define glib2_version 2.3.0
%define desktop_file_utils_version 0.9

Name:           mate-charmap
Version:        1.1.0
Release:        alt1_1.1
Summary:        Unicode character picker and font browser

Group:          File tools
License:        GPLv3+ and GFDL and MIT
				# GPL for the source code, GFDL for the docs, MIT for Unicode data
URL:           	https://github.com/gfunkmonk2
Source:         %{name}-%{version}.tar.gz

BuildRequires: 	mate-doc-utils >= 1.0.0
BuildRequires: 	glib2-devel >= %{glib2_version}
BuildRequires: 	gobject-introspection-devel
BuildRequires: 	mate-conf-devel
BuildRequires: 	desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: 	scrollkeeper
BuildRequires: 	gettext
BuildRequires: 	intltool
BuildRequires: 	mate-common
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  libcairo-gobject-devel

Requires(post): desktop-file-utils >= %{desktop_file_utils_version}
Requires(postun): desktop-file-utils >= %{desktop_file_utils_version}

Provides: mate-charmap = %{version}-%{release}
Obsoletes: mate-character-map
Source44: import.info

%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package devel
Summary: Libraries and headers for libmcharmap
Group: Development/C
Requires: mate-charmap = %{version}-%{release}
Provides: mate-charmap-devel = %{version}-%{release}
Obsoletes: mate-character-map-devel

%description devel
The mcharmap-devel package contains header files and other resources
needed to use the mcharmap library.

%prep
%setup -q -n  %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--with-gtk=2.0 \
	--disable-scrollkeeper \
	--enable-introspection

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT RUN_QUERY_IMMODULES_TEST=false

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

sed -i -e "s#Icon=mcharmap.png#Icon=/usr/share/icons/hicolor/48x48/apps/mcharmap.png#" \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-charmap.desktop


%find_lang mcharmap --all-name


%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/mcharmap.schemas \
	> /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mcharmap.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/mcharmap.schemas \
	> /dev/null || :
fi

%files -f mcharmap.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mcharmap
%{_libdir}/libmcharmap.so.*
%{_datadir}/applications/mate-charmap.desktop
%{_sysconfdir}/mateconf/schemas/mcharmap.schemas
%{_libdir}/girepository-1.0
%{_datadir}/mate/help/mcharmap/*
%{_datadir}/omf/mcharmap/*

%files devel
%{_includedir}/mcharmap-2.0
%{_libdir}/libmcharmap.so
%{_libdir}/pkmateconfig/mcharmap-2.pc
%{_datadir}/gir-1.0


%changelog
* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new release

