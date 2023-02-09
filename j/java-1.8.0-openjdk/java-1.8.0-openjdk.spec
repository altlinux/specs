# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
BuildRequires: ca-certificates-java
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
%define name java-1.8.0-openjdk
%define version 1.8.0.362.b09
%define release 0
# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release, fastdebug *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-1.8.0-openjdk.spec
#
# Produce only release builds (no debug builds) on x86_64:
# $ rpmbuild -ba java-1.8.0-openjdk.spec --without slowdebug --without fastdebug
#
# Only produce a release build on x86_64:
# $ rhpkg mockbuild --without slowdebug --without fastdebug
#
# Enable fastdebug builds by default on relevant arches.
%bcond_without fastdebug
# Enable slowdebug builds by default on relevant arches.
%bcond_without slowdebug
# Enable release builds by default on relevant arches.
%bcond_without release

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
%global fastdebug_suffix_unquoted -fastdebug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global fastdebug_suffix "%{fastdebug_suffix_unquoted}"
%global normal_suffix ""

%global debug_warning This package is unoptimised with full debugging. Install only as needed and remove ASAP.
%global debug_on with full debug on
%global fastdebug_warning This package is optimised with full debugging. Install only as needed and remove ASAP.
%global for_fastdebug_on with minimal debug on
%global for_debug for packages with debug on

%if %{with release}
%global include_normal_build 1
%else
%global include_normal_build 0
%endif

%if %{include_normal_build}
%global normal_build %{normal_suffix}
%else
%global normal_build %{nil}
%endif

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global jit_arches      %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64}
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64}
%global jfr_arches      %{jit_arches}
%global fastdebug_arches x86_64 ppc64le aarch64

# By default, we build a debug build during main build on JIT architectures
%if %{with slowdebug}
%ifarch %{jit_arches}
%ifnarch %{arm}
%global include_debug_build 0
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif

# By default, we build a fastdebug build during main build only on fastdebug architectures
%if %{with fastdebug}
%ifarch %{fastdebug_arches}
%global include_fastdebug_build 0
%else
%global include_fastdebug_build 0
%endif
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

# If you disable both builds, then the build fails
# Build and test slowdebug first as it provides the best diagnostics
%global build_loop  %{slowdebug_build} %{fastdebug_build} %{normal_build}

%ifarch %{jit_arches}
%global bootstrap_build 1
%else
%global bootstrap_build 1
%endif

%global bootstrap_targets images
%global release_targets images docs-zip
# No docs nor bootcycle for debug builds
%global debug_targets images

# Disable LTO as this causes build failures at the moment.
%define optflags_lto %nil

# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
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
%global NSS_LIBS %(pkg-config --libs nss)
%global NSS_CFLAGS %(pkg-config --cflags nss)
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332456
%global NSS_BUILDTIME_NUMBER %(pkg-config --modversion nss || : )
# this is workaround for processing of requires during srpm creation
%global NSS_BUILDTIME_VERSION %(if [ "x%{NSS_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSS_BUILDTIME_NUMBER}" ;fi)

# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349.
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1590796
# as to why some libraries *cannot* be excluded. In particular,
# these are:
# libjsig.so, libjava.so, libjawt.so, libjvm.so and libverify.so
#%global _privatelibs libattach[.]so.*|libawt_headless[.]so.*|libawt[.]so.*|libawt_xawt[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libhprof[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas_unix[.]so.*|libjava_crw_demo[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjli[.]so.*|libjsdt[.]so.*|libjsoundalsa[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libnpt[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsplashscreen[.]so.*|libsunec[.]so.*|libunpack[.]so.*|libzip[.]so.*|lib[.]so\\(SUNWprivate_.*

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
%global archinstall i386
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
# Need to support noarch for srpm build
%ifarch noarch
%global archinstall %{nil}
%global stapinstall %{nil}
%endif

%if_enabled systemtap
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

%ifarch %{ix86} x86_64
%global with_openjfx_binding 0
%global openjfx_path %{_jvmdir}/openjfx8
# links src directories
%global jfx_jre_libs_dir %{openjfx_path}/rt/lib
%global jfx_jre_native_dir %{jfx_jre_libs_dir}/%{archinstall}
%global jfx_sdk_libs_dir %{openjfx_path}/lib
%global jfx_sdk_bins_dir %{openjfx_path}/bin
%global jfx_jre_exts_dir %{jfx_sdk_libs_dir}/ext
# links src files
# maybe depend on jfx and generate the lists in build time? Yes, bad idea to inlcude cyclic depndenci, but this list is aweful
%global jfx_jre_libs jfxswt.jar javafx.properties
%global jfx_jre_native libprism_es2.so libprism_common.so libjavafx_font.so libdecora_sse.so libjavafx_font_freetype.so libprism_sw.so libjavafx_font_pango.so ibglass.so libjavafx_iio.so libglassgtk2.so libglassgtk3.so
%global jfx_sdk_libs javafx-mx.jar packager.jar ant-javafx.jar
%global jfx_sdk_bins javafxpackager javapackager
%global jfx_jre_exts jfxrt.jar
%else
%global with_openjfx_binding 0
%endif

# New Version-String scheme-style defines
%global majorver 8

# Standard JPackage naming and versioning defines.
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{origin}

# Define vendor information used by OpenJDK
%global oj_vendor Red Hat, Inc.
%global oj_vendor_url "https://www.redhat.com/"
# Define what url should JVM offer in case of a crash report
# order may be important, epel may have rhel declared
%if 0%{?epel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{name}&version=epel%{epel}
%else
%if 0%{?fedora}
# Does not work for rawhide, keeps the version field empty
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{name}&version=%{fedora}
%else
%if 0%{?rhel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%20%{rhel}&component=%{name}
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif

# note, following three variables are sedded from update_sources if used correctly. Hardcode them rather there.
%global shenandoah_project openjdk
%global shenandoah_repo shenandoah-jdk8u
%global shenandoah_revision shenandoah-jdk8u362-b09
# Define old aarch64/jdk8u tree variables for compatibility
%global project         %{shenandoah_project}
%global repo            %{shenandoah_repo}
%global revision        %{shenandoah_revision}
# Define IcedTea version used for SystemTap tapsets and desktop files
%global icedteaver      3.15.0

# e.g. aarch64-shenandoah-jdk8u212-b04-shenandoah-merge-2019-04-30 -> aarch64-shenandoah-jdk8u212-b04
%global version_tag     %(VERSION=%{revision}; echo ${VERSION%%-shenandoah-merge*})
# eg # jdk8u60-b27 -> jdk8u60 or # aarch64-jdk8u60-b27 -> aarch64-jdk8u60  (dont forget spec escape % by %%)
%global whole_update    %(VERSION=%{version_tag}; echo ${VERSION%%-*})
# eg  jdk8u60 -> 60 or aarch64-jdk8u60 -> 60
%global updatever       %(VERSION=%{whole_update}; echo ${VERSION##*u})
# eg jdk8u60-b27 -> b27
%global buildver        %(VERSION=%{version_tag}; echo ${VERSION##*-})
%global rpmrelease      1
%global dist            jpp8
# Define milestone (EA for pre-releases, GA ("fcs") for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga           1
%if %{is_ga}
%global milestone          fcs
%global milestone_version  %{nil}
%global extraver %{nil}
%global eaprefix %{nil}
%else
%global milestone          ea
%global milestone_version  "-ea"
%global extraver .%{milestone}
%global eaprefix 0.
%endif
# priority must be 7 digits in total. The expression is workarounding tip
%global priority        %(TIP=1800%{updatever};  echo ${TIP/tip/999})

%global javaver         1.%{majorver}.0

# parametrized macros are order-sensitive
%global compatiblename  %{name}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images stub
%global jdkimage       j2sdk-image
# output dir stub
%define buildoutputdir build/jdk8.build
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir %{fullversion}
# main id and dir of this jdk
%define uniquesuffix %{fullversion}.%{_arch}

%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix}}
# Standard JPackage directories and symbolic links.
%define sdkdir %{uniquesuffix}
%define jrelnk jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}

%define jredir %{sdkdir}/jre
%define sdkbindir %{_jvmdir}/%{sdkdir}/bin
%define jrebindir %{_jvmdir}/%{jredir}/bin
%global alt_java_name     alt-java

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

%if_enabled systemtap
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

# not-duplicated scriptlets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{updatever}.%{buildver}
Release: alt0_%{?eaprefix}%{rpmrelease}%{?extraver}%{?dist}
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
Group:   Development/Other

# HotSpot code is licensed under GPLv2
# JDK library code is licensed under GPLv2 with the Classpath exception
# The Apache license is used in code taken from Apache projects (primarily JAXP & JAXWS)
# DOM levels 2 & 3 and the XML digital signature schemas are licensed under the W3C Software License
# The JSR166 concurrency code is in the public domain
# The BSD and MIT licenses are used for a number of third-party libraries (see THIRD_PARTY_README)
# The OpenJDK source tree includes the JPEG library (IJG), zlib & libpng (zlib), giflib and LCMS (MIT)
# The test code includes copies of NSS under the Mozilla Public License v2.0
# The PCSClite headers are under a BSD with advertising license
# The elliptic curve cryptography (ECC) source code is licensed under the LGPLv2.1 or any later version
License:  ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib
URL:      http://openjdk.java.net/

# Shenandoah HotSpot
# aarch64-port/jdk8u-shenandoah contains an integration forest of
# OpenJDK 8u, the aarch64 port and Shenandoah
# To regenerate, use:
# VERSION=%%{shenandoah_revision}
# FILE_NAME_ROOT=%%{shenandoah_project}-%%{shenandoah_repo}-${VERSION}
# REPO_ROOT=<path to checked-out repository> generate_source_tarball.sh
# where the source is obtained from http://hg.openjdk.java.net/%%{project}/%%{repo}
Source0: %{shenandoah_project}-%{shenandoah_repo}-%{shenandoah_revision}-4curve.tar.xz

# Custom README for -src subpackage
Source2: README.md

# Release notes
Source7: NEWS

# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (3.x).
# Systemtap tapsets. Zipped up to keep it small.
Source8: tapsets-icedtea-%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in
Source10: policytool.desktop.in

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: %{name}-remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

Source20: repackReproduciblePolycies.sh

# New versions of config files with aarch64 support. This is not upstream yet.
Source100: config.guess
Source101: config.sub


############################################
#
# RPM/distribution specific patches
#
# This section includes patches specific to
# Fedora/RHEL which can not be upstreamed
# either in their current form or at all.
############################################

# Accessibility patches
# Turn on AssumeMP by default on RHEL systems
Patch534: rh1648246-always_instruct_vm_to_assume_multiple_processors_are_available.patch
# RH1655466: Support RHEL FIPS mode using SunPKCS11 provider

#############################################
#
# Upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed to the current development
# tree of OpenJDK.
#############################################
# PR2737: Allow multiple initialization of PKCS11 libraries
Patch5: pr2737-allow_multiple_pkcs11_library_initialisation_to_be_a_non_critical_error.patch
# Turn off strict overflow on IndicRearrangementProcessor{,2}.cpp following 8140543: Arrange font actions
Patch512: rh1649664-awt2dlibraries_compiled_with_no_strict_overflow.patch
# RH1337583, PR2974: PKCS#10 certificate requests now use CRLF line endings rather than system line endings
Patch523: pr2974-rh1337583-add_systemlineendings_option_to_keytool_and_use_line_separator_instead_of_crlf_in_pkcs10.patch
# PR3083, RH1346460: Regression in SSL debug output without an ECC provider
Patch528: pr3083-rh1346460-for_ssl_debug_return_null_instead_of_exception_when_theres_no_ecc_provider.patch
# PR2888: OpenJDK should check for system cacerts database (e.g. /etc/pki/java/cacerts)
# PR3575, RH1567204: System cacerts database handling should not affect jssecacerts
Patch539: pr2888-openjdk_should_check_for_system_cacerts_database_eg_etc_pki_java_cacerts.patch
# PR3183, RH1340845: Support Fedora/RHEL8 system crypto policy
Patch400: pr3183-rh1340845-support_fedora_rhel_system_crypto_policy.patch
# PR3655: Allow use of system crypto policy to be disabled by the user
Patch401: pr3655-toggle_system_crypto_policy.patch
# enable build of speculative store bypass hardened alt-java
Patch600: rh1750419-redhat_alt_java.patch
# JDK-8218811: replace open by os::open in hotspot coding
# This fixes a GCC 10 build issue
Patch111: jdk8218811-perfMemory_linux.patch
# Similar for GCC 11
Patch112: %name-gcc11.patch

#############################################
#
# Arch-specific upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed upstream and are specific
# to certain architectures. This usually means the
# current OpenJDK development branch, but may also
# include other trees e.g. for the AArch64 port for
# OpenJDK 8u.
#############################################
# s390: PR3593: Use "%z" for size_t on s390 as size_t != intptr_t
Patch103: pr3593-s390_use_z_format_specifier_for_size_t_arguments_as_size_t_not_equals_to_int.patch
# x86: S8199936, PR3533: HotSpot generates code with unaligned stack, crashes on SSE operations (-mstackrealign workaround)
Patch105: jdk8199936-pr3533-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x.patch
# S390 ambiguous log2_intptr calls
Patch107: s390-8214206_fix.patch

#############################################
#
# Patches which need backporting to 8u
#
# This section includes patches which have
# been pushed upstream to the latest OpenJDK
# development tree, but need to be backported
# to OpenJDK 8u.
#############################################
# S8074839, PR2462: Resolve disabled warnings for libunpack and the unpack200 binary
# This fixes printf warnings that lead to build failure with -Werror=format-security from optflags
Patch502: pr2462-resolve_disabled_warnings_for_libunpack_and_the_unpack200_binary.patch
# PR3591: Fix for bug 3533 doesn't add -mstackrealign to JDK code
Patch571: jdk8199936-pr3591-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x_jdk.patch
# 8143245, PR3548: Zero build requires disabled warnings
Patch574: jdk8143245-pr3548-zero_build_requires_disabled_warnings.patch
# s390: JDK-8203030, Type fixing for s390
Patch102: jdk8203030-zero_s390_31_bit_size_t_type_conflicts_in_shared_code.patch
# 8035341: Allow using a system installed libpng
Patch202: jdk8035341-allow_using_system_installed_libpng.patch
# 8042159: Allow using a system-installed lcms2
Patch203: jdk8042159-allow_using_system_installed_lcms2-root.patch
Patch204: jdk8042159-allow_using_system_installed_lcms2-jdk.patch
Patch205: jdk8281098-pr3836-pass_compiler_flags_to_adlc.patch
Patch206: jdk8282231-x86_32-missing_call_effects.patch
Patch207: rh1582504-rsa_default_for_keytool.patch
Patch208: rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch

#############################################
#
# Patches ineligible for 8u
#
# This section includes patches which are present
# upstream, but ineligible for upstream 8u backport.
#############################################
# 8043805: Allow using a system-installed libjpeg
Patch201: jdk8043805-allow_using_system_installed_libjpeg.patch

#############################################
#
# Shenandoah fixes
#
# This section includes patches which are
# specific to the Shenandoah garbage collector
# and should be upstreamed to the appropriate
# trees.
#############################################

#############################################
#
# Non-OpenJDK fixes
#
# This section includes patches to code other
# that from OpenJDK.
#############################################

#############################################
#
# Dependencies
#
#############################################
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
BuildRequires: liblcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxslt xsltproc
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirements for setting up the nss.cfg
BuildRequires: libnss-devel
BuildRequires: libX11-devel libXvMC-devel xorg-proto-devel
BuildRequires: zip
BuildRequires: unzip
# Use OpenJDK 7 where available (on RHEL) to avoid
# having to use the rhel-7.x-java-unsafe-candidate hack
%if ! 0%{?fedora} && 0%{?rhel} <= 7
# Require a boot JDK which doesn't fail due to RH1482244
BuildRequires: java-1.7.0-openjdk-devel >= 1.7.0.151
%else
BuildRequires: java-1.8.0-openjdk-devel
%endif
# Zero-assembler build requirement
%ifnarch %{jit_arches}
BuildRequires: libffi-devel
%endif
# 2021a required as of JDK-8260356 in April CPU
Requires: tzdata-java >= 2021a
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3

%if_enabled systemtap
BuildRequires: systemtap-sdt-devel
%endif

# this is always built, also during debug-only build
# when it is built in debug-only this package is just placeholder
Requires: fontconfig
Requires: fonts-type1-xorg
# Require libXcomposite explicitly since it's only dynamically loaded
# at runtime. Fixes screenshot issues. See JDK-8150954.
Requires: libXcomposite
# Requires rest of java
Requires: %{name}-headless = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# for java-X-openjdk package's desktop binding
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: libgail libgtk+2
%endif

Provides: java-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}

# Standard JPackage base provides
Provides: jre = %{javaver}
Provides: jre-%{origin} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver} = %{epoch}:%{version}-%{release}
Provides: java-%{origin} = %{epoch}:%{version}-%{release}
Provides: java = %{epoch}:%{javaver}
Source44: import.info

%define altname %name
%define label -%{name}
%define javaws_ver      %{javaver}

%if "%{_lib}" == "lib64"
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()(64bit)
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so()(64bit)
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)(64bit)
%else
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so()
Provides: /usr/lib/jvm/java/jre/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so()
Provides: %{_jvmdir}/%{jredir}/lib/%archinstall/server/libjvm.so(SUNWprivate_1.1)
%endif
Patch33: java-1.8.0-openjdk-alt-no-Werror.patch
Patch34: java-1.8.0-openjdk-alt-link.patch
Patch35: java-1.8.0-openjdk-alt-libjawt-link.patch

# Fix upgrade path after removal of accessibility subpackage
# on commit 0c79c1451ef42c540682fb75329a92bb110609e7
# As main accessibility was requiring main package, main package now have to
# obsolete java-1.8.0-openjdk-accessibility-{release, slowdebug, fastdebug} < 1:1.8.0.292.b06
# otherwise update fails
Obsoletes: java-1.8.0-openjdk-accessibility < 1:1.8.0.292.b06
Obsoletes: java-1.8.0-openjdk-accessibility-slowdebug < 1:1.8.0.292.b06
Obsoletes: java-1.8.0-openjdk-accessibility-fastdebug < 1:1.8.0.292.b06

%description
The %{origin_nice} runtime environment %{majorver}.

%if %{include_debug_build}
%package slowdebug
Summary: %{origin_nice} Runtime Environment %{majorver} %{debug_on}
Group:   Development/Other

%description slowdebug
The %{origin_nice} runtime environment %{majorver}.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package fastdebug
Summary: %{origin_nice} Runtime Environment %{majorver} %{fastdebug_on}
Group:   Development/Other

%description fastdebug
The %{origin_nice} runtime environment.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: %{origin_nice} Headless Runtime Environment %{majorver}
Group:   Development/Other

# Require /etc/pki/java/cacerts
Requires: ca-trust-java
# Require javapackages-filesystem for ownership of /usr/lib/jvm/
Requires: javapackages-filesystem
# Require zoneinfo data provided by tzdata-java subpackage.
# 2021a required as of JDK-8260356 in April CPU
Requires: tzdata-java >= 2021a
# libsctp.so.1 is being `dlopen`ed on demand
Requires: liblksctp lksctp-tools
# for printing support
Requires: libcups
# Post requires alternatives to install tool alternatives
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives
# in version 1.7 and higher for --family switch
# for optional support of kernel stream control, card reader and printing bindings
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: liblksctp lksctp-tools libpcsclite
%endif

# Standard JPackage base provides
Provides: jre-headless = %{epoch}:%{javaver}
Provides: jre-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-headless = %{epoch}:%{version}-%{release}
Provides: java-headless = %{epoch}:%{javaver}
Requires: java-common
Requires: /proc
Requires(post): /proc

%description headless
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%endif

%if %{include_debug_build}
%package headless-slowdebug
Summary: %{origin_nice} Runtime Environment %{majorver} %{debug_on}
Group:   Development/Other

%description headless-slowdebug
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package headless-fastdebug
Summary: %{origin_nice} Runtime Environment %{fastdebug_on}
Group:   Development/Other

%description headless-fastdebug
The %{origin_nice} runtime environment %{majorver} without audio and video support.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} Development Environment %{majorver}
Group:   Development/Java

