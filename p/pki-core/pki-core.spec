%define _unpackaged_files_terminate_build 1

# RESTEasy
%define resteasy_lib /usr/share/java/resteasy
%define jaxrs_api_jar /usr/share/java/jboss-jaxrs-2.0-api.jar

# Java
%define java_home /usr/lib/jvm/jre

Name: pki-core
Version: 10.5.3
Release: alt1%ubt
Summary: Certificate System - PKI Core Components
# Source-git: https://github.com/dogtagpki/pki
Url: http://pki.fedoraproject.org
License: %gpl2only
Group: System/Servers
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-macros-java
BuildRequires(pre): java-1.8.0-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: sh4
BuildRequires: zip
BuildRequires: ldapjdk
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: jakarta-commons-httpclient

BuildRequires: libnspr-devel
BuildRequires: libnss-devel

BuildRequires: libnuxwdog-java

BuildRequires: libldap-devel
BuildRequires: pkg-config
BuildRequires: policycoreutils
BuildRequires: velocity
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: slf4j
BuildRequires: slf4j-jdk14

BuildRequires: jboss-annotations-1.2-api
BuildRequires: jboss-jaxrs-2.0-api
BuildRequires: jboss-logging
BuildRequires: resteasy-atom-provider
BuildRequires: resteasy-client
BuildRequires: resteasy-jaxb-provider
BuildRequires: resteasy-core
BuildRequires: resteasy-jackson-provider
BuildRequires: junit
BuildRequires: javapackages-tools
BuildRequires: jss >= 4.4.2
BuildRequires: tomcatjss >= 7.2.4
BuildRequires: tomcat-servlet-3.1-api
BuildRequires: tomcat-lib

BuildRequires: pylint
BuildRequires: python-module-flake8
BuildRequires: pyflakes
BuildRequires: python-module-lxml
BuildRequires: python-module-sphinx
BuildRequires: python-module-nss
BuildRequires: python-module-requests
BuildRequires: python-module-pyldap
BuildRequires: python-module-six
BuildRequires: python-module-cryptography
BuildRequires: python-module-selinux
BuildRequires: python-module-sepolgen
BuildRequires: python3-module-flake8
BuildRequires: python3-pyflakes
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-lxml
BuildRequires: python3-module-nss
BuildRequires: python3-module-pyldap
BuildRequires: python3-module-requests
BuildRequires: python3-module-six

BuildRequires: systemd

# additional build requirements needed to build native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
BuildRequires: libsasl2-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: apache2-devel >= 2.4.2
BuildRequires: libpcrecpp-devel
BuildRequires: python
BuildRequires: zlib-devel

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
%package -n pki-symkey
Summary: Symmetric Key JNI Package
Group: System/Libraries
Requires: jss >= 4.4.2
Requires: libnss
Requires: javapackages-tools
Provides: symkey = %EVR
Obsoletes: symkey < %EVR

%description -n pki-symkey
The Symmetric Key Java Native Interface (JNI) package supplies various native
symmetric key operations to Java programs.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n pki-base
Summary: Certificate System - PKI Framework
Group: System/Base
BuildArch: noarch
Provides: pki-common = %EVR
Provides: pki-util = %EVR
Obsoletes: pki-common < %EVR
Obsoletes: pki-util < %EVR
Requires: libnss

%description -n pki-base
The PKI Framework contains the common and client libraries and utilities.
This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n pki-base-java
Summary: Certificate System - Java Framework
Group: System/Base
BuildArch: noarch
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: jakarta-commons-httpclient
Requires: slf4j
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
Requires: xerces-j2
Requires: xml-commons-apis
Requires: xml-commons-resolver

%description -n pki-base-java
The PKI Framework contains the common and client libraries and utilities
written in Java.  This package is a part of the PKI Core used by the
Certificate System.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n python-module-pki-base
Summary: Certificate System - PKI Framework
Group: Development/Python

BuildArch: noarch

Requires: pki-base = %version-%release
Requires: python-module-nss
Requires: python-module-six
Requires: python-module-requests
Requires: python-module-cryptography

%description -n python-module-pki-base
This package contains PKI client library for Python 3.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n python3-module-pki-base
Summary: Certificate System - PKI Framework
Group: Development/Python3

