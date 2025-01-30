%define _unpackaged_files_terminate_build 1

%define abiversion 5
%define libffms libffms2_%abiversion

Name: ffms2
Version: 5.0
Release: alt1

Summary: Wrapper library around libffmpeg
License: MIT
Group: System/Libraries
Url: https://github.com/FFMS/ffms2/
VCS: https://github.com/FFMS/ffms2.git

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libavcodec-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libpostproc-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libtool
BuildRequires: zlib-devel

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

#---------------------------------------------------------------------------

%package -n %libffms
Summary: Library for %name
Group: System/Libraries

%description -n %libffms
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

#---------------------------------------------------------------------------

%package -n libffms2-devel
Summary: Development package for %name
Group: Development/C++

%description -n libffms2-devel
Header files for development with %name.

#---------------------------------------------------------------------------
%prep
%setup

sed -i 's/\r$//' COPYING

# make autoreconf happy
mkdir -p src/config

%build
autoreconf -fi
%configure \
  --disable-static \
  --docdir=%_docdir/lib%name-devel \
  --enable-shared \
  #
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_bindir/ffmsindex

%files -n %libffms
%_libdir/libffms2.so.%{abiversion}*

%files -n libffms2-devel
%_docdir/libffms2-devel
%_includedir/ffms*.h
%_libdir/libffms2.so
%_libdir/pkgconfig/ffms2.pc

%changelog
* Thu Jan 30 2025 Constantin Sunzow <protvin@altlinux.org> 5.0-alt1
- New version.

* Wed May 11 2022 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1_0.0.git20211209.1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_5
- new version
