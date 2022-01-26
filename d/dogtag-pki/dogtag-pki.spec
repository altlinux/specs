%define _unpackaged_files_terminate_build 1

%def_with check
%def_without javadoc

%define nss_default_db_type sql

%define pki_username pkiuser
%define pki_groupname pkiuser
%define pki_homedir %_localstatedir/pki

%define java_home           %_jvmdir/jre
%define resteasy_lib        %_javadir/resteasy
%define jaxrs_api_jar       %_javadir/jboss-jaxrs-2.0-api.jar

# tomcatjss built with Java11
%define tomcatjss_version 8.0.0
# jss built with Java11
%define jss_version 5.0.0
# ldapjdk built with Java11
%define ldapjdk_version 5.0.0

# https://bugzilla.altlinux.org/40727
%define java_version 11

# first dogtag-pki renamed from pki-core
%define pki_rebranded_version 11.0.0-alt1

Name: dogtag-pki
Version: 11.0.3
Release: alt1

Summary: Dogtag PKI Certificate System
License: %gpl2only
Group: System/Servers
# Source-git: https://github.com/dogtagpki/pki
Url: http://www.dogtagpki.org

Source: %name-%version.tar
Patch: %name-%version-alt.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-java

BuildRequires: java-devel >= %java_version
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: sh4
BuildRequires: apache2-devel
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-httpclient
BuildRequires: apache-commons-net
BuildRequires: apache-commons-logging

BuildRequires: libnss-devel
BuildRequires: zlib-devel
BuildRequires: selinux-policy-alt

BuildRequires: jackson
BuildRequires: ldapjdk >= %ldapjdk_version
BuildRequires: resteasy
BuildRequires: tomcatjss >= %tomcatjss_version
BuildRequires: xalan-j2
BuildRequires: slf4j-jdk14
BuildRequires: junit

# build dependency to build man pages
BuildRequires: go-md2man

BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: /dev/shm
BuildRequires: ctest
BuildRequires: nss-utils
BuildRequires: openssl
BuildRequires: python3-module-flake8
BuildRequires: python3-module-ldap
BuildRequires: python3-module-lxml
BuildRequires: python3-module-pyflakes
BuildRequires: python3-module-pylint
BuildRequires: python3-module-selinux
BuildRequires: python3-module-tox
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

# mark upgrade code as Python3 code
%add_python3_path %_datadir/pki/upgrade/
%add_python3_path %_datadir/pki/server/upgrade/
%add_python3_compile_exclude %_datadir/pki/upgrade/
%add_python3_compile_exclude %_datadir/pki/server/upgrade/

#### Meta package ####
Requires: dogtag-pki-server-theme
Requires: python3-module-dogtag-pki
Requires: dogtag-pki-base-java
Requires: dogtag-pki-tools
Requires: dogtag-pki-server
Requires: dogtag-pki-acme
Requires: dogtag-pki-ca
Requires: dogtag-pki-kra
Requires: dogtag-pki-ocsp
Requires: dogtag-pki-tks
Requires: dogtag-pki-tps

# removed from Sisyphus
Obsoletes: idm-console-framework <= 1.2.0-alt1
Obsoletes: pki-console < 11.0.0
Obsoletes: dogtag-pki-console-theme < 11.0.0

Provides: pki-core = %EVR
Obsoletes: pki-core < %pki_rebranded_version

%description
Dogtag PKI is an enterprise software system designed
to manage enterprise Public Key Infrastructure deployments.

Dogtag PKI consists of the following components:

  * Automatic Certificate Management Environment (ACME) Responder
  * Certificate Authority (CA)
  * Key Recovery Authority (KRA)
  * Online Certificate Status Protocol (OCSP) Manager
  * Token Key Service (TKS)
  * Token Processing Service (TPS)


%package -n dogtag-pki-symkey
Summary: Dogtag PKI Symmetric Key Package
Group: System/Libraries
Requires: jss >= %jss_version
Requires: javapackages-tools
Provides: symkey = %EVR
Obsoletes: symkey < %EVR
Provides: pki-symkey = %EVR
Obsoletes: pki-symkey < %pki_rebranded_version

