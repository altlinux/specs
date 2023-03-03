%def_without java
%def_with php
%def_without perl
%def_with python
%def_without wsf
%def_without tests

%define soname 3

Summary: Liberty Alliance Single Sign On
Name: 	 lasso
Version: 2.8.1
Release: alt1
License: GPLv2+
Group:   System/Libraries
Url: 	 http://lasso.entrouvert.org/

Source:  http://dev.entrouvert.org/lasso/lasso-%{version}.tar.gz
Source1: %name.watch
Patch1:  lasso-export-symbols-from-logging.h.patch
# debian patches
Patch2:  build-without-python2.diff

BuildRequires: gtk-doc
BuildRequires: glib2-devel swig
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python3-module-six
BuildRequires: zlib-devel
%if_with java
BuildRequires(pre): rpm-build-java
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: jpackage-utils
BuildRequires: /proc
%endif
%if_with perl
BuildRequires: perl-devel
BuildRequires: perl-Error
%endif
%if_with php
BuildRequires: rpm-build-php7-version
BuildRequires: php7-devel
BuildRequires: libexpat-devel
BuildRequires: python3
%endif
%if_with python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-lxml
%endif
%if_with wsf
BuildRequires: libgsasl-devel
%endif

%description
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to
handle the whole life-cycle of SAML based Federations, and provides
bindings for multiple languages.

%package -n lib%name%soname
Summary: Liberty Alliance Single Sign On
Group:   System/Libraries
Provides: %name = %version-%release
Provides: lib%name = %version-%release

%description -n lib%name%soname
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to
handle the whole life-cycle of SAML based Federations, and provides
bindings for multiple languages.

%package -n lib%name-devel
Summary: Lasso development headers and documentation
Group:   Development/C
Provides: %name-devel = %version-%release
Requires: lib%name%soname = %version-%release

%description -n lib%name-devel
This package contains the header files, static libraries and development
documentation for Lasso.

%if_with perl
%package -n perl-%name
Summary: Liberty Alliance Single Sign On (lasso) Perl bindings
Group:   Development/Perl
Provides: %name-perl %version-%release
Requires: lib%name%soname = %version-%release

%description -n perl-%name
Perl language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with java
%package java
Summary: Liberty Alliance Single Sign On (lasso) Java bindings
Group:   Development/Java
Requires: lib%name%soname = %version-%release

%description java
Java language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with php
%package -n php7-%name
Summary: Liberty Alliance Single Sign On (lasso) PHP bindings
Group:   System/Servers
Provides: %name-php = %version-%release
Requires: lib%name%soname = %version-%release

%description -n php7-%name
PHP language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with python
%package -n python3-module-%name
Summary: Liberty Alliance Single Sign On (lasso) Python bindings
Group:   Development/Python
Provides: %name-python = %version-%release
Requires: lib%name%soname = %version-%release

%description -n python3-module-%name
Python language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%prep
%setup -q -n %{name}-%{version}
# %%patch1 -p2
# %%patch2 -p1
sed -i 's|echo $VERSION |echo %version |' configure.ac
sed -i 's|@VERSION@|%version|' lasso.pc.in

%build
%add_optflags -fPIC
%autoreconf
%configure \
%if_with java
  --enable-java \
%endif
%if_without python
  --disable-python \
%endif
%if_without perl
  --disable-perl \
%endif
%if_with php
  --enable-php7=yes \
  --with-php7-config-dir=%php_sysconfdir \
%else
  --enable-php7=no \
%endif
%if_with wsf
  --enable-wsf \
  --with-sasl2=%_prefix/sasl2 \
%endif
%if_with tests
  --enable-tests
%endif
# --with-html-dir=%{_datadir}/gtk-doc/html

%make_build

%install
%makeinstall_std exec_prefix=%_prefix

find %buildroot -type f -name '*.la' -delete
find %buildroot -type f -name '*.a' -delete

# %%_includedir/lasso/keyprivate.h:
# fatal error: xml/private.h: No such file or directory
install -m 644 lasso/xml/private.h %buildroot%_includedir/%name/xml/

# Perl subpackage
%if_with perl
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;

find %{buildroot}/usr/lib*/perl5 -type f -print |
        sed "s@^%{buildroot}@@g" > %{name}-perl-filelist
if [ "$(cat %{name}-perl-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi
%endif

# PHP subpackage
%if_with php
install -m 755 -d %buildroot%php_datadir/%name
mv %buildroot%php_datadir/lasso.php %buildroot%php_datadir/%name/

# rename the PHP config file when needed (PHP 5.6+)
mkdir -p %buildroot%php_sysconfdir/cli/php.d
mv %buildroot%php_sysconfdir/%name.ini %buildroot%php_sysconfdir/cli/php.d/%name.ini
%endif

# Remove bogus doc files
rm -fr %buildroot%_defaultdocdir/%name

%check
%if_with tests
%if_with perl
# This is so the perl test can find the built, but not yet installed library
export LD_LIBRARY_PATH=%_builddir/%buildsubdir/lasso/.libs
%endif
make check
%endif

%files -n lib%name%soname
%doc AUTHORS COPYING NEWS README
%_libdir/liblasso.so.%{soname}*

%files -n lib%name-devel
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_includedir/%name

%if_with perl
%files -n perl-%name -f %{name}-perl-filelist
%endif

%if_with java
%files java
%_javadir/lasso.jar
%_libdir/java/libjnilasso.so
%endif

%if_with php
%files -n php7-%name
%php_extdir/lasso.so
%config(noreplace) %php_sysconfdir/cli/php.d/%name.ini
%dir %php_datadir/%name
%php_datadir/%name/lasso.php
%endif

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/lasso.py*
%python3_sitelibdir/_lasso.so
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Fri Mar 03 2023 Leontiy Volodin <lvol@altlinux.org> 2.8.1-alt1
- New version.

* Mon Jul 12 2021 Leontiy Volodin <lvol@altlinux.org> 2.7.0-alt1
- New version.
- Upstream:
  + CVE-2021-28091: Fix signature checking on unsigned response with multiple assertions.
  + configure.ac: Disable java bindings.

* Sat Jul 10 2021 Leontiy Volodin <lvol@altlinux.org> 2.6.1-alt4
- FTBFS: switch to macros with recent changes in rpm-build-php (thanks rider@).

* Fri Jul 09 2021 Leontiy Volodin <lvol@altlinux.org> 2.6.1-alt3
- Fixed build with php7 macros.

* Fri Jan 29 2021 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt2
- Respect all versions of python3.

* Fri Apr 24 2020 Leontiy Volodin <lvol@altlinux.org> 2.6.1-alt1
- New version.
- Built with PHP7 support.

* Tue Mar 24 2020 Leontiy Volodin <lvol@altlinux.org> 2.6.0-alt4
- Built with java support again.

* Tue Mar 24 2020 Leontiy Volodin <lvol@altlinux.org> 2.6.0-alt3
- Built without python2 support (thanks debian for this patch).

* Mon Mar 11 2019 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt2
- Build without PHP5 support.

* Tue Sep 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt2.2
- NMU: Rebuild with new openssl 1.1.0.

* Fri Apr 27 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2.1
- NMU: e2k support

* Thu Mar 01 2018 Alexey Shabalin <shaba@altlinux.ru> 2.5.1-alt2
- Rebuild with libxmlsec1-1.2.25

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version

* Fri Nov 20 2015 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build in Sisyphus (thanks Fedora for src.rpm)

