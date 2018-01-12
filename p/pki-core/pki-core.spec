%filter_from_requires /^java-headless/d

# For more precise reqs:
%python_req_hier

# RESTEasy
%define resteasy_lib /usr/share/java/resteasy
%define jaxrs_api_jar /usr/share/java/jboss-jaxrs-2.0-api.jar

%define java_home /usr/lib/jvm/java

# ignore unpackaged files from native 'tpsclient'
# REMINDER:  Remove this '%%define' once 'tpsclient' is rewritten as a Java app
%define _unpackaged_files_terminate_build 0

# pkiuser and group. The uid and gid are preallocated
# see /usr/share/doc/setup/uidgid
%define pki_username pkiuser
%define pki_uid 17
%define pki_groupname pkiuser
%define pki_gid 17
%define pki_homedir /usr/share/pki

Name: pki-core
Version: 10.4.8
Release: alt5%ubt
Summary: Certificate System - PKI Core Components
Url: http://pki.fedoraproject.org/
License: GPLv2
Group: System/Servers

BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires(pre): rpm-macros-java rpm-build-ubt
BuildRequires: gcc-c++ ctest
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: sh4
BuildRequires: ldapjdk
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-io
BuildRequires: jakarta-commons-httpclient
BuildRequires: slf4j-jdk14

BuildRequires: libnuxwdog-java

BuildRequires: libldap-devel
BuildRequires: velocity
BuildRequires: xalan-j2

BuildRequires: jboss-annotations-1.2-api
BuildRequires: jboss-jaxrs-2.0-api
BuildRequires: jboss-logging
BuildRequires: resteasy-atom-provider
BuildRequires: resteasy-client
BuildRequires: resteasy-jaxb-provider
BuildRequires: resteasy-core
BuildRequires: resteasy-jackson-provider

BuildRequires: pylint >= 1.5.1
BuildRequires: python-module-flake8
BuildRequires: python-module-lxml
BuildRequires: python-module-sphinx
BuildRequires: python-module-nss
BuildRequires: python-module-requests
BuildRequires: python-module-pyldap
BuildRequires: python-module-six
BuildRequires: python-module-cryptography
BuildRequires: python-module-singledispatch
BuildRequires: python-module-selinux
BuildRequires: policycoreutils-sandbox
BuildRequires: junit
BuildRequires: jss >= 4.4.2

BuildRequires: tomcatjss >= 7.2.4
BuildRequires: tomcat >= 8.0.32

# additional build requirements needed to build native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
BuildRequires: libsasl2-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: apache2-devel >= 2.4.2
BuildRequires: libpcrecpp-devel
BuildRequires: python
BuildRequires: libsvrcore-devel
BuildRequires: zlib-devel

Source0: http://pki.fedoraproject.org/pki/sources/%name/%version/%release/%name-%version%{?prerel}.tar.gz

#######################
## pki-core-10.4.8-2
#######################
Patch0: pki-core-Fix-3DES-archival.patch
Patch1: pki-core-Fix-token-enrollment-and-recovery-ivs.patch
Patch2: pki-core-CMC-check-HTTPS-client-authentication-cert.patch
Patch3: pki-core-Fix-regression-in-pkcs12-key-bag-creation.patch
Patch4: pki-core-Fix-Platform-Dependent-Python-Import.patch
#######################
## pki-core-10.4.8-5
#######################
Patch5: pki-core-Added-banner-validation-in-InfoService.patch
#######################
## pki-core-10.4.8-6
#######################
Patch6: pki-core-Fix-lightweight-CA-replication-NPE-failure.patch
Patch7: pki-core-Fix-missing-CN-error-in-CMC-user-signed.patch
Patch8: pki-core-FixDeploymentDescriptor-upgrade-scriptlet.patch
Patch9: pki-core-KRA-use-AES-in-PKCS12-encrypted-key-recovery.patch
Patch10: pki-core-Fix-JSON-encoding-in-Python-3.patch
Patch11: pki-core-Fix-tokenOrigin-and-tokentType-attrs-in-recovered-certs.patch
Patch12: pki-core-Display-tokentType-and-tokenOrigin-in-TPS-UI-and-CLI-Server.patch
Patch13: pki-core-Display-tokentType-and-tokenOrigin-in-TPS-UI-and-CLI.patch
#######################
## pki-core-10.4.8-7
#######################
Patch14:          pki-core-Make-PKCS12-files-compatible-with-PBES2.patch
#######################
## AltLinux
#######################
Patch15: pki-core-alt-fix-paths.patch
Patch16: pki-core-alt-change-port.patch
Patch17: pki-core-alt-sphinx.patch