%description -n dogtag-pki-symkey
The Dogtag PKI Symmetric Key Java Package supplies various native
symmetric key operations to Java programs.

%package -n dogtag-pki-base
Summary: Dogtag PKI Base Package
Group: System/Base
Requires: python3-module-dogtag-pki
Provides: pki-common = %EVR
Provides: pki-util = %EVR
Obsoletes: pki-common < %EVR
Obsoletes: pki-util < %EVR
Provides: pki-base = %EVR
Obsoletes: pki-base < %pki_rebranded_version
Requires(post): python3-module-dogtag-pki

%description -n dogtag-pki-base
The Dogtag PKI Base Package contains the common and client libraries
and utilities written in Python.

%package -n dogtag-pki-base-java
Summary: Dogtag PKI Base Java Package
Group: System/Base
Requires: dogtag-pki-base
Requires: java >= %java_version
Requires: xalan-j2
Requires: xml-commons-resolver
Provides: pki-base-java = %EVR
Obsoletes: pki-base-java < %pki_rebranded_version

%description -n dogtag-pki-base-java
The Dogtag PKI Base Java Package contains the common and client
libraries and utilities written in Java.

%package -n python3-module-dogtag-pki
Summary: Dogtag PKI Python3 Package
Group: Development/Python3
Requires: dogtag-pki-base
Provides: python3-module-pki-base = %EVR
Obsoletes: python3-module-pki-base < %pki_rebranded_version

%description -n python3-module-dogtag-pki
This package contains Dogtag PKI client library for Python3.

%package -n dogtag-pki-tools
Summary: Dogtag PKI Tools Package
Group: System/Base
Requires: dogtag-pki-base-java
Requires: openldap-clients
Requires: nss-utils
Requires: p11-kit-trust
Provides: pki-native-tools = %EVR
Provides: pki-java-tools = %EVR
Obsoletes: pki-native-tools < %EVR
Obsoletes: pki-java-tools < %EVR
Provides: pki-tools = %EVR
Obsoletes: pki-tools < %pki_rebranded_version

%description -n dogtag-pki-tools
This package contains Dogtag PKI executables that can be used to help make
Certificate System into a more complete and robust PKI solution.

%package -n dogtag-pki-server
Summary: Dogtag PKI Server Package
Group: System/Base
Requires: dogtag-pki-symkey
Requires: dogtag-pki-tools
Requires: openssl
# https://bugzilla.altlinux.org/40819
Requires: tomcat >= 1:9.0.50-alt2_2jpp11
Requires: tomcatjss >= %tomcatjss_version

Provides: pki-deploy = %EVR
Provides: pki-setup = %EVR
Provides: pki-silent = %EVR

Obsoletes: pki-deploy < %EVR
Obsoletes: pki-setup < %EVR
Obsoletes: pki-silent < %EVR
Provides: pki-server = %EVR
Obsoletes: pki-server < %pki_rebranded_version

# https://pagure.io/freeipa/issue/7742
Conflicts: freeipa-server < 4.7.1

%description -n dogtag-pki-server
The Dogtag PKI Server Package contains libraries and utilities needed by other
Dogtag PKI subsystems.

%package -n dogtag-pki-acme
Summary: Dogtag PKI ACME Package
Group: System/Base
Requires: dogtag-pki-server
Provides: pki-acme = %EVR
Obsoletes: pki-acme < %pki_rebranded_version

%description -n dogtag-pki-acme
The Dogtag PKI ACME responder is a service that provides an automatic
certificate management via ACME v2 protocol defined in RFC 8555.

%package -n dogtag-pki-ca
Summary: Dogtag PKI CA Package
Group: System/Servers
Requires: dogtag-pki-server
Provides: pki-ca = %EVR
Obsoletes: pki-ca < %pki_rebranded_version

