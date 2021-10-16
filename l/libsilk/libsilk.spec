%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 0
%define libname libsilk%{major}
%define libnamedev libsilk-devel

Summary:    	libsilk is a library for the silk codec
Name:       	libsilk
Version:    	1.0.8
Release:    	alt1_5
License:    	Skype BSD-like 
Group:      	System/Libraries
URL:        	http://stash.freeswitch.org
Source:     	libsilk-1.0.8.tar.gz
BuildRequires: 	automake
BuildRequires: 	libtool

Source44: import.info

%description
libsilk is a library for the silk codec

%package	-n %{libname}
Summary:    	Silk development files
Group:      	System/Libraries
Conflicts: libsilk < 1.0.8-alt1_5

%description 	-n %{libname}
silk codec libraries.


%package	-n %{libnamedev}
Summary:    	Silk development files
Group:      	Development/C
Requires:   	%{libname} = %{version}

%description 	-n %{libnamedev}
silk development files.

%package -n     %{libnamedev}-static
Summary:        Static library for the %{name} library
Group:          Development/C
Requires:       %{libnamedev} = %EVR

%description -n %{libnamedev}-static
This package contains the static %{name} library

%files -n %{libnamedev}-static
%{_libdir}/*.a


%prep
%setup -q

%build
./bootstrap.sh
%configure
%make_build

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.la

%files 	-n %{libname}
%doc ChangeLog AUTHORS COPYING NEWS README 

%{_libdir}/libSKP_SILK_SDK.so.0
%{_libdir}/libSKP_SILK_SDK.so.0.*

%files
%doc ChangeLog AUTHORS COPYING NEWS README 
%{_bindir}/Decoder
%{_bindir}/Encoder
%{_bindir}/signalCompare

%files 	-n %{libnamedev}
%{_includedir}/silk
%{_libdir}/libSKP_SILK_SDK.so
%{_libdir}/pkgconfig/silk.pc



%changelog
* Sat Oct 16 2021 Igor Vlasenko <viy@altlinux.org> 1.0.8-alt1_5
- picked up

* Wed Mar 02 2016 Anton Farygin <rider@altlinux.ru> 1.0.8-alt1
- first build for Sisyphus
