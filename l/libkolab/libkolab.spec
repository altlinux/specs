%def_without php
%def_without python

Name: libkolab
Version: 0.5.3
Release: alt1.qa1

Summary: Kolab Object Handling Library
License: LGPLv3+
Group: System/Servers

Url: http://git.kolab.org/libkolab
Source: http://git.kolab.org/%name/snapshot/%name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: boost-devel boost-program_options-devel
BuildRequires: libcurl-devel
BuildRequires: kde4pimlibs-devel >= 4.9
BuildRequires: libkolabxml-devel >= 1.0.2
%if_with php
BuildRequires: php-devel php5
%endif
%if_with python
BuildRequires: python-devel
%endif
BuildRequires: qt4-devel
BuildRequires: swig
BuildRequires: libxerces-c-devel

%if_with php
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %_libdir/php)
%{!?php_inidir: %global php_inidir %_sysconfdir/php.d/}
%endif

# Filter out private python and php libs. Does not work on EPEL5,
# therefor we use it conditionally
%{?filter_setup:
%filter_provides_in %python_sitelibdir/.*\.so$
%filter_provides_in %php_extdir/.*\.so$
%filter_setup
}

%description
The libkolab library is an advanced library to handle Kolab objects.

%package devel
Summary: Kolab library development headers
Group: System/Libraries
Requires: %name = %version-%release
Requires: libkolabxml-devel >= 0.8

%description devel
Development headers for the Kolab object libraries.

%if_with php
%package -n php-kolab
Summary: PHP Bindings for libkolab
Group: System/Libraries
Requires: %name = %version-%release
Requires: php-kolabformat >= 0.7

%description -n php-kolab
PHP Bindings for libkolab
%endif

%if_with python
%package -n python-kolab
Summary: Python bindings for libkolab
Group: System/Libraries
Requires: %name = %version-%release
Requires: python-kolabformat >= 0.7

%description -n python-kolab
Python bindings for libkolab
%endif

%prep
%setup

%build
%cmake_insource \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DUSE_LIBCALENDARING=OFF \
%if_with php
    -DPHP_BINDINGS=ON \
    -DPHP_INSTALL_DIR=%php_extdir \
%endif
%if_with php
    -DPYTHON_BINDINGS=ON \
    -DPYTHON_INSTALL_DIR=%python_sitelibdir
%endif

%make_build

%install
%makeinstall_std

%if_with php
mkdir -p %buildroot%_datadir/php
mv %buildroot%php_extdir/*.php %buildroot%_datadir/php/.

mkdir -p %buildroot%php_inidir
cat >%buildroot%php_inidir/kolab.ini <<EOF
extension=kolabcalendaring.so
extension=kolabicalendar.so
extension=kolabobject.so
extension=kolabshared.so
EOF
%endif

%check
pushd tests
./benchmarktest || :
./calendaringtest || :
./formattest || :
./freebusytest || :
./icalendartest || :
./kcalconversiontest || :
./upgradetest || :
popd

%files
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%_libdir/cmake/Libkolab
%_includedir/kolab

%if_with php
%files -n php-kolab
%config(noreplace) %php_inidir/kolab.ini
%_datadir/php/kolabcalendaring.php
%php_extdir/kolabcalendaring.so
%_datadir/php/kolabicalendar.php
%php_extdir/kolabicalendar.so
%_datadir/php/kolabobject.php
%php_extdir/kolabobject.so
%_datadir/php/kolabshared.php
%php_extdir/kolabshared.so
%endif

%if_with python
%files -n python-kolab
%python_sitelibdir/kolab/_calendaring.so
%python_sitelibdir/kolab/calendaring.py*
%python_sitelibdir/kolab/_icalendar.so
%python_sitelibdir/kolab/icalendar.py*
%python_sitelibdir/kolab/_shared.so*
%python_sitelibdir/kolab/shared.py*
%python_sitelibdir/kolab/_kolabobject.so
%python_sitelibdir/kolab/kolabobject.py*
%endif

%changelog
* Fri Apr 08 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.3-alt1.qa1
- NMU: rebuilt with rebuilt libkolabxml.

* Sat Mar 07 2015 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- built for ALT Linux (based on Mageia's 0.5.3-5.mga5 package)
- disabled php/python bindings for now