BuildArch: noarch

Requires: pki-base = %version-%release
Requires: python3-module-nss
Requires: python3-module-six
Requires: python3-module-lxml
Requires: python3-module-requests
Requires: python3-module-cryptography

%description -n python3-module-pki-base
This package contains PKI client library for Python 3.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n pki-tools
Summary: Certificate System - PKI Tools
Group: System/Base
Provides: pki-native-tools = %EVR
Provides: pki-java-tools = %EVR
Obsoletes: pki-native-tools < %EVR
Obsoletes: pki-java-tools < %EVR
Requires: openldap-clients
Requires: libnss
Requires: pki-base = %version-%release
Requires: pki-base-java = %version-%release
Requires: javapackages-tools
Requires: tomcat-servlet-3.1-api
Conflicts: strongswan

%description -n pki-tools
This package contains PKI executables that can be used to help make
Certificate System into a more complete and robust PKI solution.

This package is a part of the PKI Core used by the Certificate System.

%overview

%package -n pki-server
Summary: Certificate System - PKI Server Framework
Group: System/Base

BuildArch: noarch

Provides: pki-deploy = %EVR
Provides: pki-setup = %EVR
Provides: pki-silent = %EVR

Obsoletes: pki-deploy < %EVR
Obsoletes: pki-setup < %EVR
Obsoletes: pki-silent < %EVR

Requires: net-tools
Requires: openldap-clients
Requires: openssl
Requires: pki-tools = %version-%release
Requires: pki-base = %version-%release
Requires: pki-base-java = %version-%release
Requires: policycoreutils
Requires: python-module-lxml
Requires: python-module-pyldap
Requires: python-module-selinux

Requires: selinux-policy-targeted
Obsoletes: pki-selinux

Requires: tomcat >= 8.0.32
Requires: tomcat-el-3.0-api
Requires: tomcat-jsp-2.3-api
Requires: tomcat-servlet-3.1-api
Requires: velocity
Requires: systemd
Requires: tomcatjss >= 7.2.4
Requires: libnuxwdog
Requires: libnuxwdog-java

%description -n pki-server
The PKI Server Framework is required by the following four PKI subsystems:

    the Certificate Authority (CA),
    the Data Recovery Manager (DRM),
    the Online Certificate Status Protocol (OCSP) Manager,
    the Token Key Service (TKS), and
    the Token Processing Service (TPS).

This package is a part of the PKI Core used by the Certificate System.
The package contains scripts to create and remove PKI subsystems.

%overview

%package -n pki-ca
Summary: Certificate System - Certificate Authority
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n pki-ca
The Certificate Authority (CA) is a required PKI subsystem which issues,
renews, revokes, and publishes certificates as well as compiling and
publishing Certificate Revocation Lists (CRLs).

The Certificate Authority can be configured as a self-signing Certificate
Authority, where it is the root CA, or it can act as a subordinate CA,
where it obtains its own signing certificate from a public CA.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n pki-kra
Summary: Certificate System - Data Recovery Manager
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n pki-kra
The Key Recovery Authority (KRA) is an optional PKI subsystem that can act
as a key archival facility.  When configured in conjunction with the
Certificate Authority (CA), the KRA stores private encryption keys as part of
the certificate enrollment process.  The key archival mechanism is triggered
when a user enrolls in the PKI and creates the certificate request.  Using the
Certificate Request Message Format (CRMF) request format, a request is
generated for the user's private encryption key.  This key is then stored in
the KRA which is configured to store keys in an encrypted format that can only
be decrypted by several agents requesting the key at one time, providing for
protection of the public encryption keys for the users in the PKI deployment.

Note that the KRA archives encryption keys; it does NOT archive signing keys,
since such archival would undermine non-repudiation properties of signing keys.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%overview

%package -n pki-ocsp
Summary: Certificate System - Online Certificate Status Protocol Manager
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release

%description -n pki-ocsp
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

%package -n pki-tks
Summary: Certificate System - Token Key Service
Group: System/Servers

BuildArch: noarch

Requires: pki-server = %version-%release
Requires: pki-symkey = %version-%release

