# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/java /usr/bin/xprop
# END SourceDeps(oneline)
BuildRequires: ca-certificates-java
%def_enable accessibility
%def_disable javaws
%def_disable moz_plugin
%def_disable systemtap
%def_disable desktop
BuildRequires: gcc-c++ libstdc++-devel-static 
BuildRequires: libXext-devel libXrender-devel
BuildRequires(pre): browser-plugins-npapi-devel
BuildRequires(pre): rpm-build-java
%set_compress_method none
%define with_systemtap 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-1.7.0-openjdk
%define version 1.7.0.3
# If gcjbootstrap is 1 OpenJDK is bootstrapped against
# java-1.6.0-sun-devel.  If gcjbootstrap is 0 OpenJDK is built against
# java-1.6.0-openjdk-devel.
%global gcjbootstrap 0

# If debug is 1, OpenJDK is built with all debug info present.
%global debug 0

# If runtests is 0 test suites will not be run.
%global runtests 0

%global icedtea_version 2.2.1
%global hg_tag icedtea-{icedtea_version}

%global accessmajorver 1.23
%global accessminorver 0
%global accessver %{accessmajorver}.%{accessminorver}
%global accessurl http://ftp.gnome.org/pub/GNOME/sources/java-access-bridge/

%global mauvedate 2008-10-22

%global multilib_arches ppc64 sparc64 x86_64

%global jit_arches %{ix86} x86_64 sparcv9 sparc64

%ifarch x86_64
%global archbuild amd64
%global archinstall amd64
%endif
%ifarch ppc
%global archbuild ppc
%global archinstall ppc
%global archdef PPC
%endif
%ifarch ppc64
%global archbuild ppc64
%global archinstall ppc64
%global archdef PPC
%endif
%ifarch %{ix86}
%global archbuild i586
%global archinstall i386
%endif
%ifarch ia64
%global archbuild ia64
%global archinstall ia64
%endif
%ifarch s390
%global archbuild s390
%global archinstall s390
%global archdef S390
%endif
%ifarch s390x
%global archbuild s390x
%global archinstall s390x
%global archdef S390
%endif
%ifarch %{arm}
%global archbuild arm
%global archinstall arm
%global archdef ARM
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archbuild sparc
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archbuild sparcv9
%global archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%global archbuild %{_arch}
%global archinstall %{_arch}
%endif

%if %{debug}
%global debugbuild debug_build
%else
%global debugbuild %{nil}
%endif

%global buildoutputdir openjdk/build/linux-%{archbuild}

%global with_pulseaudio 1

%if_enabled systemtap
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel %{__perl} -e %{script}

# Hard-code libdir on 64-bit architectures to make the 64-bit JDK
# simply be another alternative.
%ifarch %{multilib_arches}
%global syslibdir       %{_libdir}
%global archname        %{name}.%{_arch}
%else
%global syslibdir       %{_libdir}
%global archname        %{name}
%endif

# Standard JPackage naming and versioning defines.
%global origin          openjdk
%global priority        17000
%global javaver         1.7.0
%global buildver        3

# Standard JPackage directories and symbolic links.
# Make 64-bit JDKs just another alternative on 64-bit architectures.
%ifarch %{multilib_arches}
%global sdklnk          java-%{javaver}-%{origin}.%{_arch}
%global jrelnk          jre-%{javaver}-%{origin}.%{_arch}
%global sdkdir          %{name}-%{version}.%{_arch}
%else
%global sdklnk          java-%{javaver}-%{origin}
%global jrelnk          jre-%{javaver}-%{origin}
%global sdkdir          %{name}-%{version}
%endif
%global jredir          %{sdkdir}/jre
%global sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%global jrebindir       %{_jvmdir}/%{jrelnk}/bin
%ifarch %{multilib_arches}
%global jvmjardir       %{_jvmjardir}/%{name}-%{version}.%{_arch}
%else
%global jvmjardir       %{_jvmjardir}/%{name}-%{version}
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
%global tapsetroot /usr/share/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{_build_cpu}
%endif

# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{buildver}
Release: alt3_2.2.1.8jpp7
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

License:  ASL 1.1 and ASL 2.0 and GPL+ and GPLv2 and GPLv2 with exceptions and LGPL+ and LGPLv2 and MPLv1.0 and MPLv1.1 and Public Domain and W3C
URL:      http://openjdk.java.net/