%description -n dogtag-pki-ca
The Certificate Authority (CA) is a required Dogtag PKI subsystem which issues,
renews, revokes, and publishes certificates as well as compiling and
publishing Certificate Revocation Lists (CRLs).

The Certificate Authority can be configured as a self-signing Certificate
Authority, where it is the root CA, or it can act as a subordinate CA,
where it obtains its own signing certificate from a public CA.

%package -n dogtag-pki-kra
Summary: Dogtag PKI KRA Package
Group: System/Servers
Requires: dogtag-pki-server
Provides: pki-kra = %EVR
Obsoletes: pki-kra < %pki_rebranded_version

%description -n dogtag-pki-kra
The Key Recovery Authority (KRA) is an optional Dogtag PKI subsystem that can
act as a key archival facility.  When configured in conjunction with the
Certificate Authority (CA), the KRA stores private encryption keys as part of
the certificate enrollment process.  The key archival mechanism is triggered
when a user enrolls in the Dogtag PKI and creates the certificate request.
Using the Certificate Request Message Format (CRMF) request format, a request
is generated for the user's private encryption key.  This key is then stored in
the KRA which is configured to store keys in an encrypted format that can only
be decrypted by several agents requesting the key at one time, providing for
protection of the public encryption keys for the users in the Dogtag PKI
deployment.

Note that the KRA archives encryption keys; it does NOT archive signing keys,
since such archival would undermine non-repudiation properties of signing keys.

%package -n dogtag-pki-ocsp
Summary: Dogtag PKI OCSP Package
Group: System/Servers
Requires: dogtag-pki-server
Provides: pki-ocsp = %EVR
Obsoletes: pki-ocsp < %pki_rebranded_version

%description -n dogtag-pki-ocsp
The Online Certificate Status Protocol (OCSP) Manager is an optional Dogtag PKI
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

%package -n dogtag-pki-tks
Summary: Dogtag PKI TKS Package
Group: System/Servers
Requires: dogtag-pki-server
Provides: pki-tks = %EVR
Obsoletes: pki-tks < %pki_rebranded_version

%description -n dogtag-pki-tks
The Token Key Service (TKS) is an optional Dogtag PKI subsystem that manages
the master key(s) and the transport key(s) required to generate and distribute
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

%package -n dogtag-pki-tps
Summary: Dogtag PKI TPS Package
Group: System/Servers
Requires: dogtag-pki-server
Provides: pki-tps = %EVR
Obsoletes: pki-tps < %pki_rebranded_version

Provides: pki-tps-tomcat = %EVR
Provides: pki-tps-client = %EVR
Obsoletes: pki-tps-tomcat < %EVR
Obsoletes: pki-tps-client < %EVR

%description -n dogtag-pki-tps
The Token Processing System (TPS) is an optional Dogtag PKI subsystem that acts
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

%if_with javadoc
%package -n dogtag-pki-javadoc
Summary: Dogtag PKI Javadoc Package
Group: Documentation
Requires: javapackages-tools
Provides: pki-javadoc = %EVR
Obsoletes: pki-javadoc < %pki_rebranded_version

Provides: pki-util-javadoc = %EVR
Provides: pki-java-tools-javadoc = %EVR
Provides: pki-common-javadoc = %EVR
Obsoletes: pki-util-javadoc < %EVR
Obsoletes: pki-java-tools-javadoc < %EVR
Obsoletes: pki-common-javadoc < %EVR

%description -n dogtag-pki-javadoc
This package contains Dogtag PKI API documentation.
%endif

%package -n dogtag-pki-healthcheck
Summary: Dogtag PKI Healthcheck
Group: System/Servers
Provides: pki-healthcheck = %EVR
Obsoletes: pki-healthcheck < %pki_rebranded_version

%description -n dogtag-pki-healthcheck
The healthcheck tool is intended for executing health checks against Dogtag
PKI. This is the plugin for freeipa-healthcheck.

%package -n dogtag-pki-server-theme
Summary: Dogtag PKI Server Theme Package
Group: Networking/Other
Provides: pki-server-theme = %EVR
Obsoletes: pki-server-theme < %EVR

