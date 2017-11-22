# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-python rpm-macros-fedora-compat rpm-macros-java
BuildRequires: /usr/bin/bundle /usr/bin/cabal /usr/bin/haxe /usr/bin/mcs /usr/bin/npm /usr/bin/perl /usr/bin/php /usr/bin/phpunit /usr/bin/ruby /usr/bin/runhaskell /usr/bin/trial gcc-c++ perl(Encode.pm) perl(HTTP/Request.pm) perl(IO/Select.pm) perl(IO/Socket/INET.pm) perl(IO/Socket/SSL.pm) perl(IO/Socket/UNIX.pm) perl(IO/String.pm) perl(LWP/UserAgent.pm) perl(Time/HiRes.pm) perl(base.pm) perl(overload.pm) perl-podlators pkgconfig(Qt5Core) pkgconfig(Qt5Network) pkgconfig(mono) rpm-build-java
# END SourceDeps(oneline)
BuildRequires: mono-web javapackages-local
BuildRequires: chrpath
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")


%global __provides_exclude_from ^(%{python_sitelibdir}/.*\\.so|%{php_extdir}/.*\\.so)$

%global have_mongrel 0

# erlang-jsx is available in F19 but orphaned in F22
%global have_jsx 0

# We should be able to enable this in the future
%global want_d 0

# Thrift's Ruby support depends on Mongrel.  Since Mongrel is
# deprecated in Fedora, we can't support Ruby bindings for Thrift
# unless and until Thrift is patched to use a different HTTP server.
%if 0%{?have_mongrel} == 0
%global ruby_configure --without-ruby
%global with_ruby 0
%else
%global ruby_configure --with-ruby
%global want_ruby 1
%endif

# Thrift's Erlang support depends on the JSX library, which is not
# currently available in Fedora.

%if 0%{?have_jsx} == 0
%global erlang_configure --without-erlang
%global want_erlang 0
%else
%global erlang_configure --with-erlang
%global want_erlang 1
%endif

# PHP appears broken in Thrift 0.9.1
%global want_php 0

%if 0%{?want_php} == 0
%global php_langname %{nil}
%global php_configure --without-php
%else
%global php_langname PHP,\ 
%global php_configure --with-php
%endif

# Thrift's GO support doesn't build under Fedora
%global want_golang 0
%global golang_configure --without-go

Name:    thrift
Version: 0.10.0
Release: alt1_4jpp8
Summary: Software framework for cross-language services development

# Parts of the source are used under the BSD and zlib licenses, but
# these are OK for inclusion in an Apache 2.0-licensed whole:
# https://www.apache.org/legal/3party.html

# Here's the breakdown:
# ./lib/py/compat/win32/stdint.h is 2-clause BSD
# ./compiler/cpp/src/md5.[ch] are zlib
License: ASL 2.0 and BSD and zlib
URL:     https://thrift.apache.org/

Source0: https://archive.apache.org/dist/%{name}/%{version}/%{name}-%{version}.tar.gz

Source1: https://repo1.maven.org/maven2/org/apache/thrift/lib%{name}/%{version}/lib%{name}-%{version}.pom
Source2: https://raw.github.com/apache/%{name}/%{version}/bootstrap.sh

Source3: https://repo1.maven.org/maven2/org/apache/thrift/libfb303/%{version}/libfb303-%{version}.pom

# this patch is adapted from Gil Cattaneo's thrift-0.7.0 package
Patch0: %{name}-%{version}-buildxml.patch
# for fb303, excise maven ant tasks; build against system libraries; etc.
Patch1: fb303-%{version}-buildxml.patch
# fix configure.ac insistence on using /usr/local/lib for JAVA_PREFIX
Patch2: configure-java-prefix.patch
# fix for ppc64le builds not linking to /usr/lib64 directory
Patch3: fix-ppc64le-builds.patch

Group: Development/Other

# BuildRequires for language-specific bindings are listed under these
# subpackages, to facilitate enabling or disabling individual language
# bindings in the future

BuildRequires: ant >= 1.7
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires: boost-devel-static
BuildRequires: flex
BuildRequires: flex
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libevent-devel
BuildRequires: libstdc++-devel
BuildRequires: libtool
BuildRequires: libssl-devel
BuildRequires: libqt4-declarative libqt4-devel qt4-designer
BuildRequires: texlive-latex-recommended texlive-base-bin texlive-generic-recommended
BuildRequires: zlib-devel

%if 0%{?want_golang} > 0
BuildRequires: golang
Requires: golang
%endif
Source44: import.info

%description

The Apache Thrift software framework for cross-language services
development combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java,
Python, %{?php_langname}and other languages.