#head
#REPO=http://icedtea.classpath.org/hg/icedtea7-forest
#current release
#REPO=http://icedtea.classpath.org/hg/release/icedtea7-forest-2.2
# hg clone $REPO/ openjdk -r %{hg_tag}
# hg clone $REPO/corba/ openjdk/corba -r %{hg_tag}
# hg clone $REPO/hotspot/ openjdk/hotspot -r %{hg_tag}
# hg clone $REPO/jaxp/ openjdk/jaxp -r %{hg_tag}
# hg clone $REPO/jaxws/ openjdk/jaxws -r %{hg_tag}
# hg clone $REPO/jdk/ openjdk/jdk -r %{hg_tag}
# hg clone $REPO/langtools/ openjdk/langtools -r %{hg_tag}
# find openjdk -name ".hg" -exec rm -rf '{}' \;
# find openjdk -name ".hgtags" -exec rm -rf '{}' \;
# tar czf openjdk-icedtea-%{icedtea_version}.tar.gz openjdk
Source0:  openjdk-icedtea-%{icedtea_version}.tar.gz

# Gnome access bridge
Source1:  %{accessurl}%{accessmajorver}/java-access-bridge-%{accessver}.tar.bz2

# README file
Source2:  README.src

# Mauve test suite
# FIXME: Is this applicable for 7?
Source3:  mauve-%{mauvedate}.tar.gz
Source4:  mauve_tests

# javac wrapper (used during bootstrap to strip what ecj doesn't support)
Source5: javac-wrapper

# Auto-generated files (used only in bootstrap)
# To reproduce: 
# build OpenJDK7 tarball above with any JDK
# mv generated.build generated
# tar czf generated-files.tar.gz generated
Source6: generated-files.tar.gz

# Class rewrite to rewrite rhino hierarchy
Source7: class-rewriter.tar.gz

# Systemtap tapsets. Zipped up to keep it small.
Source8: systemtap-tapset.tar.gz

# .desktop files. Zipped up to keep it small.
Source9: desktop-files.tar.gz

# nss configuration file
Source10: nss.cfg

# FIXME: Taken from IcedTea snapshot 877ad5f00f69, but needs to be moved out
# hg clone -r 877ad5f00f69 http://icedtea.classpath.org/hg/icedtea7
Source11: pulseaudio.tar.gz

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# RPM/distribution specific patches

# Allow TCK to pass with access bridge wired in
Patch1:   java-1.7.0-openjdk-java-access-bridge-tck.patch

# Adjust idlj compilation switches to match what system idlj supports
Patch2:   java-1.7.0-openjdk-java-access-bridge-idlj.patch

# Disable access to access-bridge packages by untrusted apps
Patch3:   java-1.7.0-openjdk-java-access-bridge-security.patch

# Ignore AWTError when assistive technologies are loaded 
Patch4:   java-1.7.0-openjdk-accessible-toolkit.patch

# Build docs even in debug
Patch5:   java-1.7.0-openjdk-debugdocs.patch

# Add debuginfo where missing
Patch6:   %{name}-debuginfo.patch

#
# OpenJDK specific patches
#

# Add rhino support
Patch100: rhino.patch

# Type fixing for s390
Patch101: %{name}-bitmap.patch
Patch102: %{name}-size_t.patch

# Patches for Arm
Patch103: %{name}-arm-fixes.patch

# Patch for PPC/PPC64
Patch104: %{name}-ppc-zero-jdk.patch
Patch105: %{name}-ppc-zero-hotspot.patch

#
# Bootstrap patches (code with this is never shipped)
#

# Explicitly set javac, so that the bootstrap version is used
Patch200: bootstrap-ant-javac.patch

# Adjusted generated sources path to use prebuilt ones
Patch201: bootstrap-corba-defs.patch

# Do not use idlj to generate sources, as we use prebuilt ones
Patch202: bootstrap-corba-idlj.patch

# Disable decending into sources dir for generation
Patch203: bootstrap-corba-no-gen.patch

# Explicitly compile ORB.java
Patch204: bootstrap-corba-orb.patch

# Don't build demos in bootstrap
Patch205: bootstrap-demos.patch

# Change hex constants to be numbers instead of 0x... so that ecj can compile them right
Patch206: bootstrap-ecj-fphexconstants.patch

# Adjust opt flags to remove what ecj doesn't support
Patch207: bootstrap-ecj-opts.patch

# use pre-generated font config files
Patch208: bootstrap-fontconfig.patch

