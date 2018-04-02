# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api 4
%define major 3
%define libname libmusicbrainz%{api}_%{major}
%define develname libmusicbrainz%{api}-devel

Name:		libmusicbrainz4
Version:	4.0.3
Release:	alt1_10
Summary:	A software library for accesing MusicBrainz servers
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/libmusicbrainz-%{version}.tar.gz
URL:		http://musicbrainz.org/doc/libmusicbrainz
Group:		System/Libraries
License:	LGPLv2+
BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(neon)
Source44: import.info

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %develname
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%develname
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%prep
%setup -qn libmusicbrainz-%{version}

%build

cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif

%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS.txt COPYING.txt NEWS.txt
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %develname
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc


%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt1_10
- new version

* Thu Oct 11 2012 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt2
- fixed includes

* Mon Jun 04 2012 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- first build for Sisyphus