%global overview                                                       \
==================================                                     \
||  ABOUT "CERTIFICATE SYSTEM"  ||                                     \
==================================                                     \
                                                                       \
Certificate System (CS) is an enterprise software system designed      \
to manage enterprise Public Key Infrastructure (PKI) deployments.      \
                                                                       \
PKI Core contains ALL top-level java-based Tomcat PKI components:      \
                                                                       \
  * pki-symkey                                                         \
  * pki-base                                                           \
  * pki-base-python2 (alias for pki-base)                              \
  * pki-base-python3                                                   \
  * pki-base-java                                                      \
  * pki-tools                                                          \
  * pki-server                                                         \
  * pki-ca                                                             \
  * pki-kra                                                            \
  * pki-ocsp                                                           \
  * pki-tks                                                            \
  * pki-tps                                                            \
  * pki-javadoc                                                        \
                                                                       \
which comprise the following corresponding PKI subsystems:             \
                                                                       \
  * Certificate Authority (CA)                                         \
  * Key Recovery Authority (KRA)                                        \
  * Online Certificate Status Protocol (OCSP) Manager                  \
  * Token Key Service (TKS)                                            \
  * Token Processing Service (TPS)                                     \
                                                                       \
Python clients need only install the pki-base package.  This           \
package contains the python REST client packages and the client        \
upgrade framework.                                                     \
                                                                       \
Java clients should install the pki-base-java package.  This package   \
contains the legacy and REST Java client packages.  These clients      \
should also consider installing the pki-tools package, which contain   \
native and Java-based PKI tools and utilities.                         \
                                                                       \
Certificate Server instances require the fundamental classes and       \
modules in pki-base and pki-base-java, as well as the utilities in     \
pki-tools.  The main server classes are in pki-server, with subsystem  \
specific Java classes and resources in pki-ca, pki-kra, pki-ocsp etc.  \
                                                                       \
Finally, if Certificate System is being deployed as an individual or   \
set of standalone rather than embedded server(s)/service(s), it is     \
strongly recommended (though not explicitly required) to include at    \
least one PKI Theme package:                                           \
                                                                       \
  * dogtag-pki-theme (Dogtag Certificate System deployments)           \
    * dogtag-pki-server-theme                                          \
  * redhat-pki-server-theme (Red Hat Certificate System deployments)   \
    * redhat-pki-server-theme                                          \
  * customized pki theme (Customized Certificate System deployments)   \
    * <customized>-pki-server-theme                                    \
                                                                       \
  NOTE:  As a convenience for standalone deployments, top-level meta   \
         packages may be provided which bind a particular theme to     \
         these certificate server packages.                            \
                                                                       \
%nil

%description %overview
%package -n       pki-symkey
Summary: Symmetric Key JNI Package
Group: System/Libraries
Requires: jss >= 4.4.2
Requires: javapackages-tools
Provides: symkey = %EVR
Obsoletes: symkey < %EVR

%description -n   pki-symkey
The Symmetric Key Java Native Interface (JNI) package supplies various native
symmetric key operations to Java programs.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n       pki-base
Summary: Certificate System - PKI Framework
Group: System/Base
BuildArch: noarch
Provides: pki-common = %EVR
Provides: pki-util = %EVR
Obsoletes: pki-common < %EVR
Obsoletes: pki-util < %EVR
Conflicts: freeipa-server < 3.0.0
Requires: python-module-nss
Requires: python-module-requests
Requires: python-module-cryptography
Requires: python-module-six

%description -n   pki-base
The PKI Framework contains the common and client libraries and utilities.
This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n       pki-base-java
Summary: Certificate System - Java Framework
Group: System/Base
BuildArch: noarch
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: jakarta-commons-httpclient
Requires: slf4j-jdk14
Requires: javassist
Requires: javapackages-tools
Requires: jss >= 4.4.2
Requires: ldapjdk
Requires: pki-base = %version-%release
Requires: resteasy-atom-provider >= 3.0.6
Requires: resteasy-client >= 3.0.6
Requires: resteasy-jackson-provider >= 3.0.6
Requires: resteasy-core >= 3.0.6
Requires: resteasy-jaxb-provider >= 3.0.6
Requires: xalan-j2
Requires: xml-commons-apis
Requires: xml-commons-resolver

