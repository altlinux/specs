# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: ruby-stdlibs zlib-devel
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           sdljava
Version:        0.9.1
Release:        alt1_17jpp7
Summary:        Java binding to the SDL API
Group:          System/Libraries
License:        LGPLv2+
Url:            http://sdljava.sourceforge.net/
# this is http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# with the included Microsoft Copyrighted Arial fonts removed
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-runtest.sh
Patch0:         sdljava-0.9.1-regen.patch
Patch1:         sdljava-0.9.1-ftgl213.patch
BuildRequires:  ftgl-devel libglew-devel libSDL-devel libSDL_gfx-devel libSDL_image-devel
BuildRequires:  libSDL_mixer-devel libSDL_ttf-devel jpackage-utils
BuildRequires:  java-javadoc ant xml-commons-apis swig bsh jdom ruby
Requires:       bsh jdom
Source44: import.info
Patch33: sdljava-0.9.1-alt-ruby19.patch
Source45: post-process.rb

%description
sdljava is a Java binding to the SDL API being developed by Ivan Ganza.

sdljava provides the ability to write games and other applications
from the java programming language. sdljava is designed to be fast,
efficient and easy to use.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch:      noarch
Requires:       sdljava = %{version}-%{release}

%description javadoc
Javadoc for %{name}.


%package demo
Summary:        Some examples for %{name}
Group:          Development/Java
BuildArch:      noarch
Requires:       sdljava = %{version}-%{release}
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-Bold.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-Oblique.ttf
Requires:       /usr/share/fonts/ttf/dejavu/DejaVuSans-BoldOblique.ttf
Requires:       jpackage-utils

%description demo
Demonstrations and samples for %{name}.


%prep
%setup -q
%patch0 -p1 -z .regen
%patch1 -p1
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
pushd lib
rm *.jar
ln -s /usr/share/java/jdom.jar .
ln -s /usr/share/java/bsh.jar .
popd

# copy the Linux Makefiles into place
cp etc/build/linux/Makefile src/sdljava/native
cp etc/build/gljava/linux/Makefile src/org/gljava/opengl/native
cp etc/build/gljava/linux/ftgl/Makefile src/org/gljava/opengl/native/ftgl

# and remove the swig generated code so that it gets regenerated
rm src/sdljava/native/SDL*_wrap.c src/sdljava/native/SDL_types.h
rm src/org/gljava/opengl/native/glew_wrap.c
%patch33 -p1
cp %{S:45} src/org/gljava/opengl/native/ftgl/post-process.rb


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
# special case ix86 as all of ix86 should define __i386__
%ifarch %{ix86}
export ARCH_DEFINE="-D__i386__"
%endif
# All other archs
if [ -z "$ARCH_DEFINE" ]; then
  export ARCH_DEFINE="-D__%{_arch}__"
fi

#export JAVA_HOME=/usr/lib/jvm/java

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

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc


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
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_17jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_16jpp6
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_14jpp6
- update to new release by jppimport

