%global with_java 0
%global with_php 0
%global with_python 0

Name: libkolabxml
Version: 1.0.3
Release: alt1.qa1

Summary: Kolab XML format collection parser library
License: LGPLv3+
Group: System/Libraries

Url: http://www.kolab.org
Source: http://git.kolab.org/libkolabxml/snapshot/%name-%version.tar.gz
Patch: libkolabxml-0.8.4-link.patch

BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: cmake >= 2.6
BuildRequires: libcurl-devel
BuildRequires: swig
BuildRequires: libxerces-c-devel
BuildRequires: xsd
BuildRequires: qt4-devel
BuildRequires: boost-devel

%if_with php
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %_libdir/php)
%{!?php_inidir: %global php_inidir %_sysconfdir/php.d/}
%endif

%if_with python
%{!?python_sitelib: %global python_sitelib %(%__python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%__python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

# Filter out private python and php libs. Does not work on EPEL5,
# therefor we use it conditionally
%if_with php
%if_with python
%{?filter_setup:
%filter_provides_in %python_sitearch/.*\.so$
%filter_provides_in %php_extdir/.*\.so$
%filter_setup
}
%else
%{?filter_setup:
%filter_provides_in %php_extdir/.*\.so$
%filter_setup
}
%endif
%else
%if_with python
%{?filter_setup:
%filter_provides_in %python_sitearch/.*\.so$
%filter_setup
}
%endif
%endif

%description
The libkolabxml parsing library interprets Kolab XML formats (xCal, xCard)
with bindings for Python, PHP and other languages. The language bindings
are available through sub-packages.

%package devel
Summary: Kolab XML library development headers
Group: System/Libraries
Requires: %name = %version-%release

%description devel
Development headers for the Kolab XML libraries.

%if_with java
%package -n java-kolabformat
Summary: Java Bindings for libkolabxml
Group: System/Libraries

%description -n java-kolabformat
Java bindings for libkolabxml
%endif

%if_with php
%package -n php-kolabformat
Summary: PHP bindings for libkolabxml
Group: System/Libraries
BuildRequires: php5-devel >= 5.4
BuildRequires: php5

%description -n php-kolabformat
The PHP kolabformat package offers a comprehensible PHP library using the
bindings provided through libkolabxml.
%endif

%if_with python
%package -n python-kolabformat
Summary: Python bindings for libkolabxml
Group: System/Libraries
BuildRequires: python-devel

%description -n python-kolabformat
The PyKolab format package offers a comprehensive Python library using the
bindings provided through libkolabxml.
%endif

%prep
%setup
%patch0 -p1  -b .libkolabxml-link

%build
%cmake_insource \
%if_with java
    -DJAVA_BINDINGS=ON \
    -DJAVA_INSTALL_DIR=%_datadir/%name/java/ \
%endif
%if_with php
    -DPHP_BINDINGS=ON \
    -DPHP_INSTALL_DIR=%php_extdir \
%endif
%if_with python
    -DPYTHON_BINDINGS=ON \
    -DPYTHON_INCLUDE_DIRS=%python_includedir \
    -DPYTHON_INSTALL_DIR=%python_sitearch \
%endif

%make_build

%install
%makeinstall_std

%if_with php
mkdir -p %buildroot/%_datadir/php
mv %buildroot/%php_extdir/kolabformat.php %buildroot/%_datadir/php/kolabformat.php

mkdir -p %buildroot/%php_inidir/
cat >%buildroot/%php_inidir/kolabformat.ini <<EOF
extension=kolabformat.so
EOF
%endif

%check
# Make sure libkolabxml.so.* is found, otherwise the tests fail
export LD_LIBRARY_PATH=$( pwd )/src/
pushd tests
./bindingstest ||:
./conversiontest ||:
./parsingtest ||:
popd
%if_with php
php -d enable_dl=On -dextension=src/php/kolabformat.so src/php/test.php ||:
%endif
%if_with python
python src/python/test.py ||:
%endif

%files
%doc DEVELOPMENT NEWS README
%_libdir/*.so.*

%files devel
%_includedir/kolabxml
%_libdir/*.so
%_libdir/cmake/Libkolabxml

%if_with java
%files -n java-kolabformat
%dir %_datadir/%name
%_datadir/%name/java
%endif

%if_with php
%files -n php-kolabformat
%config(noreplace) %php_inidir/kolabformat.ini
%_datadir/php/kolabformat.php
%php_extdir/kolabformat.so
%endif

%if_with python
%files -n python-kolabformat
%python_sitearch/kolabformat.py*
%python_sitearch/_kolabformat.so
%endif

%changelog
* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.3-alt1.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Mar 07 2015 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- built for ALT Linux (package based on Mageia's 1.0.3-1.mga5)
- disabled java/python/php bindings for now