%description -n pki-tks
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

%package -n pki-tps
Summary: Certificate System - Token Processing Service
Group: System/Servers

Provides: pki-tps-tomcat
Provides: pki-tps-client

Obsoletes: pki-tps-tomcat
Obsoletes: pki-tps-client

Requires: pki-server = %version-%release

# additional runtime requirements needed to run native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
Requires: libnss
Requires: nss-utils
Requires: openldap-clients
Requires: pki-symkey = %version-%release

%description -n pki-tps
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

%package -n pki-javadoc
Summary: Certificate System - PKI Framework Javadocs
Group: Documentation

BuildArch: noarch

Provides: pki-util-javadoc = %EVR
Provides: pki-java-tools-javadoc = %EVR
Provides: pki-common-javadoc = %EVR

Obsoletes: pki-util-javadoc < %EVR
Obsoletes: pki-java-tools-javadoc < %EVR
Obsoletes: pki-common-javadoc < %EVR

%description -n pki-javadoc
This documentation pertains exclusively to version %version of
the PKI Framework and Tools.

This package is a part of the PKI Core used by the Certificate System.

%overview

%prep
%setup
%patch0 -p1
# from sem@:
# At least one script required bash4.
# Just use sh4 for all scripts.
egrep -rl '^#!/bin/(sh|bash)' | \
	xargs sed -r -i 's;^#!/bin/(sh|bash)( -X)?;#!/bin/sh4;'

%build
%add_optflags -I/usr/include/apu-1
mkdir BUILD
pushd BUILD
%fedora_cmake -DVERSION=%version-%release \
	-DVAR_INSTALL_DIR:PATH=%_var \
	-DBUILD_PKI_CORE:BOOL=ON \
	-DJAVA_HOME=%java_home \
	-DJAVA_LIB_INSTALL_DIR=%_jnidir \
	-DSYSTEMD_LIB_INSTALL_DIR=%_unitdir \
	-DWITH_TOMCAT7:BOOL=OFF \
	-DJAXRS_API_JAR=%jaxrs_api_jar \
	-DRESTEASY_LIB=%resteasy_lib \
        ..
popd
%cmake_build VERBOSE=1 all

%check
%cmake_build VERBOSE=1 unit-test

# Scanning the python code with pylint.
python pylint-build-scan.py rpm --prefix %buildroot
if [ $? -ne 0 ]; then
    echo "pylint failed. RC: $?"
    exit 1
fi

python pylint-build-scan.py rpm --prefix %buildroot -- --py3k
if [ $? -ne 0 ]; then
    echo "pylint --py3k failed. RC: $?"
    exit 1
fi

flake8 --config tox.ini %buildroot
if [ $? -ne 0 ]; then
    echo "flake8 for Python 2 failed. RC: $?"
    exit 1
fi

python3-flake8 --config tox.ini %buildroot
if [ $? -ne 0 ]; then
    echo "flake8 for Python 3 failed. RC: $?"
    exit 1
fi

%install
%cmakeinstall_std
# Create symlinks for admin console (TPS does not use admin console)
for subsystem in ca kra ocsp tks; do
    mkdir -p %buildroot%_datadir/pki/$subsystem/webapps/$subsystem/admin
    ln -s %_datadir/pki/server/webapps/pki/admin/console %buildroot%_datadir/pki/$subsystem/webapps/$subsystem/admin
done

# Create compatibility symlink for DRMTool -> KRATool
ln -s %_bindir/KRATool %buildroot%_bindir/DRMTool
# Create compatibility symlink for DRMTool.cfg -> KRATool.cfg
ln -s %_datadir/pki/java-tools/KRATool.cfg %buildroot%_datadir/pki/java-tools/DRMTool.cfg
# Create compatibility symlink for DRMTool.1.gz -> KRATool.1.gz
ln -s %_man1dir/KRATool.1.xz %buildroot%_man1dir/DRMTool.1.xz

