BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ffms2
%define major		4
%define libname		lib%{name}_%{major}
%define develname	lib%{name}-devel

Name:		ffms2
Version:	2.23
Release:	alt1_5
Summary:	Wrapper library around libffmpeg
License:	MIT
Group:		System/Libraries
URL:		https://github.com/FFMS/ffms2/
Source0:	https://github.com/FFMS/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	libtool
BuildRequires:	libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavresample-devel libavutil-devel libpostproc-devel libswresample-devel libswscale-devel
BuildRequires:	pkgconfig(zlib)
Source44: import.info

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

#---------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

#---------------------------------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

#---------------------------------------------------------------------------
%prep
%setup -q

sed -i 's/\r$//' COPYING

%build
%configure \
		--docdir=%{_docdir}/lib%{name}-devel \
		--enable-shared \
		--disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files
%doc COPYING
%{_bindir}/ffmsindex

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%{_includedir}/ffms*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_docdir}/lib%{name}-devel


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_5
- new version