# Don't write auto-generation message in bootstrap
Patch209: bootstrap-generated-comments.patch

# Adjust bootclasspath to match what ecj has
Patch210: bootstrap-xbootclasspath.patch

# Wire in icedtea rt.jar (FIXME: name needs update, kept same for now to match icedtea name)
Patch211: bootstrap-icedteart.patch

# Wire in custom compiles rt classes
Patch212: bootstrap-jar.patch

# Compile inner opengl class explicitly
Patch213: bootstrap-javah.patch

# Disable ct.sym creation for bootstrap
Patch214: bootstrap-symbols.patch

# Disable icon generation for bootstrap
Patch215: bootstrap-tobin.patch

# Don't run test_gamma
Patch216: bootstrap-test_gamma.patch

# Disable requirement of module_lib path which bootstrap java_home doesn't have
Patch217: bootstrap-tools.jar.patch

# Allow -J opts to jar only if jar knows of them
Patch218: bootstrap-jopt.patch

# Explicitly add jaxp classes to classpath
Patch219: bootstrap-jaxp-dependency.patch

# Don't fork when generating stubs
Patch220: bootstrap-genstubs-nofork.patch

# Remove dependency on ProcessBuilder which is package private to Oracle implementation
Patch221: bootstrap-break-processbuilder-dependency.patch

# Allow to build with 1.5
Patch222: bootstrap-revert-6973616.patch

# Avoid trying to load system zone info provider and failing
Patch223: bootstrap-revert-6941137.patch

# Replace usage of string switch with if/elseif/else
Patch224: bootstrap-ecj-stringswitch.patch

# Allow langtools to use older jdk
Patch225: bootstrap-langtools-force-old-jdk.patch

# Access JDK sources and classes from langtools build
Patch226: bootstrap-corba-dependencies.patch

# Access langtools classes for Javadoc
Patch227: bootstrap-jaxws-langtools-dependency.patch

# Access JDK sources for com.sun.net.httpserver
Patch228: bootstrap-jaxws-jdk-dependency.patch

# Access JDK and generated sources to build servicability agent
Patch229: bootstrap-hotspot-jdk-dependency.patch

# Remove use of multi-catch and replace with regular multi-level catch
Patch230: bootstrap-ecj-multicatch.patch

# Remove use of try-with-resources and replace with manual close
Patch231: bootstrap-ecj-trywithresources.patch

# Disable auto-boxing and manally cast
Patch232: bootstrap-ecj-autoboxing.patch

# Use custom xslt processor
Patch233: bootstrap-xsltproc.patch

# Use constants from interface rather than impl
Patch234: bootstrap-pr40188.patch

# Remove use of diamond operator and replace with manual
Patch235: bootstrap-ecj-diamond.patch

# Adjust javah switches to only use what bootstrap version supports
Patch236: bootstrap-javah-xbootclasspath.patch

#
# Optional component packages
#

# Make the ALSA based mixer the default when building with the pulseaudio based
# mixer
Patch300: pulse-soundproperties.patch

# SystemTap support
# Workaround for RH613824
Patch302: systemtap.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libalsa-devel
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: libungif-devel
BuildRequires: liblcms2-devel
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXp-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: wget
BuildRequires: xsltproc libxslt
BuildRequires: xorg-x11-proto-devel
BuildRequires: mercurial
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: libXinerama-devel
BuildRequires: rhino
BuildRequires: zip
%if %{gcjbootstrap}
BuildRequires: java-1.6.0-sun-devel
%else
BuildRequires: java-1.7.0-openjdk-devel
%endif
# Mauve build requirements.
BuildRequires: xorg-x11-xvfb
BuildRequires: fonts-type1-xorg
BuildRequires: fonts-bitmap-misc
BuildRequires: libfreetype-devel >= 2.3.0
BuildRequires: fontconfig
BuildRequires: ecj
# Java Access Bridge for GNOME build requirements.
#BuildRequires: libat-spi-devel
BuildRequires: gawk
BuildRequires: libbonobo-devel
BuildRequires: xorg-x11-utils
# PulseAudio build requirements.
%if %{with_pulseaudio}
BuildRequires: libpulseaudio-devel >= 0.9.11
BuildRequires: pulseaudio >= 0.9.11
%endif
# Zero-assembler build requirement.
%ifnarch %{jit_arches}
BuildRequires: libffi-devel >= 3.0.10
%endif