# Customize client library links in /usr/share/pki/lib
rm -f %buildroot%_datadir/pki/lib/scannotation.jar
rm -f %buildroot%_datadir/pki/lib/resteasy-jaxrs-api.jar
rm -f %buildroot%_datadir/pki/lib/resteasy-jaxrs-jandex.jar
ln -sf %jaxrs_api_jar %buildroot%_datadir/pki/lib/jboss-jaxrs-2.0-api.jar
ln -sf %_datadir/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/lib/jboss-logging.jar
ln -sf %_datadir/java/jboss-annotations-1.2-api/jboss-annotations-api_1.2_spec.jar %buildroot%_datadir/pki/lib/jboss-annotations-api_1.2_spec.jar

# Customize server library links in /usr/share/pki/server/common/lib
rm -f %buildroot%_datadir/pki/server/common/lib/scannotation.jar
rm -f %buildroot%_datadir/pki/server/common/lib/resteasy-jaxrs-api.jar
ln -sf %jaxrs_api_jar %buildroot%_datadir/pki/server/common/lib/jboss-jaxrs-2.0-api.jar
ln -sf %_datadir/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/server/common/lib/jboss-logging.jar
ln -sf %_datadir/java/jboss-annotations-1.2-api/jboss-annotations-api_1.2_spec.jar %buildroot%_datadir/pki/server/common/lib/jboss-annotations-api_1.2_spec.jar

rm -rf %buildroot%_datadir/pki/server/lib

mkdir -p %buildroot%_logdir/pki
mkdir -p %buildroot%_sharedstatedir/pki
# from sem@:
# This file should be sourced only
chmod -x %buildroot%_datadir/pki/scripts/operations
touch %buildroot%_sysconfdir/pki/pki.version
touch %buildroot%_logdir/pki/pki-upgrade-%version.log
touch %buildroot%_logdir/pki/pki-server-upgrade-%version.log

%pre -n pki-server
%define pki_username pkiuser
%define pki_groupname pkiuser
%define pki_homedir %_localstatedir/pki

/usr/sbin/groupadd -r -f %pki_groupname ||:
/usr/sbin/useradd -g %pki_groupname -c 'Certificate System' \
                  -d %pki_homedir -s /sbin/nologin -r %pki_username \
                  > /dev/null 2>&1 ||:

%post -n pki-base
if [ $1 -eq 1 ]
then
    # On RPM installation create system upgrade tracker
    echo "Configuration-Version: %version" > %_sysconfdir/pki/pki.version

else
    # On RPM upgrade run system upgrade
    echo "Upgrading PKI system configuration at `/bin/date`." >> %_logdir/pki/pki-upgrade-%version.log 2>&1
    /usr/sbin/pki-upgrade --silent >> %_logdir/pki/pki-upgrade-%version.log 2>&1
    echo >> %_logdir/pki/pki-upgrade-%version.log 2>&1
fi

%postun -n pki-base
if [ $1 -eq 0 ]
then
    # On RPM uninstallation remove system upgrade tracker
    rm -f %_sysconfdir/pki/pki.version
fi

%post -n pki-server
echo "Upgrading PKI server configuration at `/bin/date`." >> %_logdir/pki/pki-server-upgrade-%version.log 2>&1
 /usr/sbin/pki-server-upgrade --silent >> %_logdir/pki/pki-server-upgrade-%version.log 2>&1
echo >> %_logdir/pki/pki-server-upgrade-%version.log 2>&1

# Migrate Tomcat configuration
 /usr/sbin/pki-server migrate >> %_logdir/pki/pki-server-upgrade-%version.log 2>&1
echo >> %_logdir/pki/pki-server-upgrade-%version.log 2>&1

if [ "$1" == "2" ]
then
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
%doc %_datadir/doc/pki-base
%_datadir/pki/VERSION
%_datadir/pki/etc/
%_datadir/pki/upgrade/
%dir %_datadir/pki/examples
%dir %_datadir/pki/key
%_datadir/pki/key/templates
%config(noreplace) %_sysconfdir/pki/pki.conf
%ghost %_sysconfdir/pki/pki.version
%dir %_logdir/pki
%ghost %_logdir/pki/pki-upgrade-%version.log
%_sbindir/pki-upgrade
%_man1dir/pki-python-client.1.*
%_man5dir/pki-logging.5.*
%_man8dir/pki-upgrade.8.*

