# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums pkgconfig(gio-unix-2.0) pkgconfig(gmodule-2.0)
# END SourceDeps(oneline)
BuildRequires: chrpath
Summary:	Shared functions for Ayatana indicators
Name:		libindicator
Version:	0.4.94
Release:	alt1_2
License:	GPLv3
Group:		System/Libraries
URL:		https://launchpad.net/libindicator
Source0:	http://launchpad.net/libindicator/0.5/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libdbus-glib-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libgtk+3-devel
Source44: import.info

%description
A set of symbols and convenience functions that all Ayatana indicators
are likely to use.

%package	tools
Summary:	Tools for %{name}
Group:		System/Libraries

%description	tools
This package contains tools used by the %{name} package, the
Ayatana indicators system.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	gtk3
Summary:	GTK+3 build of %{name}
Group:		System/Libraries

%description	gtk3
A set of symbols and convenience functions that all Ayatana indicators
are likely to use. This is the GTK+ 3 build of %{name}, for use
by GTK+ 3 apps.

%package	gtk3-tools
Summary:	Tools for %{name}
Group:		System/Libraries

%description	gtk3-tools
This package contains tools used by the %{name}-gtk3 package, the
Ayatana indicators system. This package contains the builds of the
tools for the GTK+3 build of %{name}.

%package	gtk3-devel
Summary:	Development files for %{name}-gtk3
Group:		Development/C
Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}

%description	gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%prep
%setup -q

%build
# we build it twice, once against GTK+ 3 and once against GTK+ 2, so
# both GTK+ 2 and GTK+ 3 apps can use it; the GTK+ 3 build is
# libindicator-gtk3. When we have no need for the GTK+ 2 build any more
# we can drop the -gtk3 package and have the main package build against
# GTK+ 3.
%global _configure_script ../configure
rm -rf build-gtk3 build-gtk2
mkdir build-gtk3 build-gtk2
pushd build-gtk2
%configure --disable-static --with-gtk=2
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd
pushd build-gtk3
%configure --disable-static --with-gtk=3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
popd

%install
make -C build-gtk2 DESTDIR=%{buildroot} install
make -C build-gtk3 DESTDIR=%{buildroot} install
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

# this dummy indicator is fairly useless, it's not shipped in Ubuntu
rm -f %{buildroot}%{_libdir}/libdummy-indicator*.so
# kill rpath
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
	chrpath -d $i ||:
done
	    

%files
%doc COPYING
%{_libdir}/libindicator.so.*

%files	tools
%doc COPYING
%{_libexecdir}/indicator-loader

%files	devel
%doc COPYING
%{_includedir}/libindicator-0.4
%{_libdir}/libindicator.so
%{_libdir}/pkgconfig/indicator-0.4.pc
# Contains 80indicator-debugging
# This is marked as 'for development use only'
%{_datadir}/libindicator/

%files	gtk3
%doc COPYING
%{_libdir}/libindicator3.so.*

%files	gtk3-tools
%doc COPYING
%{_libexecdir}/indicator-loader3

%files	gtk3-devel
%doc COPYING
%{_includedir}/libindicator3-0.4
%{_libdir}/libindicator3.so
%{_libdir}/pkgconfig/indicator3-0.4.pc

%changelog
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.94-alt1_2
- new version

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.22-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.22-alt1_1
- initial import by fcimport