# Requires base package
Requires:         %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall tool alternatives
# in version 1.7 and higher for --family switch

# Standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin} = %{epoch}:%{version}
Provides: java-sdk-%{javaver} = %{epoch}:%{version}
Provides: java-sdk-%{origin} = %{epoch}:%{version}
Provides: java-sdk = %{epoch}:%{javaver}
Provides: java-%{javaver}-devel = %{epoch}:%{version}
Provides: java-%{javaver}-%{origin}-devel = %{epoch}:%{version}
Provides: java-devel-%{origin} = %{epoch}:%{version}
Provides: java-devel = %{epoch}:%{javaver}

%description devel
The %{origin_nice} development tools %{majorver}.
%endif

%if %{include_debug_build}
%package devel-slowdebug
Summary: %{origin_nice} Development Environment %{majorver} %{debug_on}
Group:   Development/Java

%description devel-slowdebug
The %{origin_nice} development tools %{majorver}.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package devel-fastdebug
Summary: %{origin_nice} Development Environment %{majorver} %{fastdebug_on}
Group:   Development/Java

%description devel-fastdebug
The %{origin_nice} development tools %{majorver}.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package demo
Summary: %{origin_nice} Demos %{majorver}
Group:   Development/Other

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}

Provides: java-demo = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-demo = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-demo = %{epoch}:%{version}-%{release}

%description demo
The %{origin_nice} demos %{majorver}.
%endif

%if %{include_debug_build}
%package demo-slowdebug
Summary: %{origin_nice} Demos %{majorver} %{debug_on}
Group:   Development/Other

%description demo-slowdebug
The %{origin_nice} demos %{majorver}.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package demo-fastdebug
Summary: %{origin_nice} Demos %{majorver} %{fastdebug_on}
Group:   Development/Other

%description demo-fastdebug
The %{origin_nice} demos %{majorver}.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: %{origin_nice} Source Bundle %{majorver}
Group:   Development/Other

Requires: %{name}-headless = %{epoch}:%{version}-%{release}

# Standard JPackage sources provides
Provides: java-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-src = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src = %{epoch}:%{version}-%{release}

%description src
The java-%{origin}-src sub-package contains the complete %{origin_nice} %{majorver}
class library source code for use by IDE indexers and debuggers.
%endif

%if %{include_debug_build}
%package src-slowdebug
Summary: %{origin_nice} Source Bundle %{majorver} %{for_debug}
Group:   Development/Other

%description src-slowdebug
The java-%{origin}-src-slowdebug sub-package contains the complete %{origin_nice} %{majorver}
 class library source code for use by IDE indexers and debuggers. Debugging %{for_debug}.
%endif

%if %{include_fastdebug_build}
%package src-fastdebug
Summary: %{origin_nice} Source Bundle %{majorver} %{for_fastdebug}
Group:   Development/Other

%description src-fastdebug
The java-%{origin}-src-fastdebug sub-package contains the complete %{origin_nice} %{majorver}
 class library source code for use by IDE indexers and debuggers. Debugging %{for_fastdebug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: %{origin_nice} %{majorver} API documentation
Group:   Development/Java
Requires: javapackages-filesystem
Obsoletes: javadoc-debug
BuildArch: noarch

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}
# hack till java 9+ will come
Provides: java-javadoc = 1:1.9.0

%description javadoc
The %{origin_nice} %{majorver} API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Summary: %{origin_nice} %{majorver} API documentation compressed in single archive
Group:   Development/Java
Requires: javapackages-filesystem
Obsoletes: javadoc-zip-debug
BuildArch: noarch

Requires: %{name}-headless%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
# in version 1.7 and higher for --family switch
# Postun requires alternatives to uninstall javadoc alternative
# in version 1.7 and higher for --family switch

# Standard JPackage javadoc provides
Provides: java-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc = %{epoch}:%{version}-%{release}

%description javadoc-zip
The %{origin_nice} %{majorver} API documentation compressed in a single archive.
%endif

%if %{with_openjfx_binding}
%package openjfx
Summary: OpenJDK x OpenJFX connector. This package adds symliks finishing Java FX integration to %{name}
Group: Development/Other
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx%{?_isa}
%description openjfx
Set of links from OpenJDK (jre) to OpenJFX

%package openjfx-devel
Summary: OpenJDK x OpenJFX connector for FX developers. This package adds symliks finishing Java FX integration to %{name}-devel
Group: Development/Other
Requires: %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx-devel
%description openjfx-devel
Set of links from OpenJDK (sdk) to OpenJFX

%if %{include_debug_build}
%package openjfx-debug
Summary: OpenJDK x OpenJFX connector %{for_debug}. his package adds symliks finishing Java FX integration to %{name}-debug
Group: Development/Other
Requires: %{name}-debug%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx%{?_isa}
%description openjfx-debug
Set of links from OpenJDK-debug (jre) to normal OpenJFX. OpenJFX do not support
debug builds of itself

