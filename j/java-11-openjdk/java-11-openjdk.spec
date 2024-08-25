%define _unpackaged_files_terminate_build 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# from java9/hotspot/make/lib/JvmOverrideFiles.gmk:
# Performance measurements show that by compiling GC related code, we could
# significantly reduce the GC pause time on 32 bit Linux/Unix platforms by
# compiling without the PIC flag (-fPIC on linux).
# See 6454213 for more details.
# for arm it is fix by Gleb Fotengauer-Malinovskiy <glebfm@altlinux.org>
%if "%_libsuff" != "64"
%set_verify_elf_method textrel=relaxed
%endif

BuildRequires: ca-certificates-java
%def_enable accessibility
%def_disable javaws
%def_disable moz_plugin
%def_disable control_panel
%def_disable desktop
%def_disable systemtap
%def_disable check
BuildRequires: unzip gcc-c++ libstdc++-devel-static
BuildRequires: libXext-devel libXrender-devel libXcomposite-devel
BuildRequires(pre): browser-plugins-npapi-devel lsb-release
BuildRequires(pre): rpm-macros-java
BuildRequires(pre): ca-trust-java
%set_compress_method none
%filter_from_requires /.usr.bin.java/d
BuildRequires: /proc rpm-build-java
%define fedora 32
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version and %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-11-openjdk
%define version 11.0.24.0.8
%define release 0
# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-1.8.0-openjdk.spec
#
# Produce only release builds (no slowdebug builds) on x86_64:
# $ rpmbuild -ba java-1.8.0-openjdk.spec --without slowdebug
#
# Only produce a release build on x86_64:
# $ fedpkg mockbuild --without slowdebug
#
# Only produce a debug build on x86_64:
# $ fedpkg local --without release
#
# Enable slowdebug builds by default on relevant arches.
%bcond_without slowdebug
# Enable release builds by default on relevant arches.
%bcond_without release

# Workaround for stripping of debug symbols from static libraries
%define __brp_strip_static_archive %{nil}

# The -g flag says to use strip -g instead of full strip on DSOs or EXEs.
# This fixes detailed NMT and other tools which need minimal debug info.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1520879
%global _find_debuginfo_opts -g

# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
# see the difference between global and define:
# See https://github.com/rpm-software-management/rpm/issues/127 to comments at  "pmatilai commented on Aug 18, 2017"
# (initiated in https://bugzilla.redhat.com/show_bug.cgi?id=1482192)
%global debug_suffix_unquoted -slowdebug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global normal_suffix ""

# if you want only debug build but providing java build only normal build but set normalbuild_parameter
%global debug_warning This package has full debug on. Install only in need and remove asap.
%global debug_on with full debug on
%global for_debug for packages with debug on

%if %{with release}
%global include_normal_build 1
%else
%global include_normal_build 1
%endif

%if %{include_normal_build}
%global build_loop1 %{normal_suffix}
%else
%global build_loop1 %{nil}
%endif

# We have hardcoded list of files, which  is appearing in alternatives, and in files
# in alternatives those are slaves and master, very often triplicated by man pages
# in files all masters and slaves are ghosted
# the ghosts are here to allow installation via query like `dnf install /usr/bin/java`
# you can list those files, with appropriate sections: cat *.spec | grep -e --install -e --slave -e post_ 
# TODO - fix those hardcoded lists via single list
# those files ,must *NOT* be ghosted for *slowdebug* packages
# FIXME - if you are moving jshell or jlink or simialr, always modify all three sections
# you can check via headless and devels:
#    rpm -ql --noghost java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# == rpm -ql           java-11-openjdk-headless-slowdebug-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# != rpm -ql           java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# similarly for other %%{_jvmdir}/{jre,java} and %%{_javadocdir}/{java,java-zip}
%define is_release_build() %( if [ "" == "%{debug_suffix_unquoted}" ]; then echo "0" ; else echo "1"; fi )

# while JDK is a techpreview(is_system_jdk=0), some provides are turned off. Once jdk stops to be an techpreview, move it to 1
# as sytem JDK, we mean any JDK which can run whole system java stack without issues (like bytecode issues, module issues, dependencies...)
%global is_system_jdk 1

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
# Set of architectures which support multiple ABIs
%global multilib_arches %{power64} sparc64 x86_64
# Set of architectures for which we build debug builds
%global debug_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} s390x
# Set of architectures with a Just-In-Time (JIT) compiler
%global jit_arches      %{debug_arches} %{arm} loongarch64
# Set of architectures which run a full bootstrap cycle
%global bootstrap_arches %{jit_arches}
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures with a Ahead-Of-Time (AOT) compiler
%global aot_arches      x86_64 %{aarch64}
# Set of architectures which support the serviceability agent
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} loongarch64
# Set of architectures which support class data sharing
# See https://bugzilla.redhat.com/show_bug.cgi?id=513605
# MetaspaceShared::generate_vtable_methods is not implemented for the PPC JIT
%global share_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{arm} s390x
# Set of architectures for which we build the Shenandoah garbage collector
%global shenandoah_arches x86_64 %{aarch64}
# Set of architectures for which we build the Z garbage collector
%global zgc_arches x86_64

# By default, we build a debug build during main build on JIT architectures
%if %{with slowdebug}
%ifarch %{debug_arches}
%global include_debug_build 0
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif

# On certain architectures, we compile the Shenandoah GC
%ifarch %{shenandoah_arches}
%global use_shenandoah_hotspot 1
%global shenandoah_feature shenandoahgc
%else
%global use_shenandoah_hotspot 0
%global shenandoah_feature -shenandoahgc
%endif

# On certain architectures, we compile the ZGC
%ifarch %{zgc_arches}
%global use_zgc_hotspot 1
%global zgc_feature zgc
%else
%global use_zgc_hotspot 0
%global zgc_feature -zgc
%endif

%if %{include_debug_build}
%global build_loop2 %{debug_suffix}
%else
%global build_loop2 %{nil}
%endif

# if you disable both builds, then the build fails
%global build_loop  %{build_loop1} %{build_loop2}
# note: that order: normal_suffix debug_suffix, in case of both enabled
# is expected in one single case at the end of the build
%global rev_build_loop  %{build_loop2} %{build_loop1}

%ifarch %{bootstrap_arches}
%global bootstrap_build 0
%else
%global bootstrap_build 0
%endif

%if %{bootstrap_build}
%global release_targets bootcycle-images static-libs-image docs-zip
%else
%global release_targets images docs-zip static-libs-image
%endif
# No docs nor bootcycle for debug builds
%global debug_targets images static-libs-image

