# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:           jss
Version:        4.2.6
Release:        alt6_42jpp8
Summary:        Java Security Services (JSS)

Group:          System/Libraries
License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://www.mozilla.org/projects/security/pki/jss/
# The source for this package was pulled from upstream's cvs. Use the
# following commands to generate the tarball:
# cvs -d :pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot export -r JSS_4_2_6_RTM -d jss-4.2.6 -N mozilla/security/coreconf mozilla/security/jss
# tar -czvf jss-4.2.6.tar.gz jss-4.2.6
Source0:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}-%{release}/%{name}-%{version}.tar.gz
Source1:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}-%{release}/MPL-1.1.txt
Source2:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}-%{release}/gpl.txt
Source3:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}-%{release}/lgpl.txt

BuildRequires: libnss-devel libnss-devel-static
BuildRequires:  libnspr-devel >= 4.11.0
%if 0%{?fedora} >= 25
BuildRequires:     perl
%endif
Requires:       libnss >= 3.21.0

Patch1:         jss-key_pair_usage_with_op_flags.patch
Patch2:         jss-javadocs-param.patch
Patch3:         jss-ipv6.patch
Patch4:         jss-ECC-pop.patch
Patch5:         jss-loadlibrary.patch
Patch6:         jss-ocspSettings.patch
Patch7:         jss-ECC_keygen_byCurveName.patch
Patch8:         jss-VerifyCertificate.patch
Patch9:         jss-bad-error-string-pointer.patch
Patch10:        jss-VerifyCertificateReturnCU.patch
#Patch11:        jss-slots-not-freed.patch
Patch12:        jss-ECC-HSM-FIPS.patch
Patch13:        jss-eliminate-native-compiler-warnings.patch
Patch14:        jss-eliminate-java-compiler-warnings.patch
Patch15:        jss-PKCS12-FIPS.patch
Patch16:        jss-eliminate-native-coverity-defects.patch
Patch17:        jss-PBE-PKCS5-V2-secure-P12.patch
Patch18:        jss-wrapInToken.patch
Patch19:        jss-HSM-manufacturerID.patch
Patch20:        jss-ECC-Phase2KeyArchivalRecovery.patch
Patch21:        jss-undo-JCA-deprecations.patch
Patch22:        jss-undo-BadPaddingException-deprecation.patch
Patch23:        jss-fixed-build-issue-on-F17-or-newer.patch
Patch24:        jss-SHA-OID-fix.patch
Patch25:        jss-RC4-strengh-verify.patch
Patch26:        jss-support-TLS1_1-TLS1_2.patch
Patch27:        jss-WindowsCompileFix.patch
Patch28:        jss-WindowsLoadLibrary.patch
Patch29:        jss-Fixed-build-failures.patch
Patch30:        jss-VerifyCertificate-enhancement.patch
Patch31:        jss-lunasaUnwrap.patch
Patch32:        jss-symkey-enhancements.patch
Patch33:        jss-crmf-envelopedData.patch
Source44: import.info
Patch34: jss-link-alt.patch
Patch35: jss-alt-sem-as-needed.patch


%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%package javadoc
Summary:        Java Security Services (JSS) Javadocs
Group:          Development/Java
Requires:       jss = %{version}
BuildArch: noarch

%description javadoc
This package contains the API documentation for JSS.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java

# Enable compiler optimizations and disable debugging code
BUILD_OPT=1
export BUILD_OPT

# Generate symbolic info for debuggers
XCFLAGS="-g $RPM_OPT_FLAGS"
export XCFLAGS

PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

export PKG_CONFIG_ALLOW_SYSTEM_LIBS
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS

NSPR_INCLUDE_DIR=`/usr/bin/pkg-config --cflags-only-I nspr | sed 's/-I//'`
NSPR_LIB_DIR=`/usr/bin/pkg-config --libs-only-L nspr | sed 's/-L//'`

NSS_INCLUDE_DIR=`/usr/bin/pkg-config --cflags-only-I nss | sed 's/-I//'`
NSS_LIB_DIR=`/usr/bin/pkg-config --libs-only-L nss | sed 's/-L//'`

