# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major   1
%define libname libtcod%{major}
%define devname libtcod-devel

%define date    20170226

Name:           libtcod
Version:        1.6.3
Release:        alt1_1
Summary:        Color console, input management and other tools for roguelike games
Group:          System/Libraries
License:        BSD
URL:            https://bitbucket.org/libtcod/libtcod
# https://bitbucket.org/libtcod/libtcod/downloads?tab=tags
Source0:        https://bitbucket.org/libtcod/libtcod/downloads/%{date}-%{name}-%{version}.tbz2
# TODO: Have upstream handle their soname properly
Patch0:         libtcod-1.6.1-mga-soname.patch

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Source44: import.info

%description
libtcod, a.k.a. "The Doryen Library", is a free, fast, portable and
uncomplicated API for roguelike developpers providing an advanced
true color console, input, and lots of other utilities frequently
used in roguelikes.

#----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Color console, input management and other tools for roguelike games
Group:          System/Libraries

%description -n %{libname}
libtcod, a.k.a. "The Doryen Library", is a free, fast, portable and
uncomplicated API for roguelike developpers providing an advanced
true color console, input, and lots of other utilities frequently
used in roguelikes.

%files -n       %{libname}
%{_libdir}/%{name}*.so.%{major}
%{_libdir}/%{name}*.so.%{major}.*

#----------------------------------------------------------------------

%package -n     %{devname}
Summary:        Development headers for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development headers and libraries for %{name}.

%files -n       %{devname}
%doc libtcod-CHANGELOG.txt LIBTCOD-CREDITS.txt LIBTCOD-LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------

%prep
%setup -q -n %{date}-%{name}-%{version}
%patch0 -p1
rm -rf src/zlib

%build
cd build/autotools
autoreconf -vfi
%configure
%make_build

%install
cd build/autotools
%makeinstall_std

find %{buildroot}%{_libdir} -name "*.la" -delete -o -name "*.a" -delete

# pkg-config entry
install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${exec_prefix}/include
libdir=\${exec_prefix}/%{_lib}

Name: %{name}
Description: Color console, input management and other tools for roguelike games
Version: %{version}
Libs: -L\${libdir} -ltcod
Libs.private: -lz -lSDL
Cflags: -I\${includedir}/%{name}
EOF


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_1
- new version

