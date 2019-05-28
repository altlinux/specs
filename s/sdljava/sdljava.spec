Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: ruby-stdlibs zlib-devel
BuildRequires: bsh
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           sdljava
Version:        0.9.1
Release:        alt2_43jpp8
Summary:        Java binding to the SDL API
License:        LGPLv2+
URL:            http://sdljava.sourceforge.net/
# this is http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# with the included Microsoft Copyrighted Arial fonts removed
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-runtest.sh
Patch0:         sdljava-0.9.1-regen.patch
Patch1:         sdljava-0.9.1-ftgl213.patch
Patch2:         sdljava-0.9.1-ruby19.patch

BuildRequires:  gcc-c++
BuildRequires:  libftgl-devel
BuildRequires:  libGLEW-devel
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_gfx-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  swig
BuildRequires:  bsh
BuildRequires:  jdom
BuildRequires:  xml-commons-apis

BuildRequires:  jruby
BuildRequires:  %{_bindir}/ruby

Requires:       java
Requires:       javapackages-tools
Requires:       bsh
Requires:       jdom
Source44: import.info

%description
sdljava is a Java binding to the SDL API being developed by Ivan Ganza.

sdljava provides the ability to write games and other applications
from the java programming language. sdljava is designed to be fast,
efficient and easy to use.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc for %{name}.


%package demo
Group: Development/Java
Summary:        Some examples for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-Bold.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-Oblique.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-BoldOblique.ttf

%description demo
Demonstrations and samples for %{name}.


%prep
%setup -q
%patch0 -p1 -z .regen
%patch1 -p1
%patch2 -p1

find -name '*.jar' -or -name '*.class' -or -name '*.bat' -name '*.so' -delete
rm -r etc/build/gljava/windows etc/build/windows

# Newer ftgl no longer exports the FTFace class
rm src/org/gljava/opengl/ftgl/FTFace.java
iconv -f ISO_8859-2 -t UTF8 docs/CHANGES_0_9_1 > docs/CHANGES_0_9_1.tmp
touch -r docs/CHANGES_0_9_1 docs/CHANGES_0_9_1.tmp
mv docs/CHANGES_0_9_1.tmp docs/CHANGES_0_9_1

# patch in gcc include path so that swig can find it
GCC_PATH=`gcc -print-search-dirs | grep install | cut -f 2 -d " "`
sed -i "s#@GCC_INCLUDE_PATH@#$GCC_PATH/include#g" \
  etc/build/linux/Makefile \
  etc/build/gljava/linux/Makefile \
  etc/build/gljava/linux/ftgl/Makefile

# adjust testdata path in demos
find ./testsrc -name '*.java' | xargs sed -i \
  -e 's|testdata|%{_datadir}/%{name}/testdata|g'

# use system versions of bsh & jdom
build-jar-repository -p lib jdom bsh

# copy the Linux Makefiles into place
cp etc/build/linux/Makefile src/sdljava/native
cp etc/build/gljava/linux/Makefile src/org/gljava/opengl/native
cp etc/build/gljava/linux/ftgl/Makefile src/org/gljava/opengl/native/ftgl

# and remove the swig generated code so that it gets regenerated
rm src/sdljava/native/SDL*_wrap.c src/sdljava/native/SDL_types.h
rm src/org/gljava/opengl/native/glew_wrap.c


%build
# We must add -D__%{_arch}__ to swigs arguments as swig doesn't do that itself.
# Special case ppc as the define is powerpc not ppc and both ppc and ppc64
# must be set for ppc64, also add -D__LONG_DOUBLE_128__ which works around
# swig barfing on bits/stdlib-ldbl.h
%ifarch ppc
export ARCH_DEFINE="-D__powerpc__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64le
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LITTLE_ENDIAN__ -D\"__BYTE_ORDER__=1234\" -D\"_CALL_ELF=2\" -D__LONG_DOUBLE_128__"
%endif
%ifarch s390x
export ARCH_DEFINE="-D__s390x__ -D__LONG_DOUBLE_128__"
%endif
# special case ix86 as all of ix86 should define __i386__
%ifarch %{ix86}
export ARCH_DEFINE="-D__i386__"
%endif
# arm also needs a bunch of special defines
%ifarch %{arm}
export ARCH_DEFINE="-D__arm__ -D__ARMEL__ -D__ARM_EABI__"
%ifnarch armv5tel
export ARCH_DEFINE="$ARCH_DEFINE -D__ARM_PCS_VFP"
%endif
%endif
# All other archs
if [ -z "$ARCH_DEFINE" ]; then
  export ARCH_DEFINE="-D__%{_arch}__"
fi

export JAVA_HOME=%{_jvmdir}/java

pushd src/sdljava/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
make libsdljava_gfx.so CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

pushd src/org/gljava/opengl/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

pushd src/org/gljava/opengl/native/ftgl
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd

ant jar javadoc


%install
# dirs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_javadir}
# should be just %{_javadocdir}/%{name} but that is a ghosted symlink in older
# versions and rpm does not grok replacing that with a dir
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# jars
install -m 644 lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# native libraries
install -m 755 lib/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}

# javadoc
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

# demo scripts
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
pushd bin
rm runtest.sh
for i in `ls -1 *.sh`; do
   sed -i -e 's|./runtest.sh|%{_bindir}/%{name}-runtest.sh|g' $i
   FN=`echo $i | awk 'BEGIN { FS="." }{ print $1 }'`
   install -m 755 $i $RPM_BUILD_ROOT%{_bindir}/%{name}-$FN.sh
done
popd

#test data
cp -a testdata $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s ../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arial.ttf
ln -s ../../fonts/ttf/dejavu/DejaVuSans-Bold.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbd.ttf
ln -s ../../fonts/ttf/dejavu/DejaVuSans-Oblique.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/ariali.ttf
ln -s ../../fonts/ttf/dejavu/DejaVuSans-BoldOblique.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbi.ttf


%files
%doc README TODO docs/CHANGES_0_9_1
%{_javadir}/%{name}.jar
%{_libdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}

%files demo
%{_bindir}/%{name}-*.sh
%{_datadir}/%{name}


%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_43jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_40jpp8
- java update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_38jpp8
- new jpp release

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_34jpp8
- new jpp release

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_23jpp7
- rebuild with new SDL

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_23jpp7
- updated release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_21jpp7
- fixed build - use pre-generated sources

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_17jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_16jpp6
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_14jpp6
- update to new release by jppimport