# cacerts build requirement.
BuildRequires: openssl
# execstack build requirement.
# no prelink on ARM yet
%ifnarch %{arm}
BuildRequires: prelink
%endif
%if_enabled systemtap
#systemtap build requirement.
BuildRequires: systemtap-sdt-devel
%endif

Requires: rhino
Requires: liblcms2
#Requires: libjpeg = 6b
# Require /etc/pki/java/cacerts.
Requires: ca-certificates
# Require jpackage-utils for ant.
Requires: jpackage-utils >= 1.7.3-1jpp.2
# Require zoneinfo data provided by tzdata-java subpackage.
Requires: tzdata-java
# Post requires alternatives to install tool alternatives.
Requires(post):   alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): alternatives

# Standard JPackage base provides.
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre = %{javaver}
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: jndi = %{epoch}:%{version}
Provides: jndi-ldap = %{epoch}:%{version}
Provides: jndi-cos = %{epoch}:%{version}
Provides: jndi-rmi = %{epoch}:%{version}
Provides: jndi-dns = %{epoch}:%{version}
Provides: jaas = %{epoch}:%{version}
Provides: jsse = %{epoch}:%{version}
Provides: jce = %{epoch}:%{version}
Provides: jdbc-stdext = 4.1
Provides: java-sasl = %{epoch}:%{version}
Provides: java-fonts = %{epoch}:%{version}

# Obsolete older 1.6 packages as it cannot use the new bytecode
#Obsoletes: java-1.6.0-openjdk
#Obsoletes: java-1.6.0-openjdk-demo
#Obsoletes: java-1.6.0-openjdk-devel
#Obsoletes: java-1.6.0-openjdk-javadoc
#Obsoletes: java-1.6.0-openjdk-src
Source44: import.info

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
Requires:         java-1.7.0-openjdk = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives.
Requires(post):   alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): alternatives

# Standard JPackage devel provides.
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}
Provides: java-sdk-%{origin} = %{epoch}:%{version}
Provides: java-sdk = %{epoch}:%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
Provides: java-devel-%{origin} = %{epoch}:%{version}
Provides: java-devel = %{epoch}:%{javaver}


%description devel
The OpenJDK development tools.

%package demo
Summary: OpenJDK Demos
Group:   Development/Java

Requires: java-1.7.0-openjdk = %{epoch}:%{version}-%{release}

%description demo
The OpenJDK demos.

%package src
Summary: OpenJDK Source Bundle
Group:   Development/Java

Requires: java-1.7.0-openjdk = %{epoch}:%{version}-%{release}

%description src
The OpenJDK source bundle.

%package javadoc
Summary: OpenJDK API Documentation
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

# Post requires alternatives to install javadoc alternative.
Requires(post):   alternatives
# Postun requires alternatives to uninstall javadoc alternative.
Requires(postun): alternatives

# Standard JPackage javadoc provides.
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
# fc provides
Provides: java-javadoc = 1:1.7.0

%description javadoc
The OpenJDK API documentation.

%prep
%setup -q -c -n %{name}
%setup -q -n %{name} -T -D -a 3
%setup -q -n %{name} -T -D -a 1
cp %{SOURCE2} .
cp %{SOURCE4} .

# OpenJDK patches
%patch100

# pulseaudio support
%if %{with_pulseaudio}
%patch300
%endif

# Add systemtap patches if enabled
%if_enabled systemtap
%patch302
%endif

# Remove libraries that are linked
sh %{SOURCE12}

# Copy jaxp, jaf and jaxws drops
mkdir drops/

# Extract the generated files
tar xzf %{SOURCE6}

# Extract the rewriter (to rewrite rhino classes)
tar xzf %{SOURCE7}

# Extract systemtap tapsets
%if_enabled systemtap

tar xzf %{SOURCE8}