%description -n   pki-base-java
The PKI Framework contains the common and client libraries and utilities
written in Java.  This package is a part of the PKI Core used by the
Certificate System.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n       pki-tools
Summary: Certificate System - PKI Tools
Group: System/Base
Provides: pki-native-tools = %EVR
Provides: pki-java-tools = %EVR
Obsoletes: pki-native-tools < %EVR
Obsoletes: pki-java-tools < %EVR
Requires: openldap-clients
Requires: pki-base = %version-%release
Requires: pki-base-java = %version-%release
Requires: javapackages-tools
Requires: tomcat-servlet-3.1-api
Conflicts: strongswan

%description -n   pki-tools
This package contains PKI executables that can be used to help make
Certificate System into a more complete and robust PKI solution.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n       pki-server
Summary: Certificate System - PKI Server Framework
Group: System/Base

BuildArch: noarch

Provides: pki-deploy = %EVR
Provides: pki-setup = %EVR
Provides: pki-silent = %EVR

Obsoletes: pki-deploy < %EVR
Obsoletes: pki-setup < %EVR
Obsoletes: pki-silent < %EVR

Requires: etherwake net-tools
Requires: openldap-clients
Requires: libnss
Requires: pki-tools = %version-%release
Requires: pki-base = %version-%release
Requires: pki-base-java = %version-%release
Requires: policycoreutils-sandbox
Requires: python-module-lxml
Requires: python-module-pyldap

Obsoletes: pki-selinux

Requires: tomcat >= 8.0.32
Requires: tomcat-el-3.0-api >= 8.0.32
Requires: tomcat-jsp-2.3-api >= 8.0.32
Requires: tomcat-servlet-3.1-api >= 8.0.32
Requires: velocity
Requires: tomcatjss >= 7.2.4
Requires: libnuxwdog
Requires: libnuxwdog-java

%description -n   pki-server
The PKI Server Framework is required by the following four PKI subsystems:

    the Certificate Authority (CA),
    the Data Recovery Manager (DRM),
    the Online Certificate Status Protocol (OCSP) Manager,
    the Token Key Service (TKS), and
    the Token Processing Service (TPS).

This package is a part of the PKI Core used by the Certificate System.
The package contains scripts to create and remove PKI subsystems.

%overview

%package -n       pki-ca
Summary: Certificate System - Certificate Authority
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n   pki-ca
The Certificate Authority (CA) is a required PKI subsystem which issues,
renews, revokes, and publishes certificates as well as compiling and
publishing Certificate Revocation Lists (CRLs).

The Certificate Authority can be configured as a self-signing Certificate
Authority, where it is the root CA, or it can act as a subordinate CA,
where it obtains its own signing certificate from a public CA.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n       pki-kra
Summary: Certificate System - Data Recovery Manager
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n   pki-kra
The Data Recovery Manager (DRM) is an optional PKI subsystem that can act
as a Key Recovery Authority (KRA).  When configured in conjunction with the
Certificate Authority (CA), the DRM stores private encryption keys as part of
the certificate enrollment process.  The key archival mechanism is triggered
when a user enrolls in the PKI and creates the certificate request.  Using the
Certificate Request Message Format (CRMF) request format, a request is
generated for the user's private encryption key.  This key is then stored in
the DRM which is configured to store keys in an encrypted format that can only
be decrypted by several agents requesting the key at one time, providing for
protection of the public encryption keys for the users in the PKI deployment.

Note that the DRM archives encryption keys; it does NOT archive signing keys,
since such archival would undermine non-repudiation properties of signing keys.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n       pki-ocsp
Summary: Certificate System - Online Certificate Status Protocol Manager
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n   pki-ocsp
The Online Certificate Status Protocol (OCSP) Manager is an optional PKI
subsystem that can act as a stand-alone OCSP service.  The OCSP Manager
performs the task of an online certificate validation authority by enabling
OCSP-compliant clients to do real-time verification of certificates.  Note
that an online certificate-validation authority is often referred to as an
OCSP Responder.

