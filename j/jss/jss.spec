%define _unpackaged_files_terminate_build 1
%define java_home %_jvmdir/jre

%def_with check

%define nss_version 3.66
%define java_version 17

# jss was renamed dogtag-jss
%define jss_rebranded_version 5.2.0-alt1

Name: jss
Version: 5.4.2
Release: alt3

Summary: Java Security Services (JSS)
License: MPL-1.1 or GPLv2+ or LGPLv2+
Group: System/Libraries
Url: https://github.com/dogtagpki/jss
Vcs: https://github.com/dogtagpki/jss

Source0: %name-%version.tar
Source1: jss.watch
Patch: %name-%version-alt.patch

# - upstream doesn't support i586 (Fedora's Java 17 is not built for that arch)
# - ALT's Java 17 is not built for armh
ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: jaxb-api
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: java-devel >= %java_version
BuildRequires: jpackage-generic-compat
BuildRequires: libnss-devel >= %nss_version
BuildRequires: libnspr-devel
BuildRequires: apache-commons-lang3
BuildRequires: slf4j
BuildRequires: slf4j-jdk14

# deps for tools/reproducible_jar.sh
BuildRequires: zip
BuildRequires: unzip

# not an optional though used only in tests
BuildRequires: junit

%if_with check
BuildRequires: ctest
BuildRequires: nss-utils >= %nss_version
%endif

%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%package -n dogtag-jss
Summary: Java Security Services (JSS)
Group: System/Libraries

Provides: jss = %EVR
Obsoletes: jss < %jss_rebranded_version

Requires: apache-commons-lang3
Requires: jaxb-api
Requires: slf4j
Requires: libnss >= %nss_version
Requires: java >= %java_version

%description -n dogtag-jss
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%prep
%setup
%patch -p1

%build
# Enable compiler optimizations and disable debugging code
# NOTE: If you ever need to create a debug build with optimizations disabled
# just comment out this line and change in the %%install section below the
# line that copies jars xpclass.jar to be xpclass_dbg.jar
export BUILD_OPT=1

%cmake \
    -DJAVA_HOME=%java_home \
    -DVERSION=%version \
    -DJNI_DIR=%_jnidir \
    -DLIB_DIR=%_libdir \
    -DWITH_JAVADOC=FALSE \
    ..

%cmake_build --target all

%check
# fails on migration to Java11, need to investigate
%ifnarch ppc64le
# FIPS is not enabled in kernel
cat > %_cmake__builddir/CTestCustom.cmake <<EOF
set(CTEST_CUSTOM_TESTS_IGNORE
   Enable_FipsMODE
   # NSS 3.81 failures
   # https://github.com/dogtagpki/jss/issues/882
   SSLClientAuth
   SSLEngine_RSA
   TestBufferPRFDSSL_RSA
   JSS_Test_BufferPRFD
   SSLClientAuth_FIPSMODE
   SSLEngine_RSA_FIPSMODE
)
EOF
CTEST_OUTPUT_ON_FAILURE=1 %cmake_build --target test
%endif

%install
%cmake_install

%files -n dogtag-jss
%dir %_libdir/jss
%_libdir/jss/jss.jar
%_libdir/jss/libjss.so
%_libdir/jss/libjss-symkey.so
%_jnidir/jss.jar

%changelog
* Tue Jul 30 2024 Stanislav Levin <slev@altlinux.org> 5.4.2-alt3
- Fixed FTBFS (NSS 3.101).

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 5.4.2-alt2
- Fixed FTBFS (NSS 3.97).

* Tue Aug 01 2023 Stanislav Levin <slev@altlinux.org> 5.4.2-alt1
- 5.2.1 -> 5.4.2.

* Mon Sep 26 2022 Stanislav Levin <slev@altlinux.org> 5.2.1-alt1
- 5.2.0 -> 5.2.1.

* Tue Aug 23 2022 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1
- 5.1.0 -> 5.2.0.

