%set_verify_elf_method relaxed

Name: jss
Version: 4.2.6
Release: alt2
Summary: Java Security Services (JSS)

Group: Development/Java
License: MPL/GPL/LGPL
Url: http://www.mozilla.org/projects/security/pki/jss/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: MPL-1.1.txt
Source2: gpl.txt
Source3: lgpl.txt

BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: java-1.6.0-sun-devel

# don't use sun.net.www.protocol.http.HttpURLConnection.userAgent
Patch1: jss-link-alt.patch
Patch2: jss-4.2.6-fc-jss-key_pair_usage_with_op_flags.patch
Patch3: jss-4.2.6-fc-jss-javadocs-param.patch
Patch4: jss-4.2.6-fc-jss-ipv6.patch
Patch5: jss-4.2.6-fc-jss-ECC-pop.patch
Patch6: jss-4.2.6-fc-jss-loadlibrary.patch
Patch7: jss-4.2.6-fc-jss-ocspSettings.patch
Patch8: jss-4.2.6-fc-jss-ECC_keygen_byCurveName.patch
Patch9: jss-4.2.6-fc-jss-VerifyCertificate.patch
Patch10: jss-4.2.6-fc-jss-bad-error-string-pointer.patch
Patch11: jss-4.2.6-fc-jss-VerifyCertificateReturnCU.patch
Patch12: jss-4.2.6-fc-jss-ECC-HSM-FIPS.patch
Patch13: jss-4.2.6-fc-jss-eliminate-native-compiler-warnings.patch
Patch14: jss-4.2.6-fc-jss-eliminate-java-compiler-warnings.patch
Patch15: jss-4.2.6-fc-jss-PKCS12-FIPS.patch
Patch16: jss-4.2.6-fc-jss-eliminate-native-coverity-defects.patch
Patch17: jss-4.2.6-fc-jss-PBE-PKCS5-V2-secure-P12.patch
Patch18: jss-4.2.6-fc-jss-wrapInToken.patch

%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
#export JAVA_HOME=/usr/lib/jvm/java-1.4.2

# Generate symbolic info for debuggers
XCFLAGS="-g $RPM_OPT_FLAGS"
export XCFLAGS

PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

export PKG_CONFIG_ALLOW_SYSTEM_LIBS
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS

NSPR_INCLUDE_DIR=`%_bindir/pkg-config --cflags-only-I nspr | sed 's/-I//'`
NSPR_LIB_DIR=`%_bindir/pkg-config --libs-only-L nspr | sed 's/-L//'`

NSS_INCLUDE_DIR=`%_bindir/pkg-config --cflags-only-I nss | sed 's/-I//'`
NSS_LIB_DIR=`%_bindir/pkg-config --libs-only-L nss | sed 's/-L//'`

export NSPR_INCLUDE_DIR
export NSPR_LIB_DIR
export NSS_INCLUDE_DIR
export NSS_LIB_DIR

%ifarch x86_64 ppc64 ia64 s390x sparc64
USE_64=1
export USE_64
%endif

cp -p mozilla/security/coreconf/Linux2.6.mk mozilla/security/coreconf/Linux3.1.mk
sed -i -e 's;LINUX2_1;LINUX3_1;' mozilla/security/coreconf/Linux3.1.mk
cp -p mozilla/security/coreconf/Linux2.6.mk mozilla/security/coreconf/Linux3.0.mk
sed -i -e 's;LINUX2_1;LINUX3_1;' mozilla/security/coreconf/Linux3.0.mk

# The Makefile is not thread-safe
make -C mozilla/security/coreconf
make -C mozilla/security/jss

%install
# Copy the license files here so we can include them in %doc
cp -p %SOURCE1 .
cp -p %SOURCE2 .
cp -p %SOURCE3 .

# There is no install target so we'll do it by hand

# jars
install -d -m 0755 %buildroot%_datadir/java/
install -m 644 mozilla/dist/xpclass_dbg.jar %buildroot%_datadir/java/jss4-%version.jar
pushd  %buildroot%_datadir/java
    ln -fs jss4-%version.jar jss4.jar
popd

# We have to use the name libjss4.so because this is dynamically
# loaded by the jar file.
install -d -m 0755 %buildroot%_libdir
install -m 0755 mozilla/dist/Linux*.OBJ/lib/libjss4.so %buildroot%_libdir/

# FIXME - sign jss4.jar. In order to use JSS as a JCE provider it needs to be
# signed with a Sun-issued certificate. Since we would need to make this
# certificate and private key public to provide reproducability in the rpm
# building we have to ship an unsigned jar.
#
# Instructions for getting a signing cert can be found here:
# http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/HowToImplAProvider.html#Step61
#
# This signing is not required by every JVM. gcj ignores the signature and does
# not require one. The Sun and IBM JVMs both check and enforce the signature.
# Behavior of other JVMs is not known but they probably enforce the signature
# as well.

%files
%doc mozilla/security/jss/jss.html MPL-1.1.txt gpl.txt lgpl.txt
%_datadir/java/*
%_libdir/lib*.so

%changelog
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
