BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

%global nativename libzip

Name:           mingw32-%{nativename}
Version:        0.9
Release:        alt1_3
Summary:        C library for reading, creating, and modifying zip archives

Group:          System/Libraries
License:        BSD
URL:            http://www.nih.at/libzip/index.html
Source0:        http://www.nih.at/libzip/%{nativename}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  libtool
BuildRequires:  mingw32-filesystem >= 35
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib >= 1.1.2
Source44: import.info

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from 
other zip archives. Changes made without closing the archive can be reverted. 
The API is documented by man pages.

%prep
%setup -q -n %{nativename}-%{version}

%build
%{_mingw32_configure} --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

#Remove files we don't need
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -R $RPM_BUILD_ROOT%{_mingw32_datadir}/*

%files
%doc AUTHORS NEWS README THANKS TODO
%{_mingw32_bindir}/zipcmp.exe
%{_mingw32_bindir}/zipmerge.exe
%{_mingw32_bindir}/ziptorrent.exe
%{_mingw32_bindir}/*.dll
%{_mingw32_libdir}/libzip.dll.a
%{_mingw32_libdir}/pkgconfig/libzip.pc
%{_mingw32_includedir}/*.h

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- initial release by fcimport

