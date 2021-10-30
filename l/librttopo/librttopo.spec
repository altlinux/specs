Name:           librttopo
Version:        1.1.0
Release:        alt1
Summary:        Create and manage SQL/MM topologies
Group:		System/Libraries
License:        GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source0:        https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libgeos-devel
BuildRequires:  libtool
BuildRequires:  make


%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores.


%package        devel
Summary:        Development files for %{name}
Group: System/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -n %name

%build
autoreconf -ifv
%configure --disable-static
%make_build


%install
#make_install
%makeinstall_std

%files

%doc CREDITS NEWS.md README.md TODO COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_geom.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rttopo.pc


%changelog
* Sat Oct 30 2021 Ilya Mashkin <oddity@altlinux.ru> 1.1.0-alt1
- Build for Sisyphus

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-5
- Rebuild (geos)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-3
- Rebuild (geos)

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> 1.1.0-1
- Initial package