# Disable LTO as this causes build failures at the moment.
%define optflags_lto %nil

# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security) and -Wno-cpp to avoid FORTIFY_SOURCE warnings
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat -Wno-cpp|' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||')
%global ourldflags %{__global_ldflags}

# With disabled nss is NSS deactivated, so NSS_LIBDIR can contain the wrong path
# the initialization must be here. Later the pkg-config have buggy behavior
# looks like openjdk RPM specific bug
# Always set this so the nss.cfg file is not broken
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)

# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _build_cpu
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%endif
%ifarch %{ix86}
%global archinstall i686
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifarch loongarch64
%global archinstall loongarch64
%global stapinstall loongarch64
%endif
%ifnarch %{jit_arches}
%global archinstall %{_arch}
%endif

%ifarch %{systemtap_arches}
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

# New Version-String scheme-style defines
# If you bump majorver, you must bump also vendor_version_string
%global majorver 11
# Used via new version scheme. JDK 11 was
# GA'ed in September 2018 => 18.9
%global vendor_version_string 18.9
# buildjdkver is usually same as %%{majorver},
# but in time of bootstrap of next jdk, it is majorver-1, 
# and this it is better to change it here, on single place
%global buildjdkver %{majorver}
# Add LTS designator for RHEL builds
%if 0%{?rhel}
  %global lts_designator "LTS"
  %global lts_designator_zip -%{lts_designator}
%else
  %global lts_designator ""
  %global lts_designator_zip ""
%endif

# Define IcedTea version used for SystemTap tapsets and desktop file
%global icedteaver      6.0.0pre00-c848b93a8598

# Standard JPackage naming and versioning defines
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{origin}
%global securityver 24
%global minorver    0
%global buildver    8
%global rpmrelease  1
%global dist		jpp11
#%%global tagsuffix      ""
# priority must be 8 digits in total; untill openjdk 1.8 we were using 18..... so when moving to 11 we had to add another digit
%if %is_system_jdk
%define priority %( printf '%02d%02d%02d%02d' %{majorver} %{minorver} %{securityver} %{buildver} )
%else
# for techpreview, using 1, so slowdebugs can have 0
%define priority %( printf '%08d' 3 )
%endif
%global newjavaver      %{majorver}.%{minorver}.%{securityver}.0
%global javaver         %{majorver}

# Define milestone (EA for pre-releases, GA for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga           1
%if %{is_ga}
%global ea_designator ""
%global ea_designator_zip ""
%global extraver %{nil}
%global eaprefix %{nil}
%else
%global ea_designator ea
%global ea_designator_zip -%{ea_designator}
%global extraver .%{ea_designator}
%global eaprefix 0.
%endif

# Define what url should JVM offer in case of a crash report
# order may be important, epel may have rhel declared
%if 0%{?epel}
%global bugs  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{name}&version=epel%{epel}
%else
%if 0%{?fedora}
# Does not work for rawhide, keeps the version field empty
%global bugs  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{name}&version=%{fedora}
%else
%if 0%{?rhel}
%global bugs  https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%20%{rhel}&component=%{name}
%else
%global bugs  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif

# parametrized macros are order-sensitive
%global compatiblename  java-%{majorver}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images directories from upstream build
%global jdkimage                jdk
%global static_libs_image       static-libs
# output dir stub
%define buildoutputdir openjdk/build
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir %{fullversion}.%{_arch}
# main id and dir of this jdk
%define uniquesuffix %{fullversion}.%{_arch}

#################################################################
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
#         https://bugzilla.redhat.com/show_bug.cgi?id=1590796#c14
#         https://bugzilla.redhat.com/show_bug.cgi?id=1655938
#%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsunec[.]so.*|libunpack[.]so.*|libzip[.]so.*
%global _publiclibs libjawt[.]so.*|libjava[.]so.*|libjvm[.]so.*|libverify[.]so.*|libjsig[.]so.*
%if %is_system_jdk
# Never generate lib-style provides/requires for slowdebug packages
%global __provides_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%global __requires_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%else
# Don't generate provides/requires for JDK provided shared libraries at all.
%endif

%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix}}
# Standard JPackage directories and symbolic links.
%define sdkdir %{uniquesuffix}
%define jrelnk jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%define sdkbindir %{_jvmdir}/%{sdkdir}/bin
%define jrebindir %{_jvmdir}/%{sdkdir}/bin

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

%if_enabled systemtap
# Where to install systemtap tapset (links)
# We would like these to be in a package specific sub-dir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinguish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdirttapset %{tapsetroot}/tapset/
%global tapsetdir %{tapsetdirttapset}/%{_build_cpu}
%endif

# not-duplicated scriptlets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
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

Epoch:   0
Summary: %{origin_nice} Runtime Environment %{majorver}

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


# to regenerate source0 (jdk) run update_package.sh
# update_package.sh contains hard-coded repos, revisions, tags, and projects to regenerate the source archives
Source0: openjdk-%{majorver}.%{minorver}.%{securityver}+%{buildver}%{?tagsuffix:-%{tagsuffix}}.tar.xz

# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (3.x).
# Systemtap tapsets. Zipped up to keep it small.
Source8: tapsets-icedtea-%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in

# Release notes
Source10: NEWS

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

# Verify system crypto (policy) can be disabled via a property
Source15: TestSecurityProperties.java

############################################
#
# RPM/distribution specific patches
#
############################################

# NSS via SunPKCS11 Provider (disabled comment
# due to memory leak).
Patch1000: rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch

# Ignore AWTError when assistive technologies are loaded
Patch1:    rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch
# Restrict access to java-atk-wrapper classes
Patch2:    rh1648644-java_access_bridge_privileged_security.patch

#############################################
#
# Shenandoah specific patches
#
#############################################

# Currently empty

#############################################
#
# OpenJDK specific patches
#
#############################################

Patch3:    rh649512-remove_uses_of_far_in_jpeg_libjpeg_turbo_1_4_compat_for_jdk10_and_up.patch

