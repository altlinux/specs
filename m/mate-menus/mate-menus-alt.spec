# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: pkgconfig(gio-2.0)
# END SourceDeps(oneline)
Requires: altlinux-freedesktop-menu-mate
%define _libexecdir %_prefix/libexec
%global enable_debugging 0

Summary:  		A menu system for the MATE project
Name: 			mate-menus
Version: 		1.4.0
Release: 		alt2_1.1.1
License: 		LGPLv2+
Group: 			System/Libraries
URL: 			http://pub.mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
				# Keep release notes from showing up in Applications>Other
Patch0: 		other-docs.patch

Requires:  		altlinux-freedesktop-menu-common
BuildRequires: 	gamin-devel
BuildRequires: 	gawk
BuildRequires: 	gettext
BuildRequires: 	glib2-devel
BuildRequires: 	python-devel
 
BuildRequires: 	intltool
BuildRequires: 	mate-common
BuildRequires:  gobject-introspection-devel
Patch33: gnome-menus-2.14-alt-add-config-dir.patch
Patch34: gnome-menus-alt-applications-menu-no-legacy-kde.patch

%description
mate-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the MATE menu layout configuration files,
.directory files and assorted menu related utility programs,
Python bindings, and a simple menu editor.

%package devel
Summary: Libraries and include files for the MATE menu system
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for
writing applications that use the MATE menu system.

%prep
%setup -q
%patch0 -p1 -b .other-docs

NOCONFIGURE=1 ./autogen.sh
%patch33 -p0
%patch34 -p1

%build

%configure \
	--disable-static \
	--enable-python \
	--enable-introspection=yes \
	%if %{enable_debugging}
	--enable-debug=yes
	%else
	--enable-debug=no
	%endif

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS COPYING.LIB
%{_libdir}/libmate-menu.so.*
%{python_sitelibdir}/matemenu.so
%{_datadir}/mate/desktop-directories/*.directory
#%{_sysconfdir}/xdg/menus/*.menu
%{_datadir}/mate-menus/examples/mate-menus-ls.*
%{_libdir}/girepository-1.0/MateMenu-2.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/mate-menus
%{_datadir}/gir-1.0/MateMenu-2.0.gir


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

