# Work around this for now by disabling LTO:
%define optflags_lto %nil

Name:    thrift
Version: 0.14.0
Release: alt2
Summary: Software framework for cross-language services development
Group: Development/Other
ExcludeArch: armh

# Parts of the source are used under the BSD and zlib licenses, but
# these are OK for inclusion in an Apache 2.0-licensed whole:
# https://www.apache.org/legal/3party.html

# Here's the breakdown:
# ./lib/py/compat/win32/stdint.h is 2-clause BSD
# ./compiler/cpp/src/md5.[ch] are zlib
License: ASL 2.0 and BSD and zlib
URL:     https://thrift.apache.org/

Source0: %name-%version.tar

Source1: https://repo1.maven.org/maven2/org/apache/thrift/lib%name/%version/lib%name-%version.pom
Source2: https://raw.github.com/apache/%name/%version/bootstrap.sh

# Fix char warning
# https://issues.apache.org/jira/browse/THRIFT-5350
Patch0: thrift-char.patch

BuildRequires(pre): rpm-build-perl rpm-build-python3
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel perl(CPAN/Meta.pm) perl(Encode.pm) perl(HTTP/Request.pm) perl(IO/Socket/SSL.pm) perl(IO/String.pm) perl(LWP/UserAgent.pm) perl(Test/Exception.pm) perl(parent.pm) perl-podlators
BuildRequires: chrpath
BuildRequires: boost-complete
#BuildRequires: boost-devel-static
BuildRequires: gcc-c++
BuildRequires: glib2-devel libgio libgio-devel
#BuildRequires: libevent-devel # for libthriftnb.so
BuildRequires: libssl-devel
BuildRequires: qt5-base-devel
BuildRequires: texlive-texmf
BuildRequires: zlib-devel

%description
The Apache Thrift software framework for cross-language services
development combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java,
Python, %{?php_langname}and other languages.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %EVR
Requires: boost-complete

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package qt5
Group: Development/Other
Summary: Qt5 support for %{name}
Requires: %name = %EVR

%description qt5
The %{name}-qt package contains Qt bindings for %name.

%package glib
Group: Development/Other
Summary: GLib support for %name
Requires: %name = %EVR

%description glib
The %name-qt package contains GLib bindings for %name.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python 3 support for %name
BuildRequires: python3-devel
BuildRequires: python3-module-pkg_resources python3-module-setuptools
Requires: %name = %EVR

%description -n python3-module-thrift
The python3-%name package contains Python bindings for %name.

%package -n perl-%name
Group: Development/Perl
Summary: Perl support for %{name}
BuildArch: noarch
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

%description -n perl-%name
The perl-%name package contains Perl bindings for %name.

%prep
%setup
%patch0 -p1

# avoid spurious executable permissions in debuginfo package
find . -name \*.cpp -or -name \*.cc -or -name \*.h | xargs -r chmod 644

cp -p %SOURCE2 bootstrap.sh

# work around linking issues
echo 'libthrift_c_glib_la_LIBADD = $(GLIB_LIBS) $(GOBJECT_LIBS) -L../cpp/.libs ' >> lib/c_glib/Makefile.am
echo 'libthriftqt5_la_LIBADD = $(QT_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'libthriftz_la_LIBADD = $(ZLIB_LIBS) -lthrift -L.libs' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftqt5_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftz_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am

# explicitly set python3
shopt -s globstar
sed -i -E 's@^(#!.*/env) *python *$@\1 python3@' **/*.py

%build
export PY_PREFIX=%prefix
export PERL_PREFIX=%prefix
export GLIB_LIBS=$(pkg-config --libs glib-2.0)
export GLIB_CFLAGS=$(pkg-config --cflags glib-2.0)
export GOBJECT_LIBS=$(pkg-config --libs gobject-2.0)
export GOBJECT_CFLAGS=$(pkg-config --cflags gobject-2.0)

find . -name rebar -exec rm -f '{}' \;
find . -name Makefile\* -exec sed -i -e 's/[.][/]rebar/rebar/g' {} \;

sh ./bootstrap.sh

# use unversioned doc dirs where appropriate (via _pkgdocdir macro)
export PYTHON=%{_bindir}/python3
%configure --disable-dependency-tracking --disable-static --with-boost=%prefix \
  --docdir=%_docdir/%name-%version

# eliminate unused direct shlib dependencies
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name fastbinary.so | xargs -r chmod 755
find %buildroot -name \*.erl -or -name \*.hrl -or -name \*.app | xargs -r chmod 644

# Move perl files into appropriate places
find %buildroot -name \*.pod -exec rm -f '{}' \;
find %buildroot -name .packlist -exec rm -f '{}' \;
find %buildroot/usr/lib/perl5 -type d -empty -delete
mkdir -p %buildroot/%perl_vendor_privlib/
mv %buildroot/usr/lib/perl5/* %buildroot/%perl_vendor_privlib

# Fix permissions on Thread.h
find %buildroot -name Thread.h -exec chmod a-x '{}' \;

# Ensure all python scripts are executable
find %buildroot -name \*.py -exec grep -q /usr/bin/env {} \; -print | xargs -r chmod 755
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files
%doc LICENSE NOTICE
%_bindir/thrift
%_libdir/libthrift-%version.so
%_libdir/libthriftz-%version.so
#_libdir/libthriftnb-%version.so

%files glib
%_libdir/libthrift_c_glib.so.*

%files qt5
%_libdir/libthriftqt5-%version.so

%files devel
%_includedir/thrift
%_libdir/*.so
%exclude %_libdir/lib*-%version.so
%_libdir/pkgconfig/thrift-z.pc
%_libdir/pkgconfig/thrift-qt5.pc
#_libdir/pkgconfig/thrift-nb.pc
%_libdir/pkgconfig/thrift.pc
%_libdir/pkgconfig/thrift_c_glib.pc
%doc NOTICE

%files -n perl-%name
%perl_vendor_privlib/Thrift
%perl_vendor_privlib/Thrift.pm
%doc NOTICE

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py*.egg-info

%changelog
* Wed Mar 15 2023 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt2
- fix build
- disable build libthriftnb.so
- cleanup spec
- ExcludeArch: armh

* Wed Jul 27 2022 Igor Vlasenko <viy@altlinux.org> 0.14.0-alt1_10
- new version

* Thu Apr 15 2021 Cronbuild Service <cronbuild@altlinux.org> 0.13.0-alt2_9
- rebuild to get rid of unmets

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
