%define _unpackaged_files_terminate_build 1
%define _jvmdir /usr/lib/jvm

# Enable fastdebug builds by default on relevant arches.
%def_without fastdebug
# Enable slowdebug builds by default on relevant arches.
%def_without slowdebug
# Enable release builds by default on relevant arches.
%def_without release
# Enable static library builds by default.
%def_without staticlibs
# Build a fresh libjvm.so for use in a copy of the bootstrap JDK
%def_without fresh_libjvm
# Build with system libraries
%def_with system_libs

%global include_staticlibs 0

%if_with system_libs
%global system_libs 1
%global link_type system
%global freetype_lib %{nil}
%else
%global system_libs 0
%global link_type bundled
%global freetype_lib |libfreetype[.]so.*
%endif

# The -g flag says to use strip -g instead of full strip on DSOs or EXEs.
# This fixes detailed NMT and other tools which need minimal debug info.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1520879
%global _find_debuginfo_opts -g

# With LTO flags enabled, debuginfo checks fail for some reason. Disable
# LTO for a passing build. This really needs to be looked at.
%define _lto_cflags %{nil}
%ifarch loongarch64
# See https://github.com/loongson/jdk21u/issues/15
%define optflags_lto %nil
%endif

# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
# see the difference between global and define:
# See https://github.com/rpm-software-management/rpm/issues/127 to comments at  "pmatilai commented on Aug 18, 2017"
# (initiated in https://bugzilla.redhat.com/show_bug.cgi?id=1482192)
%global debug_suffix_unquoted -slowdebug
%global fastdebug_suffix_unquoted -fastdebug
%global main_suffix_unquoted -main
%global staticlibs_suffix_unquoted -staticlibs
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global fastdebug_suffix "%{fastdebug_suffix_unquoted}"
%global normal_suffix ""
%global main_suffix "%{main_suffix_unquoted}"
%global staticlibs_suffix "%{staticlibs_suffix_unquoted}"

%global debug_warning This package is unoptimised with full debugging. Install only as needed and remove ASAP.
%global fastdebug_warning This package is optimised with full debugging. Install only as needed and remove ASAP.
%global debug_on unoptimised with full debugging on
%global fastdebug_on optimised with full debugging on
%global for_fastdebug for packages with debugging on and optimisation
%global for_debug for packages with debugging on and no optimisation

%global include_normal_build 1

%if %{include_normal_build}
%global normal_build %{normal_suffix}
%else
%global normal_build %{nil}
%endif

# We have hardcoded list of files, which  is appearing in alternatives, and in files
# in alternatives those are slaves and master, very often triplicated by man pages
# in files all masters and slaves are ghosted
# the ghosts are here to allow installation via query like `dnf install /usr/bin/java`
# you can list those files, with appropriate sections: cat *.spec | grep -e --install -e --slave -e post_ -e alternatives
# TODO - fix those hardcoded lists via single list
# Those files must *NOT* be ghosted for *slowdebug* packages
# FIXME - if you are moving jshell or jlink or similar, always modify all three sections
# you can check via headless and devels:
#    rpm -ql --noghost java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# == rpm -ql           java-11-openjdk-headless-slowdebug-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# != rpm -ql           java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# similarly for other %%{_jvmdir}/{jre,java} and %%{_javadocdir}/{java,java-zip}
%define is_release_build 1

# while JDK is a techpreview(is_system_jdk=0), some provides are turned off. Once jdk stops to be an techpreview, move it to 1
# as sytem JDK, we mean any JDK which can run whole system java stack without issues (like bytecode issues, module issues, dependencies...)
%global is_system_jdk 1

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
# Set of architectures which support multiple ABIs
%global multilib_arches sparc64 x86_64
# Set of architectures for which we build slowdebug builds
%global debug_arches    x86_64 aarch64 loongarch64
# Set of architectures for which we build fastdebug builds
%global fastdebug_arches x86_64 ppc64le aarch64
# Set of architectures with a Just-In-Time (JIT) compiler
%global jit_arches      %{aarch64} x86_64 loongarch64
# Set of architectures which use the Zero assembler port (!jit_arches)
%global zero_arches ppc s390
# Set of architectures which run a full bootstrap cycle
%global bootstrap_arches %{jit_arches}
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures with a Ahead-Of-Time (AOT) compiler
%global aot_arches      x86_64 %{aarch64}
# Set of architectures which support the serviceability agent
%global sa_arches       x86_64 aarch64 loongarch64
# Set of architectures which support class data sharing
# See https://bugzilla.redhat.com/show_bug.cgi?id=513605
# MetaspaceShared::generate_vtable_methods is not implemented for the PPC JIT
%global share_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{arm} s390x
# Set of architectures for which we build the Shenandoah garbage collector
%global shenandoah_arches x86_64 %{aarch64}
# Set of architectures for which we build the Z garbage collector
%global zgc_arches x86_64
# Set of architectures for which alt-java has SSB mitigation
%global ssbd_arches x86_64
# Set of architectures for which java has short vector math library (libsvml.so)
%global svml_arches x86_64
%global gdb_arches %{jit_arches} %{zero_arches}

# By default, we build a debug build during main build on JIT architectures
%if_with slowdebug
%ifarch %{debug_arches}
%global include_debug_build 1
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif

# On certain architectures, we compile the Shenandoah GC
%ifarch %{shenandoah_arches}
%global use_shenandoah_hotspot 1
%else
%global use_shenandoah_hotspot 0
%endif

# By default, we build a fastdebug build during main build only on fastdebug architectures
%if_with fastdebug
%ifarch %{fastdebug_arches}
%global include_fastdebug_build 1
%else
%global include_fastdebug_build 0
%endif
%else
%global include_fastdebug_build 0
%endif

%if %{include_debug_build}
%global slowdebug_build %{debug_suffix}
%else
%global slowdebug_build %{nil}
%endif

%if %{include_fastdebug_build}
%global fastdebug_build %{fastdebug_suffix}
%else
%global fastdebug_build %{nil}
%endif

# If you disable all builds, then the build fails
# Build and test slowdebug first as it provides the best diagnostics
%global build_loop %{slowdebug_build} %{fastdebug_build} %{normal_build}

%if %{include_staticlibs}
%global staticlibs_loop %{staticlibs_suffix}
%else
%global staticlibs_loop %{nil}
%endif

%if 0%{?flatpak}
%global bootstrap_build false
%else
%ifarch %{bootstrap_arches}
%global bootstrap_build true
%else
%global bootstrap_build false
%endif
%endif

%if %{include_staticlibs}
# Extra target for producing the static-libraries. Separate from
# other targets since this target is configured to use in-tree
# AWT dependencies: lcms, libjpeg, libpng, libharfbuzz, giflib
# and possibly others
%global static_libs_target static-libs-image
%else
%global static_libs_target %{nil}
%endif

# RPM JDK builds keep the debug symbols internal, to be later stripped by RPM
%global debug_symbols internal

# unlike portables,the rpms have to use static_libs_target very dynamically
%global bootstrap_targets images legacy-jre-image
%global release_targets images docs-zip legacy-jre-image
# No docs nor bootcycle for debug builds
%global debug_targets images legacy-jre-image
# Target to use to just build HotSpot
%global hotspot_target hotspot

# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security) and -Wno-cpp to avoid FORTIFY_SOURCE warnings
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat -Wno-cpp|' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||')
%global ourldflags %optflags

# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _target_cpu
%ifarch x86_64
%global archinstall amd64
%global stapinstall x86_64
%endif
%ifarch ppc
%global archinstall ppc
%global stapinstall powerpc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%global stapinstall powerpc
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%global stapinstall powerpc
%endif
%ifarch %{ix86}
%global archinstall i686
%global stapinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%global stapinstall ia64
%endif
%ifarch s390
%global archinstall s390
%global stapinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%global stapinstall s390
%endif
%ifarch %{arm}
%global archinstall arm
%global stapinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%global stapinstall arm64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%global stapinstall %{_target_cpu}
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%global stapinstall %{_target_cpu}
%endif
%ifarch loongarch64
%global archinstall loongarch64
%global stapinstall loongarch64
%endif
# Need to support noarch for srpm build
%ifarch noarch
%global archinstall %{nil}
%global stapinstall %{nil}
%endif

