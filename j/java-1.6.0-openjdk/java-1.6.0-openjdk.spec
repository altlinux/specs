# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xprop /usr/bin/xvfb-run libgif-devel pkgconfig(xproto) pkgconfig(xrender) unzip xorg-xproto-devel zlib-devel
# END SourceDeps(oneline)
BuildRequires: ca-certificates-java
%def_enable accessibility
%def_disable javaws
%def_disable moz_plugin
%def_disable systemtap
BuildRequires: gcc-c++ libstdc++-devel-static 
BuildRequires: libXext-devel libXrender-devel
BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires(pre): rpm-build-java
%set_compress_method none
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
%define fedora 15
%define version 1.6.0.0
%define name java-1.6.0-openjdk
#and If gcjbootstrap is 1 IcedTea is bootstrapped against
# java-1.6.0-sun-devel.  If gcjbootstrap is 0 IcedTea is built against
# java-1.6.0-openjdk-devel.
%define gcjbootstrap 0

# If runtests is 0 test suites will not be run.
%define runtests 0

%define icedteaver 1.11
%define icedteasnapshot %{nil}
%define openjdkver b24
%define openjdkdate 14_nov_2011

%define genurl http://cvs.fedoraproject.org/viewcvs/devel/java-1.6.0-openjdk/

%define accessmajorver 1.23
%define accessminorver 0
%define accessver %{accessmajorver}.%{accessminorver}
%define accessurl http://ftp.gnome.org/pub/GNOME/sources/java-access-bridge/

%define jaxpurl     https://jaxp.dev.java.net/files/documents/913/150648/
%define jafurl      https://jax-ws.dev.java.net/files/documents/4202/150725/
%define jaxwsurl    https://jax-ws.dev.java.net/files/documents/4202/150724/

%define openjdkurlbase http://www.java.net/download/openjdk/jdk6/promoted/
%define openjdkurl %{openjdkurlbase}%{openjdkver}/
%define fedorazip  openjdk-6-src-%{openjdkver}-%{openjdkdate}-fedora.tar.gz

%define mauvedate 2008-10-22

%define multilib_arches ppc64 sparc64 x86_64

%define jit_arches %{ix86} x86_64 sparcv9 sparc64

%ifarch %{ix86}
%define archbuild i586
%define archinstall i386
%endif
%ifarch x86_64
%define archbuild amd64
%define archinstall amd64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%define archbuild sparc
%define archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%define archbuild sparcv9
%define archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%define archbuild %{_arch}
%define archinstall %{_arch}
%endif

# Reduce build time from 27 hours to 12 hours by only running test
# suites on JIT architectures.
%ifnarch %{jit_arches}
%define runtests 0
%endif

%define buildoutputdir openjdk.build

%if %{gcjbootstrap}
%if_enabled systemtap
%define icedteaopt %{subst_enable systemtap}
%else
%define icedteaopt %{nil}
%endif
%else
%if_enabled systemtap
%define icedteaopt --disable-bootstrap --with-jdk-home=/usr/lib/jvm/java-openjdk %{subst_enable systemtap}
%else
%define icedteaopt --disable-bootstrap --with-jdk-home=/usr/lib/jvm/java-openjdk
%endif
%endif

# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%define script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%define abs2rel %{__perl} -e %{script}

# Hard-code libdir on 64-bit architectures to make the 64-bit JDK
# simply be another alternative.
%ifarch %{multilib_arches}
# define syslibdir       %{_prefix}/lib64
# define _libdir         %{_prefix}/lib
%define archname        %{name}.%{_arch}
%else
# define syslibdir       %{_libdir}
%define archname        %{name}
%endif

# Standard JPackage naming and versioning defines.
%define origin          openjdk
%define priority        16000
%define javaver         1.6.0
%define buildver        0

# Standard JPackage directories and symbolic links.
# Make 64-bit JDKs just another alternative on 64-bit architectures.
%ifarch %{multilib_arches}
%define sdklnk          java-%{javaver}-%{origin}.%{_arch}
%define jrelnk          jre-%{javaver}-%{origin}.%{_arch}
%define sdkdir          %{name}-%{version}.%{_arch}
%else
%define sdklnk          java-%{javaver}-%{origin}
%define jrelnk          jre-%{javaver}-%{origin}
%define sdkdir          %{name}-%{version}
%endif
%define jredir          %{sdkdir}/jre
%define sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%define jrebindir       %{_jvmdir}/%{jrelnk}/bin
%ifarch %{multilib_arches}
%define jvmjardir       %{_jvmjardir}/%{name}-%{version}.%{_arch}
%else
%define jvmjardir       %{_jvmjardir}/%{name}-%{version}
%endif

