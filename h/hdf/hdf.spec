# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/diff /usr/bin/makeinfo /usr/bin/neqn /usr/bin/tbl gcc-c++ libsz2-devel libtirpc-devel
# END SourceDeps(oneline)
Name: hdf
Version: 4.2.10
Release: alt2
Summary: A general purpose library and file format for storing scientific data
License: BSD
Group: System/Libraries
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL: http://hdfgroup.org/products/hdf4/index.html
Source0: ftp://ftp.hdfgroup.org/HDF/HDF_Current/src/%{name}-%{version}.tar.bz2
Patch0: hdf-4.2.5-maxavailfiles.patch
Patch1: hdf-ppc.patch
Patch2: hdf-4.2.4-sparc.patch
Patch3: hdf-s390.patch
Patch4: hdf-arm.patch
# Support DESTDIR in install-examples
Patch5: hdf-destdir.patch
# Install examples into the right location
Patch6: hdf-examplesdir.patch
# Fix build with -Werror=format-security
# https://bugzilla.redhat.com/show_bug.cgi?id=1037120
Patch7: hdf-format.patch
# For destdir/examplesdir patches
BuildRequires: automake libtool
BuildRequires: flex bison libjpeg-devel zlib-devel
%if "%{?dist}" != ".el4"
BuildRequires: gcc-fortran
%else
BuildRequires: gcc-g77
%endif
Source44: import.info


%description
HDF is a general purpose library and file format for storing scientific data.
HDF can store two primary objects: datasets and groups. A dataset is 
essentially a multidimensional array of data elements, and a group is a 
structure for organizing objects in an HDF file. Using these two basic 
objects, one can create and store almost any kind of scientific data 
structure, such as images, arrays of vectors, and structured and unstructured 
grids. You can also mix and match them in HDF files according to your needs.


%package devel
Summary: HDF development files
Group: Development/C
Provides: %{name}-static = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description devel
HDF development headers and libraries.


%prep
%setup -q
%patch0 -p1 -b .maxavailfiles
%patch1 -p1 -b .ppc
%patch2 -p1 -b .sparc
%patch3 -p1 -b .s390
%patch4 -p1 -b .arm
%patch5 -p1 -b .destdir
%patch6 -p1 -b .examplesdir
%patch7 -p1 -b .format
# For destdir/examplesdir patches
autoreconf -i

chmod a-x *hdf/*/*.c hdf/*/*.h
# restore include file timestamps modified by patching
touch -c -r ./hdf/src/hdfi.h.ppc ./hdf/src/hdfi.h


%build
# avoid upstream compiler flags settings
rm config/*linux-gnu
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export FFLAGS="$RPM_OPT_FLAGS -fPIC -ffixed-line-length-none"
%configure --disable-production --disable-netcdf \
 --includedir=%{_includedir}/%{name} --libdir=%{_libdir}/%{name}

make
# correct the timestamps based on files used to generate the header files
touch -c -r hdf/src/hdf.inc hdf/src/hdf.f90
touch -c -r hdf/src/dffunc.inc hdf/src/dffunc.f90
touch -c -r mfhdf/fortran/mffunc.inc mfhdf/fortran/mffunc.f90
# netcdf fortran include need same treatement, but they are not shipped


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
#Don't conflict with netcdf
#rm $RPM_BUILD_ROOT%{_bindir}/nc* $RPM_BUILD_ROOT%{_mandir}/man1/nc*
for file in ncdump ncgen; do
  mv $RPM_BUILD_ROOT%{_bindir}/$file $RPM_BUILD_ROOT%{_bindir}/h$file
  # man pages are the same than netcdf ones
  rm $RPM_BUILD_ROOT%{_mandir}/man1/${file}.1
done

# this is done to have the same timestamp on multiarch setups
touch -c -r README.txt $RPM_BUILD_ROOT/%{_includedir}/hdf/h4config.h

# Remove an autoconf conditional from the API that is unused and cause
# the API to be different on x86 and x86_64
pushd $RPM_BUILD_ROOT/%{_includedir}/hdf
grep -v 'H4_SIZEOF_INTP' h4config.h > h4config.h.tmp
touch -c -r h4config.h h4config.h.tmp
mv h4config.h.tmp h4config.h
popd


%check
make check


%files
%doc COPYING MANIFEST README.txt release_notes/*.txt
%exclude %{_defaultdocdir}/%{name}/examples
%{_bindir}/*
%{_mandir}/man1/**

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_defaultdocdir}/%{name}/examples


%changelog
* Wed Aug 06 2014 Ilya Mashkin <oddity@altlinux.ru> 4.2.10-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.10-alt1_3
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.10-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.9-alt1_3
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.9-alt1_1
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.8-alt1_3
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.8-alt1_2
- update to new release by fcimport

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.8-alt1_1
- fc import