Although the Certificate Authority (CA) is already configured with an
internal OCSP service.  An external OCSP Responder is offered as a separate
subsystem in case the user wants the OCSP service provided outside of a
firewall while the CA resides inside of a firewall, or to take the load of
requests off of the CA.

The OCSP Manager can receive Certificate Revocation Lists (CRLs) from
multiple CA servers, and clients can query the OCSP Manager for the
revocation status of certificates issued by all of these CA servers.

When an instance of OCSP Manager is set up with an instance of CA, and
publishing is set up to this OCSP Manager, CRLs are published to it
whenever they are issued or updated.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n       pki-tks
Summary: Certificate System - Token Key Service
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release
Requires: pki-symkey = %version-%release

%description -n   pki-tks
The Token Key Service (TKS) is an optional PKI subsystem that manages the
master key(s) and the transport key(s) required to generate and distribute
keys for hardware tokens.  TKS provides the security between tokens and an
instance of Token Processing System (TPS), where the security relies upon the
relationship between the master key and the token keys.  A TPS communicates
with a TKS over SSL using client authentication.

TKS helps establish a secure channel (signed and encrypted) between the token
and the TPS, provides proof of presence of the security token during
enrollment, and supports key changeover when the master key changes on the
TKS.  Tokens with older keys will get new token keys.

Because of the sensitivity of the data that TKS manages, TKS should be set up
behind the firewall with restricted access.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n       pki-tps
Summary: Certificate System - Token Processing Service
Group: System/Servers

Provides: pki-tps-tomcat
Provides: pki-tps-client

Obsoletes: pki-tps-tomcat
Obsoletes: pki-tps-client

Requires: pki-server = %version-%release

# additional runtime requirements needed to run native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
Requires: libnss >= 3.14.3
Requires: nss-utils >= 3.14.3
Requires: openldap-clients
Requires: pki-symkey = %version-%release

%description -n   pki-tps
The Token Processing System (TPS) is an optional PKI subsystem that acts
as a Registration Authority (RA) for authenticating and processing
enrollment requests, PIN reset requests, and formatting requests from
the Enterprise Security Client (ESC).

TPS is designed to communicate with tokens that conform to
Global Platform's Open Platform Specification.

TPS communicates over SSL with various PKI backend subsystems (including
the Certificate Authority (CA), the Data Recovery Manager (DRM), and the
Token Key Service (TKS)) to fulfill the user's requests.

TPS also interacts with the token database, an LDAP server that stores
information about individual tokens.

The utility "tpsclient" is a test tool that interacts with TPS.  This
tool is useful to test TPS server configs without risking an actual
smart card.

%overview

%package -n       pki-javadoc
Summary: Certificate System - PKI Framework Javadocs
Group: Development/Java

BuildArch: noarch

Provides: pki-util-javadoc = %EVR
Provides: pki-java-tools-javadoc = %EVR
Provides: pki-common-javadoc = %EVR

Obsoletes: pki-util-javadoc < %EVR
Obsoletes: pki-java-tools-javadoc < %EVR
Obsoletes: pki-common-javadoc < %EVR

%description -n   pki-javadoc
This documentation pertains exclusively to version %version of
the PKI Framework and Tools.

This package is a part of the PKI Core used by the Certificate System.

%overview

%prep
%setup -n %name-%version%{?prerel}
%patch0 -p1
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
%patch17 -p2
# from sem@:
# At least one script required bash4.
# Just use sh4 for all scripts.
egrep -rH '^#!/bin/(sh|bash)' . | cut -f1 -d: | sort -u | \
	xargs sed -r -i 's;^#!/bin/(sh|bash)( -X)?;#!/bin/sh4;'

%build
# ugly hacks for ALTLinux; fix me
# part 1: nss hacks
%add_optflags -I/usr/include/nss
sed -i -e 's,"nss3/base64.h","nss/base64.h",' \
	base/tps-client/src/modules/tokendb/mod_tokendb.cpp
# part 2: httpd/ -> apache2/
%add_optflags -I/usr/include/apu-1
grep -rlP "#include \x22httpd" | xargs sed -i 's/#include \x22httpd/#include \x22apache2/g'
# end ugly hacks

