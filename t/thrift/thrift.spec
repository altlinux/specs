Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-php7 rpm-build-python3 rpm-macros-java
BuildRequires: /usr/bin/perl /usr/bin/php /usr/bin/rustc boost-devel boost-filesystem-devel boost-program_options-devel perl(Encode.pm) perl(HTTP/Request.pm) perl(IO/Select.pm) perl(IO/Socket/INET.pm) perl(IO/Socket/SSL.pm) perl(IO/Socket/UNIX.pm) perl(IO/String.pm) perl(LWP/UserAgent.pm) perl(Time/HiRes.pm) perl(base.pm) perl(overload.pm) perl(parent.pm) perl-podlators pkgconfig(mono) python-devel rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /usr/bin/curl mono-web
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")


%global have_mongrel 0

# erlang-jsx is available in F19 but orphaned in F22
%global have_jsx 0

# We should be able to enable this in the future
%global want_d 0

# Can't do anything with java with all the build deps in modules
%global want_java 0

%if 0%{?want_java} == 0
%global java_configure --without-java
%else
%global java_configure --with-java
%endif

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

# Thrift's Lua support has not yet been worked on
%global want_lua 0
%global lua_configure --without-lua

# NOTE: thrift versions their libraries by package version, so each version
# change is a SONAME change and dependencies need to be rebuilt
Name:    thrift
Version: 0.13.0
Release: alt1_9
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

# this patch is adapted from Gil Cattaneo's thrift-0.7.0 package
#Patch0: %{name}-%{version}-buildxml.patch
# fix configure.ac insistence on using /usr/local/lib for JAVA_PREFIX
Patch2: configure-java-prefix.patch


# BuildRequires for language-specific bindings are listed under these
# subpackages, to facilitate enabling or disabling individual language
# bindings in the future

%if 0%{?want_java} > 0
BuildRequires: ant >= 1.7
%endif
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: boost-complete
BuildRequires: boost-devel-static
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libevent-devel
BuildRequires: libstdc++-devel
BuildRequires: libtool
BuildRequires: libssl-devel
BuildRequires: qt5-base-devel
BuildRequires: texlive-texmf
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
Requires: pkgconfig
Requires: boost-complete

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

%package -n python3-module-thrift
Group: Development/Other
Summary: Python 3 support for %{name}
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
Requires: %{name} = %{version}-%{release}
Requires: python3
Obsoletes: python-%{name} < 0.10.0-1%{?dist}
Obsoletes: python2-%{name} < 0.10.0-14%{?dist}

%description -n python3-module-thrift
The python3-%{name} package contains Python bindings for %{name}.

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
# thrift improperly packages some components in files with names different
# than the package they contain
Provides: perl(Thrift/Exception.pm)
Provides: perl(Thrift/MessageType.pm)
Provides: perl(Thrift/Type.pm)
BuildArch: noarch

%description -n perl-%{name}
The perl-%{name} package contains Perl bindings for %{name}.

%if %{?want_d}
%package -n d-%{name}
Group: Development/Java
Summary: D support for %{name}
BuildRequires: ldc

%description -n d-%{name}
The d-%{name} package contains D bindings for %{name}.
%endif

%if 0%{?want_php} != 0
%package -n php-%{name}
Group: Development/Java
Summary: PHP support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: php(language) >= 5.3.0
Requires: php7-bz2 php7-calendar php7-curl php7-exif php7-fileinfo php7-sockets
Requires: php-json
BuildRequires: php-devel

%description -n php-%{name}
The php-%{name} package contains PHP bindings for %{name}.
%endif

%if 0%{?want_java} > 0
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
BuildRequires: javapackages-local
BuildRequires: junit
BuildRequires: log4j
BuildRequires: slf4j
# javax.servlet-api 3.1.0 is provided by glassfish-servlet-api
BuildRequires: mvn(javax.servlet:javax.servlet-api) = 3.1.0

Requires: java-headless >= 1.6.0
Requires: javapackages-tools
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.httpcomponents:httpcore)
BuildArch: noarch

%description -n lib%{name}-java
The lib%{name}-java package contains Java bindings for %{name}.
%endif

%if 0%{?want_ruby} > 0
%package -n ruby-%{name}
Group: Development/Other
Summary: Ruby support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: ruby(release)
BuildRequires: libruby-devel

%description -n ruby-%{name}
The ruby-%{name} package contains Ruby bindings for %{name}.
%endif

%if 0%{?want_erlang} > 0
%package -n erlang-%{name}
Group: Development/Erlang
Summary: Erlang support for %{name}
Requires: %{name} = %{version}-%{release}
Requires: erlang
Requires: erlang-jsx
BuildRequires: erlang
BuildRequires: rebar2

%description -n erlang-%{name}
The erlang-%{name} package contains Erlang bindings for %{name}.
%endif