%ifarch %{jit_arches}
# Where to install systemtap tapset (links)
# We would like these to be in a package specific subdir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinquish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
#%define tapsetdir	/usr/share/systemtap/tapset/%{sdkdir}
%define tapsetdir	/usr/share/systemtap/tapset/%{_build_cpu}
%endif

# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{buildver}
Release: alt19_65.1.11jpp6
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons,
# and this change was brought into RHEL-4.  java-1.5.0-ibm packages
# also included the epoch in their virtual provides.  This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0".  In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0.  So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages.  Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".
Epoch:   0
Summary: OpenJDK Runtime Environment
Group:   Development/Java

License:  GPLv2 with exceptions
URL:      http://icedtea.classpath.org/
Source0:  %{url}download/source/icedtea6-%{icedteaver}%{icedteasnapshot}.tar.gz
Source1:  %{fedorazip}
Source2:  %{accessurl}%{accessmajorver}/java-access-bridge-%{accessver}.tar.bz2
Source3:  %{genurl}generate-fedora-zip.sh
Source4:  README.src
Source5:  mauve-%{mauvedate}.tar.gz
Source6:  mauve_tests
Source7:  %{jaxpurl}jaxp144_03.zip
Source8:  %{jafurl}jdk6-jaf-b20.zip
Source9: %{jaxwsurl}jdk6-jaxws2_1_6-2011_06_13.zip
# FIXME: This patch needs to be fixed. optflags argument
# -mtune=generic is being ignored because it breaks several graphical
# applications.
Patch0:   java-1.6.0-openjdk-optflags.patch
Patch1:   java-1.6.0-openjdk-java-access-bridge-tck.patch
Patch2:   java-1.6.0-openjdk-java-access-bridge-idlj.patch
Patch3:	  java-1.6.0-openjdk-java-access-bridge-security.patch
Patch4:   java-1.6.0-openjdk-accessible-toolkit.patch


BuildRequires: libalsa-devel
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
BuildRequires: libungif-devel
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXp-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: wget
#BuildRequires: xalan-j2
#BuildRequires: xerces-j2
BuildRequires: xsltproc libxslt
BuildRequires: xorg-x11-proto-devel
BuildRequires: mercurial
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: libXinerama-devel
BuildRequires: rhino
%if %{gcjbootstrap}
BuildRequires: java-1.6.0-sun-devel
%else
BuildRequires: java-1.6.0-openjdk-devel
%endif
# Mauve build requirements.
BuildRequires: xorg-x11-xvfb
BuildRequires: fonts-type1-xorg
BuildRequires: fonts-bitmap-misc
BuildRequires: libfreetype-devel >= 2.3.0
BuildRequires: fontconfig
BuildRequires: eclipse-ecj
# Java Access Bridge for GNOME build requirements.
#BuildRequires: libat-spi-devel
BuildRequires: gawk
BuildRequires: libbonobo-devel
BuildRequires: xorg-x11-utils
# PulseAudio build requirements.
BuildRequires: libpulseaudio-devel >= 0.9.11
BuildRequires: pulseaudio >= 0.9.11
# Zero-assembler build requirement.
%ifnarch %{jit_arches}
BuildRequires: libffi-devel
%endif
%if_enabled systemtap
#systemtap build requirement.
BuildRequires: systemtap-sdt-devel
%endif
#fixing  648499

#fix for rhbz721033
Requires: fonts-type1-xorg
Requires: fontconfig
Requires: rhino
#Requires: libjpeg = 6b
%if 0%{?fedora} > 9
# Require /etc/pki/java/cacerts.
Requires: ca-certificates
%else
# Require /etc/pki/tls/certs/ca-bundle.crt instead of generating
# cacerts.
Requires: openssl
%endif
# Require jpackage-utils for ant.
Requires: jpackage-utils >= 1.7.3-1jpp.2
# Require zoneinfo data provided by tzdata-java subpackage.
Requires: tzdata-java
# Post requires alternatives to install tool alternatives.
Requires(post):   alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): alternatives