%__mkdir_p build
cd build
%fedora_cmake -DVERSION=%version-%release \
	-DVAR_INSTALL_DIR:PATH=/var \
	-DBUILD_PKI_CORE:BOOL=ON \
	-DJAVA_HOME=%java_home \
	-DJAVA_LIB_INSTALL_DIR=%_jnidir \
	-DSYSTEMD_LIB_INSTALL_DIR=%_unitdir \
	-DWITH_TOMCAT7:BOOL=OFF \
	-DJAXRS_API_JAR=%jaxrs_api_jar \
	-DRESTEASY_LIB=%resteasy_lib \
        ..
%__make VERBOSE=1 %{?_smp_mflags} all

%install
cd build
%__make install DESTDIR=%buildroot INSTALL="install -p"
# Create symlinks for admin console (TPS does not use admin console)
for subsystem in ca kra ocsp tks; do
    %__mkdir_p %buildroot%_datadir/pki/$subsystem/webapps/$subsystem/admin
    ln -s %_datadir/pki/server/webapps/pki/admin/console %buildroot%_datadir/pki/$subsystem/webapps/$subsystem/admin
done

# Create compatibility symlink for DRMTool -> KRATool
ln -s %_bindir/KRATool %buildroot%_bindir/DRMTool
# Create compatibility symlink for DRMTool.cfg -> KRATool.cfg
ln -s %_datadir/pki/java-tools/KRATool.cfg %buildroot%_datadir/pki/java-tools/DRMTool.cfg
# Create compatibility symlink for DRMTool.1.gz -> KRATool.1.gz
ln -s %_mandir/man1/KRATool.1.xz %buildroot%_mandir/man1/DRMTool.1.xz

# Customize client library links in /usr/share/pki/lib
rm -f %buildroot%_datadir/pki/lib/scannotation.jar
rm -f %buildroot%_datadir/pki/lib/resteasy-jaxrs-api.jar
rm -f %buildroot%_datadir/pki/lib/resteasy-jaxrs-jandex.jar
ln -sf %jaxrs_api_jar %buildroot%_datadir/pki/lib/jboss-jaxrs-2.0-api.jar
ln -sf /usr/share/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/lib/jboss-logging.jar
ln -sf /usr/share/java/jboss-annotations-1.2-api/jboss-annotations-api_1.2_spec.jar %buildroot%_datadir/pki/lib/jboss-annotations-api_1.2_spec.jar
ln -sf /usr/share/java/scannotation.jar %buildroot%_datadir/pki/lib/scannotation.jar

# Customize server library links in /usr/share/pki/server/common/lib
rm -f %buildroot%_datadir/pki/server/common/lib/scannotation.jar
rm -f %buildroot%_datadir/pki/server/common/lib/resteasy-jaxrs-api.jar
ln -sf %jaxrs_api_jar %buildroot%_datadir/pki/server/common/lib/jboss-jaxrs-2.0-api.jar
ln -sf /usr/share/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/server/common/lib/jboss-logging.jar
    ln -sf /usr/share/java/jboss-annotations-1.2-api/jboss-annotations-api_1.2_spec.jar %buildroot%_datadir/pki/server/common/lib/jboss-annotations-api_1.2_spec.jar

# Scanning the python code with pylint.
#%__python ../pylint-build-scan.py rpm --prefix %buildroot
#if [ $? -ne 0 ]; then
#    echo "pylint failed. RC: $?"
#    exit 1
#fi
#
#%__python ../pylint-build-scan.py rpm --prefix %buildroot -- --py3k
#if [ $? -ne 0 ]; then
#    echo "pylint --py3k failed. RC: $?"
#    exit 1
#fi

#flake8 --config ../tox.ini %buildroot
#if [ $? -ne 0 ]; then
#    echo "flake8 for Python 2 failed. RC: $?"
#    exit 1
#fi
#
#python3-flake8 --config ../tox.ini %buildroot
#if [ $? -ne 0 ]; then
#    echo "flake8 for Python 3 failed. RC: $?"
#    exit 1
#fi

%__rm -rf %buildroot%_datadir/pki/server/lib

%__mkdir_p %buildroot%_var/log/pki
%__mkdir_p %buildroot%_sharedstatedir/pki
# from sem@:
# This file should be sourced only
chmod -x %buildroot%_datadir/pki/scripts/operations

