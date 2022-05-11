# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ffms2
#
# git clone https://github.com/FFMS/ffms2.git
# cd ffms2
# DATE=$(git log -1 --format="%cd" --date=short | sed "s|-||g")
# git config tar.tar.xz.command "xz -c"
# git archive --format=tar.xz -o ffms2-${DATE}.tar.xz --prefix=ffms2-${DATE}/ master
#
%define gitdate		20211209
%define rel		1

%define major		5
%define libname		lib%{name}_%{major}
%define develname	lib%{name}-devel

Name:		ffms2
Version:	3.0.1
Release:	alt1_0.0.git20211209.1
Summary:	Wrapper library around libffmpeg
License:	MIT
Group:		System/Libraries
URL:		https://github.com/FFMS/ffms2/
Source0:	https://github.com/FFMS/%{name}/archive/%{version}/%{name}-%{?gitdate}%{!?gitdate:%version}.tar.%{?gitdate:xz}%{!?gitdate:gz}

BuildRequires:	libtool
BuildRequires:	libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavutil-devel libpostproc-devel libswresample-devel libswscale-devel
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
%setup -q -n %{name}-%{?gitdate}%{!?gitdate:%version}


sed -i 's/\r$//' COPYING

# make autoreconf happy
mkdir -p src/config

%build
autoreconf -fi
%configure \
	--docdir=%{_docdir}/lib%{name}-devel \
	--enable-shared \
	--disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

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
* Wed May 11 2022 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1_0.0.git20211209.1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_5
- new version