%description -n dogtag-pki-server-theme
This Dogtag PKI Server Theme Package contains textual and graphical user
interface for Dogtag PKI Server.

%prep
%setup
%patch -p1
# change port from 8080 to 8090
# Port 8080 is used by alterator-ahttpd-server
grep -rl 8080 | xargs sed -i 's/\(\W\|^\)8080\(\W\|$\)/\18090\2/g'
# change apache2 alt paths
grep -rPl '#include \x22httpd/' | \
xargs sed -i 's/#include \x22httpd\//#include \x22apache2\//g'

# replace python2 shebangs with python3 to fix unmets
grep -rlsm1 '^#!/usr/bin/python[[:space:]]*$' | \
xargs sed -i '1s|^#!/usr/bin/python[[:space:]]*$|#!/usr/bin/python3|'

%build
# get Java <major>.<minor> version number
set -o pipefail
java_version="$(%java_home/bin/java -XshowSettings:properties -version  2>&1 | \
    sed -n 's/ *java.version *= *\([0-9]\+\.[0-9]\+\).*/\1/p')"
# if <major> == 1, get <minor> version number
# otherwise get <major> version number
java_version="$(echo $java_version | sed -e 's/^1\.//' -e 's/\..*$//')"

app_server=tomcat-9.0
set +o pipefail

%add_optflags -I/usr/include/apu-1
%cmake \
    --no-warn-unused-cli \
    -DVERSION=%version-%release \
    -DVAR_INSTALL_DIR:PATH=%_var \
    -DP11_KIT_TRUST=%_libdir/libnssckbi.so \
    -DJAVA_VERSION=$java_version \
    -DJAVA_HOME=%java_home \
    -DJAVA_LIB_INSTALL_DIR=%_jnidir \
    -DSYSTEMD_LIB_INSTALL_DIR=%_unitdir \
    -DAPP_SERVER=$app_server \
    -DJAXRS_API_JAR=%jaxrs_api_jar \
    -DRESTEASY_LIB=%resteasy_lib \
    -DNSS_DEFAULT_DB_TYPE=%nss_default_db_type \
    -DBUILD_PKI_CORE:BOOL=ON \
    -DPYTHON_EXECUTABLE=%__python3 \
%if_with check
    -DWITH_TEST:BOOL=ON \
%else
    -DWITH_TEST:BOOL=OFF \
%endif
%if_with javadoc
    -DWITH_JAVADOC:BOOL=ON \
%else
    -DWITH_JAVADOC:BOOL=OFF \
%endif
    -DTHEME=dogtag \
     ..

%cmake_build -t all

%install
%cmakeinstall_std
# Customize client library links in /usr/share/pki/lib
ln -sf %_datadir/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/lib/jboss-logging.jar
ln -sf %_datadir/java/jakarta-annotations/jakarta.annotation-api.jar %buildroot%_datadir/pki/lib/jakarta.annotation-api.jar

# Customize server library links in /usr/share/pki/server/common/lib
ln -sf %jaxrs_api_jar %buildroot%_datadir/pki/server/common/lib/jboss-jaxrs-2.0-api.jar
ln -sf %_datadir/java/jboss-logging/jboss-logging.jar %buildroot%_datadir/pki/server/common/lib/jboss-logging.jar
ln -sf %_datadir/java/jakarta-annotations/jakarta.annotation-api.jar %buildroot%_datadir/pki/server/common/lib/jakarta.annotation-api.jar

# from sem@:
# This file should be sourced only
chmod -x %buildroot%_datadir/pki/scripts/operations
touch %buildroot%_sysconfdir/pki/pki.version
touch %buildroot%_logdir/pki/pki-upgrade-%version.log
touch %buildroot%_logdir/pki/pki-server-upgrade-%version.log
mkdir %buildroot%_logdir/pki/server
mkdir %buildroot%_logdir/pki/server/upgrade

ln -sf tps/libtps.so %buildroot%_libdir/libtps.so
ln -sf tps/libtokendb.so %buildroot%_libdir/libtokendb.so

