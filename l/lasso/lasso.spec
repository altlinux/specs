%def_with    java
%def_with    php
%def_without perl
%def_with    python
%def_without wsf
%def_without tests

Summary: Liberty Alliance Single Sign On
Name: 	 lasso
Version: 2.5.0
Release: alt1
License: GPLv2+
Group:   System/Libraries
Url: 	 http://lasso.entrouvert.org/

Source:  http://dev.entrouvert.org/lasso/lasso-%{version}.tar.gz
Patch1:  lasso-export-symbols-from-logging.h.patch

BuildRequires: gtk-doc
BuildRequires: glib2-devel swig
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python-module-six
BuildRequires: zlib-devel
%if_with java
BuildRequires(pre): rpm-build-java
BuildRequires: java-1.7.0-openjdk-devel
BuildRequires: jpackage-utils
%endif
%if_with perl
BuildRequires: perl-devel
BuildRequires: perl-Error
%endif
%if_with php
BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel
BuildRequires: libexpat-devel
BuildRequires: python
%endif
%if_with python
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-lxml
%endif
%if_with wsf
BuildRequires: libgsasl-devel
%endif

%description
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to
handle the whole life-cycle of SAML based Federations, and provides
bindings for multiple languages.

%package -n lib%name
Summary: Liberty Alliance Single Sign On
Group:   System/Libraries
Provides: %name = %version-%release

%description -n lib%name
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to
handle the whole life-cycle of SAML based Federations, and provides
bindings for multiple languages.

%package -n lib%name-devel
Summary: Lasso development headers and documentation
Group:   Development/C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files, static libraries and development
documentation for Lasso.

%if_with perl
%package -n perl-%name
Summary: Liberty Alliance Single Sign On (lasso) Perl bindings
Group:   Development/Perl
Provides: %name-perl %version-%release
Requires: lib%name = %version-%release

%description -n perl-%name
Perl language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with java
%package java
Summary: Liberty Alliance Single Sign On (lasso) Java bindings
Group:   Development/Java
Requires: lib%name = %version-%release

%description java
Java language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with php
%package -n php5-%name
Summary: Liberty Alliance Single Sign On (lasso) PHP bindings
Group:   System/Servers
Provides: %name-php = %version-%release
Requires: lib%name = %version-%release

%description -n php5-%name
PHP language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%if_with python
%package -n python-module-%name
Summary: Liberty Alliance Single Sign On (lasso) Python bindings
Group:   Development/Python
Provides: %name-python = %version-%release
Requires: lib%name = %version-%release

%description -n python-module-%name
Python language bindings for the lasso (Liberty Alliance Single Sign On)
library.
%endif

%prep
%setup -q -n %{name}-%{version}
%patch1 -p2

%build
%add_optflags -fPIC
./autogen.sh
%configure \
%if_without java
           --disable-java \
%endif
%if_without python
           --disable-python \
%endif
%if_without perl
           --disable-perl \
%endif
%if_with php
           --enable-php5=yes \
           --with-php5-config-dir=%php5_sysconfdir \
%else
           --enable-php5=no \
%endif
%if_with wsf
           --enable-wsf \
           --with-sasl2=%_prefix/sasl2 \
%endif
%if_with tests
           --enable-tests
%endif
#           --with-html-dir=%{_datadir}/gtk-doc/html

%make_build

%install
%makeinstall_std exec_prefix=%_prefix

find %buildroot -type f -name '*.la' -delete
find %buildroot -type f -name '*.a' -delete

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
install -m 755 -d %buildroot%php5_datadir/%name
mv %buildroot%php5_datadir/lasso.php %buildroot%php5_datadir/%name/

# rename the PHP config file when needed (PHP 5.6+)
mkdir -p %buildroot%php5_sysconfdir/cli/php.d
mv %buildroot%php5_sysconfdir/%name.ini %buildroot%php5_sysconfdir/cli/php.d/%name.ini
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

%files -n lib%name
%doc AUTHORS COPYING NEWS README
%_libdir/liblasso.so.*

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
%_jnidir/libjnilasso.so
%endif

%if_with php
%files -n php5-%name
%attr(755,root,root) %php5_extdir/lasso.so
%config(noreplace) %attr(644,root,root) %php5_sysconfdir/cli/php.d/%name.ini
%attr(755,root,root) %dir %php5_datadir/%name
%attr(644,root,root) %php5_datadir/%name/lasso.php
%endif

%if_with python
%files -n python-module-%name
%python_sitelibdir/lasso.py*
%python_sitelibdir/_lasso.so
%endif

%changelog
* Fri Nov 20 2015 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build in Sisyphus (thanks Fedora for src.rpm)

