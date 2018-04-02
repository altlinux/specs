# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major   0
%define libname libdlna%{major}
%define develname libdlna-devel

Summary: Implementation of DLNA (Digital Living Network Alliance)
Name: libdlna
Version: 0.2.4
Release: alt1_9
Source0: http://libdlna.geexbox.org/releases/%{name}-%{version}.tar.bz2
Patch0: libdlna-0.2.4-mga-ffmpeg-2.4.patch
# Patch from ArchLinux: https://git.archlinux.org/svntogit/community.git/tree/trunk?h=packages/libdlna
Patch1: libdlna-ffmpeg3.patch
License: LGPLv2+
Group: System/Libraries
Url: http://libdlna.geexbox.org/
BuildRequires: libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavresample-devel libavutil-devel libpostproc-devel libswresample-devel libswscale-devel
Source44: import.info

%description
libdlna aims at being the reference open-source implementation of DLNA
(Digital Living Network Alliance) standards.
Its primary goal is to provide DLNA support to uShare, an embedded DLNA &
UPnP A/V Media Server, but it will be used to build both DLNA servers
and players in the long term.

%package -n     %{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n     %{develname}
Summary:        Header files and static libraries from %name
Group:          Development/C
Requires:       %{libname} >= %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %name-devel < %{version}-%{release}
Obsoletes:	%{_lib}dlna0-devel

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

# No support for parallel make nor %%configure
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --enable-shared
make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*pc


%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_9
- new version

* Mon Jul 14 2008 Sir Raorn <raorn@altlinux.ru> 0.2.3-alt1
- initial build for ALT Linux