# java-1.6.0-openjdk replaces java-1.7.0-icedtea.
#Provides: java-1.7.0-icedtea = 0:1.7.0.0-0.999
#Obsoletes: java-1.7.0-icedtea < 0:1.7.0.0-0.999

# Standard JPackage base provides.
Provides: jre6-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre6-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre6-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java6-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre6 = %{javaver}
Provides: java6-%{origin} = %{epoch}:%{version}-%{release}
Provides: java6 = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: jndi6 = %{epoch}:%{version}
Provides: jndi6-ldap = %{epoch}:%{version}
Provides: jndi6-cos = %{epoch}:%{version}
Provides: jndi6-rmi = %{epoch}:%{version}
Provides: jndi6-dns = %{epoch}:%{version}
Provides: jaas6 = %{epoch}:%{version}
Provides: jsse6 = %{epoch}:%{version}
Provides: jce6 = %{epoch}:%{version}
Provides: jdbc6-stdext = 3.0
Provides: java6-sasl = %{epoch}:%{version}
Provides: java6-fonts = %{epoch}:%{version}
Source44: import.info
# jpp provides
Provides: java = %version
Provides: java-1.6.0 = %version
Provides: java-openjdk = %version
Provides: java-sasl = %version
#define mozilla_java_plugin_so %{_jvmdir}/%{jrelnk}/lib/%{archinstall}/gcjwebplugin.so
%define mozilla_java_plugin_so %{_jvmdir}/%{jrelnk}/lib/%{archinstall}/IcedTeaPlugin.so
%define altname %name
%define label -%{name}
%define javaws_ver      %{javaver}

# it is needed for those apps which links with libjvm.so
%add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%archinstall/server
%ifnarch x86_64
%add_findprov_lib_path %{_jvmdir}/%{jredir}/lib/%archinstall/client
%endif

%ifarch x86_64
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
%endif
%ifarch %ix86
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/client/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/client/libjvm.so(SUNWprivate_1.1)
%endif
Requires: java-common
Requires: /proc

%description
The OpenJDK runtime environment.

%package devel
Summary: OpenJDK Development Environment
Group:   Development/Java

# Require base package.
Requires:         %{name} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives.
Requires(post):   alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): alternatives

# java-1.6.0-openjdk-devel replaces java-1.7.0-icedtea-devel.
#Provides: java-1.7.0-icedtea-devel = 0:1.7.0.0-0.999
#Obsoletes: java-1.7.0-icedtea-devel < 0:1.7.0.0-0.999

# Standard JPackage devel provides.
Provides: java6-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java6-sdk-%{javaver} = %{epoch}:%{version}
Provides: java6-sdk-%{origin} = %{epoch}:%{version}
Provides: java6-sdk = %{epoch}:%{javaver}
Provides: java6-%{javaver}-devel = %{epoch}:%{version}
Provides: java6-devel-%{origin} = %{epoch}:%{version}
Provides: java6-devel = %{epoch}:%{javaver}
# jpp provides
Provides: java-1.6.0-devel = %version
Provides: java-devel = %version
Provides: java-devel-openjdk = %version

# hack for missing java 1.5.0 on ppc
%ifarch ppc ppc64
Provides: java-devel = 1.5.0
%endif

%description devel
The OpenJDK development tools.

%package demo
Summary: OpenJDK Demos
Group:   Development/Java

Requires: %{name} = %{epoch}:%{version}-%{release}

# java-1.6.0-openjdk-demo replaces java-1.7.0-icedtea-demo.
#Provides: java-1.7.0-icedtea-demo = 0:1.7.0.0-0.999
#Obsoletes: java-1.7.0-icedtea-demo < 0:1.7.0.0-0.999

%description demo
The OpenJDK demos.

%package src
Summary: OpenJDK Source Bundle
Group:   Development/Java

Requires: %{name} = %{epoch}:%{version}-%{release}

%description src
The OpenJDK source bundle.

%package javadoc
Summary: OpenJDK API Documentation
Group:   Development/Java

# Post requires alternatives to install javadoc alternative.
Requires(post):   alternatives
# Postun requires alternatives to uninstall javadoc alternative.
Requires(postun): alternatives