# don't package tests
rm -r %buildroot%_datadir/pki/tests/

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=lint3,pep8py3,py%{python_version_nodots python3}
ln -sr ./tests/tox.ini ./
tox.py3 --sitepackages -p auto -o -vvr --no-deps --console-scripts -s false
%cmake_build -t test

%pre -n dogtag-pki-server
%_sbindir/groupadd -r -f %pki_groupname ||:
%_sbindir/useradd -g %pki_groupname -c 'Certificate System' \
                  -d %pki_homedir -s /sbin/nologin -r %pki_username \
                  > /dev/null 2>&1 ||:

%post -n dogtag-pki-base
if [ $1 -eq 1 ]
then
    # On RPM installation create system upgrade tracker
    echo "Configuration-Version: %version" > %_sysconfdir/pki/pki.version

else
    # On RPM upgrade run system upgrade
    echo "pki-base: Upgrading PKI system configuration"
    echo "Upgrading PKI system configuration at `/bin/date`." >> %_logdir/pki/pki-upgrade-%version.log 2>&1
    %_sbindir/pki-upgrade -v >> %_logdir/pki/pki-upgrade-%version.log 2>&1
    echo >> %_logdir/pki/pki-upgrade-%version.log 2>&1
    echo "pki-base: PKI system upgrade status:"
    %_sbindir/pki-upgrade --status 2>&1 | sed 's/^/pki-base: /'
fi

%postun -n dogtag-pki-base
if [ $1 -eq 0 ]
then
    # On RPM uninstallation remove system upgrade tracker
    rm -f %_sysconfdir/pki/pki.version
fi

%post -n dogtag-pki-server
# upgrade
if [ "$1" -ge 2 ]
then
    # CVE-2021-3551: Remove world access from existing installation logs
    find %_logdir/pki -maxdepth 1 -type f -exec chmod o-rwx {} \;

    # pki-tomcat is the hardcoded instance name used by ipa
    # https://pagure.io/dogtagpki/issue/3195
    chown -R -P %pki_username:%pki_groupname \
        %_sysconfdir/pki/pki-tomcat/alias >/dev/null 2>&1 ||:

    systemctl daemon-reload ||:
fi

%files

%files -n dogtag-pki-symkey
%_jnidir/symkey.jar
%_libdir/symkey/

%files -n dogtag-pki-base
%doc %_datadir/doc/pki-base/html
%doc %_datadir/pki/server/docs
%dir %_datadir/pki/etc
%dir %_datadir/pki/lib
%dir %_datadir/pki/scripts
%dir %_datadir/pki/examples
%dir %_logdir/pki
%_datadir/pki/VERSION
%_datadir/pki/pom.xml
%_datadir/pki/etc/pki.conf
%_datadir/pki/etc/logging.properties
%_datadir/pki/scripts/config
%_datadir/pki/upgrade/
%_datadir/pki/key/
%config(noreplace) %_sysconfdir/pki/pki.conf
%ghost %_sysconfdir/pki/pki.version
%ghost %_logdir/pki/pki-upgrade-%version.log
%_sbindir/pki-upgrade
%_man1dir/pki-python-client.1.*
%_man5dir/pki-logging.5.*
%_man8dir/pki-upgrade.8.*