%if ! 0%_unpackaged_files_terminate_build
#tps client's files
    rm -f %buildroot%_initdir/pki-tpsd
    rm -f %buildroot%_unitdir/pki-tpsd.target
    rm -f %buildroot%_unitdir/pki-tpsd@.service
    rm -f %buildroot%_libdir/httpd/modules/mod_tokendb.so
    rm -f %buildroot%_libdir/httpd/modules/mod_tps.so
    rm -f %buildroot%_libdir/tps/libldapauth.so
    rm -rf %buildroot%_datadir/pki/tps/cgi-bin/
    rm -rf %buildroot%_datadir/pki/tps/docroot/
    rm -rf %buildroot%_datadir/pki/tps/lib/
    rm -rf %buildroot%_datadir/pki/tps/samples/
    rm -rf %buildroot%_datadir/pki/tps/scripts/
#python3 files
    rm -rf %buildroot/usr/lib/python3/site-packages/pki/
%endif #_unpackaged_files_terminate_build

# ALT Configuration
grep -q "CLASSPATH" %buildroot%_datadir/pki/server/conf/tomcat.conf ||
    echo CLASSPATH="${CLASSPATH}:/usr/share/pki/lib/*" >>%buildroot%_datadir/pki/server/conf/tomcat.conf
sed -i 's|^JAVA_HOME=.*|JAVA_HOME=/usr/lib/jvm/jre|' %buildroot%_datadir/pki/etc/pki.conf

%pre -n pki-server
getent group %pki_groupname >/dev/null || groupadd -f -g %pki_gid -r %pki_groupname
if ! getent passwd %pki_username >/dev/null ; then
    if ! getent passwd %pki_uid >/dev/null ; then
      useradd -r -u %pki_uid -g %pki_groupname -d %pki_homedir -s /sbin/nologin -c "Certificate System" %pki_username
    else
      useradd -r -g %pki_groupname -d %pki_homedir -s /sbin/nologin -c "Certificate System" %pki_username
    fi
fi
exit 0

%post -n pki-base
if [ $1 -eq 1 ]
then
    # On RPM installation create system upgrade tracker
    echo "Configuration-Version: %version" > %_sysconfdir/pki/pki.version

else
    # On RPM upgrade run system upgrade
    echo "Upgrading PKI system configuration at `/bin/date`." >> /var/log/pki/pki-upgrade-%version.log 2>&1
    /usr/sbin/pki-upgrade --silent >> /var/log/pki/pki-upgrade-%version.log 2>&1
    echo >> /var/log/pki/pki-upgrade-%version.log 2>&1
fi

%postun -n pki-base
if [ $1 -eq 0 ]
then
    # On RPM uninstallation remove system upgrade tracker
    rm -f %_sysconfdir/pki/pki.version
fi

%post -n pki-server
echo "Upgrading PKI server configuration at `/bin/date`." >> /var/log/pki/pki-server-upgrade-%version.log 2>&1
 /usr/sbin/pki-server-upgrade --silent >> /var/log/pki/pki-server-upgrade-%version.log 2>&1
echo >> /var/log/pki/pki-server-upgrade-%version.log 2>&1

# Migrate Tomcat configuration
 /usr/sbin/pki-server migrate >> /var/log/pki/pki-server-upgrade-%version.log 2>&1
echo >> /var/log/pki/pki-server-upgrade-%version.log 2>&1

# ALT add Java CLASSPATH on upgrade
if [ "$1" == "2" ]
then
    grep -q "CLASSPATH" %_sysconfdir/tomcat/tomcat.conf ||
        echo CLASSPATH="${CLASSPATH}:/usr/share/pki/lib/*" >>%_sysconfdir/tomcat/tomcat.conf
    systemctl daemon-reload
    systemctl restart pki-tomcatd@pki-tomcat.service
fi

%files -n pki-symkey
%doc base/symkey/LICENSE
%_jnidir/symkey.jar
%_libdir/symkey/

%files -n pki-base
%doc base/common/LICENSE
%doc base/common/LICENSE.LESSER
%doc %_datadir/doc/pki-base/html
%_datadir/pki/VERSION
%_datadir/pki/etc/
%_datadir/pki/upgrade/
%dir %_datadir/pki/key
%_datadir/pki/key/templates
%config(noreplace) %_sysconfdir/pki/pki.conf
%exclude %python_sitelibdir_noarch/pki/server
%python_sitelibdir_noarch/pki
%dir %_var/log/pki
%_sbindir/pki-upgrade
%_mandir/man1/pki-python-client.1.*
%_mandir/man5/pki-logging.5.*
%_mandir/man8/pki-upgrade.8.*