# java-1.6.0-openjdk-javadoc replaces java-1.7.0-icedtea-javadoc.
#Provides: java-1.7.0-icedtea-javadoc = 0:1.7.0.0-0.999
#Obsoletes: java-1.7.0-icedtea-javadoc < 0:1.7.0.0-0.999

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch
# fc provides
Provides: java-javadoc = 1:1.6.0

%description javadoc
The OpenJDK API documentation.


%prep
%setup -q -n icedtea6-%{icedteaver}
%setup -q -n icedtea6-%{icedteaver} -T -D -a 5
%setup -q -n icedtea6-%{icedteaver} -T -D -a 2
#%patch0
cp %{SOURCE4} .
cp %{SOURCE6} .

%build
unset JAVA_HOME
%autoreconf
# Build IcedTea and OpenJDK.
%ifarch sparc64 alpha
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

./autogen.sh
./configure %{icedteaopt} --with-openjdk-src-zip=%{SOURCE1} \
  --with-pkgversion=ALTLinux-%{release}-%{_arch} --enable-pulse-java \
  --with-jaf-drop-zip=%{SOURCE8} \
  --with-jaxp-drop-zip=%{SOURCE7} --with-jaxws-drop-zip=%{SOURCE9} \
  --with-abs-install-dir=%{_jvmdir}/%{sdkdir}
%if %{gcjbootstrap}
make MEMORY_LIMIT=-J-Xmx512m stamps/patch-ecj.stamp
%endif

make MEMORY_LIMIT=-J-Xmx512m patch
patch -l -p0 < %{PATCH3}
patch -l -p0 < %{PATCH4}
make MEMORY_LIMIT=-J-Xmx512m

export JAVA_HOME=$(pwd)/%{buildoutputdir}/j2sdk-image

%if_with java_access_bridge
# Build Java Access Bridge for GNOME.
pushd java-access-bridge-%{accessver}
  patch -l -p1 < %{PATCH1}
  patch -l -p1 < %{PATCH2}
  OLD_PATH=$PATH
  export PATH=$JAVA_HOME/bin:$OLD_PATH
  ./configure
make MEMORY_LIMIT=-J-Xmx512m
  export PATH=$OLD_PATH
  cp -a bridge/accessibility.properties $JAVA_HOME/jre/lib
  cp -a gnome-java-bridge.jar $JAVA_HOME/jre/lib/ext
popd
%endif
%if %{runtests}
# Run jtreg test suite.
{
  echo ====================JTREG TESTING========================
  export DISPLAY=:20
  Xvfb :20 -screen 0 1x1x24 -ac&
  echo $! > Xvfb.pid
make MEMORY_LIMIT=-J-Xmx512m jtregcheck -k
  kill -9 `cat Xvfb.pid` || :
  unset DISPLAY
  rm -f Xvfb.pid
  echo ====================JTREG TESTING END====================
} || :

# Run Mauve test suite.
{
  pushd mauve-%{mauvedate}
    ./configure
make MEMORY_LIMIT=-J-Xmx512m
    echo ====================MAUVE TESTING========================
    export DISPLAY=:20
    Xvfb :20 -screen 0 1x1x24 -ac&
    echo $! > Xvfb.pid
    $JAVA_HOME/bin/java Harness -vm $JAVA_HOME/bin/java \
      -file %{SOURCE6} -timeout 30000 2>&1 | tee mauve_output
    kill -9 `cat Xvfb.pid` || :
    unset DISPLAY
    rm -f Xvfb.pid
    echo ====================MAUVE TESTING END====================
  popd
} || :
%endif

%install
unset JAVA_HOME

pushd %{buildoutputdir}/j2sdk-image

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