%files -n pki-base-java
%_datadir/pki/examples/java/
%_datadir/pki/lib/
%dir %_javadir/pki
%_javadir/pki/pki-cmsutil.jar
%_javadir/pki/pki-nsutil.jar
%_javadir/pki/pki-certsrv.jar

%files -n python-module-pki-base
%doc base/common/LICENSE
%doc base/common/LICENSE.LESSER
%exclude %python_sitelibdir_noarch/pki/server
%python_sitelibdir_noarch/pki

%files -n python3-module-pki-base
%doc base/common/LICENSE
%doc base/common/LICENSE.LESSER
%python3_sitelibdir_noarch/pki

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
%_bindir/CMCSharedToken
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
%_man1dir/AtoB.1.*
%_man1dir/AuditVerify.1.*
%_man1dir/BtoA.1.*
%_man1dir/CMCEnroll.1.*
%_man1dir/DRMTool.1.*
%_man1dir/KRATool.1.*
%_man1dir/PrettyPrintCert.1.*
%_man1dir/PrettyPrintCrl.1.*
%_man1dir/pki.1.*
%_man1dir/pki-audit.1.*
%_man1dir/pki-ca-kraconnector.1.*
%_man1dir/pki-ca-profile.1.*
%_man1dir/pki-cert.1.*
%_man1dir/pki-client.1.*
%_man1dir/pki-group.1.*
%_man1dir/pki-group-member.1.*
%_man1dir/pki-key.1.*
%_man1dir/pki-pkcs12-cert.1.*
%_man1dir/pki-pkcs12-key.1.*
%_man1dir/pki-pkcs12.1.*
%_man1dir/pki-securitydomain.1.*
%_man1dir/pki-tps-profile.1.*
%_man1dir/pki-user.1.*
%_man1dir/pki-user-cert.1.*
%_man1dir/pki-user-membership.1.*

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
%ghost %_logdir/pki/pki-server-upgrade-%version.log
%attr(644,root,root) %_unitdir/pki-tomcatd-nuxwdog@.service
%attr(644,root,root) %_unitdir/pki-tomcatd-nuxwdog.target
%_javadir/pki/pki-cms.jar
%_javadir/pki/pki-cmsbundle.jar
%_javadir/pki/pki-cmscore.jar
%_javadir/pki/pki-tomcat.jar
%dir %_sharedstatedir/pki
%_man1dir/pkidaemon.1.*
%_man5dir/pki_default.cfg.5.*
%_man5dir/pki-server-logging.5.*
%_man8dir/pki-server-upgrade.8.*
%_man8dir/pkidestroy.8.*
%_man8dir/pkispawn.8.*
%_man8dir/pki-server.8.*
%_man8dir/pki-server-instance.8.*
%_man8dir/pki-server-subsystem.8.*
%_man8dir/pki-server-nuxwdog.8.*
%_man8dir/pki-server-migrate.8.*
%_man8dir/pki-server-cert.8.*

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
%_man5dir/pki-tps-connector.5.*
%_man5dir/pki-tps-profile.5.*
%_man1dir/tpsclient.1.*
# files for native 'tpsclient'
# REMINDER:  Remove this comment once 'tpsclient' is rewritten as a Java app
%exclude %_initdir/pki-tpsd
%exclude %_unitdir/pki-tpsd.target
%exclude %_unitdir/pki-tpsd@.service
%exclude %_libdir/httpd/modules/mod_tokendb.so
%exclude %_libdir/httpd/modules/mod_tps.so
%exclude %_libdir/tps/libldapauth.so
%exclude %_datadir/pki/tps/cgi-bin/
%exclude %_datadir/pki/tps/docroot/
%exclude %_datadir/pki/tps/lib/
%exclude %_datadir/pki/tps/samples/
%exclude %_datadir/pki/tps/scripts/
%_bindir/tpsclient
%_libdir/tps/libtps.so
%_libdir/tps/libtokendb.so

%files -n pki-javadoc
%_javadocdir/pki-%version/

%changelog
* Mon Jan 15 2018 Stanislav Levin <slev@altlinux.org> 10.5.3-alt1%ubt
- 10.4.8 -> 10.5.3

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