%prep
%setup -q
%patch2 -p1


%{?!el5:sed -i -e 's/^AC_PROG_LIBTOOL/LT_INIT/g' configure.ac}

# avoid spurious executable permissions in debuginfo package
find . -name \*.cpp -or -name \*.cc -or -name \*.h | xargs -r chmod 644

cp -p %{SOURCE2} bootstrap.sh

# work around linking issues
echo 'libthrift_c_glib_la_LIBADD = $(GLIB_LIBS) $(GOBJECT_LIBS) -L../cpp/.libs ' >> lib/c_glib/Makefile.am
echo 'libthriftqt5_la_LIBADD = $(QT_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftz_la_LIBADD = $(ZLIB_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftnb_la_LIBADD = $(ZLIB_LIBS) -levent -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftqt5_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftz_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftnb_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am

# fix broken upstream check for ant version; we enforce this with BuildRequires, so no need to check here
sed -i 's|ANT_VALID=.*|ANT_VALID=1|' aclocal/ax_javac_and_java.m4

# explicitly set python3
shopt -s globstar
sed -i -E 's@^(#!.*/env) *python *$@\1 python3@' **/*.py

%build
export PY_PREFIX=%{_prefix}
export PERL_PREFIX=%{_prefix}
export PHP_PREFIX=%{php7_extdir}
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
#sed -i 's|${thrift.artifactid}-${version}|${thrift.artifactid}|' lib/java/build.xml

# Proper permissions for Erlang files
sed -i 's|$(INSTALL) $$p|$(INSTALL) --mode 644 $$p|g' lib/erl/Makefile.am

sh ./bootstrap.sh

# use unversioned doc dirs where appropriate (via _pkgdocdir macro)
export PYTHON=%{_bindir}/python3
%configure --disable-dependency-tracking --disable-static --with-boost=/usr \
  --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}} \
  %{java_configure} %{ruby_configure} %{erlang_configure} %{golang_configure} %{php_configure} %{lua_configure}

# eliminate unused direct shlib dependencies
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

%make_build


%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name fastbinary.so | xargs -r chmod 755
find %{buildroot} -name \*.erl -or -name \*.hrl -or -name \*.app | xargs -r chmod 644

# Remove javadocs jar
%if 0%{?want_java} > 0
find %{buildroot}/%{_javadir} -name lib%{name}-javadoc.jar -exec rm -f '{}' \;
# Add POM file and depmap
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-libthrift.pom
%add_maven_depmap JPP-libthrift.pom libthrift.jar
%endif

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
mv %{buildroot}/%{php7_extdir}/Thrift %{buildroot}/%{_datadir}/php/
%endif # want_php

# Fix permissions on Thread.h
find %{buildroot} -name Thread.h -exec chmod a-x '{}' \;

# Ensure all python scripts are executable
find %{buildroot} -name \*.py -exec grep -q /usr/bin/env {} \; -print | xargs -r chmod 755
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done



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
%{_libdir}/libthriftqt5.so
%{_libdir}/libthriftqt5-%{version}.so

%files devel
%{_includedir}/thrift
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.0
%exclude %{_libdir}/lib*-%{version}.so
%{_libdir}/pkgconfig/thrift-z.pc
%{_libdir}/pkgconfig/thrift-qt5.pc
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
%{php7_extdir}/thrift_protocol.so
%doc LICENSE NOTICE
%endif

%if %{?want_erlang} > 0
%files -n erlang-%{name}
%{_libdir}/erlang/lib/%{name}-%{version}/
%doc LICENSE NOTICE
%endif

%files -n python3-module-thrift
%{python3_sitelibdir}/%{name}
%{python3_sitelibdir}/%{name}-%{version}-py%{__python3_version}.egg-info
%doc LICENSE NOTICE

%if 0%{?want_java} > 0
%files -n lib%{name}-javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%files -n lib%{name}-java -f .mfiles
%doc LICENSE NOTICE
%endif


%changelog
* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_9
- new version

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt8_15jpp8
- fixed build with new java

* Sat Apr 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt7_15jpp8
- + lost binaries for ruby gem
- * rpm tags and syntax
- ! duplication file adding

* Mon Jul 08 2019 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt6_15jpp8
- build to Sisyphus

* Wed Mar 27 2019 Ivan A. Melnikov <iv@altlinux.org> 0.10.0-alt5_15jpp8.0.mips1
- build on mipsel
  + drop mono
  + fix linking with boost_atomic (debian patch)

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt5_15jpp8
- Use Ruby Policy 2.0

* Sat Mar 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt4_15jpp8
- fixed build (closes: #36255)

* Sat Feb 02 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt3_15jpp8
- fixed build

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_15jpp8
- build with new ssl

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_11jpp8
- java fc28+ update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_9jpp8
- rebuild with tomcat9

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_9jpp8
- e2k support; java update

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