%files -n dogtag-pki-base-java
%_datadir/pki/examples/java/
%_datadir/pki/lib/*.jar
%dir %_javadir/pki
%_javadir/pki/pki-cmsutil.jar
%_javadir/pki/pki-certsrv.jar

%files -n python3-module-dogtag-pki
%exclude %python3_sitelibdir/pki/server/
%python3_sitelibdir/pki/

%files -n dogtag-pki-tools
%doc base/tools/doc/README
%_bindir/p7tool
%_bindir/p12tool
%_bindir/pistool
%_bindir/pki
%_bindir/revoker
%_bindir/setpin
%_bindir/sslget
%_bindir/tkstool
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
%_bindir/PKICertImport
%_bindir/PrettyPrintCert
%_bindir/PrettyPrintCrl
%_bindir/TokenInfo
%_javadir/pki/pki-tools.jar
%_datadir/pki/tools/
%_datadir/pki/lib/p11-kit-trust.so
%_man1dir/AtoB.1.*
%_man1dir/AuditVerify.1.*
%_man1dir/BtoA.1.*
%_man1dir/CMCEnroll.1.*
%_man1dir/CMCRequest.1.*
%_man1dir/CMCSharedToken.1.*
%_man1dir/CMCResponse.1.*
%_man1dir/DRMTool.1.*
%_man1dir/KRATool.1.*
%_man1dir/PrettyPrintCert.1.*
%_man1dir/PrettyPrintCrl.1.*
%_man1dir/pki.1.*
%_man1dir/pki-audit.1.*
%_man1dir/pki-ca-cert.1.*
%_man1dir/pki-ca-kraconnector.1.*
%_man1dir/pki-ca-profile.1.*
%_man1dir/pki-client.1.*
%_man1dir/pki-group.1.*
%_man1dir/pki-group-member.1.*
%_man1dir/pki-kra-key.1.*
%_man1dir/pki-pkcs12-cert.1.*
%_man1dir/pki-pkcs12-key.1.*
%_man1dir/pki-pkcs12.1.*
%_man1dir/pki-securitydomain.1.*
%_man1dir/pki-tps-profile.1.*
%_man1dir/pki-user.1.*
%_man1dir/pki-user-cert.1.*
%_man1dir/pki-user-membership.1.*
%_man1dir/PKCS10Client.1.*
%_man1dir/PKICertImport.1.*

%files -n dogtag-pki-server
%doc base/common/THIRD_PARTY_LICENSES
%doc base/server/LICENSE
%doc base/server/README
%dir %_sysconfdir/sysconfig/pki
%dir %_sysconfdir/sysconfig/pki/tomcat
%_sbindir/pkispawn
%_sbindir/pkidestroy
%_sbindir/pki-server
%_sbindir/pki-server-upgrade
%python3_sitelibdir/pki/server/
%exclude %python3_sitelibdir/pki/server/healthcheck/

%_datadir/pki/etc/tomcat.conf
%dir %_datadir/pki/deployment
%_datadir/pki/deployment/config/
%_datadir/pki/scripts/operations
%_bindir/pkidaemon
%_bindir/pki-server-nuxwdog
%dir %_sysconfdir/systemd/system/pki-tomcatd.target.wants
%_unitdir/pki-tomcatd@.service
%_unitdir/pki-tomcatd.target
%dir %_sysconfdir/systemd/system/pki-tomcatd-nuxwdog.target.wants
%ghost %_logdir/pki/pki-server-upgrade-%version.log
%ghost %_logdir/pki/server/
%_unitdir/pki-tomcatd-nuxwdog@.service
%_unitdir/pki-tomcatd-nuxwdog.target
%_javadir/pki/pki-cms.jar
%_javadir/pki/pki-cmsbundle.jar
%_javadir/pki/pki-tomcat.jar
%dir %_sharedstatedir/pki
%_man1dir/pkidaemon.1.*
%_man5dir/pki_default.cfg.5.*
%_man5dir/pki-server-logging.5.*
%_man8dir/pki-server-upgrade.8.*
%_man8dir/pkidestroy.8.*
%_man8dir/pkispawn.8.*
%_man8dir/pki-server.8.*
%_man8dir/pki-server-acme.8.*
%_man8dir/pki-server-instance.8.*
%_man8dir/pki-server-subsystem.8.*
%_man8dir/pki-server-nuxwdog.8.*
%_man8dir/pki-server-migrate.8.*
%_man8dir/pki-server-cert.8.*
%_man8dir/pki-server-ca.8.*
%_man8dir/pki-server-kra.8.*
%_man8dir/pki-server-ocsp.8.*
%_man8dir/pki-server-tks.8.*
%_man8dir/pki-server-tps.8.*

%_datadir/pki/setup/
%dir %_datadir/pki/server
%_datadir/pki/server/common/
%_datadir/pki/server/conf/
%_datadir/pki/server/etc/
%_datadir/pki/server/lib/
%_datadir/pki/server/upgrade/
%_datadir/pki/server/certs/
%_datadir/pki/server/examples/

%files -n dogtag-pki-acme
%_javadir/pki/pki-acme.jar
%_datadir/pki/acme/

%files -n dogtag-pki-ca
%_javadir/pki/pki-ca.jar
%_datadir/pki/ca/

%files -n dogtag-pki-kra
%_javadir/pki/pki-kra.jar
%_datadir/pki/kra/

%files -n dogtag-pki-ocsp
%_javadir/pki/pki-ocsp.jar
%_datadir/pki/ocsp/

%files -n dogtag-pki-tks
%_javadir/pki/pki-tks.jar
%_datadir/pki/tks/

%files -n dogtag-pki-tps
%_javadir/pki/pki-tps.jar
%_datadir/pki/tps/
%_man5dir/pki-tps-connector.5.*
%_man5dir/pki-tps-profile.5.*
%_man1dir/tpsclient.1.*
%_bindir/tpsclient
%_libdir/tps/libtps.so
%_libdir/tps/libtokendb.so
%_libdir/libtps.so
%_libdir/libtokendb.so

%if_with javadoc
%files -n dogtag-pki-javadoc
%_javadocdir/pki-%version/
%endif

%files -n dogtag-pki-healthcheck
%_sbindir/pki-healthcheck
%python3_sitelibdir/pki/server/healthcheck/
%python3_sitelibdir/pkihealthcheck-*.egg-info/
%config(noreplace) %_sysconfdir/pki/healthcheck.conf
%_man5dir/pki_healthcheck.conf.*
%_man8dir/pki-healthcheck.8.*

%files -n dogtag-pki-server-theme
%_datadir/pki/common-ui/
%_datadir/pki/CS_SERVER_VERSION
%dir %_datadir/pki/server
%dir %_datadir/pki/server/webapps
%dir %_datadir/pki/server/webapps/pki
%_datadir/pki/server/webapps/ROOT/
%_datadir/pki/server/webapps/pki/admin/
%_datadir/pki/server/webapps/pki/ca/
%_datadir/pki/server/webapps/pki/css/
%_datadir/pki/server/webapps/pki/esc/
%_datadir/pki/server/webapps/pki/fonts/
%_datadir/pki/server/webapps/pki/images/
%_datadir/pki/server/webapps/pki/js/
%_datadir/pki/server/webapps/pki/index.jsp
%_datadir/pki/server/webapps/pki/kra/
%_datadir/pki/server/webapps/pki/ocsp/
%_datadir/pki/server/webapps/pki/pki.properties/
%_datadir/pki/server/webapps/pki/tks/
%_datadir/pki/server/webapps/pki/ui/
%_datadir/pki/server/webapps/pki/WEB-INF/

%changelog
* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 11.0.3-alt1
- 11.0.2 -> 11.0.3.

* Wed Dec 15 2021 Stanislav Levin <slev@altlinux.org> 11.0.2-alt1
- 11.0.0 -> 11.0.2.

* Thu Dec 02 2021 Stanislav Levin <slev@altlinux.org> 11.0.0-alt2
- Cleaned up buildtime dependency on no longer shipped idm-console.

* Thu Nov 25 2021 Stanislav Levin <slev@altlinux.org> 11.0.0-alt1
- 10.10.6 -> 11.0.0.

* Wed Jun 23 2021 Stanislav Levin <slev@altlinux.org> 10.10.6-alt2
- Made python-nss really optional.

* Fri Jun 18 2021 Stanislav Levin <slev@altlinux.org> 10.10.6-alt1
- 10.10.5 -> 10.10.6 (fixes: CVE-2021-3551).

* Fri Jun 11 2021 Stanislav Levin <slev@altlinux.org> 10.10.5-alt3
- Built with Java11.

* Mon May 31 2021 Stanislav Levin <slev@altlinux.org> 10.10.5-alt2
- Fixed FTBFS(new CMake policy).

* Wed Mar 03 2021 Stanislav Levin <slev@altlinux.org> 10.10.5-alt1
- 10.10.4 -> 10.10.5.

* Mon Feb 15 2021 Stanislav Levin <slev@altlinux.org> 10.10.4-alt1
- 10.10.3 -> 10.10.4.

* Fri Feb 05 2021 Stanislav Levin <slev@altlinux.org> 10.10.3-alt1
- 10.10.0 -> 10.10.3.

* Tue Nov 03 2020 Stanislav Levin <slev@altlinux.org> 10.10.0-alt1
- 10.9.4 -> 10.10.0.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 10.9.4-alt2
- Fixed FTBFS (new flake8 and pylint).

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 10.9.4-alt1
- 10.7.4 -> 10.9.4.

* Tue Aug 04 2020 Stanislav Levin <slev@altlinux.org> 10.7.4-alt4
- Fixed FTBFS(new pylint 2.5.3).
- Fixed group ownership of pki nssdb.

* Fri Jul 17 2020 Stanislav Levin <slev@altlinux.org> 10.7.4-alt3
- Removed Conflict against strongswan.

* Fri Nov 08 2019 Stanislav Levin <slev@altlinux.org> 10.7.4-alt2
- Fixed build against Pylint-2.4.2.

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 10.7.4-alt1
- 10.7.3 -> 10.7.4.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 10.7.3-alt1
- 10.7.0 -> 10.7.3.

* Mon Aug 05 2019 Stanislav Levin <slev@altlinux.org> 10.7.0-alt3
- Fixed upgrade 10.2.x => 10.7.x.

* Thu Jul 11 2019 Stanislav Levin <slev@altlinux.org> 10.7.0-alt2
- Pinned supported Java.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 10.7.0-alt1
- 10.6.9 -> 10.7.0.

* Tue Feb 05 2019 Stanislav Levin <slev@altlinux.org> 10.6.9-alt3
- Added BR on "certutil" (needed for testing).

* Thu Jan 31 2019 Stanislav Levin <slev@altlinux.org> 10.6.9-alt2
- Fixed name of flake8 executable.

* Mon Jan 21 2019 Stanislav Levin <slev@altlinux.org> 10.6.9-alt1
- 10.6.7 -> 10.6.9.
- Fixed pylint, flake8 errors (closes: #35938).

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 10.6.7-alt1
- 10.6.6 -> 10.6.7.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 10.6.6-alt1
- 10.6.1 -> 10.6.6.

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 10.6.1-alt2
- removed Requires: tomcat-servlet-3.1-api (useless)

* Thu May 24 2018 Stanislav Levin <slev@altlinux.org> 10.6.1-alt1
- 10.5.6 -> 10.6.1

* Tue Feb 20 2018 Stanislav Levin <slev@altlinux.org> 10.5.6-alt1
- 10.5.5 -> 10.5.6

* Fri Feb 16 2018 Stanislav Levin <slev@altlinux.org> 10.5.5-alt1
- 10.5.3 -> 10.5.5

* Mon Jan 15 2018 Stanislav Levin <slev@altlinux.org> 10.5.3-alt1
- 10.4.8 -> 10.5.3

* Fri Jan 12 2018 Stanislav Levin <slev@altlinux.org> 10.4.8-alt5
- Fix package build broken due to new ca-certificates system
  Directory /etc/pki and /usr/share/pki belong to
  filesystem package

* Mon Oct 02 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt4
- Fix Java CLASSPATH on RPM package upgrade

* Fri Sep 29 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt3
- Fix Java CLASSPATH by Evgeny Sinelnikov <sin@altlinux.org>
- Clean up spec

* Mon Sep 25 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt2
- Fix version compare for sphinx python module

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt6_19jpp8
- added Conflicts: strongswan (closes: #33037)

* Thu Sep 21 2017 Stanislav Levin <slev@altlinux.org> 10.4.8-alt1
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