%if_enabled systemtap
  # Install systemtap support files.
  cp -a tapset $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  pushd $RPM_BUILD_ROOT%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    ln -sf $RELATIVE/*.stp .
  popd
%endif

%if 0%{?fedora} > 9
  # Install cacerts symlink.
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/cacerts
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
    RELATIVE=$(%{abs2rel} %{_sysconfdir}/pki/java \
      %{_jvmdir}/%{jredir}/lib/security)
    ln -sf $RELATIVE/cacerts .
  popd
%endif

  # Install extension symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{jvmjardir}
  pushd $RPM_BUILD_ROOT%{jvmjardir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{jredir}/lib %{jvmjardir})
    ln -sf $RELATIVE/jsse.jar jsse-%{version}.jar
    ln -sf $RELATIVE/jce.jar jce-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-ldap-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-cos-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-rmi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jaas-%{version}.jar
    ln -sf $RELATIVE/rt.jar jdbc-stdext-%{version}.jar
    ln -sf jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
    ln -sf $RELATIVE/rt.jar sasl-%{version}.jar
    for jar in *-%{version}.jar
    do
      if [ x%{version} != x%{javaver} ]
      then
        ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      fi
      ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|.jar|g")
    done
  popd

  # Install JCE policy symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{archname}/jce/vanilla

  # Install versionless symlinks.
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{jredir} %{jrelnk}
    ln -sf %{sdkdir} %{sdklnk}
  popd

  pushd $RPM_BUILD_ROOT%{_jvmjardir}
    ln -sf %{sdkdir} %{jrelnk}
    ln -sf %{sdkdir} %{sdklnk}
  popd

  # Install man pages.
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding.
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{name}.1
  done

  # Install demos and samples.
  cp -a demo $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  mkdir -p sample/rmi
  #mv bin/java-rmi.cgi sample/rmi
  cp -a sample $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

popd

# Install Javadoc documentation.
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java.png
done

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole policytool ; do
    desktop-file-install  --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# Find JRE directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type d \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}.files
# Find JRE files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir} -type f -o -type l \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}.files
# Find demo directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample -type d \
  | sed 's|'$RPM_BUILD_ROOT'|%%dir |' \
  > %{name}-demo.files

# FIXME: remove SONAME entries from demo DSOs.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}-demo.files
# Find documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%%doc |' \
  >> %{name}-demo.files
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javadocdir_java-1.6.0-openjdk-javadoc<<EOF
%{_javadocdir}/java	%{_javadocdir}/%{name}/api	%{priority}
EOF

%__subst 's,^Categories=.*,Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/policytool.desktop
%__subst 's,^Categories=.*,Categories=Development;Profiling;System;Monitor;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/jconsole.desktop

# HACK around find-requires
%define __find_requires    $RPM_BUILD_ROOT/.find-requires
cat > $RPM_BUILD_ROOT/.find-requires <<EOF
(/usr/lib/rpm/find-requires | grep -v %{_jvmdir}/%{sdkdir} | grep -v /usr/bin/java | sed -e s,^/usr/lib64/lib,lib, | sed -e s,^/usr/lib/lib,lib,) || :
EOF
chmod 755 $RPM_BUILD_ROOT/.find-requires
# end HACK around find-requires

##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/jvisualvm ]; then
  cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-jvisualvm.desktop << EOF
[Desktop Entry]
Name=Java VisualVM (%{name})
Comment=Java Virtual Machine Monitoring, Troubleshooting, and Profiling Tool
Exec=jvisualvm
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
fi

%if_enabled moz_plugin
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java Plugin Control Panel (%{name})
Comment=Java Control Panel
Exec=jcontrol
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

%if_enabled javaws
# javaws freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-javaws.desktop << EOF
[Desktop Entry]
Name=Java Web Start (%{name})
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=%{_jvmdir}/%{jredir}/bin/javaws %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

# Install substitute rules for buildreq
echo java >j2se-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

%__install -d %buildroot%_altdir

# J2SE alternative
%__cat <<EOF >%buildroot%_altdir/%altname-java
%{_bindir}/java	%{_jvmdir}/%{jredir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# binaries and manuals
for i in keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  %__cat <<EOF >>%buildroot%_altdir/%altname-java
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
done

# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-java
%{_jvmdir}/jre	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{origin}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmjardir}/jre-%{javaver}	%{_jvmjardir}/%{jrelnk}	%{_jvmdir}/%{jredir}/bin/java
EOF
%if_enabled moz_plugin
%__cat <<EOF >>%buildroot%_altdir/%altname-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{jredir}/bin/ControlPanel	%{_jvmdir}/%{jredir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{jredir}/bin/jcontrol	%{_jvmdir}/%{jredir}/bin/java
EOF
%endif
# JPackage specific: alternatives for security policy
if [ -e %buildroot%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar ]; then
    %__cat <<EOF >>%buildroot%_altdir/%altname-java
%{_jvmdir}/%{jrelnk}/lib/security/local_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar	%{priority}
%{_jvmdir}/%{jrelnk}/lib/security/US_export_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/US_export_policy.jar	%{_jvmprivdir}/%{name}/jce/vanilla/local_policy.jar
EOF
fi
# ----- end: JPackage compatibility alternatives ------


# Javac alternative
%__cat <<EOF >%buildroot%_altdir/%altname-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_prefix/lib/jdk	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
fi
done

# ----- JPackage compatibility alternatives ------
  %__cat <<EOF >>%buildroot%_altdir/%altname-javac
%{_jvmdir}/java	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{origin}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmjardir}/java-%{javaver}	%{_jvmjardir}/%{sdklnk}	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
# ----- end: JPackage compatibility alternatives ------

%if_enabled moz_plugin
# Mozilla plugin alternative
%__cat <<EOF >%buildroot%_altdir/%name-mozilla
%browser_plugins_path/libjavaplugin_oji.so	%mozilla_java_plugin_so	%priority
EOF
%endif	# enabled moz_plugin

%if_enabled javaws
# Java Web Start alternative
%__cat <<EOF >%buildroot%_altdir/%altname-javaws
%_bindir/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/javaws.1.gz	%_man1dir/javaws%label.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- JPackage compatibility alternatives ------
%__cat <<EOF >>%buildroot%_altdir/%altname-javaws
%{_datadir}/javaws	%{_jvmdir}/%{jredir}/bin/javaws	%{_jvmdir}/%{jredir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------
%endif	# enabled javaws

# hack (see altbug #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

%post
%force_update_alternatives

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################




%files -f %{name}.files
%_altdir/%altname-java
%_sysconfdir/buildreqs/packages/substitute.d/%name
%doc %{buildoutputdir}/j2sdk-image/jre/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/j2sdk-image/jre/LICENSE
#%doc %{buildoutputdir}/j2sdk-image/jre/README.html
%doc %{buildoutputdir}/j2sdk-image/jre/THIRD_PARTY_README
# FIXME: The TRADEMARK file should be in j2sdk-image.
%doc openjdk/TRADEMARK
%doc AUTHORS
%doc COPYING
#doc ChangeLog
%doc NEWS
%doc README
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%{_datadir}/icons/hicolor/*x*/apps/java.png
%{_mandir}/man1/java-%{name}.1*
%{_mandir}/man1/keytool-%{name}.1*
%{_mandir}/man1/orbd-%{name}.1*
%{_mandir}/man1/pack200-%{name}.1*
%{_mandir}/man1/rmid-%{name}.1*
%{_mandir}/man1/rmiregistry-%{name}.1*
%{_mandir}/man1/servertool-%{name}.1*
%{_mandir}/man1/tnameserv-%{name}.1*
%{_mandir}/man1/unpack200-%{name}.1*
%{_jvmdir}/%{jredir}/lib/security/nss.cfg
%{_sysconfdir}/.java/
%{_sysconfdir}/.java/.systemPrefs