* Thu Mar 03 2022 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Wed Nov 24 2021 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.8.1 -> 5.0.0.

* Thu Jun 24 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt3
- Fixed FTBFS(missing deps).

* Fri Jun 11 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt2
- Built with Java11.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 4.8.1-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Feb 05 2021 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1
- 4.8.0 -> 4.8.1.

* Tue Nov 03 2020 Stanislav Levin <slev@altlinux.org> 4.8.0-alt1
- 4.7.3 -> 4.8.0.

* Mon Sep 28 2020 Stanislav Levin <slev@altlinux.org> 4.7.3-alt1
- 4.6.2 -> 4.7.3.

* Sat Sep 19 2020 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt2.1
- NMU: Fix build with nss-3.52.
- NMU: Fix bigus timestamp in changelog.

* Thu Nov 07 2019 Stanislav Levin <slev@altlinux.org> 4.6.2-alt2
- Fixed NPE during FreeIPA installations (RHBZ: 1766451).

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 4.6.2-alt1
- 4.6.1 -> 4.6.2 (closes: CVE-2019-14823).

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 4.6.1-alt1
- 4.5.3 -> 4.6.1.

* Thu Jul 11 2019 Stanislav Levin <slev@altlinux.org> 4.5.3-alt2
- Pinned supported Java.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 4.5.3-alt1
- 4.5.2 -> 4.5.3.

* Fri Jan 18 2019 Stanislav Levin <slev@altlinux.org> 4.5.2-alt1
- 4.5.0 -> 4.5.2.

* Mon Aug 13 2018 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 4.4.5 -> 4.5.0.

* Tue Jul 10 2018 Stanislav Levin <slev@altlinux.org> 4.4.5-alt1
- 4.4.4 -> 4.4.5

* Fri Jun 01 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.4-alt2
- fixed packaging on aarch64

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 4.4.4-alt1
- 4.4.3 -> 4.4.4

* Wed May 23 2018 Stanislav Levin <slev@altlinux.org> 4.4.3-alt1
- 4.4.2 -> 4.4.3

* Wed Sep 20 2017 Levin Stanislav <slev@altlinux.org> 4.4.2-alt1
- Update to upstream 4.4.2 version

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 4.2.6-alt6_41jpp8.M80P.1
- Build for p8.

* Mon Nov 21 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt6_42jpp8
- update (closes: #32779)

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt6_37jpp8
- new version

* Wed Nov 18 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.6-alt6_31jpp7
- Provide Tomcat support for TLS v1.1 and TLS v1.2 via NSS through JSS

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt5_31jpp7
- any-kernel patch thanks to gleb

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_31jpp7
- new version (closes: 29317)

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_29jpp7
- new release

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_28jpp7
- fixed build

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt4_25jpp7
- added jss4 compat symlink

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt3_25jpp7
- added jss4 compat symlink

* Tue Oct 30 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6-alt2_25jpp7
- new release; fixed build, updated fedora patches

* Wed Dec 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.6-alt2
- Fix build on 3.x kernels

* Sat Dec 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.6-alt1
- 4.2.6 with Fedora patches

* Tue Oct 23 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.5-alt1
- 4.2.5, spec cleanup

* Thu May 31 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.4-alt0
- Initial for Sisyphus

* Wed May 16 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-5
- Include the 3 license files
- Remove Requires for nss and nspr. These libraries have versioned symbols
  so BuildRequires is enough to set the minimum.
- Add sparc64 for the 64-bit list

* Mon May 14 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-4
- Included additional comments on jar signing and why ldconfig is not
  required.

* Thu May 10 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-3
- Added information on how to pull the source into a tar.gz

* Thu Mar 15 2007  Rob Crittenden <rcritten@redhat.com> 4.2.4-2
- Added RPM_OPT_FLAGS to XCFLAGS
- Added link to Sun JCE information

* Tue Feb 27 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-1
- Initial build