%package devel
Group: Development/C++
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkg-config
Requires: boost-devel-headers boost-python-headers

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt
Group: Development/Java
Summary:        Qt support for %{name}
Requires:       %{name} = %{version}-%{release}

%description    qt
The %{name}-qt package contains Qt bindings for %{name}.

%package        glib
Group: Development/Java
Summary:        GLib support for %{name}
Requires:       %{name} = %{version}-%{release}

%description    glib
The %{name}-qt package contains GLib bindings for %{name}.

%package -n python-module-thrift
Group: Development/Python
Summary: Python 2 support for %{name}
BuildRequires: python-devel
Requires: %{name} = %{version}-%{release}
Requires: python
Obsoletes: python-%{name} < 0.10.0-1%{?dist}
BuildArch: noarch

%description -n python-module-thrift
The python2-%{name} package contains Python bindings for %{name}.

%package -n perl-%{name}
Group: Development/Java
Summary: Perl support for %{name}
Provides: perl(Thrift.pm) = %{version}-%{release}
BuildRequires: perl(Bit/Vector.pm)
BuildRequires: perl(Class/Accessor.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: rpm-build-perl
Requires: perl(Bit/Vector.pm)
Requires: perl(Encode.pm)
Requires: perl(HTTP/Request.pm)
Requires: perl(IO/Select.pm)
Requires: perl(IO/Socket/INET.pm)
Requires: perl(IO/String.pm)
Requires: perl(LWP/UserAgent.pm)
Requires: perl(POSIX.pm)
Requires: perl(base.pm)
Requires: perl(constant.pm)
Requires: perl(strict.pm)
Requires: perl(utf8.pm)
Requires: perl(warnings.pm)
BuildArch: noarch

%description -n perl-%{name}
The perl-%{name} package contains Perl bindings for %{name}.

%if %{?want_d}
%package -n d-%{name}
Group: Development/Java
Summary: D support for %{name}
BuildRequires: dmd

%description -n d-%{name}
The d-%{name} package contains D bindings for %{name}.
%endif

%if 0%{?want_php} != 0
%package -n php-%{name}
Group: Development/Java
Summary: PHP support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: php(language) >= 5.3.0
Requires: php-date
Requires: php-json
BuildRequires: php5-devel

%description -n php-%{name}
The php-%{name} package contains PHP bindings for %{name}.
%endif

%package -n lib%{name}-javadoc
Group: Development/Java
Summary: API documentation for java-%{name}
Requires: lib%{name}-java = %{version}-%{release}
BuildArch: noarch

%description -n lib%{name}-javadoc 
The lib%{name}-javadoc package contains API documentation for the
Java bindings for %{name}.

%package -n lib%{name}-java
Group: Development/Java
Summary: Java support for %{name}

BuildRequires: apache-commons-codec
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: junit
BuildRequires: log4j
BuildRequires: slf4j
BuildRequires: tomcat-servlet-3.1-api

Requires: javapackages-tools
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.httpcomponents:httpcore)
BuildArch: noarch

%description -n lib%{name}-java
The lib%{name}-java package contains Java bindings for %{name}.

%if 0%{?want_ruby} > 0
%package -n ruby-%{name}
Group: Development/Java
Summary: Ruby support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: ruby(release)
BuildRequires: libruby-devel

%description -n ruby-%{name}
The ruby-%{name} package contains Ruby bindings for %{name}.
%endif

%if 0%{?want_erlang} > 0
%package -n erlang-%{name}
Group: Development/Java
Summary: Erlang support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: erlang
Requires: erlang-jsx
BuildRequires: erlang
BuildRequires: rebar

%description -n erlang-%{name}
The erlang-%{name} package contains Erlang bindings for %{name}.
%endif

%package -n fb303
Group: Development/Java
Summary: Basic interface for Thrift services
Requires: %{name} = %{version}-%{release}

%description -n fb303
fb303 is the shared root of all Thrift services; it provides a
standard interface to monitoring, dynamic options and configuration,
uptime reports, activity, etc.

%package -n fb303-devel
Group: Development/Java
Summary: Development files for fb303
Requires: fb303 = %{version}-%{release}

%description -n fb303-devel
The fb303-devel package contains header files for fb303

%package -n python-module-fb303
Group: Development/Java
Summary: Python 2 bindings for fb303
Requires: fb303 = %{version}-%{release}
BuildRequires: python-devel
BuildArch: noarch

%description -n python-module-fb303
The python2-fb303 package contains Python bindings for fb303.

%package -n fb303-java
Group: Development/Java
Summary: Java bindings for fb303
Requires: javapackages-tools
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.httpcomponents:httpcore)
BuildArch: noarch