%package openjfx-devel-debug
Summary: OpenJDK x OpenJFX connector for FX developers %{for_debug}. This package adds symliks finishing Java FX integration to %{name}-devel-debug
Group: Development/Other
Requires: %{name}-devel-debug%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx-devel
%description openjfx-devel-debug
Set of links from OpenJDK-debug (sdk) to normal OpenJFX. OpenJFX do not support
debug builds of itself
%endif

%if %{include_fastdebug_build}
%package openjfx-fastdebug
Summary: OpenJDK x OpenJFX connector %{for_fastdebug}. his package adds symliks finishing Java FX integration to %{name}-fastdebug
Group: Development/Other
Requires: %{name}-fastdebug%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx8%{?_isa}
Provides: javafx-fastdebug = %{epoch}:%{version}-%{release}
%description openjfx-fastdebug
Set of links from OpenJDK-fastdebug (jre) to normal OpenJFX. OpenJFX do not
support debug builds of itself

%package openjfx-devel-fastdebug
Summary: OpenJDK x OpenJFX connector for FX developers %{for_fastdebug}. This package adds symliks finishing Java FX integration to %{name}-devel-slowdebug
Group: Development/Other
Requires: %{name}-devel-fastdebug%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openjfx8-devel%{?_isa}
Provides: javafx-devel-fastdebug = %{epoch}:%{version}-%{release}
%description openjfx-devel-fastdebug
Set of links from OpenJDK-fastdebug (sdk) to normal OpenJFX. OpenJFX do not
support debug builds of itself
%endif
%endif

%prep

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
  echo "You have disabled all builds (normal,fastdebug,debug). That is a no go."
  exit 14
fi
if [ %{include_normal_build} -eq 0 ] ; then
  echo "You have disabled the normal build, but this is required to provide docs for the debug build."
  exit 15
fi

echo "Update version: %{updatever}"
echo "Build number: %{buildver}"
echo "Milestone: %{milestone}"
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
# For old patches
ln -s %{top_level_dir_name} jdk8

cp %{SOURCE2} .

# replace outdated configure guess script
#
# the configure macro will do this too, but it also passes a few flags not
# supported by openjdk configure script
cp %{SOURCE100} %{top_level_dir_name}/common/autoconf/build-aux/
cp %{SOURCE101} %{top_level_dir_name}/common/autoconf/build-aux/

# OpenJDK patches

# Remove libraries that are linked
sh %{SOURCE12}

# System library fixes
%patch201
%patch202
%patch203
%patch204
%patch205
%patch206
%patch207
%patch208

# System security policy fixes
%patch400
%patch401

%patch5

# s390 build fixes
%patch102
%patch103
%patch107

# x86 fixes
%patch105

# Upstreamable fixes
%patch502
%patch512
%patch523
%patch528
%patch571
%patch574
%patch111
%patch112
%patch539
%patch600

# RHEL-only patches
%if ! 0%{?fedora} && 0%{?rhel} <= 7
%patch534
%endif

# Shenandoah patches

# Extract systemtap tapsets
%if_enabled systemtap
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
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/server/libjvm.so:g" $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/client/libjvm.so:g" $file.1 > $OUTPUT_FILE
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
for file in %{SOURCE9} %{SOURCE10} ; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:_SDKBINDIR_:%{sdkbindir}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:_JREBINDIR_:%{jrebindir}:g" $OUTPUT_FILE
    sed -i -e  "s:@target_cpu@:%{_arch}:g" $OUTPUT_FILE
    sed -i -e  "s:@OPENJDK_VER@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VER@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg

sed -i -e 's, -m32, -m32 %optflags_shared -fpic -D_BLA_BLA_BLA1,' openjdk/hotspot/make/linux/makefiles/gcc.make
sed -i -e 's,DEF_OBJCOPY=/usr/bin/objcopy,DEF_OBJCOPY=/usr/bin/NO-objcopy,' openjdk/hotspot/make/linux/makefiles/defs.make
%patch33 -p1
%patch34 -p0
%patch35 -p1 -d openjdk

%build
# zerg's girar armh hack:
(while true; do date; sleep 7m; done) &
# end armh hack, kill it when girar will be fixed
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
# Explicitly set the C++ standard as the default has changed on GCC >= 6
EXTRA_CFLAGS="%ourcppflags -Wno-error"
EXTRA_CPP_FLAGS="%ourcppflags"

%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
EXTRA_ASFLAGS="${EXTRA_CFLAGS} -Wa,--generate-missing-build-notes=yes"
export EXTRA_CFLAGS EXTRA_ASFLAGS

(cd %{top_level_dir_name}/common/autoconf
 bash ./autogen.sh
)

function buildjdk() {
    local outputdir=${1}
    local buildjdk=${2}
    local maketargets=${3}
    local debuglevel=${4}

    local top_srcdir_abs_path=$(pwd)/%{top_level_dir_name}
    # Variable used in hs_err hook on build failures
    local top_builddir_abs_path=$(pwd)/${outputdir}

    echo "Using output directory: ${outputdir}";
    echo "Checking build JDK ${buildjdk} is operational..."
    ${buildjdk}/bin/java -version
    echo "Using make targets: ${maketargets}"
    echo "Using debuglevel: ${debuglevel}"
    echo "Building 8u%{updatever}-%{buildver}, milestone %{milestone}"

    mkdir -p ${outputdir}
    pushd ${outputdir}

    bash ${top_srcdir_abs_path}/configure \
%ifarch %{jfr_arches}
    --enable-jfr \
%else
    --disable-jfr \
%endif
%ifnarch %{jit_arches}
    --with-jvm-variants=zero \
%endif
    --with-native-debug-symbols=internal \
    --with-milestone=%{milestone} \
    --with-update-version=%{updatever} \
    --with-build-number=%{buildver} \
    --with-vendor-name="%{oj_vendor}" \
    --with-vendor-url="%{oj_vendor_url}" \
    --with-vendor-bug-url="%{oj_vendor_bug_url}" \
    --with-vendor-vm-bug-url="%{oj_vendor_bug_url}" \
    --with-boot-jdk=${buildjdk} \
    --with-debug-level=${debuglevel} \
    --enable-unlimited-crypto \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-asflags="$EXTRA_ASFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC"

    cat spec.gmk
    cat hotspot-spec.gmk

    make \
	JAVAC_FLAGS=-g \
	LOG=trace \
	SCTP_WERROR= \
	${maketargets} || ( pwd; find ${top_srcdir_abs_path} ${top_builddir_abs_path} -name "hs_err_pid*.log" | xargs cat && false )

    # the build (erroneously) removes read permissions from some jars
    # this is a regression in OpenJDK 7 (our compiler):
    # http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
    find images/%{jdkimage} -iname '*.jar' -exec chmod ugo+r {} \;
    chmod ugo+r images/%{jdkimage}/lib/ct.sym

    # remove redundant *diz and *debuginfo files
    find images/%{jdkimage} -iname '*.diz' -exec rm -v {} \;
    find images/%{jdkimage} -iname '*.debuginfo' -exec rm -v {} \;

    # Build screws up permissions on binaries
    # https://bugs.openjdk.java.net/browse/JDK-8173610
    find images/%{jdkimage} -iname '*.so' -exec chmod +x {} \;
    find images/%{jdkimage}/bin/ -exec chmod +x {} \;

    popd >& /dev/null
}

for suffix in %{build_loop} ; do
if [ "x$suffix" = "x" ] ; then
  debugbuild=release
else
  # change --something to something
  debugbuild=`echo $suffix  | sed "s/-//g"`
fi

systemjdk=/usr/lib/jvm/java-openjdk
builddir=%{buildoutputdir}
bootbuilddir=boot${builddir}

# Debug builds don't need same targets as release for
# build speed-up
maketargets="%{release_targets}"
if echo $debugbuild | grep -q "debug" ; then
  maketargets="%{debug_targets}"
fi

%if %{bootstrap_build}
buildjdk ${bootbuilddir} ${systemjdk} "%{bootstrap_targets}" ${debugbuild}
buildjdk ${builddir} $(pwd)/${bootbuilddir}/images/%{jdkimage} "${maketargets}" ${debugbuild}
rm -rf ${bootbuilddir}
%else
buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild}
%endif

# Install nss.cfg right away as we will be using the JRE above
export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Install nss.cfg right away as we will be using the JRE above
install -m 644 nss.cfg $JAVA_HOME/jre/lib/security/