# LoongArch
Patch3500: jdk11u-loongarch.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libalsa-devel
BuildRequires: binutils
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
# elfutils only are OK for build without AOT
BuildRequires: libasm-devel libdw-devel libelf-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libgif-devel
BuildRequires: gcc-c++
BuildRequires: gdb libgdb-devel
BuildRequires: libharfbuzz-devel
BuildRequires: liblcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxslt xsltproc
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirements for setting up the nss.cfg
BuildRequires: libnss-devel
BuildRequires: libX11-devel libXvMC-devel xorg-proto-devel
BuildRequires: zip
BuildRequires: unzip
BuildRequires: javapackages-filesystem
BuildRequires: java-%{buildjdkver}-openjdk-devel
# Zero-assembler build requirement
%ifnarch %{jit_arches}
BuildRequires: libffi-devel
%endif
# 2020b required as of JDK-8254177 in October CPU
BuildRequires: tzdata-java >= 2020b
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3

%if_enabled systemtap
BuildRequires: systemtap-sdt-devel
%endif

Requires: %{name}-headless = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}

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
Source44: import.info
%filter_from_provides /^(%{_privatelibs}|%{_publiclibs})$/d
%filter_from_requires /^(%{_privatelibs}|%{_publiclibs})$/d

%define altname %name
%define label -%{name}
%define javaws_ver      %{javaver}

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
Patch33: java-9-openjdk-alt-no-objcopy.patch

%description
The %{origin_nice} runtime environment.

%if %{include_debug_build}
%package slowdebug
Group: Development/Java
Summary: %{origin_nice} Runtime Environment %{majorver} %{debug_on}

%description slowdebug
The %{origin_nice} runtime environment.
%{debug_warning}
%endif

%if %{include_normal_build}
%package headless
Group: Development/Java
Summary: %{origin_nice} Headless Runtime Environment %{majorver}

# Require /etc/pki/java/cacerts
Requires(pre): ca-trust-java
Requires: ca-trust
# Require javapackages-filesystem for ownership of /usr/lib/jvm/ and macros
Requires: javapackages-filesystem
# Require zone-info data provided by tzdata-java sub-package
# 2020a required as of JDK-8243541 in 11.0.8+4
Requires: tzdata-java >= 2022a

# Standard JPackage base provides
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-headless = %{epoch}:%{version}-%{release}
Provides: java-headless = %{epoch}:%{version}-%{release}
%endif
Requires: java-common
Requires: /proc
Requires(post): /proc

%description headless
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%endif

%if %{include_debug_build}
%package headless-slowdebug
Group: Development/Java
Summary: %{origin_nice} Runtime Environment %{debug_on}

%description headless-slowdebug
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%{debug_warning}
%endif

%if %{include_normal_build}
%package devel
Group: Development/Java
Summary: %{origin_nice} Development Environment %{majorver}

# Requires base package
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
# Postun requires alternatives to uninstall tool alternatives

# Standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-devel = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-devel = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-sdk-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-devel = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-devel = %{epoch}:%{version}-%{release}
Provides: java-sdk = %{epoch}:%{version}-%{release}
%endif

%description devel
The %{origin_nice} development tools %{majorver}.
%endif

%if %{include_debug_build}
%package devel-slowdebug
Group: Development/Java
Summary: %{origin_nice} Development Environment %{majorver} %{debug_on}

%description devel-slowdebug
The %{origin_nice} development tools %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package static-libs
Group: Development/Java
Summary: %{origin_nice} libraries for static linking %{majorver}

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}

%description static-libs
The %{origin_nice} libraries for static linking %{majorver}.
%endif

%if %{include_debug_build}
%package static-libs-slowdebug
Group: Development/Java
Summary: %{origin_nice} libraries for static linking %{majorver} %{debug_on}

%description static-libs-slowdebug
The %{origin_nice} libraries for static linking %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package jmods
Group: Development/Java
Summary: JMods for %{origin_nice} %{majorver}

# Requires devel package
# as jmods are bytecode, they should be OK without any _isa
Requires: %{name}-headless = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-jmods = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-jmods = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-jmods = %{epoch}:%{version}-%{release}
%endif

%description jmods
The JMods for %{origin_nice}.
%endif

%if %{include_debug_build}
%package jmods-slowdebug
Group: Development/Java
Summary: JMods for %{origin_nice} %{majorver} %{debug_on}

%description jmods-slowdebug
The JMods for %{origin_nice} %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package demo
Group: Development/Java
Summary: %{origin_nice} Demos %{majorver}

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-demo = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-demo = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-demo = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-demo = %{epoch}:%{version}-%{release}
%endif

%description demo
The %{origin_nice} demos %{majorver}.
%endif

%if %{include_debug_build}
%package demo-slowdebug
Group: Development/Java
Summary: %{origin_nice} Demos %{majorver} %{debug_on}

%description demo-slowdebug
The %{origin_nice} demos %{majorver}.
%{debug_warning}
%endif

%if %{include_normal_build}
%package src
Group: Development/Java
Summary: %{origin_nice} Source Bundle %{majorver}

Requires: %{name}-headless = %{epoch}:%{version}-%{release}

# Standard JPackage sources provides
Provides: java-%{javaver}-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-src = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-src = %{epoch}:%{version}-%{release}
%endif

%description src
The java-%{origin}-src sub-package contains the complete %{origin_nice} %{majorver}
class library source code for use by IDE indexers and debuggers.
%endif

%if %{include_debug_build}
%package src-slowdebug
Group: Development/Java
Summary: %{origin_nice} Source Bundle %{majorver} %{for_debug}

%description src-slowdebug
The java-%{origin}-src-slowdebug sub-package contains the complete %{origin_nice} %{majorver}
 class library source code for use by IDE indexers and debuggers. Debugging %{for_debug}.
%endif

%if %{include_normal_build}
%package javadoc
Group: Development/Java
Summary: %{origin_nice} %{majorver} API documentation
Requires: javapackages-filesystem
Obsoletes: javadoc-slowdebug < 1:11.0.3.7-4

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
# Postun requires alternatives to uninstall javadoc alternative

# Standard JPackage javadoc provides
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-javadoc = %{epoch}:%{version}-%{release}
%endif

%description javadoc
The %{origin_nice} %{majorver} API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Group: Development/Java
Summary: %{origin_nice} %{majorver} API documentation compressed in a single archive
Requires: javapackages-filesystem
Obsoletes: javadoc-zip-slowdebug < 1:11.0.3.7-4

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
# Postun requires alternatives to uninstall javadoc alternative

# Standard JPackage javadoc provides
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-javadoc = %{epoch}:%{version}-%{release}
%endif

%description javadoc-zip
The %{origin_nice} %{majorver} API documentation compressed in a single archive.
%endif

%prep
if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 ] ; then
  echo "You have disabled both include_debug_build and include_normal_build. That is a no go."
  exit 13
fi
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

# OpenJDK patches

