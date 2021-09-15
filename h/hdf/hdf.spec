%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects
%add_optflags -D_FILE_OFFSET_BITS=64

Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/diff /usr/bin/makeinfo /usr/bin/neqn /usr/bin/tbl
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?rhel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

Name: hdf
Version: 4.2.15
Release: alt2
Summary: A general purpose library and file format for storing scientific data
License: BSD
URL: https://portal.hdfgroup.org/
Source0: https://support.hdfgroup.org/ftp/HDF/releases/HDF%{version}/src/%{name}-%{version}.tar.bz2
Patch0: hdf-4.2.5-maxavailfiles.patch
Patch1: hdf-ppc.patch
Patch2: hdf-4.2.4-sparc.patch
Patch3: hdf-s390.patch
Patch4: hdf-arm.patch
# Support DESTDIR in install-examples
Patch5: hdf-destdir.patch
# Install examples into the right location
Patch6: hdf-examplesdir.patch
# Add AArch64 definitions
Patch8: hdf-aarch64.patch
# ppc64le support
# https://bugzilla.redhat.com/show_bug.cgi?id=1134385
Patch9: hdf-ppc64le.patch

# Fix syntax error on epel6 builds
# Use only if java is disabled
Patch10: hdf-avoid_syntax_error_el6.patch
# Fix java build
Patch11: hdf-build.patch

# For destdir/examplesdir patches
BuildRequires: automake, libtool, gcc, gcc-c++
BuildRequires: flex byacc libjpeg-devel zlib-devel libsz2-devel
BuildRequires: libtirpc-devel
BuildRequires: gcc-fortran, gcc
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
Group: Development/C
Summary: HDF development files
Provides: %{name}-static = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description devel
HDF development headers and libraries.

%prep
%setup -q

#patch0 -p1 -b .maxavailfiles
%patch1 -p1 -b .ppc
%patch2 -p1 -b .sparc
%patch3 -p1 -b .s390
%patch4 -p1 -b .arm
%patch5 -p1 -b .destdir
%patch6 -p1 -b .examplesdir
%patch8 -p1 -b .aarch64
%patch9 -p1 -b .ppc64le
%patch11 -p1 -b .build

## Fix syntax error bacause 'CLASSPATH_ENV=$H4_CLASSPATH' line on epel6 builds
# Use only if java is disabled
%if 0%{?rhel} && 0%{?rhel} < 7
%patch10 -p0
%endif

find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;

# restore include file timestamps modified by patching
touch -c -r ./hdf/src/hdfi.h.ppc ./hdf/src/hdfi.h

%build

# For destdir/examplesdir patches
autoreconf -vif
# avoid upstream compiler flags settings
rm config/*linux-gnu
# TODO: upstream fix
# Shared libraries disabled: libmfhdf.so is not correctly compiled
# for missing link to libdf.so
export CFLAGS="%{optflags} -fPIC -I%{_includedir}/tirpc"
export LIBS="-ltirpc"
export FFLAGS="%{optflags} -fPIC -ffixed-line-length-none -fallow-argument-mismatch"
%configure --disable-production --disable-java --disable-netcdf \
 --enable-shared=no --enable-static=yes --enable-fortran %{!?el6:--with-szlib} \
 --includedir=%{_includedir}/%{name} --libdir=%{_libdir}/%{name}
%make_build

# correct the timestamps based on files used to generate the header files
touch -c -r hdf/src/hdf.inc hdf/src/hdf.f90
touch -c -r hdf/src/dffunc.inc hdf/src/dffunc.f90
touch -c -r mfhdf/fortran/mffunc.inc mfhdf/fortran/mffunc.f90
# netcdf fortran include need same treatement, but they are not shipped

%install
%makeinstall_std

install -pm 644 MANIFEST README.txt release_notes/*.txt %{buildroot}%{_docdir}/%{name}/

rm -f %{buildroot}%{_libdir}/%{name}/*.la
rm -f %{buildroot}%{_libdir}/*.la

#Don't conflict with netcdf
for file in ncdump ncgen; do
  mv %{buildroot}%{_bindir}/$file %{buildroot}%{_bindir}/h$file
  # man pages are the same than netcdf ones
  rm %{buildroot}%{_mandir}/man1/${file}.1
done

# this is done to have the same timestamp on multiarch setups
touch -c -r README.txt %{buildroot}%{_includedir}/hdf/h4config.h

# Remove an autoconf conditional from the API that is unused and cause
# the API to be different on x86 and x86_64
pushd %{buildroot}%{_includedir}/hdf
grep -v 'H4_SIZEOF_INTP' h4config.h > h4config.h.tmp
touch -c -r h4config.h h4config.h.tmp
mv h4config.h.tmp h4config.h
popd

%check
make -j1 check

%files
%doc --no-dereference COPYING
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/examples
%{_bindir}/*
%{_mandir}/man1/**

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_docdir}/%{name}/examples/

%changelog
* Tue Sep 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.15-alt2
- Fixed build with LTO.

* Mon May 03 2021 Ilya Mashkin <oddity@altlinux.ru> 4.2.15-alt1
- 4.2.15

* Thu Apr 08 2021 Grigory Ustinov <grenka@altlinux.org> 4.2.14-alt2
- Fixed FTBFS.

* Tue Dec 18 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.14-alt1_1
- new version

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