for file in tapset/*.in; do

    OUTPUT_FILE=`echo $file | sed -e s:\.in$::g`
    sed -e s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/amd64/server/libjvm.so:g $file > $OUTPUT_FILE
    sed -i -e '/@ABS_CLIENT_LIBJVM_SO@/d' $OUTPUT_FILE
    sed -i -e s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir}:g $OUTPUT_FILE
    sed -i -e s:@INSTALL_ARCH_DIR@:%{archinstall}:g $OUTPUT_FILE

done

%endif

# Pulseaudio
%if %{with_pulseaudio}
tar xzf %{SOURCE11}
%endif

# Extract desktop files
tar xzf %{SOURCE9}

# If bootstrapping, apply additional patches
%if %{gcjbootstrap}

cp -a openjdk openjdk-boot

# Add bootstrap patches
%patch200
%patch201
%patch202
%patch203
%patch204
%patch205
%patch206
%patch207
%patch208
%patch209
%patch210
%patch211
%patch212
%patch213
%patch214
%patch215
%patch216
%patch217
%patch218
%patch219
%patch220
%patch221
%patch222
%patch223
%patch224
%patch225
%patch226
%patch227
%patch228
%patch229
%patch230
%patch231
%patch232
%patch233
%patch234
%patch235
%patch236

%endif
sed -i -e 's,DEF_OBJCOPY=/usr/bin/objcopy,DEF_OBJCOPY=/usr/bin/NO-objcopy,' openjdk/hotspot/make/linux/makefiles/defs.make

%build
# How many cpu's do we have?
export NUM_PROC=`/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :`
export NUM_PROC=${NUM_PROC:-1}

# Build IcedTea and OpenJDK.
%ifarch s390x sparc64 alpha ppc64
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

patch -l -p0 < %{PATCH3}
patch -l -p0 < %{PATCH4}

%if %{debug}
patch -l -p0 < %{PATCH5}
patch -l -p0 < %{PATCH6}
%endif

# Type fixes for s390
%ifarch s390 s390x
patch -l -p0 < %{PATCH101}
#patch -l -p0 < %{PATCH102} # size_t patch disabled for now as it has conflicts
%endif

# Arm fixes
%ifarch %{arm}
patch -l -p0 < %{PATCH103}
%endif

%ifarch ppc ppc64
# PPC fixes
patch -l -p0 < %{PATCH104}
patch -l -p0 < %{PATCH105}
%endif

# Add a "-icedtea" tag to the version
sed -i "s#BUILD_VARIANT_RELEASE)#BUILD_VARIANT_RELEASE)-icedtea#" openjdk/jdk/make/common/shared/Defs.gmk

# Build the re-written rhino jar
mkdir -p rhino/{old,new}

# Compile the rewriter
(cd rewriter 
 javac com/redhat/rewriter/ClassRewriter.java
)

# Extract rhino.jar contents and rewrite
(cd rhino/old 
 jar xf /usr/share/java/rhino.jar
)

java -cp rewriter com.redhat.rewriter.ClassRewriter \
    $PWD/rhino/old \
    $PWD/rhino/new \
    org.mozilla \
    sun.org.mozilla

(cd rhino/old
 for file in `find -type f -not -name '*.class'` ; do
     new_file=../new/`echo $file | sed -e 's#org#sun/org#'`
     mkdir -pv `dirname $new_file`
     cp -v $file $new_file
     sed -ie 's#org\.mozilla#sun.org.mozilla#g' $new_file
 done
)

(cd rhino/new
   jar cfm ../rhino.jar META-INF/MANIFEST.MF sun
)

%if %{gcjbootstrap}

mkdir -p bootstrap/boot

# Copy over JAVA_HOME from /usr/lib/jvm/java-gcj/
cp -aL %{_jvmdir}/java-gcj/* bootstrap/boot/ || : # broken symlinks can be non-fatal but may cause this to fail

# Replace javac with a wrapper that does some magic
cp -af %{SOURCE5} bootstrap/boot/bin/javac
chmod u+x bootstrap/boot/bin/javac # SOURCE5 may not be +x
sed -i -e s:@RT_JAR@:$PWD/bootstrap/boot/jre/lib/rt.jar:g bootstrap/boot/bin/javac

# Link the native2ascii binary
ln -sf /usr/bin/gnative2ascii bootstrap/boot/bin/native2ascii

# We don't need a disassebler, fake it
echo "#!/bin/sh
exit 0" > bootstrap/boot/bin/javap
chmod u+rx bootstrap/boot/bin/javap # We need to run this during build

# Modules directory
mkdir -p bootstrap/boot/lib/modules

# jdk1.6.0 link
rm -f bootstrap/jdk1.6.0
ln -sf boot bootstrap/jdk1.6.0

# Update rt.jar with newer classes
# Extra classes to compile for reasons like
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42003
echo "openjdk-boot/jdk/src/share/classes/java/util/regex/Matcher.java 
openjdk-boot/jdk/src/share/classes/javax/management/remote/JMXServiceURL.java 
openjdk-boot/jdk/src/share/classes/javax/management/modelmbean/ModelMBeanInfo.java 
openjdk-boot/jdk/src/share/classes/javax/swing/plaf/basic/BasicDirectoryModel.java
openjdk-boot/langtools/src/share/classes/javax/tools/JavaFileManager.java" > rt-source-files

mkdir -p rt
bootstrap/jdk1.6.0/bin/javac -g -encoding utf-8    -source 6 -target 6 -d rt \
  -classpath %{_jvmdir}/java-gcj/jre/lib/rt.jar \
  -sourcepath 'generated:openjdk-boot/jdk/src/share/classes:openjdk-boot/jdk/src/solaris/classes:openjdk-boot/langtools/src/share/classes:openjdk-boot/corba/src/share/classes' \
  -bootclasspath "\'\'" @rt-source-files

pushd rt
zip -qur ../bootstrap/jdk1.6.0/jre/lib/rt.jar *
popd

# clean up
rm -f rt-source-files
rm -rf rt

# Build it
pushd openjdk-boot
cp -a ../generated generated.build
chmod u+rwx generated.build

export ALT_DROPS_DIR=$PWD/../drops
export ALT_JDK_IMPORT_PATH="$PWD/../bootstrap/jdk1.6.0"

# Set generic profile
source jdk/make/jdk_generic_profile.sh

make MEMORY_LIMIT=-J-Xmx512m \
  ANT="/usr/bin/ant" \
  ALT_BOOTDIR="$PWD/../bootstrap/jdk1.6.0" \
  ICEDTEA_RT="$PWD/../bootstrap/jdk1.6.0/jre/lib/rt.jar" \
  HOTSPOT_BUILD_JOBS="$NUM_PROC" \
  NO_DOCS="true" \
  RHINO_JAR="$PWD/../rhino/rhino.jar" \
  GENSRCDIR="$PWD/generated.build" \
  DISABLE_NIMBUS="true" \
  XSLT="/usr/bin/xsltproc" \
  FT2_CFLAGS="-I/usr/include/freetype2 " \
  FT2_LIBS="-lfreetype " \
%ifnarch %{jit_arches}
  LIBFFI_CFLAGS="`pkg-config --cflags libffi` " \
  LIBFFI_LIBS="-lffi " \
  ZERO_BUILD="true" \
  ZERO_LIBARCH="%{archbuild}" \
  ZERO_ARCHDEF="%{archdef}" \
%ifarch ppc ppc64 s390 s390x
  ZERO_ENDIANNESS="big" \
%else
  ZERO_ENDIANNESS="little" \
%endif
%endif
  %{nil}

export JDK_TO_BUILD_WITH=$PWD/build/linux-%{archbuild}/j2sdk-image

popd

%else

export JDK_TO_BUILD_WITH=/usr/lib/jvm/java-openjdk

%endif

pushd openjdk >& /dev/null

export ALT_DROPS_DIR=$PWD/../drops
export ALT_BOOTDIR="$JDK_TO_BUILD_WITH"

# Save old umask as jdk_generic_profile overwrites it
oldumask=`umask`

# Set generic profile
source jdk/make/jdk_generic_profile.sh

# Restore old umask
umask $oldumask

make MEMORY_LIMIT=-J-Xmx512m \
  ANT="/usr/bin/ant" \
  DISTRO_NAME="Fedora" \
  DISTRO_PACKAGE_VERSION="ALTLinux-%{release}-%{_arch}" \
  JDK_UPDATE_VERSION=`printf "%02d" %{buildver}` \
  MILESTONE="fcs" \
  HOTSPOT_BUILD_JOBS="$NUM_PROC" \
  STATIC_CXX="false" \
  RHINO_JAR="$PWD/../rhino/rhino.jar" \
  GENSRCDIR="$PWD/generated.build" \
  FT2_CFLAGS="-I/usr/include/freetype2 " \
  FT2_LIBS="-lfreetype " \
  DEBUG_CLASSFILES="true" \
  DEBUG_BINARIES="true" \
  ALT_STRIP_POLICY="no_strip" \
%ifnarch %{jit_arches}
  LIBFFI_CFLAGS="`pkg-config --cflags libffi` " \
  LIBFFI_LIBS="-lffi " \
  ZERO_BUILD="true" \
  ZERO_LIBARCH="%{archbuild}" \
  ZERO_ARCHDEF="%{archdef}" \
%ifarch ppc ppc64 s390 s390x
  ZERO_ENDIANNESS="big" \
%else
  ZERO_ENDIANNESS="little" \
%endif
%endif
  %{debugbuild}

popd >& /dev/null

export JAVA_HOME=$(pwd)/%{buildoutputdir}/j2sdk-image

# Build pulseaudio and install it to JDK build location
%if %{with_pulseaudio}
pushd pulseaudio
make MEMORY_LIMIT=-J-Xmx512m JAVA_HOME=$JAVA_HOME -f Makefile.pulseaudio
cp -pPRf build/native/libpulse-java.so $JAVA_HOME/jre/lib/%{archinstall}/
cp -pPRf build/pulse-java.jar $JAVA_HOME/jre/lib/ext/
popd
%endif

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
  chmod 644 gnome-java-bridge.jar
  cp -a gnome-java-bridge.jar $JAVA_HOME/jre/lib/ext
popd
%endif

# Copy tz.properties
echo "sun.zoneinfo.dir=/usr/share/javazi" >> $JAVA_HOME/jre/lib/tz.properties

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
      -file %{SOURCE4} -timeout 30000 2>&1 | tee mauve_output
    kill -9 `cat Xvfb.pid` || :
    unset DISPLAY
    rm -f Xvfb.pid
    echo ====================MAUVE TESTING END====================
  popd
} || :
%endif

%install
unset JAVA_HOME
STRIP_KEEP_SYMTAB=libjvm*

pushd %{buildoutputdir}/j2sdk-image

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

%if_enabled systemtap
  # Install systemtap support files.
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset
  cp -a $RPM_BUILD_DIR/%{name}/tapset/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  pushd $RPM_BUILD_ROOT%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    ln -sf $RELATIVE/*.stp .
  popd
%endif

  # Install cacerts symlink.
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/cacerts
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
    RELATIVE=$(%{abs2rel} %{_sysconfdir}/pki/java \
      %{_jvmdir}/%{jredir}/lib/security)
    ln -sf $RELATIVE/cacerts .
  popd

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

  # Remove javaws man page
  rm -f man/man1/javaws*

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


# Install nss.cfg
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/


# Install Javadoc documentation.
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}.png
done

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole policytool ; do
    desktop-file-install --vendor=%{name} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

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
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javadocdir_java-1.7.0-openjdk-javadoc<<EOF
%{_javadocdir}/java	%{_javadocdir}/%{name}/api	%{priority}
EOF

%__subst 's,^Categories=.*,Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*policytool.desktop
%__subst 's,^Categories=.*,Categories=Development;Profiling;System;Monitor;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*jconsole.desktop


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications

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

# hack (see altbug #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

%post
%force_update_alternatives

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################



# FIXME: identical binaries are copied, not linked. This needs to be
# fixed upstream.
%files -f %{name}.files
%_altdir/%altname-java
%_sysconfdir/buildreqs/packages/substitute.d/%name
%doc %{buildoutputdir}/j2sdk-image/jre/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/j2sdk-image/jre/LICENSE
%doc %{buildoutputdir}/j2sdk-image/jre/THIRD_PARTY_README

%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{jredir}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}.png
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

%files devel
%_altdir/%altname-javac
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%doc %{buildoutputdir}/j2sdk-image/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir}/j2sdk-image/LICENSE
%doc %{buildoutputdir}/j2sdk-image/THIRD_PARTY_README
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
%{_mandir}/man1/jcmd-%{name}.1*
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
%{tapsetroot}
%endif

%files demo -f %{name}-demo.files
%doc %{buildoutputdir}/j2sdk-image/jre/LICENSE

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
%_altdir/javadocdir_java-1.7.0-openjdk-javadoc
%doc %{_javadocdir}/%{name}
%doc %{buildoutputdir}/j2sdk-image/jre/LICENSE

%changelog
* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt3_2.2.1.8jpp7
- removed Obsoletes: on java-1.6.0-openjdk

* Tue Jul 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt2_2.2.1.8jpp7
- new version 2.2

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt2_2.1.1jpp7
- dropped libat-spi dependency

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.3-alt1_2.1.1jpp7
- Sisyphus release

* Thu Feb 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.1-alt1_2.0.3jpp5.M60T.1
- backport

* Thu Feb 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0.1-alt1_2.0.3jpp6
- new version