%files -n pki-base-java
%_datadir/pki/examples/java/
%_datadir/pki/lib/
%dir %_javadir/pki
%_javadir/pki/pki-cmsutil.jar
%_javadir/pki/pki-nsutil.jar
%_javadir/pki/pki-certsrv.jar

%files -n pki-tools
%doc base/native-tools/LICENSE base/native-tools/doc/README
%_bindir/pki
%_bindir/p7tool
%_bindir/revoker
%_bindir/setpin
%_bindir/sslget
%_bindir/tkstool
%_datadir/pki/native-tools/
%_bindir/AtoB
%_bindir/AuditVerify
%_bindir/BtoA
%_bindir/CMCEnroll
%_bindir/CMCRequest
%_bindir/CMCResponse
%_bindir/CMCRevoke
%_bindir/CRMFPopClient
%_bindir/DRMTool
%_bindir/ExtJoiner
%_bindir/GenExtKeyUsage
%_bindir/GenIssuerAltNameExt
%_bindir/GenSubjectAltNameExt
%_bindir/HttpClient
%_bindir/KRATool
%_bindir/OCSPClient
%_bindir/PKCS10Client
%_bindir/PKCS12Export
%_bindir/PrettyPrintCert
%_bindir/PrettyPrintCrl
%_bindir/TokenInfo
%_javadir/pki/pki-tools.jar
%_datadir/pki/java-tools/
%_mandir/man1/AtoB.1.*
%_mandir/man1/AuditVerify.1.*
%_mandir/man1/BtoA.1.*
%_mandir/man1/CMCEnroll.1.*
%_mandir/man1/DRMTool.1.*
%_mandir/man1/KRATool.1.*
%_mandir/man1/PrettyPrintCert.1.*
%_mandir/man1/PrettyPrintCrl.1.*
%_mandir/man1/pki.1.*
%_mandir/man1/pki-audit.1.*
%_mandir/man1/pki-ca-kraconnector.1.*
%_mandir/man1/pki-ca-profile.1.*
%_mandir/man1/pki-cert.1.*
%_mandir/man1/pki-client.1.*
%_mandir/man1/pki-group.1.*
%_mandir/man1/pki-group-member.1.*
%_mandir/man1/pki-key.1.*
%_mandir/man1/pki-pkcs12-cert.1.*
%_mandir/man1/pki-pkcs12-key.1.*
%_mandir/man1/pki-pkcs12.1.*
%_mandir/man1/pki-securitydomain.1.*
%_mandir/man1/pki-tps-profile.1.*
%_mandir/man1/pki-user.1.*
%_mandir/man1/pki-user-cert.1.*
%_mandir/man1/pki-user-membership.1.*

%files -n pki-server
%doc base/common/THIRD_PARTY_LICENSES
%doc base/server/LICENSE
%doc base/server/README
%_sysconfdir/pki/default.cfg
%_sbindir/pkispawn
%_sbindir/pkidestroy
%_sbindir/pki-server
%_sbindir/pki-server-nuxwdog
%_sbindir/pki-server-upgrade
%python_sitelibdir_noarch/pki/server/
%dir %_datadir/pki/deployment
%_datadir/pki/deployment/config/
%dir %_datadir/pki/scripts
%_datadir/pki/scripts/operations
%_bindir/pkidaemon
%dir %_sysconfdir/systemd/system/pki-tomcatd.target.wants
%attr(644,root,root) %_unitdir/pki-tomcatd@.service
%attr(644,root,root) %_unitdir/pki-tomcatd.target
%dir %_sysconfdir/systemd/system/pki-tomcatd-nuxwdog.target.wants
%attr(644,root,root) %_unitdir/pki-tomcatd-nuxwdog@.service
%attr(644,root,root) %_unitdir/pki-tomcatd-nuxwdog.target
%_javadir/pki/pki-cms.jar
%_javadir/pki/pki-cmsbundle.jar
%_javadir/pki/pki-cmscore.jar
%_javadir/pki/pki-tomcat.jar
%dir %_sharedstatedir/pki
%_mandir/man1/pkidaemon.1.*
%_mandir/man5/pki_default.cfg.5.*
%_mandir/man5/pki-server-logging.5.*
%_mandir/man8/pki-server-upgrade.8.*
%_mandir/man8/pkidestroy.8.*
%_mandir/man8/pkispawn.8.*
%_mandir/man8/pki-server.8.*
%_mandir/man8/pki-server-instance.8.*
%_mandir/man8/pki-server-subsystem.8.*
%_mandir/man8/pki-server-nuxwdog.8.*
%_mandir/man8/pki-server-migrate.8.*