# Rename versioning subdirectory to openjdk
mv jdk-%{majorver}.%{minorver}.%{securityver}+%{buildver}%{?tagsuffix:-%{tagsuffix}} %{top_level_dir_name}

# Remove libraries that are linked
sh %{SOURCE12}
pushd %{top_level_dir_name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch3500 -p1
popd # openjdk

%patch1000

# Extract systemtap tapsets
%if_enabled systemtap
tar --strip-components=1 -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif

for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e "s:\.stp\.in$:-%{version}-%{release}.%{_arch}.stp:g"`
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/server/libjvm.so:g" $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/client/libjvm.so:g" $file.1 > $OUTPUT_FILE
%else
    sed -e "/@ABS_CLIENT_LIBJVM_SO@/d" $file.1 > $OUTPUT_FILE
%endif
    sed -i -e "s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir}:g" $OUTPUT_FILE
    sed -i -e "s:@INSTALL_ARCH_DIR@:%{archinstall}:g" $OUTPUT_FILE
    sed -i -e "s:@prefix@:%{_jvmdir}/%{sdkdir}/:g" $OUTPUT_FILE
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
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:_SDKBINDIR_:%{sdkbindir}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@target_cpu@:%{_arch}:g" $OUTPUT_FILE
    sed -i -e  "s:@OPENJDK_VER@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VER@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg
%patch33 -p0

%build
# How many CPU's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

%ifarch s390x sparc64 alpha %{power64} %{aarch64}
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
# Explicitly set -fcommon as GCC 10+ defaults to -fno-common
EXTRA_CFLAGS="%ourcppflags -Wno-error -fcommon"
EXTRA_CPP_FLAGS="%ourcppflags -fcommon"

%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
# Fixes annocheck warnings in assembler files due to missing build notes
EXTRA_ASFLAGS="${EXTRA_CFLAGS} -Wa,--generate-missing-build-notes=yes"
export EXTRA_CFLAGS EXTRA_ASFLAGS

for suffix in %{build_loop} ; do
if [ "x$suffix" = "x" ] ; then
  debugbuild=release
else
  # change --something to something
  debugbuild=`echo $suffix  | sed "s/-//g"`
fi

# Variable used in hs_err hook on build failures
top_dir_abs_path=$(pwd)/%{top_level_dir_name}

mkdir -p %{buildoutputdir}
pushd %{buildoutputdir}

bash ../configure \
%ifnarch %{jit_arches}
    --with-jvm-variants=zero \
%endif
%ifarch %{ppc64le}
    --with-jobs=1 \
%endif
    --with-version-build=1 \
    --with-version-pre="%{ea_designator}" \
    --with-version-opt=%{lts_designator} \
    --with-version-patch=1 \
    --with-vendor-version-string="%{vendor_version_string}" \
    --with-vendor-name="Red Hat, Inc." \
    --with-vendor-url="https://www.redhat.com/" \
    --with-vendor-bug-url="%{bugs}" \
    --with-vendor-vm-bug-url="%{bugs}" \
    --with-boot-jdk=/usr/lib/jvm/java-%{buildjdkver}-openjdk \
    --with-debug-level=$debugbuild \
    --with-native-debug-symbols=internal \
    --enable-unlimited-crypto \
    --with-giflib=system \
    --with-libjpeg=system \
    --with-libpng=system \
    --with-lcms=system \
    --with-harfbuzz=system \
    --with-zlib=system \
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-asflags="$EXTRA_ASFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC" \
    --disable-javac-server \
    --with-jvm-features="%{shenandoah_feature},%{zgc_feature}" \
    --disable-warnings-as-errors

# Debug builds don't need same targets as release for
# build speed-up
maketargets="%{release_targets}"
if echo $debugbuild | grep -q "debug" ; then
  maketargets="%{debug_targets}"
fi
make \
    JAVAC_FLAGS=-g \
    LOG=trace \
    WARNINGS_ARE_ERRORS="-Wno-error" \
    CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
    $maketargets || ( pwd; find $top_dir_abs_path -name "hs_err_pid*.log" | xargs cat && false )

# the build (erroneously) removes read permissions from some jars
# this is a regression in OpenJDK 7 (our compiler):
# http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
find images/%{jdkimage} -iname '*.jar' -exec chmod ugo+r {} \;

# Build screws up permissions on binaries
# https://bugs.openjdk.java.net/browse/JDK-8173610
find images/%{jdkimage} -iname '*.so' -exec chmod +x {} \;
find images/%{jdkimage}/bin/ -exec chmod +x {} \;

popd >& /dev/null

# Install nss.cfg right away as we will be using the JRE above
export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Install nss.cfg right away as we will be using the JRE above
#install -m 644 nss.cfg $JAVA_HOME/conf/security/

# Use system-wide tzdata
rm $JAVA_HOME/lib/tzdb.dat
ln -s %{_datadir}/javazi-1.8/tzdb.dat $JAVA_HOME/lib/tzdb.dat

# build cycles
done

%check
%if_enabled check
# We test debug first as it will give better diagnostics on a crash
for suffix in %{rev_build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

#check Shenandoah is enabled
%if %{use_shenandoah_hotspot}
$JAVA_HOME//bin/java -XX:+UseShenandoahGC -version
%endif

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
#$JAVA_HOME/bin/javac -d . %{SOURCE14}
#$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")

# Check system crypto (policy) can be disabled
$JAVA_HOME/bin/javac -d . %{SOURCE15}
$JAVA_HOME/bin/java -Djava.security.disableSystemPropertiesFile=true $(echo $(basename %{SOURCE15})|sed "s|\.java||")

# Check debug symbols in static libraries (smoke test)
export STATIC_LIBS_HOME=$(pwd)/%{buildoutputdir}/images/%{static_libs_image}
readelf --debug-dump $STATIC_LIBS_HOME/lib/libfdlibm.a | grep w_remainder.c
readelf --debug-dump $STATIC_LIBS_HOME/lib/libfdlibm.a | grep e_remainder.c

# Check debug symbols are present and can identify code
find "$JAVA_HOME" -iname '*.so' -print0 | while read -d $'\0' lib
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
     # We expect to see .cpp files, except for architectures like aarch64 and
     # s390 where we expect .o and .oS files
      echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|oS))?$"
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
    if eu-readelf -S "$lib" | grep '] .gnu_debuglink' | grep PROGBITS; then
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
gdb -q "$JAVA_HOME/bin/java" <<EOF | tee gdb.out
handle SIGSEGV pass nostop noprint
handle SIGILL pass nostop noprint
set breakpoint pending on
break javaCalls.cpp:1
commands 1
backtrace
quit
end
run -version
EOF
# This fails on s390x for some reason. Disable for now. See:
# https://koji.fedoraproject.org/koji/taskinfo?taskID=41499227
%ifnarch s390x
grep 'JavaCallWrapper::JavaCallWrapper' gdb.out
%endif

# Check src.zip has all sources. See RHBZ#1130490
jar -tf $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'

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
%endif

%install
STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
cp -a %{buildoutputdir}/images/%{jdkimage} \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

pushd %{buildoutputdir}/images/%{jdkimage}

%if_enabled systemtap
  # Install systemtap support files
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset
  # note, that uniquesuffix  is in BUILD dir in this case
  cp -a $RPM_BUILD_DIR/%{uniquesuffix ""}/tapset$suffix/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
  pushd  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/tapset/
   tapsetFiles=`ls *.stp`
  popd
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  for name in $tapsetFiles ; do
    targetName=`echo $name | sed "s/.stp/$suffix.stp/"`
    ln -sf %{_jvmdir}/%{sdkdir}/tapset/$name $RPM_BUILD_ROOT%{tapsetdir}/$targetName
  done
%endif

  # Remove empty cacerts database
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security/cacerts
  # Install cacerts symlink needed by some apps which hard-code the path
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/security
      ln -sf /etc/pki/java/cacerts .
  popd

  # Install version-ed symlinks
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{sdkdir} %{jrelnk}
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
  rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/man

popd
# Install static libs artefacts
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc
cp -a %{buildoutputdir}/images/%{static_libs_image}/lib/*.a \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc

if ! echo $suffix | grep -q "debug" ; then
  # Install Javadoc documentation
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  cp -a %{buildoutputdir}/images/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}
  cp -a %{buildoutputdir}/bundles/jdk-*%{lts_designator_zip}-docs.zip $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}.zip
fi

# Install release notes
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir}
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
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# copy samples next to demos; samples are mostly js files
cp -r %{top_level_dir_name}/src/sample  $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/


# moving config files to /etc
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/conf/  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib/security  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}
  ln -s %{etcjavadir -- $suffix}/conf  ./conf
popd
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/lib
  ln -s %{etcjavadir -- $suffix}/lib/security  ./security
popd
# end moving files to /etc

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "*.so" -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -type d -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/legal -type f -exec chmod 644 {} \; ; 

# end, dual install
done
for rpm404_ghost in %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa %{_bindir}/java %{_jvmdir}/jre %{_bindir}/jjs %{_bindir}/keytool %{_bindir}/pack200 %{_bindir}/rmid %{_bindir}/rmiregistry %{_bindir}/unpack200 %{_jvmdir}/jre-%{origin} %{_jvmdir}/jre-%{javaver} %{_jvmdir}/jre-%{javaver}-%{origin} %{_bindir}/javac %{_jvmdir}/java %{_bindir}/jaotc %{_bindir}/jlink %{_bindir}/jmod %{_bindir}/jhsdb %{_bindir}/jar %{_bindir}/jarsigner %{_bindir}/javadoc %{_bindir}/javap %{_bindir}/jcmd %{_bindir}/jconsole %{_bindir}/jdb %{_bindir}/jdeps %{_bindir}/jdeprscan %{_bindir}/jimage %{_bindir}/jinfo %{_bindir}/jmap %{_bindir}/jps %{_bindir}/jrunscript %{_bindir}/jshell %{_bindir}/jstack %{_bindir}/jstat %{_bindir}/jstatd %{_bindir}/rmic %{_bindir}/serialver %{_jvmdir}/java-%{origin} %{_jvmdir}/java-%{javaver} %{_jvmdir}/java-%{javaver}-%{origin} %{_javadocdir}/java %{_javadocdir}/java-zip
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

%if %{include_normal_build}
# intentionally only for non-debug
%endif

export LANG=ru_RU.UTF-8
if stat -t %buildroot/usr/share/applications/*policytool.desktop; then
  sed -i 's,^Categories=.*,Categories=Settings;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name --set-value='OpenJDK %majorver Policy Tool' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment --set-value='Manage OpenJDK %majorver policy files' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Name[ru] --set-value='Настройка политик OpenJDK %majorver' %buildroot/usr/share/applications/*policytool.desktop
  desktop-file-edit --set-key=Comment[ru] --set-value='Управление файлами политик OpenJDK %majorver' %buildroot/usr/share/applications/*policytool.desktop
fi
sed -i 's,^Categories=.*,Categories=Development;Profiling;Java;X-ALTLinux-Java;X-ALTLinux-Java-%javaver-%{origin};,' %buildroot/usr/share/applications/*jconsole.desktop
#Name=OpenJDK 8 Monitoring & Management Console
desktop-file-edit --set-key=Name --set-value='OpenJDK %majorver Management Console' %buildroot/usr/share/applications/*jconsole.desktop
#Comment=Monitor and manage OpenJDK applications
desktop-file-edit --set-key=Comment --set-value='Monitor and manage OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Name[ru] --set-value='Консоль OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop
desktop-file-edit --set-key=Comment[ru] --set-value='Мониторинг и управление приложениями OpenJDK %majorver' %buildroot/usr/share/applications/*jconsole.desktop

##### javadoc Alt specific #####
echo java-javadoc >java-javadoc-buildreq-substitute
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
install -m644 java-javadoc-buildreq-substitute \
    %buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%altname-javadoc<<EOF
%{_javadocdir}/java	%{_javadocdir}/%{uniquejavadocdir}/api	%{priority}
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
%{_bindir}/java	%{_jvmdir}/%{sdkdir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/java
EOF
# binaries and manuals
for i in jjs keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  if [ -e %buildroot%{_jvmdir}/%{sdkdir}/bin/$i ]; then
    cat <<EOF >>%buildroot%_altdir/%name-java-headless
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/java
EOF
  fi
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{sdkdir}/bin/ControlPanel	%{_jvmdir}/%{sdkdir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{sdkdir}/bin/jcontrol	%{_jvmdir}/%{sdkdir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java-headless
%{_jvmdir}/jre	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/jre-%{javaver}-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/java
EOF
# ----- end: JPackage compatibility alternatives ------

# Javac alternative
cat <<EOF >%buildroot%_altdir/%name-javac
%_bindir/javac	%{_jvmdir}/%{sdkdir}/bin/javac	%priority
%_man1dir/javac.1.gz	%_man1dir/javac%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF

# binaries and manuals
for i in appletviewer extcheck idlj jar jarsigner javadoc javah javap jdb native2ascii rmic serialver apt jconsole jinfo jmap jmc jps jsadebugd jstack jstat jstatd \
jhat jrunscript jvisualvm schemagen wsgen wsimport xjc
do
  if [ -e $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/bin/$i ]; then
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
  fi
done
# binaries w/o manuals
for i in HtmlConverter
do
  cat <<EOF >>%buildroot%_altdir/%name-javac
%_bindir/$i	%{_jvmdir}/%{sdkdir}/bin/$i	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
done

# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-javac
%{_jvmdir}/java	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/java-%{origin}	%{_jvmdir}/%{sdkdir}	%{_jvmdir}/%{sdkdir}/bin/javac
EOF
cat <<EOF >>%buildroot%_altdir/%name-javac-versioned
%{_jvmdir}/java-%{javaver}	%{_jvmdir}/%{sdkdir}	%priority
%{_jvmdir}/java-%{javaver}-%{origin}	%{_jvmdir}/%{sdkdir}	%priority
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

%post headless
# java should be available ASAP
%force_update_alternatives

%ifarch %{jit_arches}
# MetaspaceShared::generate_vtable_methods not implemented for PPC JIT
%ifnarch %{power64}
#see https://bugzilla.redhat.com/show_bug.cgi?id=513605
java=%{jrebindir}/java
if [ -f /proc/cpuinfo ] && ! [ -d /.our ] ; then #real workstation; not a mkimage-profile, etc
    $java -Xshare:dump >/dev/null 2>/dev/null ||:
fi
%endif
%endif

%if %{include_normal_build}
%files
%_sysconfdir/buildreqs/packages/substitute.d/%name
# main package builds always
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_jvmdir}/%{sdkdir}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/lib/libjawt.so
%else
%files
# placeholder
%endif

%if %{include_normal_build}
%files headless
%_altdir/%altname-java-headless
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
%{_jvmdir}/%{sdkdir}/bin/jjs
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/pack200
%{_jvmdir}/%{sdkdir}/bin/rmid
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/bin/unpack200
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
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat
%dir %{_jvmdir}/%{sdkdir}/lib/jli
%{_jvmdir}/%{sdkdir}/lib/jli/libjli.so
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
#%{_jvmdir}/%{sdkdir}/lib/libsunec.so
%{_jvmdir}/%{sdkdir}/lib/libunpack.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_jvmdir}/%{sdkdir}/lib/libsunec.so
%dir %{_jvmdir}/%{sdkdir}/lib/jfr
%{_jvmdir}/%{sdkdir}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir}/lib/jfr/profile.jfc
%{_mandir}/man1/java%{label}.1*
%{_mandir}/man1/jjs%{label}.1*
%{_mandir}/man1/keytool%{label}.1*
%{_mandir}/man1/pack200%{label}.1*
%{_mandir}/man1/rmid%{label}.1*
%{_mandir}/man1/rmiregistry%{label}.1*
%{_mandir}/man1/unpack200%{label}.1*
%{_jvmdir}/%{sdkdir}/lib/server/
%{_jvmdir}/%{sdkdir}/lib/libjvm.so
%ifarch %{share_arches}
%attr(444, root, root) %ghost %{_jvmdir}/%{sdkdir}/lib/server/classes.jsa
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir}
%dir %{etcjavadir}/lib
%dir %{etcjavadir}/lib/security
%{etcjavadir}/lib/security/cacerts
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
 %{etcjavadir}/conf/security/policy/README.txt
%config(noreplace) %{etcjavadir}/conf/security/java.policy
%config(noreplace) %{etcjavadir}/conf/security/java.security
%config(noreplace) %{etcjavadir}/conf/logging.properties
#%config(noreplace) %{etcjavadir}/conf/security/nss.cfg
%config(noreplace) %{etcjavadir}/conf/management/jmxremote.access
# this is conifg template, thus not config-noreplace
%config  %{etcjavadir}/conf/management/jmxremote.password.template
%config(noreplace) %{etcjavadir}/conf/management/management.properties
%config(noreplace) %{etcjavadir}/conf/net.properties
%config(noreplace) %{etcjavadir}/conf/sound.properties
%{_jvmdir}/%{sdkdir}/conf
%{_jvmdir}/%{sdkdir}/lib/security
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_bindir}/java
%ghost %{_jvmdir}/jre
# https://bugzilla.redhat.com/show_bug.cgi?id=1312019
%ghost %{_bindir}/jjs
%ghost %{_bindir}/keytool
%ghost %{_bindir}/pack200
%ghost %{_bindir}/rmid
%ghost %{_bindir}/rmiregistry
%ghost %{_bindir}/unpack200
%ghost %{_jvmdir}/jre-%{origin}
%ghost %{_jvmdir}/jre-%{javaver}
%ghost %{_jvmdir}/jre-%{javaver}-%{origin}
%endif
%endif

%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
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
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/serialver
%ifarch %{aot_arches}
%{_jvmdir}/%{sdkdir}/bin/jaotc
%endif
%{_jvmdir}/%{sdkdir}/include
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%if_enabled systemtap
%{_jvmdir}/%{sdkdir}/tapset
%endif
%{_datadir}/applications/*jconsole.desktop
%{_mandir}/man1/jar%{label}.1*
%{_mandir}/man1/jarsigner%{label}.1*
%{_mandir}/man1/javac%{label}.1*
%{_mandir}/man1/javadoc%{label}.1*
%{_mandir}/man1/javap%{label}.1*
%{_mandir}/man1/jconsole%{label}.1*
%{_mandir}/man1/jcmd%{label}.1*
%{_mandir}/man1/jdb%{label}.1*
%{_mandir}/man1/jdeps%{label}.1*
%{_mandir}/man1/jinfo%{label}.1*
%{_mandir}/man1/jmap%{label}.1*
%{_mandir}/man1/jps%{label}.1*
%{_mandir}/man1/jrunscript%{label}.1*
%{_mandir}/man1/jstack%{label}.1*
%{_mandir}/man1/jstat%{label}.1*
%{_mandir}/man1/jstatd%{label}.1*
%{_mandir}/man1/rmic%{label}.1*
%{_mandir}/man1/serialver%{label}.1*
%if_enabled systemtap
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
%ghost %{_bindir}/rmic
%ghost %{_bindir}/serialver
%ghost %{_jvmdir}/java-%{origin}
%ghost %{_jvmdir}/java-%{javaver}
%ghost %{_jvmdir}/java-%{javaver}-%{origin}
%endif
%endif

%files static-libs
%dir %{_jvmdir}/%{sdkdir}/lib/static
%dir %{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}
%dir %{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc
%{_jvmdir}/%{sdkdir}/lib/static/linux-%{archinstall}/glibc/lib*.a

%files jmods
%{_jvmdir}/%{sdkdir}/jmods

%files demo
%{_jvmdir}/%{sdkdir}/demo
%{_jvmdir}/%{sdkdir}/sample

%files src
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_javadocdir}/java
%endif
%endif

# this puts huge file to /usr/share
# unluckily ti is really a documentation file
# and unluckily it really is architecture-dependent, as eg. aot and grail are now x86_64 only
# same for debug variant
%files javadoc-zip
%doc %{_javadocdir}/%{uniquejavadocdir}.zip
%if %is_system_jdk
%if %{is_release_build}
%ghost %{_javadocdir}/java-zip
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

%files src-slowdebug
%endif

%changelog
* Sun Aug 25 2024 Andrey Cherepanov <cas@altlinux.org> 0:11.0.24.0.8-alt1
- New version.
- Security fixes
  - CVE-2024-21147
  - CVE-2024-21145
  - CVE-2024-21140
  - CVE-2024-21144
  - CVE-2024-21131
  - CVE-2024-21138

* Sat Jun 29 2024 Andrey Cherepanov <cas@altlinux.org> 0:11.0.23.0.9-alt1
- New version.
- Security fixes
  - CVE-2024-21012
  - CVE-2024-21011
  - CVE-2024-21085
  - CVE-2024-21068
  - CVE-2024-21094

* Sat Feb 03 2024 Andrey Cherepanov <cas@altlinux.org> 0:11.0.22.0.7-alt1
- New version.
- Security fixes
  - CVE-2024-20918
  - CVE-2024-20919
  - CVE-2024-20921
  - CVE-2024-20926
  - CVE-2024-20945
  - CVE-2024-20952

* Tue Dec 05 2023 Andrey Cherepanov <cas@altlinux.org> 0:11.0.21.0.9-alt1
- New version (fixes CVE-2023-22081)

* Mon Sep 18 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0:11.0.20.0.8-alt1_1jpp12
- NMU: support LoongArch architecture (patch from https://github.com/loongson/jdk11u.git
  branch master-ls, commit 6d17df1e42474ecf2feb7960cc47c2b9a3ddca43)

* Thu Aug 24 2023 Andrey Cherepanov <cas@altlinux.org> 0:11.0.20.0.8-alt1_1jpp11
- New version.
- Security fixes
  + CVE-2023-22006
  + CVE-2023-22036
  + CVE-2023-22041
  + CVE-2023-22044
  + CVE-2023-22045
  + CVE-2023-22049
  + CVE-2023-25193
- Removed implicit requirements.

* Sat Jul 29 2023 Andrey Cherepanov <cas@altlinux.org> 0:11.0.19.0.7-alt1_1jpp11
- New version.
- Security fixes
  + CVE-2023-21930
  + CVE-2023-21937
  + CVE-2023-21938
  + CVE-2023-21939
  + CVE-2023-21954
  + CVE-2023-21967
  + CVE-2023-21968

* Wed Feb 08 2023 Andrey Cherepanov <cas@altlinux.org> 0:11.0.18.0.10-alt1_1jpp11
- New version.
- Security fixes
  + CVE-2023-21835
  + CVE-2023-21843
  + JDK-8286077, CVE-2022-21618: Wider MultiByte conversions
  + JDK-8286526, CVE-2022-21619: Improve NTLM support
  + JDK-8286533, CVE-2022-21626: Key X509 usages
  + JDK-8286910, CVE-2022-21624: Improve JNDI lookups
  + JDK-8286918, CVE-2022-21628: Better HttpServer service
  + JDK-8289366, CVE-2022-39399: Improve HTTP/2 client usage

* Tue Oct 04 2022 Andrey Cherepanov <cas@altlinux.org> 0:11.0.17.0.1-alt1_0.1.eajpp11
- New version.

* Wed Aug 03 2022 Andrey Cherepanov <cas@altlinux.org> 0:11.0.16.0.8-alt1_1jpp11
- New version.
- Security fixes
  + JDK-8281859, CVE-2022-21540: Improve class compilation
  + JDK-8281866, CVE-2022-21541: Enhance MethodHandle invocations
  + JDK-8285407, CVE-2022-34169: Improve Xalan supports

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 0:11.0.15.0.10-alt1_1jpp11
- New version.
- Security fixes
  + JDK-8270504, CVE-2022-21426: Better XPath expression handling
  + JDK-8275082, JDK-8278008, CVE-2022-21476: Update XML Security for Java to 2.3.0
  + JDK-8275151, CVE-2022-21443: Improved Object Identification
  + JDK-8277672, CVE-2022-21434: Better invocation handler handling
  + JDK-8278972, CVE-2022-21496: Improve URL supports

* Mon Apr 18 2022 Igor Vlasenko <viy@altlinux.org> 0:11.0.14.1.1-alt2_1jpp11
- NMU: corrected libjvm.so provides.

* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 0:11.0.14.1.1-alt1_1jpp11
- New version.
- Security fixes
  + JDK-8217375: jarsigner breaks old signature with long lines in manifest
  + JDK-8251329: (zipfs) Files.walkFileTree walks infinitely if zip has dir named "." inside
  + JDK-8264934, CVE-2022-21248: Enhance cross VM serialization
  + JDK-8268488: More valuable DerValues
  + JDK-8268494: Better inlining of inlined interfaces
  + JDK-8268512: More content for ContentInfo
  + JDK-8268795: Enhance digests of Jar files
  + JDK-8268801: Improve PKCS attribute handling
  + JDK-8268813, CVE-2022-21283: Better String matching
  + JDK-8269151: Better construction of EncryptedPrivateKeyInfo
  + JDK-8269944: Better HTTP transport redux
  + JDK-8270386, CVE-2022-21291: Better verification of scan methods
  + JDK-8270392, CVE-2022-21293: Improve String constructions
  + JDK-8270416, CVE-2022-21294: Enhance construction of Identity maps
  + JDK-8270492, CVE-2022-21282: Better resolution of URIs
  + JDK-8270498, CVE-2022-21296: Improve SAX Parser configuration management
  + JDK-8270646, CVE-2022-21299: Improved scanning of XML entities
  + JDK-8270952, CVE-2022-21277: Improve TIFF file handling
  + JDK-8271962: Better TrueType font loading
  + JDK-8271968: Better canonical naming
  + JDK-8271987: Manifest improved manifest entries
  + JDK-8272014, CVE-2022-21305: Better array indexing
  + JDK-8272026, CVE-2022-21340: Verify Jar Verification
  + JDK-8272236, CVE-2022-21341: Improve serial forms for transport
  + JDK-8272272: Enhance jcmd communication
  + JDK-8272462: Enhance image handling
  + JDK-8273290: Enhance sound handling
  + JDK-8273756, CVE-2022-21360: Enhance BMP image support
  + JDK-8273838, CVE-2022-21365: Enhanced BMP processing
  + JDK-8274096, CVE-2022-21366: Improve decoding of image files
  + JDK-8279541: Improve HarfBuzz
- Fixed linking libraries.
- Removed duplicated files with legal information from packages.

* Sun Dec 19 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.14.1-alt1_0.1.eajpp11
- New version.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.13.8-alt2_1jpp11
- Ignore possible fail of %%post scriptlet (ALT #40831).
- Optionally disable %%check by default.

* Sat Oct 23 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.13.8-alt1_1jpp11
- New version.
- Security fixes:
  + CVE-2021-35550 Update the default enabled cipher suites preference
  + CVE-2021-35565 com.sun.net.HttpsServer spins on TLS session close
  + CVE-2021-35556 Richer Text Editors
  + CVE-2021-35559 Enhanced style for RTF kit
  + CVE-2021-35561 Better hashing support
  + CVE-2021-35564 Improve Keystore integrity
  + CVE-2021-35567 More Constrained Delegation
  + CVE-2021-35578 Improve TLS client handshaking
  + CVE-2021-35586 Better BMP support
  + CVE-2021-35603 Better session identification

* Mon Oct 18 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.13.7-alt1_0jpp11
- New version.
- Fix some license names according to SPDX.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.12.7-alt2_0jpp10
- Use system libharfbuzz.

* Wed Aug 25 2021 Andrey Cherepanov <cas@altlinux.org> 0:11.0.12.7-alt1_0jpp10
- new version
- security fixes:
  + CVE-2021-2341: Improve file transfers
  + CVE-2021-2369: Better jar file validation
  + CVE-2021-2388: Enhance compiler validation
  + CVE-2021-2161: Less ambiguous processing
  + CVE-2021-2163: Enhance opening JARs
  + CVE-2020-14779: Enhance support of Proxy class
  + CVE-2020-14781: Enhanced LDAP contexts
  + CVE-2020-14782: Enhance certificate processing
  + CVE-2020-14792: Better range handling
  + CVE-2020-14796: Improved URI Support
  + CVE-2020-14797: Better Path Validation
  + CVE-2020-14798: Enhanced buffer support
  + CVE-2020-14803: Improved Buffer supports
  + CVE-2020-14562: Enhance TIFF support
  + CVE-2020-14573: Enhance Graal interface handling
  + CVE-2020-14556: Better ForkJoinPool behavior
  + CVE-2020-14577: Enhance certificate verification
  + CVE-2020-14581: Better matrix operations
  + CVE-2020-14583: Better Buffer support
  + CVE-2020-14593: Less Affine Transformations
  + CVE-2020-14621: Better XML namespace handling
  + CVE-2020-2754: Forward references to Nashorn
  + CVE-2020-2755: Improve Nashorn matching
  + CVE-2020-2756: Better mapping of serial ENUMs
  + CVE-2020-2757: Less Blocking Array Queues
  + CVE-2020-2773: Better signatures in XML
  + CVE-2020-2778: More constrained algorithms
  + CVE-2020-2767: Improve TLS verification
  + CVE-2020-2781: Improve TLS session handling
  + CVE-2020-2800: Better Headings for HTTP Servers
  + CVE-2020-2803: Enhance buffering of byte buffers
  + CVE-2020-2805: Enhance typing of methods
  + CVE-2020-2816: Enhance TLS connectivity
  + CVE-2020-2830: Better Scanner conversions
  + CVE-2020-2583: Unlink Set of LinkedHashSets
  + CVE-2020-2590: Improve Kerberos interop capabilities
  + CVE-2020-2593: Normalize normalization for all
  + CVE-2020-2601: Better Ticket Granting Services
  + CVE-2020-2604: Better serial filter handling
  + CVE-2020-2655: Better TLS messaging support
  + CVE-2020-2654: Improve Object Identifier Processing
  + CVE-2019-2933: Windows file handling redux
  + CVE-2019-2945: Better socket support
  + CVE-2019-2949: Better Kerberos ccache handling
  + CVE-2019-2958: Build Better Processes
  + CVE-2019-2964: Better support for patterns
  + CVE-2019-2962: Better Glyph Images
  + CVE-2019-2973: Better pattern compilation
  + CVE-2019-2975: Unexpected exception in jjs
  + CVE-2019-2978: Improved handling of jar files
  + CVE-2019-2977: Improve String index handling
  + CVE-2019-2981: Better Path supports
  + CVE-2019-2983: Better serial attributes
  + CVE-2019-2987: Better rendering of native glyphs
  + CVE-2019-2988: Better Graphics2D drawing
  + CVE-2019-2989: Improve TLS connection support
  + CVE-2019-2992: Enhance font glyph mapping
  + CVE-2019-2999: Commentary on Javadoc comments
  + CVE-2019-2894: Enhance ECDSA operations
  + CVE-2019-2762: Exceptional throw cases
  + CVE-2019-2766: Improve file protocol handling
  + CVE-2019-2769: Better copies of CopiesList
  + CVE-2019-2786: More limited privilege usage
  + CVE-2019-7317: Improve PNG support options
  + CVE-2019-2818: Better Poly1305 support
  + CVE-2019-2816: Normalize normalization
  + CVE-2019-2821: Improve TLS negotiation
  + CVE-2019-2602: Better String parsing
  + CVE-2019-2684: More dynamic RMI interactions
  + CVE-2019-2698: Fuzzing TrueType fonts: setCurrGlyphID()

* Thu Dec 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:11.0.9.11-alt2_0.3.eajpp10
- added alternatives for keytool, policytool, etc

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0:11.0.9.11-alt1_0.3.eajpp10
- new version

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 0:11.0.9.7-alt1_0.0.eajpp11
- new version

* Wed Jul 10 2019 Igor Vlasenko <viy@altlinux.ru> 0:11.0.3.7-alt1_5jpp8
- new version