%description -n fb303-java
The fb303-java package contains Java bindings for fb303.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{?!el5:sed -i -e 's/^AC_PROG_LIBTOOL/LT_INIT/g' configure.ac}

# avoid spurious executable permissions in debuginfo package
find . -name \*.cpp -or -name \*.cc -or -name \*.h | xargs -r chmod 644

cp -p %{SOURCE2} bootstrap.sh

# work around linking issues
echo 'libthrift_c_glib_la_LIBADD = $(GLIB_LIBS) $(GOBJECT_LIBS) -L../cpp/.libs ' >> lib/c_glib/Makefile.am
echo 'libthriftqt_la_LIBADD = $(QT_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftz_la_LIBADD = $(ZLIB_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftqt5_la_LIBADD = $(QT5_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftnb_la_LIBADD = $(LIBEVENT_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftqt_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftz_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftqt5_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftnb_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am

# echo 'libfb303_so_LIBADD = -L../../../lib/cpp/.libs -lthrift' >> contrib/fb303/cpp/Makefile.am

sed -i 's|libfb303_so_LDFLAGS = $(SHARED_LDFLAGS)|libfb303_so_LDFLAGS = $(SHARED_LDFLAGS) -Wl,--no-as-needed -lthrift -L../../../lib/cpp/.libs -Wl,--as-needed|g' contrib/fb303/cpp/Makefile.am

# fix broken upstream check for ant version; we enforce this with BuildRequires, so no need to check here
sed -i 's|ANT_VALID=.*|ANT_VALID=1|' aclocal/ax_javac_and_java.m4
sed -i 's|ANT_VALID=.*|ANT_VALID=1|' contrib/fb303/aclocal/ax_javac_and_java.m4

%build
export PY_PREFIX=%{_prefix}
export PERL_PREFIX=%{_prefix}
export PHP_PREFIX=%{php_extdir}
export JAVA_PREFIX=%{_javadir}
export RUBY_PREFIX=%{_prefix}
export GLIB_LIBS=$(pkg-config --libs glib-2.0)
export GLIB_CFLAGS=$(pkg-config --cflags glib-2.0)
export GOBJECT_LIBS=$(pkg-config --libs gobject-2.0)
export GOBJECT_CFLAGS=$(pkg-config --cflags gobject-2.0)

find %{_builddir} -name rebar -exec rm -f '{}' \;
find . -name Makefile\* -exec sed -i -e 's/[.][/]rebar/rebar/g' {} \;

# install javadocs in proper places
sed -i 's|-Dinstall.javadoc.path=$(DESTDIR)$(docdir)/java|-Dinstall.javadoc.path=$(DESTDIR)%{_javadocdir}/%{name}|' lib/java/Makefile.*

# build a jar without a version number
sed -i 's|${thrift.artifactid}-${version}|${thrift.artifactid}|' lib/java/build.xml

# Proper permissions for Erlang files
sed -i 's|$(INSTALL) $$p|$(INSTALL) --mode 644 $$p|g' lib/erl/Makefile.am

# Build fb303 jars against the in-situ copy of thrift
sed -i 's|$(thrift_home)/bin/thrift|../../../compiler/cpp/thrift|g' \
 contrib/fb303/cpp/Makefile.am \
 contrib/fb303/py/Makefile.am

sed -i 's|$(prefix)/lib$|%{_libdir}|g' contrib/fb303/cpp/Makefile.am

sed -i 's|$(thrift_home)/include/thrift|../../../lib/cpp/src|g' \
 contrib/fb303/cpp/Makefile.am

# Create a straightforward makefile for Java fb303
echo "all:
	ant
install: build/libfb303.jar
	mkdir -p %{buildroot}%{_javadir}
	/usr/bin/install -c -m 644 build/libfb303.jar %{buildroot}%{_javadir}
" > contrib/fb303/java/Makefile

sh ./bootstrap.sh

# use unversioned doc dirs where appropriate (via _pkgdocdir macro)
%configure --disable-dependency-tracking --disable-static --with-boost=/usr %{ruby_configure} %{erlang_configure} %{golang_configure} %{php_configure} --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}} \
	   --without-haskell \
	   --without-nodejs

# eliminate unused direct shlib dependencies
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

%make_build

# build fb303
(
  cd contrib/fb303
  sed -i '/^[.][/]configure.*/d' bootstrap.sh
  sh bootstrap.sh
  %configure --disable-static --with-java --without-php --libdir=%{_libdir}
%make_build
  (
      cd java
      ant dist
  )
)

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name fastbinary.so | xargs -r chmod 755
find %{buildroot} -name \*.erl -or -name \*.hrl -or -name \*.app | xargs -r chmod 644

