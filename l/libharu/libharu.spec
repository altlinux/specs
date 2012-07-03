# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ gcc-fortran python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libharu
Version:        2.1.0
Release:        alt2_3
Summary:        C library for generating PDF files

Group:          System/Libraries
License:        zlib with acknowledgement
URL:            http://libharu.org
Source0:        http://libharu.org/files/%{name}-%{version}.tar.gz

BuildRequires: glibc-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
Source44: import.info

%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-debug
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc README CHANGES 
%{_libdir}/libhpdf-%{version}.so

%files devel
%doc doc demo
%{_includedir}/*
%{_libdir}/libhpdf.so



%changelog
* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_3
- spec cleanup thanks to ldv@

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3
- converted by srpmconvert script

