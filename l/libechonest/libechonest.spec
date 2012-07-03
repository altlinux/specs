# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/valgrind cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libfreetype-devel libreadline-devel libuuid-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) python-devel unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libechonest
Version:	1.2.1
Release:	alt2_2
Summary:	C++ wrapper for the Echo Nest API

Group:		System/Libraries
License:	GPLv2+
URL:		https://projects.kde.org/projects/playground/libs/libechonest
Source0:	http://pwsp.cleinias.com/%{name}-%{version}.tar.bz2

BuildRequires:	ctest cmake
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	qjson-devel

## upstream patches
# fix reported version
Patch100: libechonest-1.2.1-version.patch
Source44: import.info


%description
libechonest is a collection of C++/Qt classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%patch100 -p1 -b .version


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libechonest)" = "%{version}"
# The tests need active internet connection, which is not available
# in koji builds
#make test -C %%{_target_platform}

%files
%doc AUTHORS COPYING README TODO
%{_libdir}/libechonest.so.1*

%files devel
%{_includedir}/echonest/
%{_libdir}/libechonest.so
%{_libdir}/pkgconfig/libechonest.pc


%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- initial import by fcimport

