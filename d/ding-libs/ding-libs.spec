%define _unpackaged_files_terminate_build 1

Name: ding-libs
Version: 0.6.1
Release: alt5%ubt

Summary: "Ding is not GLib" assorted utility libraries
License: %lgpl3plus
Group: System/Libraries
Url: https://pagure.io/SSSD/ding-libs

Source: %name-%version.tar
Patch: %name-%version.patch

%define path_utils_version 0.2.1
%define dhash_version 0.5.0
%define collection_version 0.7.0
%define ref_array_version 0.1.5
%define basicobjects_version 0.1.1
%define ini_config_version 1.3.1

BuildRequires: pkgconfig
BuildRequires: doxygen

BuildRequires(pre):rpm-build-ubt
BuildRequires(pre):rpm-build-licenses

%package -n libpath_utils
Summary: Filesystem Path Utilities
Group: System/Libraries
Version: %path_utils_version

%package -n libpath_utils-devel
Summary: Development files for libpath_utils
Group: Development/C
Requires: libpath_utils = %path_utils_version-%release
Version: %path_utils_version

%package -n libdhash
Group: System/Libraries
Summary: Dynamic hash table
Version: %dhash_version

%package -n libdhash-devel
Summary: Development files for libdhash
Group: Development/C
Requires: libdhash = %dhash_version-%release
Version: %dhash_version

%package -n libcollection
Summary: Collection data-type for C
Group: System/Libraries
Version: %collection_version

%package -n libcollection-devel
Summary: Development files for libcollection
Group: Development/C
Requires: libcollection = %collection_version-%release
Version: %collection_version

%package -n libref_array
Summary: A refcounted array for C
Group: System/Libraries
Version: %ref_array_version

%package -n libref_array-devel
Summary: Development files for libref_array
Group: Development/C
Requires: libref_array = %ref_array_version-%release
Version: %ref_array_version

%package -n libbasicobjects
Summary: Basic object types for C
Group: System/Libraries
License: GPLv3+
Version: %basicobjects_version

%package -n libbasicobjects-devel
Summary: Development files for libbasicobjects
Group: Development/C
License: GPLv3+
Version: %basicobjects_version
Requires: libbasicobjects = %basicobjects_version-%release

%package -n libini_config
Summary: INI file parser for C
Group: System/Libraries
Version: %ini_config_version

%package -n libini_config-devel
Summary: Development files for libini_config
Group: Development/C
Requires: libini_config = %ini_config_version-%release
Version: %ini_config_version

%description
A set of helpful libraries used by projects such as SSSD

%description -n libpath_utils
Utility functions to manipulate filesystem pathnames

%description -n libpath_utils-devel
Utility functions to manipulate filesystem pathnames

%description -n libdhash
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%description -n libdhash-devel
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%description -n libcollection
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%description -n libcollection-devel
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%description -n libref_array
A dynamically-growing, reference-counted array

%description -n libref_array-devel
A dynamically-growing, reference-counted array

%description -n libbasicobjects
Basic object types

%description -n libbasicobjects-devel
Basic object types

%description -n libini_config
Library to process config files in INI format into a libcollection data
structure

%description -n libini_config-devel
Library to process config files in INI format into a libcollection data
structure

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build all docs

%install
%makeinstall_std

## Remove .la files created by libtool
#rm -f $RPM_BUILD_ROOT/%_libdir/*.la
#
# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
rm -f \
    %buildroot%_defaultdocdir/%name/README.* \
    %buildroot%_defaultdocdir/%name/examples/dhash_example.c \
    %buildroot%_defaultdocdir/%name/examples/dhash_test.c

# Remove document install script. RPM is handling this
#rm -f */doc/html/installdox

%check
%make check

%files -n libpath_utils
%doc COPYING COPYING.LESSER
%_libdir/libpath_utils.so.1
%_libdir/libpath_utils.so.1.0.1

%files -n libpath_utils-devel
%_includedir/path_utils.h
%_libdir/libpath_utils.so
%_pkgconfigdir/path_utils.pc
%doc path_utils/README.path_utils
%doc path_utils/doc/html/

%files -n libdhash
%doc COPYING COPYING.LESSER
%_libdir/libdhash.so.1
%_libdir/libdhash.so.1.1.0

%files -n libdhash-devel
%_includedir/dhash.h
%_libdir/libdhash.so
%_pkgconfigdir/dhash.pc
%doc dhash/README.dhash
%doc dhash/examples/*.c

%files -n libcollection
%doc COPYING COPYING.LESSER
%_libdir/libcollection.so.4
%_libdir/libcollection.so.4.1.1

%files -n libcollection-devel
%_includedir/collection.h
%_includedir/collection_tools.h
%_includedir/collection_queue.h
%_includedir/collection_stack.h
%_libdir/libcollection.so
%_pkgconfigdir/collection.pc
%doc collection/doc/html/

%files -n libref_array
%doc COPYING COPYING.LESSER
%_libdir/libref_array.so.1
%_libdir/libref_array.so.1.2.1

%files -n libref_array-devel
%_includedir/ref_array.h
%_libdir/libref_array.so
%_pkgconfigdir/ref_array.pc
%doc refarray/README.ref_array
%doc refarray/doc/html/

%files -n libbasicobjects
%doc COPYING COPYING.LESSER
%_libdir/libbasicobjects.so.0
%_libdir/libbasicobjects.so.0.1.0

%files -n libbasicobjects-devel
%_includedir/simplebuffer.h
%_libdir/libbasicobjects.so
%_pkgconfigdir/basicobjects.pc

%files -n libini_config
%doc COPYING COPYING.LESSER
%_libdir/libini_config.so.5
%_libdir/libini_config.so.5.2.1

%files -n libini_config-devel
%_includedir/ini_config.h
%_includedir/ini_configobj.h
%_includedir/ini_valueobj.h
%_includedir/ini_comment.h
%_includedir/ini_configmod.h
%_libdir/libini_config.so
%_libdir/pkgconfig/ini_config.pc
%doc ini/doc/html/

%changelog
* Wed Nov 01 2017 Stanislav Levin <slev@altlinux.org> 0.6.1-alt5%ubt
- 0.6.1

* Mon Apr 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.6.0-alt4%ubt
- Build package with unified build tag aka ubt macros

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt4
- 0.6.0

* Thu Dec 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt3
- 0.5.0

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt2
- increase release

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Tue Feb 04 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.1-alt1.git6f829
- upstream snapshot 6f829cba74cb64f2a9aeda099c5a502f6beaaa36

* Thu Jan 27 2011 Timur Aitov <timonbl4@altlinux.org> 0.1.2-alt1
- initial build for ALT

