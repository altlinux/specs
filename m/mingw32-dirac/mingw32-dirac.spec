BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-dirac
Version:        1.0.2
Release:        alt1_4
Summary:        Dirac is an open source video codec

Group:          System/Libraries
License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://dirac.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dirac/dirac-%{version}.tar.gz
Patch0:         dirac-1.0.2-mingw32-gcc44.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn
Source44: import.info

%description
MinGW Windows dirac compression library.


%prep
%setup -q -n dirac-%{version}
%patch0 -p1 -b .gcc44
rm util/conversion/common/setstdiomode.cpp
touch util/conversion/common/setstdiomode.cpp

%build
%_mingw32_configure \
  --program-prefix=dirac_ \
  --program-transform-name=s,dirac_dirac_,dirac_, \
  --enable-overlay \
  --disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%exclude %{_mingw32_bindir}/dirac_create_dirac_testfile.pl            
%{_mingw32_bindir}/dirac_*.exe                        
%{_mingw32_includedir}/dirac/
%{_mingw32_bindir}/libdirac_decoder-0.dll
%{_mingw32_bindir}/libdirac_encoder-0.dll
%{_mingw32_libdir}/pkgconfig/dirac.pc
%{_mingw32_libdir}/libdirac_decoder.dll.a
%{_mingw32_libdir}/libdirac_decoder.la
%{_mingw32_libdir}/libdirac_encoder.dll.a
%{_mingw32_libdir}/libdirac_encoder.la

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4
- initial release by fcimport