%files devel
%_altdir/%altname-javac
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%doc %{buildoutputdir}/j2sdk-image/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/j2sdk-image/LICENSE
#%doc %{buildoutputdir}/j2sdk-image/README.html
%doc %{buildoutputdir}/j2sdk-image/THIRD_PARTY_README
# FIXME: The TRADEMARK file should be in j2sdk-image.
%doc openjdk/TRADEMARK
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%if_enabled systemtap
%dir %{_jvmdir}/%{sdkdir}/tapset
%endif
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*
%if_enabled systemtap
%{_jvmdir}/%{sdkdir}/tapset/*.stp
%endif
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%{_datadir}/applications/*jconsole.desktop
%{_datadir}/applications/*policytool.desktop
%{_mandir}/man1/appletviewer-%{name}.1*
%{_mandir}/man1/apt-%{name}.1*
%{_mandir}/man1/extcheck-%{name}.1*
%{_mandir}/man1/idlj-%{name}.1*
%{_mandir}/man1/jar-%{name}.1*
%{_mandir}/man1/jarsigner-%{name}.1*
%{_mandir}/man1/javac-%{name}.1*
%{_mandir}/man1/javadoc-%{name}.1*
%{_mandir}/man1/javah-%{name}.1*
%{_mandir}/man1/javap-%{name}.1*
%{_mandir}/man1/jconsole-%{name}.1*
%{_mandir}/man1/jdb-%{name}.1*
%{_mandir}/man1/jhat-%{name}.1*
%{_mandir}/man1/jinfo-%{name}.1*
%{_mandir}/man1/jmap-%{name}.1*
%{_mandir}/man1/jps-%{name}.1*
%{_mandir}/man1/jrunscript-%{name}.1*
%{_mandir}/man1/jsadebugd-%{name}.1*
%{_mandir}/man1/jstack-%{name}.1*
%{_mandir}/man1/jstat-%{name}.1*
%{_mandir}/man1/jstatd-%{name}.1*
%{_mandir}/man1/native2ascii-%{name}.1*
%{_mandir}/man1/policytool-%{name}.1*
%{_mandir}/man1/rmic-%{name}.1*
%{_mandir}/man1/schemagen-%{name}.1*
%{_mandir}/man1/serialver-%{name}.1*
%{_mandir}/man1/wsgen-%{name}.1*
%{_mandir}/man1/wsimport-%{name}.1*
%{_mandir}/man1/xjc-%{name}.1*
%if_enabled systemtap
%{tapsetdir}/*.stp
%endif

%files demo -f %{name}-demo.files

%files src
%doc README.src
%{_jvmdir}/%{sdkdir}/src.zip
%if %{runtests}
# FIXME: put these in a separate testresults subpackage.
%doc mauve_tests
%doc mauve-%{mauvedate}/mauve_output
%doc test/jtreg-summary.log
%endif

%files javadoc
%_altdir/javadocdir_java-1.6.0-openjdk-javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt19_65.1.11jpp6
- dropped libat-spi dependency

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt18_65.1.11jpp6
- fixed build

* Tue Feb 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt17_65.1.11jpp6
- restored jpackage jvm provides

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt16_65.1.11jpp6
- new version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt16_59.1.10.3jpp6
- updated Requires.

* Thu Sep 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt15_59.1.10.3jpp6
- update to new release by jppimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt15_50.1.9.4jpp6
- hack around #25027 (no java cacerts in ca-certificates):
  use fedora cacerts for the time being.

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt14_50.1.9.4jpp6
- new release

* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt14_44.1.9.1jpp6
- new release

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt14_37.b17jpp6
- new release

* Thu Oct 21 2010 Dmitry V. Levin <ldv@altlinux.org> 0:1.6.0.0-alt14_35.b17jpp6
- Dropped invalid and redundant manual libjpeg package requirement.

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt13_35.b17jpp6
- rebuild with new netbeans

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt12_35.b17jpp6
- rebuild with new netbeans

* Thu Jan 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt12_33.b16jpp6
- new version

* Thu Jan 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt12_31.b16jpp6
- new version

* Sat Oct 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt12_19.b14jpp6
- added commpn libjvm.so provides

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt11_19.b14jpp6
- cleaned parasite autoreqs, added libjvm.so provides

* Wed Sep 30 2009 Alexey Gladkov <legion@altlinux.ru> 0:1.6.0.0-alt10_19.b14jpp6.1
- NMU: Rebuilt with browser-plugins-npapi.

* Fri May 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt10_19.b14jpp6
- new build b14. note: yet w/o liveconnect mozilla plug-in
  due to too fresh xulrunner

* Wed Feb 18 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt10_2b12jpp6
- powerpc fixes

* Sat Jan 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt9_2b12jpp6
- fixes in alternatives

* Sun Dec 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt8_2b12jpp6
- built with visualvm and netbeans support

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt7_2b12jpp6
- converted from JPackage by jppimport script

* Sat Aug 09 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt6_0.16.b09jpp6
- spec cleanup; added provides: j2se

* Mon Aug 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt5_0.16.b09jpp6
- fixes in gccwebplugin

* Mon Aug 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt4_0.16.b09jpp6
- fixes in gccwebplugin

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt3_0.16.b09jpp5
- non-bootstrap build

* Fri Jun 27 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0.0-alt3_0.10.b09jpp6
- converted from JPackage by jppimport script

