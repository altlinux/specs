BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
# guessed from configure.ac
BuildRequires: pkgconfig(minizip)
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

%global vday 02
%global vmonth 12
%global vyear 2004
%global name1 zfstream

Name:           mingw32-%{name1}
Version:        %{vyear}%{vmonth}%{vday}
Release:        alt1_9
Summary:        MinGW Windows abstraction API for reading and writing compressed files

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.wanderinghorse.net/computing/%{name1}/
Source0:        http://www.wanderinghorse.net/computing/%{name1}/libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday}.tar.gz
# I tried half a day to get the rather peculiar original build system working,
# but I failed, so I decided to simply replace it by autotools.
# This has the further advantage that it knows how to cross-compile.
Source1:        %{name1}-autotools.tar.gz
# The patch has been sent via private mail to the author. The author responded
# that the patch had been integrated into his personal tree, but apparently
# he has not gotten around to release a new version.
Patch1:         %{name1}-zip.patch

BuildArch:      noarch

BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-minizip
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc-c++
Source44: import.info

%description
MinGW zfstream C++ compressed I/O abstraction library




%prep
%setup -q -n libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday} -a 1
%patch1 -p0 -b .zip
touch NEWS README AUTHORS
aclocal
autoconf
autoheader
libtoolize -f
automake -a -c

%build
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc LICENSE
%{_mingw32_bindir}/libzfstream-0.dll
%{_mingw32_includedir}/*
%{_mingw32_libdir}/libzfstream.dll.a
%{_mingw32_libdir}/libzfstream.la
%{_mingw32_libdir}/pkgconfig/zfstream.pc

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 20041202-alt1_9
- initial release by fcimport