# always off for portable builds
%ifarch %{systemtap_arches}
%global with_systemtap 0
%else
%global with_systemtap 0
%endif

# New Version-String scheme-style defines
%global featurever 21
%global interimver 0
%global updatever 4
%global patchver 0
%global buildver 7
# buildjdkver is usually same as %%{featurever},
# but in time of bootstrap of next jdk, it is featurever-1,
# and this it is better to change it here, on single place
%global buildjdkver %{featurever}
%global lts_designator ""
%global lts_designator_zip ""

# JDK to use for bootstrapping
%if_with fresh_libjvm
%global bootjdk %{_builddir}/bootstrap
%else
%global bootjdk /usr/lib/jvm/java-%{buildjdkver}-openjdk
%endif
# Define whether to use the bootstrap JDK directly or with a fresh libjvm.so
# This will only work where the bootstrap JDK is the same major version
# as the JDK being built
%if_with fresh_libjvm
%global build_hotspot_first 1
%else
%global build_hotspot_first 0
%endif

# Define IcedTea version used for SystemTap tapsets and desktop file
%global icedteaver      6.0.0pre00-c848b93a8598

# Standard JPackage naming and versioning defines
%global origin openjdk
%global origin_nice OpenJDK
%global priority %( printf '%%02d%%02d%%02d%%02d' %{featurever} %{interimver} %{updatever} %{buildver} )
%global newjavaver %{featurever}.%{interimver}.%{updatever}.%{patchver}
%global javaver %{featurever}

# Strip up to 6 trailing zeros in newjavaver, as the JDK does, to get the correct version used in filenames
%global filever %(svn=%{newjavaver}; for i in 1 2 3 4 5 6 ; do svn=${svn%%.0} ; done; echo ${svn})

# The tag used to create the OpenJDK tarball
%global vcstag jdk-%{filever}+%{buildver}%{?tagsuffix:-%{tagsuffix}}

# Define milestone (EA for pre-releases, GA for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga 1
%if %{is_ga}
%global build_type GA
%global ea_designator ""
%global ea_designator_zip ""
%global extraver %{nil}
%global eaprefix %{nil}
%else
%global build_type EA
%global ea_designator ea
%global ea_designator_zip -%{ea_designator}
%global extraver .%{ea_designator}
%global eaprefix 0.
%endif

Name:    java-21-%{origin}
Version: %{newjavaver}.%{buildver}
Release: alt1
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons
# and this change was brought into RHEL-4. java-1.5.0-ibm packages
# also included the epoch in their virtual provides. This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0". In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0. So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages. Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".

Epoch: 0
Summary: %{origin_nice} %{featurever} Runtime Environment
Group: Development/Java

# HotSpot code is licensed under GPLv2
# JDK library code is licensed under GPLv2 with the Classpath exception
# The Apache license is used in code taken from Apache projects (primarily xalan & xerces)
# DOM levels 2 & 3 and the XML digital signature schemas are licensed under the W3C Software License
# The JSR166 concurrency code is in the public domain
# The BSD and MIT licenses are used for a number of third-party libraries (see ADDITIONAL_LICENSE_INFO)
# The OpenJDK source tree includes:
# - JPEG library (IJG), zlib & libpng (zlib), giflib (MIT), harfbuzz (ISC),
# - freetype (FTL), jline (BSD) and LCMS (MIT)
# - jquery (MIT), jdk.crypto.cryptoki PKCS 11 wrapper (RSA)
# - public_suffix_list.dat from publicsuffix.org (MPLv2.0)
# The test code includes copies of NSS under the Mozilla Public License v2.0
# The PCSClite headers are under a BSD with advertising license
# The elliptic curve cryptography (ECC) source code is licensed under the LGPLv2.1 or any later version
License:  Apache-1.1 and Apache-2.0 and BSD and BSD with advertising and GPL-2.0 and GPL-2.0 with exceptions and IJG and LGPL-2.0+ and MIT and MPL-2.0 and ALT-Public-Domain and W3C and Zlib and ISC and FTL and RSA-MD
URL:      http://openjdk.java.net/

# Define vendor information used by OpenJDK
%global oj_vendor Red Hat, Inc.
%global oj_vendor_url https://www.redhat.com/
# Define what url should JVM offer in case of a crash report
# order may be important, epel may have rhel declared
%global oj_vendor_bug_url https://bugzilla.redhat.com
%global oj_vendor_version (Red_Hat-%{version}-%{release})

%global top_level_dir_name   %{vcstag}
%global top_level_dir_name_backup %{top_level_dir_name}-backup

# parametrized macros are order-sensitive
%global compatiblename  java-%{featurever}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images directories from upstream build
%global jdkimage                jdk
%global jreimage                jre
%global static_libs_image       static-libs
# main id and dir of this jdk
%define uniquesuffix %{fullversion}.%{_arch}
# installation directory for static libraries
%global static_libs_root        lib/static
%global static_libs_arch_dir    %{static_libs_root}/linux-%{archinstall}
%global static_libs_install_dir %{static_libs_arch_dir}/glibc
# output dir stub
%define buildoutputdir openjdk/build
%global altjavaoutputdir install/altjava.install
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir %{fullversion}.%{_arch}

#################################################################
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
#         https://bugzilla.redhat.com/show_bug.cgi?id=1590796#c14
#         https://bugzilla.redhat.com/show_bug.cgi?id=1655938
%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsystemconf[.]so.*|libzip[.]so.*%{freetype_lib}
%global _publiclibs libjawt[.]so.*|libjava[.]so.*|libjvm[.]so.*|libverify[.]so.*|libjsig[.]so.*

%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix -- %{?1}}}
# Standard JPackage directories and symbolic links.
%define sdkdir %{uniquesuffix}
%define jrelnk jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%define sdkbindir %{_jvmdir}/%{sdkdir}/bin
%define jrebindir %{_jvmdir}/%{sdkdir}/bin

%global alt_java_name     alt-java

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

# For flatpack builds hard-code /usr/sbin/alternatives,
# otherwise use %%{_sbindir} relative path.
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%else
%global alternatives_requires %{_sbindir}/alternatives
%endif

%if_with systemtap
# Where to install systemtap tapset (links)
# We would like these to be in a package specific sub-dir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinguish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka target_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdirttapset %{tapsetroot}/tapset/
%global tapsetdir %{tapsetdirttapset}/%{stapinstall}
%endif

%define java_arches x86_64 aarch64 loongarch64
ExclusiveArch: %{java_arches}

# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

# The source tarball, generated using generate_source_tarball.sh
Source0: https://openjdk-sources.osci.io/openjdk%{featurever}/open%{vcstag}.tar.xz

%if_with fresh_libjvm
Source1: bootstrap.tar
%endif

# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (6.x).
# Systemtap tapsets. Zipped up to keep it small.
# Disabled in portables
#Source8: tapsets-icedtea-%%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in

# Release notes
Source10: NEWS

# Source code for alt-java
Source11: alt-java.c

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

# Verify system crypto (policy) can be disabled via a property
Source15: TestSecurityProperties.java

# Ensure vendor settings are correct
Source16: CheckVendor.java

# Ensure translations are available for new timezones
Source18: TestTranslations.java

#############################################
#
# OpenJDK patches in need of upstreaming
#
#############################################

# LoongArch support
Patch3500: jdk21u+35-loongarch64.patch

#############################################
#
# OpenJDK patches which missed last update
#
#############################################
#empty now

BuildRequires(pre): rpm-build-java
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: /proc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libalsa-devel
BuildRequires: binutils
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: libasm-devel libdw-devel libelf-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
%if_without fresh_libjvm
BuildRequires: java-%{buildjdkver}-openjdk-devel
%endif
# gcc-c++ is already needed
BuildRequires: gcc-c++
BuildRequires: gdb libgdb-devel
BuildRequires: libxslt xsltproc
BuildRequires: libgif-devel                                                                    
BuildRequires: gdb libgdb-devel
BuildRequires: libharfbuzz-devel
BuildRequires: liblcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libX11-devel libXvMC-devel xorg-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: pkgconfig
BuildRequires: xorg-proto-devel
BuildRequires: zip
BuildRequires: tar
BuildRequires: unzip
BuildRequires: javapackages-filesystem
# Zero-assembler build requirement
%ifarch %{zero_arches}
BuildRequires: libffi-devel
%endif
# 2023c required as of JDK-8305113
BuildRequires: tzdata-java >= 2023c