%_datadir/pki/setup/
%_datadir/pki/server/

%files -n pki-ca
%doc base/ca/LICENSE
%_javadir/pki/pki-ca.jar
%dir %_datadir/pki/ca
%_datadir/pki/ca/conf/
%_datadir/pki/ca/emails/
%dir %_datadir/pki/ca/profiles
%_datadir/pki/ca/profiles/ca/
%_datadir/pki/ca/setup/
%_datadir/pki/ca/webapps/

%files -n pki-kra
%doc base/kra/LICENSE
%_javadir/pki/pki-kra.jar
%dir %_datadir/pki/kra
%_datadir/pki/kra/conf/
%_datadir/pki/kra/setup/
%_datadir/pki/kra/webapps/

%files -n pki-ocsp
%doc base/ocsp/LICENSE
%_javadir/pki/pki-ocsp.jar
%dir %_datadir/pki/ocsp
%_datadir/pki/ocsp/conf/
%_datadir/pki/ocsp/setup/
%_datadir/pki/ocsp/webapps/

%files -n pki-tks
%doc base/tks/LICENSE
%_javadir/pki/pki-tks.jar
%dir %_datadir/pki/tks
%_datadir/pki/tks/conf/
%_datadir/pki/tks/setup/
%_datadir/pki/tks/webapps/

%files -n pki-tps
%doc base/tps/LICENSE
%_javadir/pki/pki-tps.jar
%dir %_datadir/pki/tps
%_datadir/pki/tps/applets/
%_datadir/pki/tps/conf/
%_datadir/pki/tps/setup/
%_datadir/pki/tps/webapps/
%_mandir/man5/pki-tps-connector.5.*
%_mandir/man5/pki-tps-profile.5.*
%_mandir/man1/tpsclient.1.*
# files for native 'tpsclient'
# REMINDER:  Remove this comment once 'tpsclient' is rewritten as a Java app
%_bindir/tpsclient
%_libdir/tps/libtps.so
%_libdir/tps/libtokendb.so

%files -n pki-javadoc
%_javadocdir/pki-%version/

%changelog
* Fri Jan 12 2018 Stanislav Levin <slev@altlinux.org> 10.4.8-alt5%ubt
- Fix package build broken due to new ca-certificates system
  Directory /etc/pki and /usr/share/pki belong to
  filesystem package

* Mon Oct 02 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt4%ubt
- Fix Java CLASSPATH on RPM package upgrade

* Fri Sep 29 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt3%ubt
- Fix Java CLASSPATH by Evgeny Sinelnikov <sin@altlinux.org>
- Clean up spec

* Mon Sep 25 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt2%ubt
- Fix version compare for sphinx python module

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt6_19jpp8
- added Conflicts: strongswan (closes: #33037)

* Thu Sep 21 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt1%ubt
- Update to upstream's 10.4.8 version

* Wed Feb 15 2017 Mikhail Efremov <sem@altlinux.org> 10.2.6-alt4_19jpp8.M80P.1
- Build for p8.

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt5_19jpp8
- thanks to sem@
- fixed build
- changed port to 8090

* Mon Jan 23 2017 Mikhail Efremov <sem@altlinux.org> 10.2.6-alt3_19jpp8.M80P.1
- pki-tools: Add conflict with strongswan.
- Build with python-module-ldap.
- Build for p8.

* Fri Jan 20 2017 Ivan Zakharyaschev <imz@altlinux.org> 10.2.6-alt2_16jpp7.M80P.2
- %%python_req_hier - For more precise Pythin autoreqs.

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt4_19jpp8
- cleanup: removed rpm-build-java

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt3_19jpp8
- cleanup: removed conflict glitch and selinux dependency

* Mon Nov 21 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt2_19jpp8
- bugfix thanks to @sem

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt2_16jpp7.M80P.1
- backport

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt2_16jpp8
- added sem@ patch

* Fri Apr 29 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt1_16jpp8
- new version
- TODO: %_datadir/pki/tks/* not packaged