export NSPR_INCLUDE_DIR
export NSPR_LIB_DIR
export NSS_INCLUDE_DIR
export NSS_LIB_DIR

%ifarch x86_64 ppc64 ia64 s390x sparc64
USE_64=1
export USE_64
%endif

%if 0%{?fedora} >= 16
cp -p mozilla/security/coreconf/Linux2.6.mk mozilla/security/coreconf/Linux3.1.mk 
sed -i -e 's;LINUX2_1;LINUX3_1;' mozilla/security/coreconf/Linux3.1.mk

cp -p mozilla/security/coreconf/Linux3.1.mk mozilla/security/coreconf/Linux3.2.mk 
sed -i -e 's;LINUX3_1;LINUX3_2;' mozilla/security/coreconf/Linux3.2.mk

cp -p mozilla/security/coreconf/Linux3.2.mk mozilla/security/coreconf/Linux3.6.mk
sed -i -e 's;LINUX3_1;LINUX3_6;' mozilla/security/coreconf/Linux3.6.mk
%endif


# 3.0(t6), 3.5(SIS) kernels support
for i in 0 `seq 3 20`; do
cp -p mozilla/security/coreconf/Linux3.1.mk mozilla/security/coreconf/Linux3.$i.mk
sed -i -e 's;LINUX3_1;LINUX3_'$i';' mozilla/security/coreconf/Linux3.$i.mk
done

fix_kversion(){
set -- $(uname -r | cut -d. -f 1-2 --output-delimiter=" ")
local KMAJ=$1; shift
local KMIN=$1; shift
if [ ! -s "mozilla/security/coreconf/Linux$KMAJ.$KMIN.mk" ]; then
  cp -p mozilla/security/coreconf/Linux3.1.mk mozilla/security/coreconf/Linux"$KMAJ.$KMIN".mk
  sed -i -e "s;LINUX3_1;LINUX$KMAJ_$KMIN;" mozilla/security/coreconf/Linux"$KMAJ.$KMIN".mk
fi
}
fix_kversion

# The Makefile is not thread-safe
make -C mozilla/security/coreconf
make -C mozilla/security/jss
make -C mozilla/security/jss javadoc

%install
rm -rf $RPM_BUILD_ROOT docdir

# Copy the license files here so we can include them in %doc
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .

# There is no install target so we'll do it by hand

# jars
%if 0%{?fedora} >= 16
install -d -m 0755 $RPM_BUILD_ROOT%{_jnidir}
install -m 644 mozilla/dist/xpclass.jar ${RPM_BUILD_ROOT}%{_jnidir}/jss4.jar
%else
install -d -m 0755 $RPM_BUILD_ROOT%{_libdir}/jss
install -m 644 mozilla/dist/xpclass.jar ${RPM_BUILD_ROOT}%{_libdir}/jss/jss4-%{version}.jar
ln -fs jss4-%{version}.jar $RPM_BUILD_ROOT%{_libdir}/jss/jss4.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_jnidir}
ln -fs %{_libdir}/jss/jss4.jar $RPM_BUILD_ROOT%{_jnidir}/jss4.jar
%endif

# We have to use the name libjss4.so because this is dynamically
# loaded by the jar file.
install -d -m 0755 $RPM_BUILD_ROOT%{_libdir}/jss
install -m 0755 mozilla/dist/Linux*.OBJ/lib/libjss4.so ${RPM_BUILD_ROOT}%{_libdir}/jss/
%if 0%{?fedora} >= 16
pushd  ${RPM_BUILD_ROOT}%{_libdir}/jss
    ln -fs %{_jnidir}/jss4.jar jss4.jar
popd
%endif

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp mozilla/dist/jssdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
mkdir -p %buildroot%_javadir/
ln -s %_jnidir/jss4.jar %buildroot%_javadir/jss4.jar

%files
%doc mozilla/security/jss/jss.html MPL-1.1.txt gpl.txt lgpl.txt
%{_libdir}/jss/*
%{_jnidir}/*
%_javadir/jss4.jar

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*


%changelog
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
* Mon Feb 27 2007 Rob Crittenden <rcritten@redhat.com> 4.2.4-1
- Initial build