# cacerts build requirement in portable mode
BuildRequires: ca-certificates
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3-8

%if_with systemtap                                                                                                    
BuildRequires: systemtap-sdt-devel
%endif

# Standard JPackage base provides
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{version}-%{release}
Provides: jre = %{epoch}:%{version}-%{release}
%endif

%filter_from_provides /^(%{_privatelibs}|%{_publiclibs})$/d
%filter_from_requires /^(%{_privatelibs}|%{_publiclibs})$/d

%define altname %name
%define label -%{name}
%define javaws_ver %{javaver}

%if "%{_lib}" == "lib64"
Provides: /usr/lib/jvm/jre/lib/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/jre/lib/server/libjvm.so(SUNWprivate_1.1)(64bit)
Provides: %{_jvmdir}/%{sdkdir}/lib/server/libjvm.so()(64bit)
Provides: %{_jvmdir}/%{sdkdir}/lib/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/jre/lib/server/libjvm.so()
Provides: /usr/lib/jvm/jre/lib/server/libjvm.so(SUNWprivate_1.1)
Provides: %{_jvmdir}/%{sdkdir}/lib/server/libjvm.so()
Provides: %{_jvmdir}/%{sdkdir}/lib/server/libjvm.so(SUNWprivate_1.1)
%endif

%description
The %{origin_nice} %{featurever} runtime environment.

%if %{include_debug_build}
%package slowdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{debug_on}
Group:   Development/Java

%description slowdebug
The %{origin_nice} %{featurever} runtime environment.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package fastdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{fastdebug_on}
Group:   Development/Java

%description fastdebug
The %{origin_nice} %{featurever} runtime environment.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: %{origin_nice} %{featurever} Headless Runtime Environment
Group: Development/Java

# Require /etc/pki/java/cacerts
Requires: ca-trust
# Require javapackages-filesystem for ownership of /usr/lib/jvm/ and macros
Requires: javapackages-filesystem
# Require zone-info data provided by tzdata-java sub-package
# 2020a required as of JDK-8243541 in 11.0.8+4
Requires: tzdata-java >= 2020b

# Standard JPackage base provides
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-headless = %{epoch}:%{version}-%{release}
Provides: java-headless = %{epoch}:%{version}-%{release}
%endif
Requires: java-common
Requires: /proc
Requires(post): /proc

%description headless
The %{origin_nice} %{featurever} runtime environment without audio and video support.
%endif

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} %{featurever} Development Environment
Group:   Development/Java

# Requires base package
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
# Postun requires alternatives to uninstall tool alternatives

# Standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-devel = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-sdk-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-devel = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-devel = %{epoch}:%{version}-%{release}
Provides: java-sdk = %{epoch}:%{version}-%{release}
%endif

%description devel
The %{origin_nice} %{featurever} development tools.
%endif

%if %{include_debug_build}
%package devel-slowdebug
Summary: %{origin_nice} %{featurever} Runtime and Development Environment %{debug_on}
Group:   Development/Java

%description devel-slowdebug
The %{origin_nice} %{featurever} development tools.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package devel-fastdebug
Summary: %{origin_nice} %{featurever} Runtime and Development Environment %{fastdebug_on}
Group:   Development/Java

%description devel-fastdebug
The %{origin_nice} %{featurever} development tools.
%{fastdebug_warning}
%endif

%if %{include_staticlibs}
%if %{include_normal_build}
%package static-libs
Summary: %{origin_nice} %{featurever} libraries for static linking.
Group:   Development/Java

%description static-libs
The %{origin_nice} %{featurever} libraries for static linking.
%endif

%if %{include_debug_build}
%package static-libs-slowdebug
Summary: %{origin_nice} %{featurever} libraries for static linking - %{debug_on}
Group:   Development/Java

%description static-libs-slowdebug
The %{origin_nice} %{featurever} libraries for static linking.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package static-libs-fastdebug
Summary: %{origin_nice} %{featurever} libraries for static linking - %{fastdebug_on}
Group:   Development/Java

%description static-libs-fastdebug
The %{origin_nice} %{featurever} libraries for static linking.
%{fastdebug_warning}
%endif

# staticlibs
%endif

%if %{include_normal_build}
%package jmods
Summary: JMods for %{origin_nice} %{featurever}
Group: Development/Java

# Requires devel package
# as jmods are bytecode, they should be OK without any _isa
Requires: %{name}-headless = %{epoch}:%{version}-%{release}

%if %is_system_jdk
Provides: java-jmods = %{epoch}:%{version}-%{release}
%endif

%description jmods
The JMods for %{origin_nice} %{featurever}.
%endif

%if %{include_normal_build}
%package demo
Summary: %{origin_nice} %{featurever} Demos
Group: Development/Java

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}

%if %is_system_jdk
Provides: java-demo = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-demo = %{epoch}:%{version}-%{release}
%endif

%description demo
The %{origin_nice} %{featurever} demos.
%endif

%package misc
Summary: %{origin_nice} %{featurever} miscellany
Group:   Development/Java

%description misc
The %{origin_nice} %{featurever} miscellany.

%package sources
Summary: %{origin_nice} %{featurever} full patched sources of portable JDK
Group:   Development/Java

%description sources
The %{origin_nice} %{featurever} full patched sources of portable JDK to build, attach to debuggers or for debuginfo

%if %{include_normal_build}
%package javadoc
Summary: %{origin_nice} %{featurever} API documentation
Group: Documentation
Requires: javapackages-filesystem
Obsoletes: javadoc-slowdebug < 1:13.0.0.33-1.rolling

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
# Postun requires alternatives to uninstall javadoc alternative

# Standard JPackage javadoc provides
%if %is_system_jdk
Provides: java-javadoc = %{epoch}:%{version}-%{release}
%endif

%description javadoc
The %{origin_nice} %{featurever} API documentation.
%endif

%prep

echo "Preparing %{oj_vendor_version}"

# Using the echo macro breaks rpmdev-bumpspec, as it parses the first line of stdout :-(
%if 0%{?stapinstall:1}
  echo "CPU: %{_target_cpu}, arch install directory: %{archinstall}, SystemTap install directory: %{stapinstall}"
%else
  %{error:Unrecognised architecture %{_target_cpu}}
%endif

if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_fastdebug_build} -eq 0 -o  %{include_fastdebug_build} -eq 1 ] ; then
  echo "include_fastdebug_build is %{include_fastdebug_build}"
else
  echo "include_fastdebug_build is %{include_fastdebug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 13
fi

if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 -a  %{include_fastdebug_build} -eq 0 ] ; then
  echo "You have disabled all builds (normal,fastdebug,slowdebug). That is a no go."
  exit 14
fi

%if_with fresh_libjvm
echo "WARNING: The build of a fresh libjvm has been disabled due to a JDK version mismatch"
echo "Build JDK version is %{buildjdkver}, feature JDK version is %{featurever}"
%endif

%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

