# BEGIN SourceDeps(oneline):
BuildRequires: libSDL-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
BuildRequires: gcc-c++
%add_optflags %optflags_shared
Name:           libmodelfile
Version:        0.1.92
Release:        alt3_9
Summary:        Library for accessing various model file formats

Group:          Development/C
License:        zlib
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz

BuildRequires:  libSDL_image-devel libGL-devel libGLU-devel
Source44: import.info

%description
This library is a collection of small clean C libraries for loading 3D
models of various file formats. So far the range of model formats is limited.


%package        devel
Summary:        Development files for libmodelfile
Group:          Development/C
Requires:       libmodelfile = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications
that use libmodelfile.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# kill rpath
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
	chrpath -d $i ||:
done
	    


%check
make %{?_smp_mflags} check

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}-0.2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.92-alt3_9
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.92-alt2_9
- update to new release by fcimport

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.92-alt2_8
- fixed build after mass spec cleanup

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.92-alt1_8
- initial release by fcimport