# Use system-wide tzdata
rm $JAVA_HOME/jre/lib/tzdb.dat
ln -s %{_datadir}/javazi-1.8/tzdb.dat $JAVA_HOME/jre/lib/tzdb.dat

# Create fake alt-java as a placeholder for future alt-java
pushd ${JAVA_HOME}
cp -a jre/bin/java jre/bin/%{alt_java_name}
cp -a bin/java bin/%{alt_java_name}
# add alt-java man page
echo "Hardened java binary recommended for launching untrusted code from the Web e.g. javaws" > man/man1/%{alt_java_name}.1
cat man/man1/java.1 >> man/man1/%{alt_java_name}.1
popd

# build cycles
done

%check
%if_enabled check
# We test debug first as it will give better diagnostics on a crash
for suffix in %{build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir}/images/%{jdkimage}

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java TestCryptoLevel

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
break javaCalls.cpp:58
commands 1
backtrace
quit
end
run -version
EOF
grep 'JavaCallWrapper::JavaCallWrapper' gdb.out

# Check src.zip has all sources. See RHBZ#1130490
jar -tf $JAVA_HOME/src.zip | grep 'sun.misc.Unsafe'

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
pushd %{buildoutputdir}/images/%{jdkimage}

# Install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  cp -a bin include lib src.zip {ASSEMBLY_EXCEPTION,LICENSE,THIRD_PARTY_README} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib jre/{ASSEMBLY_EXCEPTION,LICENSE,THIRD_PARTY_README} $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}

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
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security/cacerts
  # Install cacerts symlink needed by some apps which hardcode the path
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir}/lib/security
      ln -sf /etc/pki/java/cacerts .
  popd

  # Install versioned symlinks
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{jredir} %{jrelnk}
  popd

  # Remove javaws man page
  rm -f man/man1/javaws*

  # Install man pages
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{uniquesuffix}.1
  done

  # Install demos and samples.
  cp -a demo $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}
  mkdir -p sample/rmi
  if [ ! -e sample/rmi/java-rmi.cgi ] ; then 
    # hack to allow --short-circuit on install
    mv bin/java-rmi.cgi sample/rmi
  fi
  cp -a sample $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}

popd

if ! echo $suffix | grep -q "debug" ; then
  # Install Javadoc documentation
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  cp -a %{buildoutputdir}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}
  built_doc_archive=jdk-%{javaver}_%{updatever}%{milestone_version}$suffix-%{buildver}-docs.zip
  cp -a %{buildoutputdir}/bundles/$built_doc_archive  $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir}.zip
fi

# Install release notes
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir}
install -d -m 755 ${commondocdir}
cp -a %{SOURCE7} ${commondocdir}

# Install icons and menu entries
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix policytool$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# FIXME: remove SONAME entries from demo DSOs. See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}-demo.files"$suffix"
# Find documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%%doc |' \
  >> %{name}-demo.files"$suffix"
# Find documentation directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir}/sample \
  -type d | sort \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%%dir |' \
  >> %{name}-demo.files"$suffix"

# intentionally after all else, fx links  with redirections on its own
%if %{with_openjfx_binding}
  FXSDK_FILES=%{name}-openjfx-devel.files"$suffix"
  FXJRE_FILES=%{name}-openjfx.files"$suffix"
  echo -n "" > $FXJRE_FILES
  echo -n "" > $FXSDK_FILES
  for file in  %{jfx_jre_libs} ; do
    srcfile=%{jfx_jre_libs_dir}/$file
    targetfile=%{_jvmdir}/%{jredir $suffix}/lib/$file
    ln -s $srcfile $RPM_BUILD_ROOT/$targetfile
    echo $targetfile >> $FXJRE_FILES
  done
  for file in  %{jfx_jre_native} ; do
    srcfile=%{jfx_jre_native_dir}/$file
    targetfile=%{_jvmdir}/%{jredir $suffix}/lib/%{archinstall}/$file
    ln -s $srcfile $RPM_BUILD_ROOT/$targetfile
    echo $targetfile >> $FXJRE_FILES
  done
  for file in  %{jfx_jre_exts} ; do
    srcfile=%{jfx_jre_exts_dir}/$file
    targetfile=%{_jvmdir}/%{jredir $suffix}/lib/ext/$file
    ln -s $srcfile $RPM_BUILD_ROOT/$targetfile
    echo $targetfile >> $FXJRE_FILES
  done
  for file in  %{jfx_sdk_libs} ; do
    srcfile=%{jfx_sdk_libs_dir}/$file
    targetfile=%{_jvmdir}/%{sdkdir $suffix}/lib/$file
    ln -s $srcfile $RPM_BUILD_ROOT/$targetfile
    echo $targetfile >> $FXSDK_FILES
  done
  for file in  %{jfx_sdk_bins} ; do
    srcfile=%{jfx_sdk_bins_dir}/$file
    targetfile=%{_jvmdir}/%{sdkdir $suffix}/bin/$file
    ln -s $srcfile $RPM_BUILD_ROOT/$targetfile
    echo $targetfile >> $FXSDK_FILES
  done
%endif

bash %{SOURCE20} $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir} %{javaver}
# https://bugzilla.redhat.com/show_bug.cgi?id=1183793
touch -t 201401010000 $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/lib/security/java.security

# moving config files to /etc
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib/security/policy/unlimited/
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib/security/policy/limited/
for file in lib/security/cacerts lib/security/policy/unlimited/US_export_policy.jar lib/security/policy/unlimited/local_policy.jar lib/security/policy/limited/US_export_policy.jar lib/security/policy/limited/local_policy.jar lib/security/java.policy lib/security/java.security lib/security/blacklisted.certs lib/logging.properties lib/calendars.properties ; do
  mv      $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/$file   $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/$file
  ln -sf  %{etcjavadir -- $suffix}/$file                          $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir}/$file
done

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "*.so" -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -type d -exec chmod 755 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "ASSEMBLY_EXCEPTION" -exec chmod 644 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "LICENSE" -exec chmod 644 {} \; ; 
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir}/ -name "THIRD_PARTY_README" -exec chmod 644 {} \; ; 

# end, dual install
done
for rpm404_ghost in %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

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
Exec=%{_jvmdir}/%{jredir}/bin/jcontrol
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
Exec=%{_jvmdir}/%{jredir}/bin/javaws %%u
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
%{_bindir}/java	%{_jvmdir}/%{jredir}/bin/java	%priority
%_man1dir/java.1.gz	%_man1dir/java%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
# binaries and manuals
for i in jjs keytool policytool servertool pack200 unpack200 \
orbd rmid rmiregistry tnameserv
do
  if [ -e %buildroot%{_jvmdir}/%{jredir}/bin/$i ]; then
    cat <<EOF >>%buildroot%_altdir/%name-java-headless
%_bindir/$i	%{_jvmdir}/%{jredir}/bin/$i	%{_jvmdir}/%{jredir}/bin/java
%_man1dir/$i.1.gz	%_man1dir/${i}%{label}.1.gz	%{_jvmdir}/%{jredir}/bin/java
EOF
  fi
done