# Extract bootstrap binaries
%if_with fresh_libjvm
tar xf %{SOURCE1}
mkdir -p %{bootjdk}
%ifnarch loongarch64
%__cp -af bootstrap/noarch/* %{bootjdk}
%endif
%__cp -af bootstrap/%archinstall/* %{bootjdk}
%endif

# OpenJDK patches

# Patch the JDK
pushd %{top_level_dir_name}
# Patches in need of upstreaming

%patch3500 -p1
popd # openjdk

# The OpenJDK version file includes the current
# upstream version information. For some reason,
# configure does not automatically use the
# default pre-version supplied there (despite
# what the file claims), so we pass it manually
# to configure
VERSION_FILE=$(pwd)/%{top_level_dir_name}/make/conf/version-numbers.conf
if [ -f ${VERSION_FILE} ] ; then
    UPSTREAM_EA_DESIGNATOR=$(grep '^DEFAULT_PROMOTED_VERSION_PRE' ${VERSION_FILE} | cut -d '=' -f 2)
else
    echo "Could not find OpenJDK version file.";
    exit 16
fi
if [ "x${UPSTREAM_EA_DESIGNATOR}" != "x%{ea_designator}" ] ; then
    echo "WARNING: Designator mismatch";
    echo "Spec file is configured for a %{build_type} build with designator '%{ea_designator}'"
    echo "Upstream version-pre setting is '${UPSTREAM_EA_DESIGNATOR}'";
    exit 17
fi

# Extract systemtap tapsets
%if %{with_systemtap}
tar --strip-components=1 -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif
%if %{include_fastdebug_build}
cp -r tapset tapset%{fastdebug_suffix}
%endif

for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e "s:\.stp\.in$:-%{version}-%{release}.%{_arch}.stp:g"`
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir -- $suffix}/lib/server/libjvm.so:g" $file > $file.1
    sed -e "s:@JAVA_SPEC_VER@:%{javaver}:g" $file.1 > $file.2
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir -- $suffix}/lib/client/libjvm.so:g" $file.2 > $OUTPUT_FILE
%else
    sed -e "/@ABS_CLIENT_LIBJVM_SO@/d" $file.2 > $OUTPUT_FILE
%endif
    sed -i -e "s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir -- $suffix}:g" $OUTPUT_FILE
    sed -i -e "s:@INSTALL_ARCH_DIR@:%{archinstall}:g" $OUTPUT_FILE
    sed -i -e "s:@prefix@:%{_jvmdir}/%{sdkdir -- $suffix}/:g" $OUTPUT_FILE
  done
done
# systemtap tapsets ends
%endif

# Prepare desktop files
# The _X_ syntax indicates variables that are replaced by make upstream
# The @X@ syntax indicates variables that are replaced by configure upstream
for suffix in %{build_loop} ; do
for file in %{SOURCE9}; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:_SDKBINDIR_:%{sdkbindir -- $suffix}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@target_cpu@:%{_arch}:g" $OUTPUT_FILE
    sed -i -e  "s:@OPENJDK_VER@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VER@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

%build
%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
mkdir bootjdk
pushd bootjdk
%ifarch %{aarch64}
tar --strip-components=1 -xf %{SOURCE1001} 
%endif
%ifarch %{ppc64le}
tar --strip-components=1 -xf %{SOURCE1002} 
%endif
%ifarch x86_64
tar --strip-components=1 -xf %{SOURCE1003} 
%endif
%ifarch s390x
tar --strip-components=1 -xf %{SOURCE1004}
%endif
BOOT_JDK=$PWD
popd
%else
BOOT_JDK=%{bootjdk}
%endif

%if_with fresh_libjvm
export LD_LIBRARY_PATH=%bootjdk/lib:$LD_LIBRARY_PATH
%endif

# How many CPU's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

%ifarch s390x sparc64 alpha aarch64 loongarch64
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
# Explicitly set the C++ standard as the default has changed on GCC >= 6
EXTRA_CFLAGS="%ourcppflags"
EXTRA_CPP_FLAGS="%ourcppflags"

%ifarch ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
%ifarch %{ix86}
# Align stack boundary on x86_32
EXTRA_CFLAGS="$(echo ${EXTRA_CFLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
EXTRA_CPP_FLAGS="$(echo ${EXTRA_CPP_FLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
%endif
export EXTRA_CFLAGS EXTRA_CPP_FLAGS

echo "Building %{SOURCE11}"
mkdir -p %{altjavaoutputdir}
gcc ${EXTRA_CFLAGS} -o %{altjavaoutputdir}/%{alt_java_name} %{SOURCE11}

function buildjdk() {
    local outputdir=${1}
    local buildjdk=${2}
    local maketargets="${3}"
    local debuglevel=${4}
    local link_opt=${5}

    local top_dir_abs_src_path=$(pwd)/%{top_level_dir_name}
    local top_dir_abs_build_path=$(pwd)/${outputdir}

    # This must be set using the global, so that the
    # static libraries still use a dynamic stdc++lib
    if [ "x%{link_type}" = "xbundled" ] ; then
        libc_link_opt="static";
    else
        libc_link_opt="dynamic";
    fi

    echo "Using output directory: ${outputdir}";
    echo "Checking build JDK ${buildjdk} is operational..."
    ${buildjdk}/bin/java -version
    echo "Using make targets: ${maketargets}"
    echo "Using debuglevel: ${debuglevel}"
    echo "Using link_opt: ${link_opt}"
    echo "Building %{newjavaver}-%{buildver}, pre=%{ea_designator}, opt=%{lts_designator}"

    mkdir -p ${outputdir}
    pushd ${outputdir}

    # Note: zlib and freetype use %{link_type}
    # rather than ${link_opt} as the system versions
    # are always used in a system_libs build, even
    # for the static library build
%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
    scl enable devtoolset-8 -- bash ${top_dir_abs_src_path}/configure \
%else
    bash ${top_dir_abs_src_path}/configure \
%endif
%ifarch %{zero_arches}
    --with-jvm-variants=zero \
%endif
%ifarch %{ppc64le}
    --with-jobs=1 \
%endif
    --with-version-feature=%{featurever} \
    --with-version-interim=%{interimver} \
    --with-version-update=%{updatever} \
    --with-version-patch=%{patchver} \
    --with-version-build=%{buildver} \
    --with-version-pre="%{ea_designator}" \
    --with-version-opt=%{lts_designator} \
    --with-vendor-version-string="%{oj_vendor_version}" \
    --with-vendor-name="%{oj_vendor}" \
    --with-vendor-url="%{oj_vendor_url}" \
    --with-vendor-bug-url="%{oj_vendor_bug_url}" \
    --with-vendor-vm-bug-url="%{oj_vendor_bug_url}" \
    --with-boot-jdk=${buildjdk} \
    --with-debug-level=${debuglevel} \
    --with-native-debug-symbols="%{debug_symbols}" \
    --enable-unlimited-crypto \
    --with-zlib=%{link_type} \
    --with-freetype=%{link_type} \
    --with-libjpeg=${link_opt} \
    --with-giflib=${link_opt} \
    --with-libpng=${link_opt} \
    --with-lcms=${link_opt} \
    --with-harfbuzz=${link_opt} \
    --with-stdc++lib=${libc_link_opt} \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC" \
    --with-source-date="${SOURCE_DATE_EPOCH}" \
    --disable-javac-server \
%ifarch %{zgc_arches}
    --with-jvm-features=zgc \
%endif
    --disable-warnings-as-errors

    cat spec.gmk
%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
    scl enable devtoolset-8  -- make \
%else
    make \
%endif
      LOG=trace \
      WARNINGS_ARE_ERRORS="-Wno-error" \
      CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
      $maketargets || ( pwd; find ${top_dir_abs_src_path} ${top_dir_abs_build_path} -name "hs_err_pid*.log" | xargs cat && false )

    popd
}

function installjdk() {
    local imagepath=${1}

    if [ -d ${imagepath} ] ; then
        # the build (erroneously) removes read permissions from some jars
        # this is a regression in OpenJDK 7 (our compiler):
        # http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
        find ${imagepath} -iname '*.jar' -exec chmod ugo+r {} \;

        # Build screws up permissions on binaries
        # https://bugs.openjdk.java.net/browse/JDK-8173610
        find ${imagepath} -iname '*.so' -exec chmod +x {} \;
        find ${imagepath}/bin/ -exec chmod +x {} \;

        # Create fake alt-java as a placeholder for future alt-java
        if [ -d man/man1 ] ; then
          pushd ${imagepath}
            # add alt-java man page
            echo "Hardened java binary recommended for launching untrusted code from the Web e.g. javaws" > man/man1/%{alt_java_name}.1
            cat man/man1/java.1 >> man/man1/%{alt_java_name}.1
          popd
       fi
    fi
}

# Checks on debuginfo must be performed before the files are stripped
# by the RPM installation stage
function debugcheckjdk() {
    local imagepath=${1}

    if [ -d ${imagepath} ] ; then

        so_suffix="so"
        # Check debug symbols are present and can identify code
        find "${imagepath}" -iname "*.$so_suffix" -print0 | while read -d $'\0' lib
        do
            if [ -f "$lib" ] ; then
                echo "Testing $lib for debug symbols"
                # All these tests rely on RPM failing the build if the exit code of any set
                # of piped commands is non-zero.

                # Test for .debug_* sections in the shared object. This is the main test
                # Stripped objects will not contain these
                eu-readelf -S "$lib" | grep "] .debug_"
                test $(eu-readelf -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2

                # Test FILE symbols. These will most likely be removed by anything that
                # manipulates symbol tables because it's generally useless. So a nice test
                # that nothing has messed with symbols
                old_IFS="$IFS"
                IFS=$'\n'
                for line in $(eu-readelf -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
                do
                    # We expect to see .cpp and .S files, except for architectures like aarch64 and
                    # s390 where we expect .o and .oS files
                    echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|S|oS))?$"
                done
                IFS="$old_IFS"

                # If this is the JVM, look for javaCalls.(cpp|o) in FILEs, for extra sanity checking
                if [ "`basename $lib`" = "libjvm.so" ]; then
                    eu-readelf -s "$lib" | \
                        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
                fi

                # Test that there are no .gnu_debuglink sections pointing to another
                # debuginfo file. There shouldn't be any debuginfo files, so the link makes
                # no sense either
                eu-readelf -S "$lib" | grep 'gnu'
                if eu-readelf -S "$lib" | grep "\] .gnu_debuglink" | grep PROGBITS; then
                   echo "bad .gnu_debuglink section."
                   eu-readelf -x .gnu_debuglink "$lib"
                   false
                fi
            fi
        done

        # Make sure gdb can do a backtrace based on line numbers on libjvm.so
        # javaCalls.cpp:58 should map to:
        # http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/ff3b27e6bcc2/src/share/vm/runtime/javaCalls.cpp#l58
        # Using line number 1 might cause build problems. See:
        # https://bugzilla.redhat.com/show_bug.cgi?id=1539664
        # https://bugzilla.redhat.com/show_bug.cgi?id=1538767
        gdb -q "${imagepath}/bin/java" <<EOF | tee gdb.out
handle SIGSEGV pass nostop noprint
handle SIGILL pass nostop noprint
set breakpoint pending on
break javaCalls.cpp:58
commands 1
backtrace
quit
end
run -version
EOF
%ifarch %{gdb_arches}
        grep 'JavaCallWrapper::JavaCallWrapper' gdb.out
%endif

    fi
}

function genchecksum() {
    local checkedfile=${1}

    checkdir=$(dirname ${1})
    checkfile=$(basename ${1})

    echo "Generating checksum for ${checkfile} in ${checkdir}..."
    pushd ${checkdir}
    sha256sum ${checkfile} > ${checkfile}.sha256sum
    sha256sum --check ${checkfile}.sha256sum
    popd
}

packagesdir=$(pwd)/..

pwd
ls -l

%if %{build_hotspot_first}
  # Build a fresh libjvm.so first and use it to bootstrap
  cp -LR --preserve=mode,timestamps %{bootjdk} newboot
  systemjdk=$(pwd)/newboot
  buildjdk build/newboot ${systemjdk} %{hotspot_target} "release" "bundled"
  mv build/newboot/jdk/lib/server/libjvm.so newboot/lib/server
%else
  systemjdk=%{bootjdk}
%endif

for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=release
  else
      # change --something to something
      debugbuild=`echo $suffix  | sed "s/-//g"`
  fi
  for loop in %{main_suffix} %{staticlibs_loop} ; do
    builddir=%{buildoutputdir -- ${suffix}${loop}}
    bootbuilddir=boot${builddir}
    if test "x${loop}" = "x%{main_suffix}" ; then
      link_opt="%{link_type}"
%if %{system_libs}
      # Copy the source tree so we can remove all in-tree libraries
      cp -a %{top_level_dir_name} %{top_level_dir_name_backup}
      # Remove all libraries that are linked
      sh %{SOURCE12} %{top_level_dir_name} full
%endif
      # Debug builds don't need same targets as release for
      # build speed-up. We also avoid bootstrapping these
      # slower builds.
      if echo $debugbuild | grep -q "debug" ; then
        maketargets="%{debug_targets}"
        run_bootstrap=false
      else
        maketargets="%{release_targets}"
        run_bootstrap=%{bootstrap_build}
      fi
      if ${run_bootstrap} ; then
        buildjdk ${bootbuilddir} ${systemjdk} "%{bootstrap_targets}" ${debugbuild} ${link_opt}
        buildjdk ${builddir} $(pwd)/${bootbuilddir}/images/%{jdkimage} "${maketargets}" ${debugbuild} ${link_opt}
        rm -rf ${bootbuilddir}
      else
        buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt}
      fi
%if %{system_libs}
      # Restore original source tree we modified by removing full in-tree sources
      rm -rf %{top_level_dir_name}
      mv %{top_level_dir_name_backup} %{top_level_dir_name}
%endif
    else
      # Use bundled libraries for building statically
      link_opt="bundled"
      # Static library cycle only builds the static libraries
      maketargets="%{static_libs_target}"
      # Always just do the one build for the static libraries
      buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt}
    fi

  done # end of main / staticlibs loop

  # Final setup on the main image
  top_dir_abs_main_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{main_suffix}}
  for image in %{jdkimage} %{jreimage} ; do
    imagePath=${top_dir_abs_main_build_path}/images/${image}
    installjdk ${imagePath}
  done

  # Print release information
  cat ${top_dir_abs_main_build_path}/images/%{jdkimage}/release

################################################################################
  pushd ${top_dir_abs_main_build_path}/images
    if [ "x$suffix" == "x" ] ; then
      nameSuffix=""
    else
      nameSuffix=`echo "$suffix"| sed s/-/./`
    fi
    # additional steps needed for fluent repack; most of them done twice, as images are already populated
    # maybe most of them should be done in upstream build?
    for imagedir  in %{jdkimage} %{jreimage} ; do
      pushd $imagedir
        # Convert man pages to UTF8 encoding
		if [ -d man/man1 ] ; then # jre do not have man pages...
          for manpage in man/man1/*  ; do
            iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
            mv -f $manpage.tmp $manpage
          done
        fi
        # Install release notes
        cp -a %{SOURCE10} `pwd`
        cp -a %{SOURCE10} `pwd`/legal
        # stabilize permissions; aprtially duplicated in instalojdk
        find `pwd` -name "*.so" -exec chmod 755 {} \; -exec echo "set 755 to so {}" \; ;
        find `pwd` -type d -exec chmod 755 {} \; -exec echo "set 755 to dir {}" \; ;
        find `pwd`/legal -type f -exec chmod 644 {} \; -exec echo "set 644 to licences {}" \; ;
      popd # jdkimage/jreimage
    done # jre/sdk work in loop
    # javadoc is done only for release sdkimage
    if ! echo $suffix | grep -q "debug" ; then
      # Install Javadoc documentation
      #cp -a docs %{jdkimage}  # not sure if the plaintext javadoc is for some use
      built_doc_archive=jdk-%{filever}%{ea_designator_zip}+%{buildver}%{lts_designator_zip}-docs.zip
      cp -a  `pwd`/../bundles/${built_doc_archive} `pwd`/%{jdkimage}/javadocs.zip || ls -l `pwd`/../bundles
    fi
    # end of additional steps

  popd #images

################################################################################
# note, currently no debuginfo, consult portbale spec for external (zipped) debuginfo, being tarred alone
################################################################################

# build cycles
done # end of release / debug cycle loop

%install
STRIP_KEEP_SYMTAB=libjvm*
                                                                                              
for suffix in %{build_loop} ; do

top_dir_abs_main_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{main_suffix}}
%if %{include_staticlibs}
top_dir_abs_staticlibs_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{staticlibs_loop}}
%endif
jdk_image=${top_dir_abs_main_build_path}/images/%{jdkimage}

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
cp -a ${jdk_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}

pushd ${jdk_image}

# Remove empty cacerts database
rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security/cacerts
# Install cacerts symlink needed by some apps which hard-code the path
pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security
    ln -sf /etc/pki/java/cacerts .
popd

# Install version-ed symlinks
pushd $RPM_BUILD_ROOT%{_jvmdir}
  ln -sf %{sdkdir -- $suffix} %{jrelnk -- $suffix}
popd

# Install man pages
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
for manpage in man/man1/*
do
  # Convert man pages to UTF8 encoding
  iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
  mv -f $manpage.tmp $manpage
  install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
    $manpage .1)%{label}.1
done
# Remove man pages from jdk image
rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/man
popd

# Install static libs artefacts
%if %{include_staticlibs}
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
cp -a ${top_dir_abs_staticlibs_build_path}/images/%{static_libs_image}/lib/*.a \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
%endif

if ! echo $suffix | grep -q "debug" ; then
  # Install Javadoc documentation
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  cp -a ${top_dir_abs_main_build_path}/images/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
  built_doc_archive=jdk-%{filever}%{ea_designator_zip}+%{buildver}%{lts_designator_zip}-docs.zip
  cp -a ${top_dir_abs_main_build_path}/bundles/${built_doc_archive} \
     $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}.zip || ls -l ${top_dir_abs_main_build_path}/bundles/
fi

# Install release notes
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir -- $suffix}
install -d -m 755 ${commondocdir}
cp -a %{SOURCE10} ${commondocdir}

# Install icons and menu entries
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix -- $suffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# moving config files to /etc
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/conf/  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib/security  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}
  ln -srv $RPM_BUILD_ROOT%{etcjavadir -- $suffix}/conf  ./conf
popd
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib
  ln -srv $RPM_BUILD_ROOT%{etcjavadir -- $suffix}/lib/security  ./security
popd
# end moving files to /etc

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -name "*.so" -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -type d -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/legal -type f -exec chmod 644 {} \; ;

# end, dual install
done

for rpm404_ghost in %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa %{_bindir}/java %{_jvmdir}/jre %{_bindir}/keytool %{_bindir}/rmid %{_bindir}/rmiregistry %{_jvmdir}/jre-%{origin} %{_jvmdir}/jre-%{javaver} %{_jvmdir}/jre-%{javaver}-%{origin} %{_bindir}/javac %{_jvmdir}/java %{_bindir}/jaotc %{_bindir}/jlink %{_bindir}/jmod %{_bindir}/jhsdb %{_bindir}/jar %{_bindir}/jarsigner %{_bindir}/javadoc %{_bindir}/javap %{_bindir}/jcmd %{_bindir}/jconsole %{_bindir}/jdb %{_bindir}/jdeps %{_bindir}/jdeprscan %{_bindir}/jimage %{_bindir}/jinfo %{_bindir}/jmap %{_bindir}/jps %{_bindir}/jrunscript %{_bindir}/jshell %{_bindir}/jstack %{_bindir}/jstat %{_bindir}/jstatd %{_bindir}/serialver %{_jvmdir}/java-%{origin} %{_jvmdir}/java-%{javaver} %{_jvmdir}/java-%{javaver}-%{origin} %{_javadocdir}/java %{_javadocdir}/java-zip %{_bindir}/jwebserver
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

export LANG=ru_RU.UTF-8
if stat -t %buildroot/usr/share/applications/*policytool.desktop; then
  sed -i 's,^Categories=.*,Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name --set-value='OpenJDK %featurever Policy Tool' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment --set-value='Manage OpenJDK %featurever policy files' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name[ru] --set-value='Настройка политик OpenJDK %featurever' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment[ru] --set-value='Управление файлами политик OpenJDK %featurever' %buildroot/usr/share/applications/*policytool.desktop
fi
sed -i 's,^Categories=.*,Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*jconsole.desktop
#Name=OpenJDK 8 Monitoring & Management Console
desktop-file-edit --set-key=Name --set-value='OpenJDK %featurever Management Console' %buildroot/usr/share/applications/*jconsole.desktop
#Comment=Monitor and manage OpenJDK applications
desktop-file-edit --set-key=Comment --set-value='Monitor and manage OpenJDK %featurever' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Name[ru] --set-value='Консоль OpenJDK %featurever' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Comment[ru] --set-value='Мониторинг и управление приложениями OpenJDK %featurever' %buildroot/usr/share/applications/*jconsole.desktop

##### javadoc Alt specific #####
echo java-javadoc >java-javadoc-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 java-javadoc-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%altname-javadoc<<EOF
%{_javadocdir}/java     %{_javadocdir}/%{uniquejavadocdir}/api  %{priority}
EOF


##################################################
# --- alt linux specific, shared with openjdk ---#
##################################################

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/jvisualvm ]; then
  cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-jvisualvm.desktop << EOF
[Desktop Entry]
Name=Java VisualVM (OpenJDK %{javaver})
Comment=Java Virtual Machine Monitoring, Troubleshooting, and Profiling Tool
Exec=%{_jvmdir}/%{sdkdir}/bin/jvisualvm
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
fi

%if_enabled control_panel
# ControlPanel freedesktop.org menu entry
cat >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-control-panel.desktop << EOF
[Desktop Entry]
Name=Java Control Panel (OpenJDK %{javaver})
Name[ru]=Настройка Java (OpenJDK %{javaver})
Comment=Java Control Panel
Comment[ru]=Панель управления Java
Exec=%{_jvmdir}/%{sdkdir}/bin/jcontrol
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
Name=Java Web Start ((OpenJDK %{javaver}))
Comment=Java Application Launcher
MimeType=application/x-java-jnlp-file;
Exec=%{_jvmdir}/%{sdkdir}/bin/javaws %%u
Icon=%{name}
Terminal=false
Type=Application
Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};
EOF
%endif

# Install substitute rules for buildreq
echo java >j2se-buildreq-substitute
echo java-headless >j2se-headless-buildreq-substitute
echo java-devel >j2se-devel-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 j2se-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name
install -m644 j2se-headless-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
install -m644 j2se-devel-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel

install -d %buildroot%_altdir

# J2SE alternative
cat <<EOF >%buildroot%_altdir/%name-java-headless
%{_bindir}/java %{_jvmdir}/%{sdkdir}/bin/java   %priority
%_man1dir/java.1.gz     %_man1dir/java%{label}.1.gz     %{_jvmdir}/%{sdkdir}/bin/java
EOF
# binaries and manuals
for i in keytool policytool servertool orbd rmiregistry tnameserv jwebserver
do
  if [ -e %buildroot%{_jvmdir}/%{sdkdir}/bin/$i ]; then
    cat <<EOF >>%buildroot%_altdir/%name-java-headless
%_bindir/$i     %{_jvmdir}/%{sdkdir}/bin/$i     %{_jvmdir}/%{sdkdir}/bin/java
%_man1dir/$i.1.gz       %_man1dir/${i}%{label}.1.gz     %{_jvmdir}/%{sdkdir}/bin/java
EOF
  fi
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel %{_jvmdir}/%{sdkdir}/bin/ControlPanel   %{_jvmdir}/%{sdkdir}/bin/java
%{_bindir}/jcontrol     %{_jvmdir}/%{sdkdir}/bin/jcontrol       %{_jvmdir}/%{sdkdir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java-headless
%{_jvmdir}/jre  %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{origin}        %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}       %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}-%{origin}     %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------

# Javac alternative
cat <<EOF >%buildroot%_altdir/%name-javac
%_bindir/javac  %{_jvmdir}/%{sdkdir}/bin/javac  %priority
%_man1dir/javac.1.gz    %_man1dir/javac%{label}.1.gz    %{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii serialver apt jconsole jinfo jmap jmc jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i     %{_jvmdir}/%{sdkdir}/bin/$i     %{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz       %_man1dir/${i}%{label}.1.gz     %{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i     %{_jvmdir}/%{sdkdir}/bin/$i     %{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}       %{_jvmdir}/%{sdkdir}    %{_jvmdir}/%{sdkdir}/bin/javac
EOF
cat <<EOF >>%buildroot%_altdir/%name-javac-versioned
%{_jvmdir}/java-%{javaver}      %{_jvmdir}/%{sdkdir}    %priority
%{_jvmdir}/java-%{javaver}-%{origin}    %{_jvmdir}/%{sdkdir}    %priority
EOF

# ----- end: JPackage compatibility alternatives ------

# hack (see #11383) to enshure that all man pages will be compressed
for i in $RPM_BUILD_ROOT%_man1dir/*.1; do
    [ -f $i ] && gzip -9 $i
done

# Make symlink to libjvm.so to main library directory
ln -s server/libjvm.so %buildroot%_jvmdir/%sdkdir/lib/libjvm.so

##################################################
# - END alt linux specific, shared with openjdk -#
##################################################
echo "install passed past alt linux specific."

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{build_loop} ; do

# Tests in the check stage are performed on the installed image
# rpmbuild operates as follows: build -> install -> test
# however in portbales, we test built image instead of installed one
top_dir_abs_main_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{main_suffix}}
export JAVA_HOME=${top_dir_abs_main_build_path}/images/%{jdkimage}

#check Shenandoah is enabled
%if %{use_shenandoah_hotspot}
$JAVA_HOME/bin/java -XX:+UnlockExperimentalVMOptions -XX:+UseShenandoahGC -version
%endif

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")

# Check system crypto (policy) is deactive and can not be enabled
# Test takes a single argument - true or false - to state whether system
# security properties are enabled or not.
$JAVA_HOME/bin/javac -d . %{SOURCE15}
export PROG=$(echo $(basename %{SOURCE15})|sed "s|\.java||")
export SEC_DEBUG="-Djava.security.debug=properties"
$JAVA_HOME/bin/java ${SEC_DEBUG} ${PROG} false
$JAVA_HOME/bin/java ${SEC_DEBUG} -Djava.security.disableSystemPropertiesFile=false ${PROG} false

# Check java launcher has no SSB mitigation
if ! nm $JAVA_HOME/bin/java | grep set_speculation ; then true ; else false; fi

# Check alt-java launcher has SSB mitigation on supported architectures
# set_speculation function exists in both cases, so check for prctl call
%ifarch %{ssbd_arches}
nm %{altjavaoutputdir}/%{alt_java_name} | grep prctl
%else
if ! nm %{altjavaoutputdir}/%{alt_java_name} | grep prctl ; then true ; else false; fi
%endif

# Check correct vendor values have been set
$JAVA_HOME/bin/javac -d . %{SOURCE16}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE16})|sed "s|\.java||") "%{oj_vendor}" "%{oj_vendor_url}" "%{oj_vendor_bug_url}" "%{oj_vendor_version}"

%if ! 0%{?flatpak}
# Check translations are available for new timezones (during flatpak builds, the
# tzdb.dat used by this test is not where the test expects it, so this is
# disabled for flatpak builds) 
$JAVA_HOME/bin/javac -d . %{SOURCE18}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE18})|sed "s|\.java||") JRE
$JAVA_HOME/bin/java -Djava.locale.providers=CLDR $(echo $(basename %{SOURCE18})|sed "s|\.java||") CLDR
%endif

%if %{include_staticlibs}
# Check debug symbols in static libraries (smoke test)
export STATIC_LIBS_HOME=${top_dir_abs_main_build_path}/../../%{buildoutputdir -- ${suffix}%{staticlibs_suffix}}/images/static-libs/lib/
readelf --debug-dump  $STATIC_LIBS_HOME/libnet.a | grep Inet4AddressImpl.c
readelf --debug-dump  $STATIC_LIBS_HOME/libnet.a | grep Inet6AddressImpl.c
%endif

# Check src.zip has all sources. See RHBZ#1130490
$JAVA_HOME/bin/jar -tf $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'

# Check class files include useful debugging information
$JAVA_HOME/bin/javap -l java.lang.Object | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.lang.Object | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.lang.Object | grep LocalVariableTable

# Check generated class files include useful debugging information
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LocalVariableTable

# build cycles check
done

# Remove unnecessary files
rm -f %buildroot%{_jvmdir}/%{sdkdir}/NEWS
rm -f %buildroot%{_jvmdir}/%{sdkdir}/javadocs.zip
rm -f %buildroot%_datadir/javadoc/*.zip
rm -f %buildroot%_datadir/javadoc/java-zip

%if %{include_normal_build}
%files
%_sysconfdir/buildreqs/packages/substitute.d/%name
# main package builds always
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_jvmdir}/%{sdkdir}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/lib/libjawt.so
%{_jvmdir}/%{sdkdir}/lib/lible.so
%else
%files
# placeholder
%endif

%if %{include_normal_build}
%files headless
%_altdir/%name-java-headless
%_sysconfdir/buildreqs/packages/substitute.d/%name-headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue
# all config/noreplace files (and more) have to be declared in pretrans. See pretrans
%{_jvmdir}/%{sdkdir}/legal
%doc %{_defaultdocdir}/%{uniquejavadocdir}/NEWS
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{jrelnk}
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/bin/jwebserver
%dir %{_jvmdir}/%{sdkdir}/lib
%ifarch %{jit_arches}
%{_jvmdir}/%{sdkdir}/lib/classlist
%endif
%{_jvmdir}/%{sdkdir}/lib/jexec
%{_jvmdir}/%{sdkdir}/lib/jspawnhelper
%{_jvmdir}/%{sdkdir}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir}/lib/modules
%{_jvmdir}/%{sdkdir}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat*
%{_jvmdir}/%{sdkdir}/lib/libjli.so
%{_jvmdir}/%{sdkdir}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir}/lib/libattach.so
%{_jvmdir}/%{sdkdir}/lib/libawt.so
%{_jvmdir}/%{sdkdir}/lib/libextnet.so
%{_jvmdir}/%{sdkdir}/lib/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir}/lib/libfontmanager.so
%{_jvmdir}/%{sdkdir}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir}/lib/libjaas.so
%{_jvmdir}/%{sdkdir}/lib/libjava.so
%{_jvmdir}/%{sdkdir}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir}/lib/libjimage.so
%{_jvmdir}/%{sdkdir}/lib/libjsound.so
%ifarch x86_64
%{_jvmdir}/%{sdkdir}/lib/libjsvml.so
%endif
%{_jvmdir}/%{sdkdir}/lib/liblcms.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_ext.so
%{_jvmdir}/%{sdkdir}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir}/lib/libnet.so
%{_jvmdir}/%{sdkdir}/lib/libnio.so
%{_jvmdir}/%{sdkdir}/lib/libprefs.so
%{_jvmdir}/%{sdkdir}/lib/librmi.so
# Some architectures don't have the serviceability agent
%ifarch %{sa_arches}
%{_jvmdir}/%{sdkdir}/lib/libsaproc.so
%endif
%{_jvmdir}/%{sdkdir}/lib/libsctp.so
%{_jvmdir}/%{sdkdir}/lib/libsyslookup.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%dir %{_jvmdir}/%{sdkdir}/lib/jfr
%{_jvmdir}/%{sdkdir}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir}/lib/jfr/profile.jfc
%{_mandir}/man1/java-%{name}.1*
%{_mandir}/man1/keytool-%{name}.1*
%{_mandir}/man1/rmiregistry-%{name}.1*
%{_mandir}/man1/jwebserver-%{name}.1*
%{_jvmdir}/%{sdkdir}/lib/server/
%{_jvmdir}/%{sdkdir}/lib/libjvm.so
%ifarch %{share_arches}
%attr(444, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir}
%dir %{etcjavadir}/lib
%dir %{etcjavadir}/lib/security
%{etcjavadir}/lib/security/cacerts*
%dir %{etcjavadir}/conf
%dir %{etcjavadir}/conf/management
%dir %{etcjavadir}/conf/security
%dir %{etcjavadir}/conf/security/policy
%dir %{etcjavadir}/conf/security/policy/limited
%dir %{etcjavadir}/conf/security/policy/unlimited
%config(noreplace) %{etcjavadir}/lib/security/default.policy
%config(noreplace) %{etcjavadir}/lib/security/blocked.certs
%config(noreplace) %{etcjavadir}/lib/security/public_suffix_list.dat
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/exempt_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/default_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/limited/default_US_export.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/unlimited/default_local.policy
%config(noreplace) %{etcjavadir}/conf/security/policy/unlimited/default_US_export.policy
%doc %{etcjavadir}/conf/security/policy/README.txt
%config(noreplace) %{etcjavadir}/conf/security/java.policy
%config(noreplace) %{etcjavadir}/conf/security/java.security
%config(noreplace) %{etcjavadir}/conf/logging.properties
#%config(noreplace) %{etcjavadir}/conf/security/nss.cfg
%config(noreplace) %{etcjavadir}/conf/management/jmxremote.access
# this is conifg template, thus not config-noreplace
%config  %{etcjavadir}/conf/management/jmxremote.password.template
%dir %{etcjavadir}/conf/sdp
%config %{etcjavadir}/conf/sdp/sdp.conf.template
%config(noreplace) %{etcjavadir}/conf/management/management.properties
%config(noreplace) %{etcjavadir}/conf/net.properties
%config(noreplace) %{etcjavadir}/conf/sound.properties
%config(noreplace) %{etcjavadir}/conf/jaxp.properties
%{_jvmdir}/%{sdkdir}/conf
%{_jvmdir}/%{sdkdir}/lib/security
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_bindir}/java
%ghost %{_jvmdir}/jre
# https://bugzilla.redhat.com/show_bug.cgi?id=1312019
%ghost %{_bindir}/keytool
%ghost %{_bindir}/rmid
%ghost %{_bindir}/rmiregistry
%ghost %{_bindir}/jwebserver
%ghost %{_jvmdir}/jre-%{origin}
%ghost %{_jvmdir}/jre-%{javaver}
%ghost %{_jvmdir}/jre-%{javaver}-%{origin}
%endif
%endif
%endif

%if %{include_normal_build}
%files devel
%_altdir/%name-javac
%_altdir/%name-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%dir %{_jvmdir}/%{sdkdir}/bin
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javap
%{_jvmdir}/%{sdkdir}/bin/jconsole
%{_jvmdir}/%{sdkdir}/bin/jcmd
%{_jvmdir}/%{sdkdir}/bin/jdb
%{_jvmdir}/%{sdkdir}/bin/jdeps
%{_jvmdir}/%{sdkdir}/bin/jdeprscan
%{_jvmdir}/%{sdkdir}/bin/jfr
%{_jvmdir}/%{sdkdir}/bin/jimage
# Some architectures don't have the serviceability agent
%ifarch %{sa_arches}
%{_jvmdir}/%{sdkdir}/bin/jhsdb
%endif
%{_jvmdir}/%{sdkdir}/bin/jinfo
%{_jvmdir}/%{sdkdir}/bin/jlink
%{_jvmdir}/%{sdkdir}/bin/jmap
%{_jvmdir}/%{sdkdir}/bin/jmod
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jpackage
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/include
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%if_with systemtap
%{_jvmdir}/%{sdkdir}/tapset
%endif
%{_datadir}/applications/*jconsole.desktop
%{_mandir}/man1/jar-%{name}.1*
%{_mandir}/man1/jarsigner-%{name}.1*
%{_mandir}/man1/javac-%{name}.1*
%{_mandir}/man1/javadoc-%{name}.1*
%{_mandir}/man1/javap-%{name}.1*
%{_mandir}/man1/jcmd-%{name}.1*
%{_mandir}/man1/jconsole-%{name}.1*
%{_mandir}/man1/jdb-%{name}.1*
%{_mandir}/man1/jdeprscan-%{name}.1*
%{_mandir}/man1/jdeps-%{name}.1*
%{_mandir}/man1/jfr-%{name}.1*
%{_mandir}/man1/jhsdb-%{name}.1*
%{_mandir}/man1/jinfo-%{name}.1*
%{_mandir}/man1/jlink-%{name}.1*
%{_mandir}/man1/jmap-%{name}.1*
%{_mandir}/man1/jmod-%{name}.1*
%{_mandir}/man1/jpackage-%{name}.1*
%{_mandir}/man1/jps-%{name}.1*
%{_mandir}/man1/jrunscript-%{name}.1*
%{_mandir}/man1/jshell-%{name}.1*
%{_mandir}/man1/jstack-%{name}.1*
%{_mandir}/man1/jstat-%{name}.1*
%{_mandir}/man1/jstatd-%{name}.1*
%{_mandir}/man1/serialver-%{name}.1*
%if_with systemtap
%dir %{tapsetroot}
%dir %{tapsetdirttapset}
%dir %{tapsetdir}
%{tapsetdir}/*%{_arch}.stp
%endif
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_bindir}/javac
%ghost %{_jvmdir}/java
%ghost %{_bindir}/jaotc
%ghost %{_bindir}/jlink
%ghost %{_bindir}/jmod
%ghost %{_bindir}/jhsdb
%ghost %{_bindir}/jar
%ghost %{_bindir}/jarsigner
%ghost %{_bindir}/javadoc
%ghost %{_bindir}/javap
%ghost %{_bindir}/jcmd
%ghost %{_bindir}/jconsole
%ghost %{_bindir}/jdb
%ghost %{_bindir}/jdeps
%ghost %{_bindir}/jdeprscan
%ghost %{_bindir}/jimage
%ghost %{_bindir}/jinfo
%ghost %{_bindir}/jmap
%ghost %{_bindir}/jps
%ghost %{_bindir}/jrunscript
%ghost %{_bindir}/jshell
%ghost %{_bindir}/jstack
%ghost %{_bindir}/jstat
%ghost %{_bindir}/jstatd
%ghost %{_bindir}/serialver
%ghost %{_jvmdir}/java-%{origin}
%ghost %{_jvmdir}/java-%{javaver}
%ghost %{_jvmdir}/java-%{javaver}-%{origin}
%endif
%endif
%endif

%if %{include_staticlibs}
%files static-libs
%dir %{_jvmdir}/%{sdkdir}/lib/static
%dir %{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}
%dir %{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc
%{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc/lib*.a
%endif

%if %{include_normal_build}
%files jmods
%{_jvmdir}/%{sdkdir}/jmods

%files demo
%{_jvmdir}/%{sdkdir}/demo

%files sources
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%_altdir/%name-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_javadocdir}/java
%endif
%endif

%endif

%if %{include_debug_build}
%files slowdebug

%files headless-slowdebug

%files devel-slowdebug

%files static-libs-slowdebug

%files jmods-slowdebug

%files demo-slowdebug

%files sources-slowdebug
%endif

%changelog
* Sat Aug 24 2024 Andrey Cherepanov <cas@altlinux.org> 0:21.0.4.0.7-alt1
- New version.
- Security fixes:
  - CVE-2024-21131
  - CVE-2024-21138
  - CVE-2024-21140
  - CVE-2024-21145
  - CVE-2024-21147

* Sun Jul 07 2024 Andrey Cherepanov <cas@altlinux.org> 0:21.0.3.0.9-alt1
- New version.
- Security fixes:
  - CVE-2024-21012
  - CVE-2024-21011
  - CVE-2024-21068

* Wed Feb 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0:21.0.2.0.13-alt2
- NMU: worked around FTBFS on LoongArch: disabled LTO until the problem
  is solved properly, see https://github.com/loongson/jdk21u/issues/15

* Mon Feb 05 2024 Andrey Cherepanov <cas@altlinux.org> 0:21.0.2.0.13-alt1
- New version.
- Security fixes:
  - CVE-2024-20918
  - CVE-2024-20919
  - CVE-2024-20921
  - CVE-2024-20945
  - CVE-2024-20952

* Thu Jan 18 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0:21.0.1.0.12-alt2
- NMU: LoongArch support from https://github.com/loongson/jdk21u.git
  branch loongarch-port
  commit 73075208466960879bf48be6dc54a84bf1113716 (notice: it's not a HEAD)

* Thu Jan 11 2024 Andrey Cherepanov <cas@altlinux.org> 0:21.0.1.0.12-alt1
- New version.
- Security fixes: CVE-2023-22081 and CVE-2023-22025.
- End of bootstrapping.

* Fri Oct 06 2023 Andrey Cherepanov <cas@altlinux.org> 0:21.0.0.0.35-alt1
- Initial built in Sisyphus (based on Fedora spec file).