# Remove javadocs jar
find %{buildroot}/%{_javadir} -name lib%{name}-javadoc.jar -exec rm -f '{}' \;

# Add POM file and depmap
mkdir -p %{buildroot}%{_mavenpomdir}

install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-libthrift.pom

%add_maven_depmap JPP-libthrift.pom libthrift.jar

# Remove bundled jar files
find %{buildroot} -name \*.jar -a \! -name \*thrift\* -exec rm -f '{}' \;

# Move perl files into appropriate places
find %{buildroot} -name \*.pod -exec rm -f '{}' \;
find %{buildroot} -name .packlist -exec rm -f '{}' \;
find %{buildroot}/usr/lib/perl5 -type d -empty -delete
mkdir -p %{buildroot}/%{perl_vendor_privlib}/
mv %{buildroot}/usr/lib/perl5/* %{buildroot}/%{perl_vendor_privlib}

%if 0%{?want_php} != 0

# Move arch-independent php files into the appropriate place
mkdir -p %{buildroot}/%{_datadir}/php/
mv %{buildroot}/%{php_extdir}/Thrift %{buildroot}/%{_datadir}/php/
%endif # want_php

# Fix permissions on Thread.h
find %{buildroot} -name Thread.h -exec chmod a-x '{}' \;

# install fb303
(
  cd contrib/fb303
  make DESTDIR=%{buildroot} install
  (
    cd java
    ant -Dinstall.path=%{buildroot}%{_javadir} -Dinstall.javadoc.path=%{buildroot}%{_javadocdir}/fb303 install
  )
)

# install maven pom and depmaps for fb303
install -pm 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-libfb303.pom
%add_maven_depmap JPP-libfb303.pom libfb303.jar -f "fb303"

# Ensure all python scripts are executable
find %{buildroot} -name \*.py -exec grep -q /usr/bin/env {} \; -print | xargs -r chmod 755
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done

# last second hack; remove me if qt5 subpackage
rm -f %buildroot%{_libdir}/libthriftqt5.so


%files
%doc LICENSE NOTICE
%{_bindir}/thrift
%{_libdir}/libthrift-%{version}.so
%{_libdir}/libthriftz-%{version}.so
%{_libdir}/libthriftnb-%{version}.so

%files glib
%{_libdir}/libthrift_c_glib.so
%{_libdir}/libthrift_c_glib.so.*

%files qt
%{_libdir}/libthriftqt.so
%{_libdir}/libthriftqt-%{version}.so

%files devel
%{_includedir}/thrift
%exclude %{_includedir}/thrift/fb303
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.0
%exclude %{_libdir}/lib*-%{version}.so
%exclude %{_libdir}/libfb303.so
%{_libdir}/pkgconfig/thrift-z.pc
%{_libdir}/pkgconfig/thrift-qt.pc
%{_libdir}/pkgconfig/thrift-nb.pc
%{_libdir}/pkgconfig/thrift.pc
%{_libdir}/pkgconfig/thrift_c_glib.pc
%doc LICENSE NOTICE

%files -n perl-%{name}
%{perl_vendor_privlib}/Thrift
%{perl_vendor_privlib}/Thrift.pm
%doc LICENSE NOTICE

%if 0%{?want_php} != 0
%files -n php-%{name}
%config(noreplace) /etc/php.d/thrift_protocol.ini
%{_datadir}/php/Thrift/
%{php_extdir}/thrift_protocol.so
%doc LICENSE NOTICE
%endif

%if %{?want_erlang} > 0
%files -n erlang-%{name}
%{_libdir}/erlang/lib/%{name}-%{version}/
%doc LICENSE NOTICE
%endif

%files -n lib%{name}-javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%files -n lib%{name}-java -f .mfiles
%doc LICENSE NOTICE

%if 1
%files -n fb303
%{_datarootdir}/fb303
%doc LICENSE NOTICE

%files -n fb303-devel
%{_libdir}/libfb303.so
%{_includedir}/thrift/fb303
%doc LICENSE NOTICE

%files -n python-module-fb303
%{python_sitelibdir_noarch}/fb303
%{python_sitelibdir_noarch}/fb303_scripts
%{python_sitelibdir_noarch}/%{name}_fb303-%{version}-py%{__python_version}.egg-info
%doc LICENSE NOTICE

%files -n fb303-java -f .mfiles-fb303
%doc LICENSE NOTICE
%endif

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_4jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_17.3jpp8
- cleaned up req on javapackages

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_16.4
- new version
- --without-haskell --without-csharp

* Mon Dec 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt3
- disable ruby module build

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2
- name thrift jars properly

* Wed May 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1
- 0.3.0
- enable tests

* Mon Apr 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1
- initial