%if_enabled control_panel
cat <<EOF >>%buildroot%_altdir/%name-java
%{_bindir}/ControlPanel	%{_jvmdir}/%{jredir}/bin/ControlPanel	%{_jvmdir}/%{jredir}/bin/java
%{_bindir}/jcontrol	%{_jvmdir}/%{jredir}/bin/jcontrol	%{_jvmdir}/%{jredir}/bin/java
EOF
%endif
# ----- JPackage compatibility alternatives ------
cat <<EOF >>%buildroot%_altdir/%name-java-headless
%{_jvmdir}/jre	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{origin}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/jre-%{javaver}-%{origin}	%{_jvmdir}/%{jredir}	%{_jvmdir}/%{jredir}/bin/java
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
ln -s server/libjvm.so %buildroot%_jvmdir/%sdkdir/jre/lib/%archinstall/libjvm.so

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
%{_datadir}/applications/*policytool.desktop
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjsoundalsa.so
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libsplashscreen.so
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/jre/lib/%{archinstall}/libjawt.so
%{_jvmdir}/%{sdkdir}/jre/bin/policytool
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
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%{_jvmdir}/%{jredir}/ASSEMBLY_EXCEPTION
%{_jvmdir}/%{jredir}/LICENSE
%{_jvmdir}/%{jredir}/THIRD_PARTY_README
%doc %{_defaultdocdir}/%{uniquejavadocdir}/NEWS
%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%dir %{_jvmdir}/%{jredir}/lib/security
%{_jvmdir}/%{jredir}/lib/security/cacerts
%dir %{_jvmdir}/%{jredir}
%dir %{_jvmdir}/%{jredir}/bin
%dir %{_jvmdir}/%{jredir}/lib
%{_jvmdir}/%{jredir}/bin/java
%{_jvmdir}/%{jredir}/bin/%{alt_java_name}
%{_jvmdir}/%{jredir}/bin/jjs
%{_jvmdir}/%{jredir}/bin/keytool
%{_jvmdir}/%{jredir}/bin/orbd
%{_jvmdir}/%{jredir}/bin/pack200
%{_jvmdir}/%{jredir}/bin/rmid
%{_jvmdir}/%{jredir}/bin/rmiregistry
%{_jvmdir}/%{jredir}/bin/servertool
%{_jvmdir}/%{jredir}/bin/tnameserv
%{_jvmdir}/%{jredir}/bin/unpack200
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited/
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited/
%dir %{_jvmdir}/%{jredir}/lib/security/policy/
%config(noreplace) %{etcjavadir}/lib/security/policy/unlimited/US_export_policy.jar
%config(noreplace) %{etcjavadir}/lib/security/policy/unlimited/local_policy.jar
%config(noreplace) %{etcjavadir}/lib/security/policy/limited/US_export_policy.jar
%config(noreplace) %{etcjavadir}/lib/security/policy/limited/local_policy.jar
%config(noreplace) %{etcjavadir}/lib/security/java.policy
%config(noreplace) %{etcjavadir}/lib/security/java.security
%config(noreplace) %{etcjavadir}/lib/security/blacklisted.certs
%config(noreplace) %{etcjavadir}/lib/logging.properties
%config(noreplace) %{etcjavadir}/lib/calendars.properties
%{_jvmdir}/%{jredir}/lib/security/policy/unlimited/US_export_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/unlimited/local_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/limited/US_export_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/limited/local_policy.jar
%{_jvmdir}/%{jredir}/lib/security/java.policy
%{_jvmdir}/%{jredir}/lib/security/java.security
%{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%{_jvmdir}/%{jredir}/lib/logging.properties
%{_jvmdir}/%{jredir}/lib/calendars.properties
%{_mandir}/man1/java-%{uniquesuffix}.1*
%{_mandir}/man1/%{alt_java_name}-%{uniquesuffix}.1*
%{_mandir}/man1/jjs-%{uniquesuffix}.1*
%{_mandir}/man1/keytool-%{uniquesuffix}.1*
%{_mandir}/man1/orbd-%{uniquesuffix}.1*
%{_mandir}/man1/pack200-%{uniquesuffix}.1*
%{_mandir}/man1/rmid-%{uniquesuffix}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix}.1*
%{_mandir}/man1/servertool-%{uniquesuffix}.1*
%{_mandir}/man1/tnameserv-%{uniquesuffix}.1*
%{_mandir}/man1/unpack200-%{uniquesuffix}.1*
%{_mandir}/man1/policytool-%{uniquesuffix}.1*
%{_jvmdir}/%{jredir}/lib/security/nss.cfg
#%config(noreplace) %{etcjavadir}/lib/security/nss.cfg
%ifarch %{jit_arches}
%ifnarch %{power64}
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/server/classes.jsa
%attr(444, root, root) %ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/client/classes.jsa
%endif
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir}
%dir %{etcjavadir}/lib
%dir %{etcjavadir}/lib/security
%{etcjavadir}/lib/security/cacerts
%dir %{etcjavadir}/lib/security/policy
%dir %{etcjavadir}/lib/security/policy/limited
%dir %{etcjavadir}/lib/security/policy/unlimited
%{_jvmdir}/%{jredir}/lib/%{archinstall}/server/
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjvm.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/client/
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/jli
%{_jvmdir}/%{jredir}/lib/%{archinstall}/jli/libjli.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/jvm.cfg
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libattach.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libawt.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libawt_headless.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libdt_socket.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libfontmanager.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libhprof.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libinstrument.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libj2gss.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libj2pcsc.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libj2pkcs11.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjaas_unix.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjava.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjava_crw_demo.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjavajpeg.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjdwp.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjsdt.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjsig.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjsound.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/liblcms.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libmanagement.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libmlib_image.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libnet.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libnio.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libnpt.so
%ifarch %{sa_arches}
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libsaproc.so
%endif
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libsctp.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libsunec.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libunpack.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libverify.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libzip.so
%{_jvmdir}/%{jredir}/lib/charsets.jar
%{_jvmdir}/%{jredir}/lib/classlist
%{_jvmdir}/%{jredir}/lib/content-types.properties
%{_jvmdir}/%{jredir}/lib/currency.data
%{_jvmdir}/%{jredir}/lib/flavormap.properties
%{_jvmdir}/%{jredir}/lib/hijrah-config-umalqura.properties
%{_jvmdir}/%{jredir}/lib/images/cursors/*
%{_jvmdir}/%{jredir}/lib/jce.jar
%{_jvmdir}/%{jredir}/lib/jexec
%{_jvmdir}/%{jredir}/lib/jsse.jar
%{_jvmdir}/%{jredir}/lib/jvm.hprof.txt
%{_jvmdir}/%{jredir}/lib/meta-index
%{_jvmdir}/%{jredir}/lib/net.properties
%{_jvmdir}/%{jredir}/lib/psfont.properties.ja
%{_jvmdir}/%{jredir}/lib/psfontj2d.properties
%{_jvmdir}/%{jredir}/lib/resources.jar
%{_jvmdir}/%{jredir}/lib/rt.jar
%{_jvmdir}/%{jredir}/lib/sound.properties
%{_jvmdir}/%{jredir}/lib/tzdb.dat
%{_jvmdir}/%{jredir}/lib/management-agent.jar
%{_jvmdir}/%{jredir}/lib/management/*
%{_jvmdir}/%{jredir}/lib/cmm/*
%{_jvmdir}/%{jredir}/lib/ext/cldrdata.jar
%{_jvmdir}/%{jredir}/lib/ext/dnsns.jar
%{_jvmdir}/%{jredir}/lib/ext/jaccess.jar
%{_jvmdir}/%{jredir}/lib/ext/localedata.jar
%{_jvmdir}/%{jredir}/lib/ext/meta-index
%{_jvmdir}/%{jredir}/lib/ext/nashorn.jar
%{_jvmdir}/%{jredir}/lib/ext/sunec.jar
%{_jvmdir}/%{jredir}/lib/ext/sunjce_provider.jar
%{_jvmdir}/%{jredir}/lib/ext/sunpkcs11.jar
%{_jvmdir}/%{jredir}/lib/ext/zipfs.jar
%ifarch %{jfr_arches}
%{_jvmdir}/%{jredir}/lib/jfr.jar
%{_jvmdir}/%{jredir}/lib/jfr/default.jfc
%{_jvmdir}/%{jredir}/lib/jfr/profile.jfc
%endif

%dir %{_jvmdir}/%{jredir}/lib/images
%dir %{_jvmdir}/%{jredir}/lib/images/cursors
%dir %{_jvmdir}/%{jredir}/lib/management
%dir %{_jvmdir}/%{jredir}/lib/cmm
%dir %{_jvmdir}/%{jredir}/lib/ext
%ifarch %{jfr_arches}
%dir %{_jvmdir}/%{jredir}/lib/jfr
%endif
# sisyphus_check
%dir %{_jvmdir}/%{jredir}/lib/security/policy
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited

%files devel
%_altdir/%altname-javac
%_altdir/%altname-javac-versioned
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%{_jvmdir}/%{sdkdir}/ASSEMBLY_EXCEPTION
%{_jvmdir}/%{sdkdir}/LICENSE
%{_jvmdir}/%{sdkdir}/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/bin/appletviewer
%{_jvmdir}/%{sdkdir}/bin/clhsdb
%{_jvmdir}/%{sdkdir}/bin/extcheck
%{_jvmdir}/%{sdkdir}/bin/hsdb
%{_jvmdir}/%{sdkdir}/bin/idlj
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/%{alt_java_name}
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javah
%{_jvmdir}/%{sdkdir}/bin/javap
%{_jvmdir}/%{sdkdir}/bin/java-rmi.cgi
%{_jvmdir}/%{sdkdir}/bin/jcmd
%{_jvmdir}/%{sdkdir}/bin/jconsole
%{_jvmdir}/%{sdkdir}/bin/jdb
%{_jvmdir}/%{sdkdir}/bin/jdeps
%ifarch %{jfr_arches}
%{_jvmdir}/%{sdkdir}/bin/jfr
%endif
%{_jvmdir}/%{sdkdir}/bin/jhat
%{_jvmdir}/%{sdkdir}/bin/jinfo
%{_jvmdir}/%{sdkdir}/bin/jjs
%{_jvmdir}/%{sdkdir}/bin/jmap
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jsadebugd
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/native2ascii
%{_jvmdir}/%{sdkdir}/bin/orbd
%{_jvmdir}/%{sdkdir}/bin/pack200
%{_jvmdir}/%{sdkdir}/bin/policytool
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/rmid
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/bin/schemagen
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/bin/servertool
%{_jvmdir}/%{sdkdir}/bin/tnameserv
%{_jvmdir}/%{sdkdir}/bin/unpack200
%{_jvmdir}/%{sdkdir}/bin/wsgen
%{_jvmdir}/%{sdkdir}/bin/wsimport
%{_jvmdir}/%{sdkdir}/bin/xjc
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/%{archinstall}
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%if_enabled systemtap
%{_jvmdir}/%{sdkdir}/tapset
%endif
%{_jvmdir}/%{sdkdir}/lib/ir.idl
%{_jvmdir}/%{sdkdir}/lib/jconsole.jar
%{_jvmdir}/%{sdkdir}/lib/orb.idl
%ifarch %{sa_arches}
%{_jvmdir}/%{sdkdir}/lib/sa-jdi.jar
%endif
%{_jvmdir}/%{sdkdir}/lib/dt.jar
%{_jvmdir}/%{sdkdir}/lib/jexec
%{_jvmdir}/%{sdkdir}/lib/tools.jar
%{_datadir}/applications/*jconsole.desktop
%{_mandir}/man1/appletviewer-%{uniquesuffix}.1*
%{_mandir}/man1/extcheck-%{uniquesuffix}.1*
%{_mandir}/man1/idlj-%{uniquesuffix}.1*
%{_mandir}/man1/jar-%{uniquesuffix}.1*
%{_mandir}/man1/jarsigner-%{uniquesuffix}.1*
%{_mandir}/man1/javac-%{uniquesuffix}.1*
%{_mandir}/man1/javadoc-%{uniquesuffix}.1*
%{_mandir}/man1/javah-%{uniquesuffix}.1*
%{_mandir}/man1/javap-%{uniquesuffix}.1*
%{_mandir}/man1/jconsole-%{uniquesuffix}.1*
%{_mandir}/man1/jcmd-%{uniquesuffix}.1*
%{_mandir}/man1/jdb-%{uniquesuffix}.1*
%{_mandir}/man1/jdeps-%{uniquesuffix}.1*
%{_mandir}/man1/jhat-%{uniquesuffix}.1*
%{_mandir}/man1/jinfo-%{uniquesuffix}.1*
%{_mandir}/man1/jmap-%{uniquesuffix}.1*
%{_mandir}/man1/jps-%{uniquesuffix}.1*
%{_mandir}/man1/jrunscript-%{uniquesuffix}.1*
%{_mandir}/man1/jsadebugd-%{uniquesuffix}.1*
%{_mandir}/man1/jstack-%{uniquesuffix}.1*
%{_mandir}/man1/jstat-%{uniquesuffix}.1*
%{_mandir}/man1/jstatd-%{uniquesuffix}.1*
%{_mandir}/man1/native2ascii-%{uniquesuffix}.1*
%{_mandir}/man1/rmic-%{uniquesuffix}.1*
%{_mandir}/man1/schemagen-%{uniquesuffix}.1*
%{_mandir}/man1/serialver-%{uniquesuffix}.1*
%{_mandir}/man1/wsgen-%{uniquesuffix}.1*
%{_mandir}/man1/wsimport-%{uniquesuffix}.1*
%{_mandir}/man1/xjc-%{uniquesuffix}.1*
%if_enabled systemtap
%dir %{tapsetroot}
%dir %{tapsetdirttapset}
%dir %{tapsetdir}
%{tapsetdir}/*%{_arch}.stp
%endif

%files demo -f %{name}-demo.files
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

%files src
%doc README.md
%{_jvmdir}/%{sdkdir}/src.zip

%files javadoc
%_altdir/%altname-javadoc
%_sysconfdir/buildreqs/packages/substitute.d/%name-javadoc
%doc %{_javadocdir}/%{uniquejavadocdir}
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

# This puts a huge documentation file in /usr/share
# It is now architecture-dependent, as eg. AOT and Graal are now x86_64 only
# same for debug variant
%files javadoc-zip
%doc %{_javadocdir}/%{uniquejavadocdir}.zip
%doc --no-dereference %{buildoutputdir}/images/%{jdkimage}/jre/LICENSE

%if %{with_openjfx_binding}
%files openjfx -f %{name}-openjfx.files

%files openjfx-devel -f %{name}-openjfx-devel.files
%endif
%endif

%if %{include_debug_build}
%files slowdebug

%files headless-slowdebug

%files devel-slowdebug

%files demo-slowdebug -f %{name}-demo.files-slowdebug

%files src-slowdebug
%if %{with_openjfx_binding}
%files openjfx-slowdebug -f %{name}-openjfx.files-slowdebug

%files openjfx-devel-slowdebug -f %{name}-openjfx-devel.files-slowdebug
%endif
%endif

%if %{include_fastdebug_build}
%files fastdebug

%files headless-fastdebug

%files devel-fastdebug

%files demo-fastdebug -f %{name}-demo.files-fastdebug

%files src-fastdebug

%if %{with_openjfx_binding}
%files openjfx-debug -f %{name}-openjfx.files-debug

%files openjfx-devel-debug -f %{name}-openjfx-devel.files-debug
%endif
%endif

%changelog
* Wed Feb 08 2023 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.362.b09-alt0_1jpp8
- New version.
- Seciruty fixes:
  + CVE-2023-21830
  + CVE-2023-21843

* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.352.b08-alt0_1jpp8
- New version.
- Seciruty fixes:
  + JDK-8286526, CVE-2022-21619: Improve NTLM support
  + JDK-8286533, CVE-2022-21626: Key X509 usages
  + JDK-8286910, CVE-2022-21624: Improve JNDI lookups
  + JDK-8286918, CVE-2022-21628: Better HttpServer service

* Fri Oct 14 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.352.b07-alt0_0.1.eajpp8
- New version.

* Sat Aug 06 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.345.b01-alt0_1jpp8
- New version.

* Wed Aug 03 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.342.b07-alt0_0.1.eajpp8
- New version.
- Seciruty fixes:
  + JDK-8281859, CVE-2022-21540: Improve class compilation
  + JDK-8281866, CVE-2022-21541: Enhance MethodHandle invocations
  + JDK-8285407, CVE-2022-34169: Improve Xalan supports

* Wed Jul 20 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.342.b06-alt0_0.1.eajpp8
- New version.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.332.b09-alt0_0.1.eajpp8
- New version.
- Seciruty fixes:
  + JDK-8270504, CVE-2022-21426: Better XPath expression handling
  + JDK-8275151, CVE-2022-21443: Improved Object Identification
  + JDK-8277672, CVE-2022-21434: Better invocation handler handling
  + JDK-8278008, CVE-2022-21476: Improve Santuario processing
  + JDK-8278972, CVE-2022-21496: Improve URL supports

* Fri Apr 22 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.332.b06-alt0_0.1.eajpp8
- New version.

* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.322.b06-alt2_1jpp8
- New version.
- Security fixes:
  + JDK-8264934, CVE-2022-21248: Enhance cross VM serialization
  + JDK-8268488: More valuable DerValues
  + JDK-8268494: Better inlining of inlined interfaces
  + JDK-8268512: More content for ContentInfo
  + JDK-8268795: Enhance digests of Jar files
  + JDK-8268801: Improve PKCS attribute handling
  + JDK-8268813, CVE-2022-21283: Better String matching
  + JDK-8269151: Better construction of EncryptedPrivateKeyInfo
  + JDK-8269944: Better HTTP transport redux
  + JDK-8270392, CVE-2022-21293: Improve String constructions
  + JDK-8270416, CVE-2022-21294: Enhance construction of Identity maps
  + JDK-8270492, CVE-2022-21282: Better resolution of URIs
  + JDK-8270498, CVE-2022-21296: Improve SAX Parser configuration management
  + JDK-8270646, CVE-2022-21299: Improved scanning of XML entities
  + JDK-8271962: Better TrueType font loading
  + JDK-8271968: Better canonical naming
  + JDK-8271987: Manifest improved manifest entries
  + JDK-8272014, CVE-2022-21305: Better array indexing
  + JDK-8272026, CVE-2022-21340: Verify Jar Verification
  + JDK-8272236, CVE-2022-21341: Improve serial forms for transport
  + JDK-8272272: Enhance jcmd communication
  + JDK-8272462: Enhance image handling
  + JDK-8273290: Enhance sound handling
  + JDK-8273748, CVE-2022-21349: Improve Solaris font rendering
  + JDK-8273756, CVE-2022-21360: Enhance BMP image support
  + JDK-8273838, CVE-2022-21365: Enhanced BMP processing

* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.322.b04-alt2_0.1.eajpp8
- FTBFS: fixed linking libraries.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.322.b04-alt1_0.1.eajpp8
- New version.

* Sun Dec 19 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.322.b02-alt1_0.1.eajpp8
- New version.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b07-alt2_1jpp8
- Ignore possible fail of %%post scriptlet (ALT #41264).
- Optionally disable %%check by default.

* Sat Oct 23 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b07-alt1_1jpp8
- New version.
- Security fixes:
  + CVE-2021-35588 InnerClasses: VM permits wrong Throw ClassFormatError if InnerClasses attribute's inner_class_info_index is 0
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

* Thu Oct 14 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b05-alt1_0.1.eajpp8
- New version.

* Thu Sep 30 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b04-alt1_0.1.eajpp8
- New version.
- Remove nss-softokn mentions.

* Wed Sep 22 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b03-alt1_0.1.eajpp8
- New version.

* Mon Sep 13 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b02-alt1_0.1.eajpp8
- New version.

* Sun Sep 05 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.312.b01-alt1_0.1.eajpp8
- New version

* Fri Aug 27 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.302.b08-alt2_0jpp8
- FTBFS: disable LTO.

* Sun Aug 08 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.302.b08-alt1_0jpp8
- New version
- Security fixes since 1.8.0.282.b08-alt1_0jpp8:
  + CVE-2021-2341: Improve file transfers
  + CVE-2021-2369: Better jar file validation
  + CVE-2021-2388: Enhance compiler validation
  + CVE-2021-2163: Enhance opening JARs
  + CVE-2021-2161: Less ambiguous processing
- Remove accessibility packages

* Wed Feb 03 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.282.b08-alt1_0jpp8
- New version (ALT #39635)
- Require ca-trust-java instead of ca-trust (ALT #35690)
- Package nss.cfg
- Security fixes since 1.8.0.212.b04-alt2_0jpp8:
  + JDK-8247619 Improve Direct Buffering of Characters
  + CVE-2020-14779 Enhance support of Proxy class.
  + CVE-2020-14781 Enhanced LDAP contexts.
  + CVE-2020-14782 Enhance certificate processing.
  + CVE-2020-14792 Better range handling.
  + CVE-2020-14796 Improved URI Support.
  + CVE-2020-14797 Better Path Validation.
  + CVE-2020-14798 Enhanced buffer support.
  + CVE-2020-14803 Improved Buffer supports.
  + CVE-2020-14779 Enhance support of Proxy class
  + CVE-2020-14781 Enhanced LDAP contexts
  + CVE-2020-14782 Enhance certificate processing
  + CVE-2020-14792 Better range handling
  + CVE-2020-14796 Improved URI Support
  + CVE-2020-14797 Better Path Validation
  + CVE-2020-14798 Enhanced buffer support
  + CVE-2020-14803 Improved Buffer supports
  + CVE-2020-14579 NullPointerException in DerValue.equals(DerValue)
  + CVE-2020-14578 NegativeArraySizeException in sun.security.util.DerInputStream.getUnalignedBitString()
  + CVE-2020-14556 Better ForkJoinPool behavior
  + CVE-2020-14577 Enhance certificate verification
  + CVE-2020-14581 Better matrix operations
  + CVE-2020-14583 Better Buffer support
  + CVE-2020-14593 Less Affine Transformations
  + CVE-2020-14621 Better XML namespace handling
  + CVE-2020-2754 Forward references to Nashorn
  + CVE-2020-2755 Improve Nashorn matching
  + CVE-2020-2756 Better mapping of serial ENUMs
  + CVE-2020-2757 Less Blocking Array Queues
  + CVE-2020-2773 Better signatures in XML
  + CVE-2020-2781 Improve TLS session handling
  + CVE-2020-2800 Better Headings for HTTP Servers
  + CVE-2020-2803 Enhance buffering of byte buffers
  + CVE-2020-2805 Enhance typing of methods
  + CVE-2020-2830 Better Scanner conversions
  + CVE-2019-2933 Windows file handling redux.
  + CVE-2019-2945 Better socket support.
  + CVE-2019-2949 Better Kerberos ccache handling.
  + CVE-2019-2958 Build Better Processes.
  + CVE-2019-2964 Better support for patterns.
  + CVE-2019-2962 Better Glyph Images.
  + CVE-2019-2973 Better pattern compilation.
  + CVE-2019-2975 Unexpected exception in jjs.
  + CVE-2019-2978 Improved handling of jar files.
  + CVE-2019-2981 Better Path supports.
  + CVE-2019-2983 Better serial attributes.
  + CVE-2019-2987 Better rendering of native glyphs.
  + CVE-2019-2988 Better Graphics2D drawing.
  + CVE-2019-2989 Improve TLS connection support.
  + CVE-2019-2992 Enhance font glyph mapping.
  + CVE-2019-2999 Commentary on Javadoc comments.
  + CVE-2019-2894 Enhance ECDSA operations.
  + CVE-2019-2745 Improved ECC Implementation.
  + CVE-2019-2762 Exceptional throw cases.
  + CVE-2019-2766 Improve file protocol handling.
  + CVE-2019-2769 Better copies of CopiesList.
  + CVE-2019-2786 More limited privilege usage.
  + CVE-2019-7317 Improve PNG support options.
  + CVE-2019-2816 Normalize normalization.
  + CVE-2019-2842 Extended AES support.

* Tue Feb 02 2021 Andrey Cherepanov <cas@altlinux.org> 0:1.8.0.272.b10-alt3_0.3.eajpp8
- Remove crypto policy support that disable TLS1.3 (ALT #38170)

* Thu Dec 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.272.b10-alt2_0.3.eajpp8
- added alternatives for keytool, policytool, etc

* Mon Dec 14 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.272.b10-alt1_0.3.eajpp8
- new version

* Sun Dec 13 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.242.b08-alt2_0.0.eajpp8
- use zerg@'s hack for armh

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.242.b08-alt1_0.0.eajpp8
- new version

* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.212.b04-alt2_0jpp8
- new alternatives layout

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.212.b04-alt1_0jpp8
- new version

* Tue Jun 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.171-alt2_8.b10jpp8
- added provides, cleaned up desktop files

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.171-alt1_8.b10jpp8
- new version

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.161-alt1_0.b14jpp8
- new version

* Wed Feb 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0:1.8.0.151-alt2_5.b12jpp8
- NMU: fixed build with gcc-8.

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.151-alt1_5.b12jpp8
- new version

* Mon May 14 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0:1.8.0.144-alt5_1.b01jpp8
- require java-1.8.0-openjdk for build on all platforms
- built for aarch64

* Thu May 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt4_1.b01jpp8
- merged e2k support

* Mon Nov 27 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt3_1.b01jpp8
- removed obsolete exports in jvmjardir
- removed obsolete security policy alternatives in _jvmprivdir
- added java-1.x.0-openjdk alternative in jvmdir

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.144-alt2_1.b01jpp8
- fixed /usr/bin/java provides (closes: #32531)

* Mon Oct 02 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0:1.8.0.144-alt1_1.b01jpp8
- new version

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0:1.8.0.71-alt7_1.b15jpp8
- Fixed build with gcc-6

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt6_1.b15jpp8
- dropped dependency on maven-local in javadoc

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt5_1.b15jpp8
- trimmed desktop names (closes: #32463)

* Fri Apr 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt4_1.b15jpp8
- hack around mkimage

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt3_1.b15jpp8
- cleaned parasyte dep on /usr/bin/java

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt2_1.b15jpp8
- dropped dependency on maven-local

* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.71-alt1_1.b15jpp8
- new version
- TODO: add java8 support to tzdata and use system-wide tzdata-java

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0:1.8.0.45-alt1_40.b14jpp7
- new version

