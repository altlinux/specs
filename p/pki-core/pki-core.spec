# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat rpm-macros-java
BuildRequires: gcc-c++ java-devel-default perl(APR/Const.pm) perl(CGI.pm) perl(CGI/Carp.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(LWP/UserAgent.pm) perl(MIME/Base64.pm) perl(ModPerl/Registry.pm) perl(Mozilla/LDAP/Conn.pm) perl(Mozilla/LDAP/LDIF.pm) perl(Parse/RecDescent.pm) perl(URI/Escape.pm) perl(URI/URL.pm) perl(XML/Simple.pm) perl(subs.pm) python-devel
# END SourceDeps(oneline)
BuildRequires: sh4
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Python
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

# Tomcat
%if 0%{?fedora} >= 23
%define with_tomcat7 0
%define with_tomcat8 1
%else
%define with_tomcat7 1
%define with_tomcat8 0
%endif

# RESTEasy
%if 0%{?rhel}
%define resteasy_lib /usr/share/java/resteasy-base
%else
%define resteasy_lib /usr/share/java/resteasy
%endif

# Dogtag
%bcond_without    server
%bcond_without    javadoc

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

Name:             pki-core
Version:          10.2.6
Release:          alt3_19jpp8
Summary:          Certificate System - PKI Core Components
URL:              http://pki.fedoraproject.org/
License:          GPLv2
Group:            System/Servers


BuildRequires: ctest cmake
BuildRequires:    zip
BuildRequires:    ldapjdk
BuildRequires:    apache-commons-cli
BuildRequires:    apache-commons-codec
BuildRequires:    apache-commons-io
BuildRequires:    apache-commons-lang
BuildRequires:    jakarta-commons-httpclient
BuildRequires:    libnspr-devel
BuildRequires: libnss-devel libnss-devel-static

%if 0%{?rhel}
BuildRequires:    libnuxwdog-java >= 1.0.1
%else
BuildRequires:    libnuxwdog-java >= 1.0.3
%endif

BuildRequires:    libldap-devel
BuildRequires:    pkg-config
BuildRequires:    policycoreutils
BuildRequires:    python-module-lxml
BuildRequires:    python-module-sphinx
BuildRequires:    velocity
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2

%if 0%{?rhel}
# 'resteasy-base' is a subset of the complete set of
# 'resteasy' packages and consists of what is needed to
# support the PKI Restful interface on RHEL platforms
BuildRequires:    resteasy-base-atom-provider >= 3.0.6
BuildRequires:    resteasy-base-client >= 3.0.6
BuildRequires:    resteasy-base-jaxb-provider >= 3.0.6
BuildRequires:    resteasy-base-jaxrs >= 3.0.6
BuildRequires:    resteasy-base-jaxrs-api >= 3.0.6
BuildRequires:    resteasy-base-jackson-provider >= 3.0.6
%else
%if 0%{?fedora} >= 22
# Starting from Fedora 22, resteasy packages were split into
# subpackages.
BuildRequires:    resteasy-atom-provider >= 3.0.6
BuildRequires:    resteasy-client >= 3.0.6
BuildRequires:    resteasy-jaxb-provider >= 3.0.6
BuildRequires:    resteasy-core >= 3.0.6
BuildRequires:    resteasy-jaxrs-api >= 3.0.6
BuildRequires:    resteasy-jackson-provider >= 3.0.6
%else
BuildRequires:    resteasy >= 3.0.6
%endif
%endif

%if ! 0%{?rhel}
BuildRequires:    pylint
%endif

BuildRequires:    python-module-nss
BuildRequires:    python-module-requests
BuildRequires:    python-module-selinux
BuildRequires: policycoreutils python-module-sepolgen
%if 0%{?fedora} >= 23
BuildRequires: policycoreutils policycoreutils-sandbox
%endif
BuildRequires:    python-module-pyldap
BuildRequires:    junit
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    jss >= 4.2.6

%if 0%{?rhel}
BuildRequires:    tomcatjss >= 7.1.0
%else
%if 0%{?fedora} >= 23
BuildRequires:    tomcatjss >= 7.1.3
%else
%if 0%{?fedora} == 22
BuildRequires:    tomcatjss >= 7.1.2
%else
BuildRequires:    tomcatjss >= 7.1.2
%endif
%endif
%endif


# additional build requirements needed to build native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
BuildRequires:    libapr1-devel
BuildRequires:    libaprutil1-devel
BuildRequires:    libsasl2-devel
BuildRequires:    apache2-devel >= 2.4.2
BuildRequires: libpcre-devel libpcrecpp-devel
BuildRequires:    python
BuildRequires: journalctl libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-services systemd-utils
BuildRequires:    libsvrcore-devel
BuildRequires:    zlib
BuildRequires:    zlib-devel

%if 0%{?rhel}
# NOTE:  In the future, as a part of its path, this URL will contain a release
#        directory which consists of the fixed number of the upstream release
#        upon which this tarball was originally based.
Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{release}/rhel/%{name}-%{version}%{?prerel}.tar.gz
%else
Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{release}/%{name}-%{version}%{?prerel}.tar.gz
%endif

## pki-core-10.2.6-2
Patch1:           pki-core-Fixed-ObjectNotFoundException-in-PKCS12Export.patch
## pki-core-10.2.6-3
## pki-core-10.2.6-4
Patch2:           pki-core-Do-Not-Create-Replication-Agreements.patch
Patch3:           pki-core-Remove-Noise-File-Generation.patch
Patch4:           pki-core-Fix-Pin-Reset-Operation.patch
Patch5:           pki-core-Externalreg-Support-Multiple-KeySets.patch
Patch6:           pki-core-Add-Externalreg-revokeCert-Parameter.patch
Patch7:           pki-core-Fix-ECC-Admin-Cert-Creation.patch
## pki-core-10.2.6-5
Patch8:           pki-core-Fix-Firefox-Warning.patch
Patch9:           pki-core-Add-Reindex-Data-During-Cloning-No-Replication.patch
Patch10:          pki-core-Fix-Base-64-Encoded-Cert-Displays.patch
Patch11:          pki-core-Fix-Missing-Cert-Request-Hostname-Address.patch
Patch12:          pki-core-Add-Bound-Bind-Connection-To-Dirauth-Plugin.patch
Patch13:          pki-core-Remove-Inaccessible-URLs-From-Pkidaemon.patch
Patch14:          pki-core-Temporarily-Silence-InsecureRequestWarning.patch
## pki-core-10.2.6-6
Patch15:          pki-core-Separate-range-and-cert-status-threads.patch
Patch16:          pki-core-Fix-admin-profiles-for-ECC-cert-reqs.patch
Patch17:          pki-core-Fix-missing-query-parms-in-ListCerts-page.patch
Patch18:          pki-core-Fix-SerialNumberUpdateTask-conditional.patch
Patch19:          pki-core-Remove-PortalEnroll-plugin.patch
Patch20:          pki-core-Fix-setpin-utility.patch
Patch21:          pki-core-Fix-weak-HTTPS-TLS-ciphers.patch
## pki-core-10.2.6-7
Patch22:          pki-core-Minor-setpin-fix.patch
Patch23:          pki-core-Fix-TLS-ciphers-on-non-CA-HSMs.patch
Patch24:          pki-core-Issue-IE-11-warning.patch
## pki-core-10.2.6-8
Patch25:          pki-core-User-Membership-Man-Page.patch
Patch26:          pki-core-Fix-SC650-Token-Format-Enroll.patch
Patch27:          pki-core-Support-Multiple-Keysets.patch
## pki-core-10.2.6-9
Patch28:          pki-core-Added-CLI-to-update-cert-data-and-request-in-CS_cfg.patch
Patch29:          pki-core-Fixed-pkidbuser-group-memberships.patch
Patch30:          pki-core-Added-support-for-secure-database-connection-in-CLI.patch
Patch31:          pki-core-KRA-via-CLI-should-honor-encrypt-decrypt-flags.patch
Patch32:          pki-core-Relocated-legacy-cert-enrollment-methods.patch
Patch33:          pki-core-Refactored-certificate-processors.patch
Patch34:          pki-core-Added-support-for-directory-authenticated-profiles.patch
Patch35:          pki-core-Added-default-subject-DN-for-pki-client-cert-request.patch
Patch36:          pki-core-HSM-failover-support.patch
## pki-core-10.2.6-10
Patch37:          pki-core-Fixed-user-search-in-PasswdUserDBAuthentication.patch
## pki-core-10.2.6-11
Patch38:          pki-core-Removed-unused-WizardServlet.patch
Patch39:          pki-core-Replaced-legacy-HttpClient.patch
## pki-core-10.2.6-12
Patch40:          pki-core-Added-automatic-Tomcat-migration.patch
## pki-core-10.2.6-13
Patch41:          pki-core-sslget-must-set-host-HTTP-header.patch
## pki-core-10.2.6-14
Patch42:          pki-core-Profile-creation-LDAPProfileSubsystem-can-fail-due-to-race-condition.patch
Patch43:          pki-core-Block-startup-until-initial-profile-load-completed.patch
## pki-core-10.2.6-15
Patch44:          pki-core-Added-support-for-existing-CA-case-CS9.patch
Patch45:          pki-core-Fixed-mismatching-certificate-validity-calculation.patch
Patch46:          pki-core-Fix-to-determine-supported-javadoc-options.patch
## pki-core-10.2.6-16
Patch47:          pki-core-Modify-dnsdomainname-test-in-pkispawn.patch
Patch48:          pki-core-Build-with-Tomcat-8.0.32.patch
## pki-core-10.2.6-17
Patch49:          pki-core-Added-support-for-cloning-3rd-party-CA-certificates.patch
Patch50:          pki-core-Fixed-certificate-chain-import-problem.patch
Patch51:          pki-core-Fix-escaping-of-password-fields-to-prevent-interpolation.patch
Patch52:          pki-core-Install-tools-clean-up.patch
Patch53:          pki-core-Fixed-KRA-install-problem.patch
Patch54:          pki-core-Fixed-missing-trust-flags-in-certificate-backup.patch
Patch55:          pki-core-Implement-total-ordering-for-PKISubsystem-and-PKIInstance.patch
Patch56:          pki-core-Added-pylint-build-scan-py-to-top-level.patch
## BEGIN:  Manually-crafted patches for use with existing tarballs
Patch57:          pki-core-Py3-modernization-libmodernize.fixes.fix_import.patch
Patch58:          pki-core-Added-Python-wrapper-for-pki-pkcs12-import.patch
## END:    Manually-crafted patches for use with existing tarballs
## pki-core-10.2.6-18
Patch59:          pki-core-Fixed-pki-pkcs12-import-backward-compatibility.patch
## pki-core-10.2.6-19
Patch60:          pki-core-Make-PKIInstance-and-PKISubsystem-hashable.patch

%global saveFileContext() \
if [ -s /etc/selinux/config ]; then \
     . %{_sysconfdir}/selinux/config; \
     FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
     if [ "${SELINUXTYPE}" == %1 -a -f ${FILE_CONTEXT} ]; then \
          cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}; \
     fi \
fi;

%global relabel() \
. %{_sysconfdir}/selinux/config; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
selinuxenabled; \
if [ $? == 0  -a "${SELINUXTYPE}" == %1 -a -f ${FILE_CONTEXT}.%{name} ]; then \
     fixfiles -C ${FILE_CONTEXT}.%{name} restore; \
     rm -f ${FILE_CONTEXT}.%name; \
fi;

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
  * Data Recovery Manager (DRM)                                        \
  * Online Certificate Status Protocol (OCSP) Manager                  \
  * Token Key Service (TKS)                                            \
  * Token Processing Service (TPS)                                     \
                                                                       \
For deployment purposes, PKI Core contains fundamental packages        \
required by BOTH native-based Apache AND java-based Tomcat             \
Certificate System instances consisting of the following components:   \
                                                                       \
  * pki-tools                                                          \
                                                                       \
Additionally, PKI Core contains the following fundamental packages     \
required ONLY by ALL java-based Tomcat Certificate System instances:   \
                                                                       \
  * pki-symkey                                                         \
  * pki-base                                                           \
  * pki-tools                                                          \
  * pki-server                                                         \
                                                                       \
PKI Core also includes the following components:                       \
                                                                       \
  * pki-javadoc                                                        \
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
%{nil}
Source44: import.info
Patch61: pki-core-alt-local-urllib3.patch
Patch62: pki-core-alt-fix-paths.patch

%description %{overview}


%package -n       pki-symkey
Summary:          Symmetric Key JNI Package
Group:            System/Libraries

Requires:         libnss
Requires: javapackages-tools rpm-build-java
Requires:         jss >= 4.2.6

Provides:         symkey = %{version}-%{release}

Obsoletes:        symkey < %{version}-%{release}

%description -n   pki-symkey
The Symmetric Key Java Native Interface (JNI) package supplies various native
symmetric key operations to Java programs.

This package is a part of the PKI Core used by the Certificate System.

%{overview}


%package -n       pki-base
Summary:          Certificate System - PKI Framework
Group:            System/Base

BuildArch:        noarch

Provides:         pki-common = %{version}-%{release}
Provides:         pki-util = %{version}-%{release}

Obsoletes:        pki-common < %{version}-%{release}
Obsoletes:        pki-util < %{version}-%{release}

Requires:         apache-commons-cli
Requires:         apache-commons-codec
Requires:         apache-commons-io
Requires:         apache-commons-lang
Requires:         apache-commons-logging
Requires:         jakarta-commons-httpclient
Requires:         javassist
Requires: javapackages-tools rpm-build-java
Requires:         jss >= 4.2.6
Requires:         ldapjdk
Requires:         python-module-pyldap
Requires:         python-module-lxml
Requires:         python-module-nss
Requires:         python-module-requests >= 1.1.0

%if 0%{?rhel}
# 'resteasy-base' is a subset of the complete set of
# 'resteasy' packages and consists of what is needed to
# support the PKI Restful interface on RHEL platforms
Requires:    resteasy-base-atom-provider >= 3.0.6
Requires:    resteasy-base-client >= 3.0.6
Requires:    resteasy-base-jaxb-provider >= 3.0.6
Requires:    resteasy-base-jaxrs >= 3.0.6
Requires:    resteasy-base-jaxrs-api >= 3.0.6
Requires:    resteasy-base-jackson-provider >= 3.0.6
%else
%if 0%{?fedora} >= 22
# Starting from Fedora 22, resteasy packages were split into
# subpackages.
Requires:    resteasy-atom-provider >= 3.0.6
Requires:    resteasy-client >= 3.0.6
Requires:    resteasy-jaxb-provider >= 3.0.6
Requires:    resteasy-core >= 3.0.6
Requires:    resteasy-jaxrs-api >= 3.0.6
Requires:    resteasy-jackson-provider >= 3.0.6
%else
Requires:         resteasy >= 3.0.6
%endif
%endif

Requires:         xalan-j2
Requires:         xerces-j2
Requires:         xml-commons-apis
Requires:         xml-commons-resolver

%description -n   pki-base
The PKI Framework contains the common and client libraries and utilities.
This package is a part of the PKI Core used by the Certificate System.

%{overview}


%package -n       pki-tools
Summary:          Certificate System - PKI Tools
Group:            System/Base

Provides:         pki-native-tools = %{version}-%{release}
Provides:         pki-java-tools = %{version}-%{release}

Obsoletes:        pki-native-tools < %{version}-%{release}
Obsoletes:        pki-java-tools < %{version}-%{release}

Requires:         openldap-clients
Requires:         libnss
Requires:         nss-utils
Requires:         pki-base = %{version}
Requires: javapackages-tools rpm-build-java
%if 0%{?fedora} >= 23
Requires:         tomcat-servlet-3.1-api >= 8.0.32
%else
%if 0%{?fedora} == 22
Requires:         tomcat-servlet-3.0-api >= 7.0.68
%else
Requires:         tomcat-servlet-3.0-api
%endif
%endif

%description -n   pki-tools
This package contains PKI executables that can be used to help make
Certificate System into a more complete and robust PKI solution.

This package is a part of the PKI Core used by the Certificate System.

%{overview}


%if %{with server}

%package -n       pki-server
Summary:          Certificate System - PKI Server Framework
Group:            System/Base

BuildArch:        noarch

Provides:         pki-deploy = %{version}-%{release}
Provides:         pki-setup = %{version}-%{release}
Provides:         pki-silent = %{version}-%{release}

Obsoletes:        pki-deploy < %{version}-%{release}
Obsoletes:        pki-setup < %{version}-%{release}
Obsoletes:        pki-silent < %{version}-%{release}

Requires: etherwake net-tools

%if 0%{?rhel}
Requires:    libnuxwdog-java >= 1.0.1
%else
Requires:    libnuxwdog-java >= 1.0.3
%endif

Requires:         policycoreutils
Requires:         openldap-clients
Requires:         pki-base = %{version}
Requires:         pki-tools = %{version}
Requires: policycoreutils python-module-sepolgen
%if 0%{?fedora} >= 23
Requires: policycoreutils policycoreutils-sandbox
%endif

%if 0%{?fedora} >= 21
#Requires:         selinux-policy-targeted 
%else
# 0%{?rhel} || 0%{?fedora} < 21
Requires:         selinux-policy-targeted >= 3.13.1
%endif
Obsoletes:        pki-selinux

%if 0%{?rhel}
Requires:         tomcat >= 7.0.54
%else
%if 0%{?fedora} >= 23
Requires:         tomcat >= 8.0.32
Requires:         tomcat-el-3.0-api >= 8.0.32
Requires:         tomcat-jsp-2.3-api >= 8.0.32
Requires:         tomcat-servlet-3.1-api >= 8.0.32
%else
%if 0%{?fedora} == 22
Requires:         tomcat >= 7.0.68
Requires:         tomcat-el-2.2-api >= 7.0.68
Requires:         tomcat-jsp-2.2-api >= 7.0.68
Requires:         tomcat-servlet-3.0-api >= 7.0.68
%else
Requires:         tomcat >= 7.0.47
Requires:         tomcat-el-2.2-api
Requires:         tomcat-jsp-2.2-api
Requires:         tomcat-servlet-3.0-api
%endif
%endif
%endif

Requires:         velocity
Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils

%if 0%{?rhel}
Requires:         tomcatjss >= 7.1.0
%else
%if 0%{?fedora} >= 23
Requires:         tomcatjss >= 7.1.3
%else
%if 0%{?fedora} == 22
Requires:         tomcatjss >= 7.1.2
%else
Requires:         tomcatjss >= 7.1.2
%endif
%endif
%endif

%description -n   pki-server
The PKI Server Framework is required by the following four PKI subsystems:

    the Certificate Authority (CA),
    the Data Recovery Manager (DRM),
    the Online Certificate Status Protocol (OCSP) Manager,
    the Token Key Service (TKS), and
    the Token Processing Service (TPS).

This package is a part of the PKI Core used by the Certificate System.
The package contains scripts to create and remove PKI subsystems.

%{overview}

%package -n       pki-ca
Summary:          Certificate System - Certificate Authority
Group:            System/Servers

BuildArch:        noarch

Requires:         pki-server = %{version}

%description -n   pki-ca
The Certificate Authority (CA) is a required PKI subsystem which issues,
renews, revokes, and publishes certificates as well as compiling and
publishing Certificate Revocation Lists (CRLs).

The Certificate Authority can be configured as a self-signing Certificate
Authority, where it is the root CA, or it can act as a subordinate CA,
where it obtains its own signing certificate from a public CA.

This package is one of the top-level java-based Tomcat PKI subsystems
provided by the PKI Core used by the Certificate System.

%{overview}


%package -n       pki-kra
Summary:          Certificate System - Data Recovery Manager
Group:            System/Servers

BuildArch:        noarch

Requires:         pki-server = %{version}

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

%{overview}


%package -n       pki-ocsp
Summary:          Certificate System - Online Certificate Status Protocol Manager
Group:            System/Servers

BuildArch:        noarch

Requires:         pki-server = %{version}

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

%{overview}


%package -n       pki-tks
Summary:          Certificate System - Token Key Service
Group:            System/Servers

BuildArch:        noarch

Requires:         pki-server = %{version}
Requires:         pki-symkey = %{version}

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

%{overview}


%package -n       pki-tps
Summary:          Certificate System - Token Processing Service
Group:            System/Servers

Provides:         pki-tps-tomcat
Provides:         pki-tps-client

Obsoletes:        pki-tps-tomcat
Obsoletes:        pki-tps-client

Requires:         pki-server = %{version}

# additional runtime requirements needed to run native 'tpsclient'
# REMINDER:  Revisit these once 'tpsclient' is rewritten as a Java app
Requires:         libnss >= 3.14.3
Requires:         nss-utils >= 3.14.3
Requires:         openldap-clients
Requires:         pki-symkey = %{version}

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

%{overview}


%package -n       pki-javadoc
Summary:          Certificate System - PKI Framework Javadocs
Group:            Development/Java

BuildArch:        noarch

Provides:         pki-util-javadoc = %{version}-%{release}
Provides:         pki-java-tools-javadoc = %{version}-%{release}
Provides:         pki-common-javadoc = %{version}-%{release}

Obsoletes:        pki-util-javadoc < %{version}-%{release}
Obsoletes:        pki-java-tools-javadoc < %{version}-%{release}
Obsoletes:        pki-common-javadoc < %{version}-%{release}

%description -n   pki-javadoc
This documentation pertains exclusively to version %{version} of
the PKI Framework and Tools.

This package is a part of the PKI Core used by the Certificate System.

%{overview}

%endif # %{with server}


%prep
%setup -q -n %{name}-%{version}%{?prerel}
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
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
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
sed -i -e 's,"httpd/httpd.h","apache2/httpd.h",' \
	base/tps-client/src/engine/RA.cpp \
	base/tps-client/stubs/modules/nss/mod_nss_stub.c \
	base/tps-client/src/modules/tps/mod_tps.cpp \
	base/tps-client/src/modules/tps/AP_Session.cpp \
	base/tps-client/src/modules/tps/AP_Context.cpp \
	base/tps-client/src/modules/tokendb/mod_tokendb.cpp \
	base/tps-client/src/engine/RA.cpp
sed -i -e 's,"httpd/http_config.h","apache2/http_config.h",' \
	base/tps-client/stubs/modules/nss/mod_nss_stub.c \
	base/tps-client/src/modules/tps/mod_tps.cpp \
	base/tps-client/src/modules/tokendb/mod_tokendb.cpp
sed -i -e 's,include "httpd/http_,include "apache2/http_,' \
	base/tps-client/stubs/modules/nss/mod_nss_stub.c \
	base/tps-client/src/modules/tps/AP_Context.cpp \
	base/tps-client/src/modules/tps/AP_Session.cpp \
	base/tps-client/src/modules/tps/mod_tps.cpp \
	base/tps-client/src/modules/tokendb/mod_tokendb.cpp
# end ugly hacks
%{__mkdir_p} build
cd build
%{fedora_cmake} -DVERSION=%{version}-%{release} \
	-DVAR_INSTALL_DIR:PATH=/var \
	-DBUILD_PKI_CORE:BOOL=ON \
	-DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
	-DSYSTEMD_LIB_INSTALL_DIR=%{_unitdir} \
%if ! %{with_tomcat7}
	-DWITH_TOMCAT7:BOOL=OFF \
%endif
%if ! %{with_tomcat8}
	-DWITH_TOMCAT8:BOOL=OFF \
%endif
	-DRESTEASY_LIB=%{resteasy_lib} \
%if ! %{with server}
	-DWITH_SERVER:BOOL=OFF \
%endif
%if ! %{with server}
	-DWITH_SERVER:BOOL=OFF \
%endif
%if ! %{with javadoc}
	-DWITH_JAVADOC:BOOL=OFF \
%endif
	..
%{__make} VERBOSE=1 %{?_smp_mflags} all
# %{__make} VERBOSE=1 %{?_smp_mflags} unit-test


%install
cd build
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"

# Create symlinks for admin console (TPS does not use admin console)
for subsystem in ca kra ocsp tks; do
    %{__mkdir_p} %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/admin
    ln -s %{_datadir}/pki/server/webapps/pki/admin/console %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/admin
done

# Create symlinks for subsystem libraries
for subsystem in ca kra ocsp tks tps; do
    %{__mkdir_p} %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-nsutil.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-cmsutil.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-certsrv.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-cms.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-cmscore.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-cmsbundle.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
    ln -s %{_javadir}/pki/pki-$subsystem.jar %{buildroot}%{_datadir}/pki/$subsystem/webapps/$subsystem/WEB-INF/lib
done

%if %{with server}

%if ! 0%{?rhel}
# Scanning the python code with pylint.
#python ../pylint-build-scan.py rpm --prefix %{buildroot}
#if [ $? -ne 0 ]; then
#    echo "pylint failed. RC: $?"
#    exit 1
#fi
%endif

%{__rm} -rf %{buildroot}%{_datadir}/pki/server/lib

%endif # %{with server}

%{__mkdir_p} %{buildroot}%{_var}/log/pki
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/pki
# from sem@:
# This file should be sourced only
chmod -x %buildroot%_datadir/pki/scripts/operations

%pre -n pki-server
getent group %{pki_groupname} >/dev/null || groupadd -f -g %{pki_gid} -r %{pki_groupname}
if ! getent passwd %{pki_username} >/dev/null ; then
    if ! getent passwd %{pki_uid} >/dev/null ; then
      useradd -r -u %{pki_uid} -g %{pki_groupname} -d %{pki_homedir} -s /sbin/nologin -c "Certificate System" %{pki_username}
    else
      useradd -r -g %{pki_groupname} -d %{pki_homedir} -s /sbin/nologin -c "Certificate System" %{pki_username}
    fi
fi
exit 0

%post -n pki-base
if [ $1 -eq 1 ]
then
    # On RPM installation create system upgrade tracker
    echo "Configuration-Version: %{version}" > %{_sysconfdir}/pki/pki.version

else
    # On RPM upgrade run system upgrade
    echo "Upgrading PKI system configuration at `/bin/date`." >> /var/log/pki/pki-upgrade-%{version}.log 2>&1
    /usr/sbin/pki-upgrade --silent >> /var/log/pki/pki-upgrade-%{version}.log 2>&1
    echo >> /var/log/pki/pki-upgrade-%{version}.log 2>&1
fi

%postun -n pki-base
if [ $1 -eq 0 ]
then
    # On RPM uninstallation remove system upgrade tracker
    rm -f %{_sysconfdir}/pki/pki.version
fi

%if %{with server}

%post -n pki-server
echo "Upgrading PKI server configuration at `/bin/date`." >> /var/log/pki/pki-server-upgrade-%{version}.log 2>&1
 /usr/sbin/pki-server-upgrade --silent >> /var/log/pki/pki-server-upgrade-%{version}.log 2>&1
echo >> /var/log/pki/pki-server-upgrade-%{version}.log 2>&1

# Migrate Tomcat configuration
 /usr/sbin/pki-server migrate >> /var/log/pki/pki-server-upgrade-%{version}.log 2>&1
echo >> /var/log/pki/pki-server-upgrade-%{version}.log 2>&1



## %preun -n pki-server
## NOTE:  At this time, NO attempt has been made to update ANY PKI subsystem
##        from EITHER 'sysVinit' OR previous 'systemd' processes to the new
##        PKI deployment process


## %postun -n pki-server
## NOTE:  At this time, NO attempt has been made to update ANY PKI subsystem
##        from EITHER 'sysVinit' OR previous 'systemd' processes to the new
##        PKI deployment process

%endif # %{with server}


%files -n pki-symkey
%doc base/symkey/LICENSE
%{_jnidir}/symkey.jar
%{_libdir}/symkey/


%files -n pki-base
%doc base/common/LICENSE
%doc %{_datadir}/doc/pki-base/html
%dir %{_datadir}/pki
%{_datadir}/pki/VERSION
%{_datadir}/pki/etc/
%{_datadir}/pki/upgrade/
%{_datadir}/pki/key/templates
%dir %{_sysconfdir}/pki
%config(noreplace) %{_sysconfdir}/pki/pki.conf
%dir %{_javadir}/pki
%{_javadir}/pki/pki-cmsutil.jar
%{_javadir}/pki/pki-nsutil.jar
%{_javadir}/pki/pki-certsrv.jar
%dir %{python_sitelibdir_noarch}/pki
%{python_sitelibdir_noarch}/pki/*.py
%{python_sitelibdir_noarch}/pki/*.pyc
%{python_sitelibdir_noarch}/pki/*.pyo
%{python_sitelibdir_noarch}/pki/cli/
%dir %{_var}/log/pki
%{_sbindir}/pki-upgrade
%{_mandir}/man8/pki-upgrade.8*
%{_mandir}/man1/pki-python-client.1*
%dir %{_datadir}/pki/key

%files -n pki-tools
%doc base/native-tools/LICENSE base/native-tools/doc/README
%{_bindir}/pki
%{_bindir}/p7tool
%{_bindir}/revoker
%{_bindir}/setpin
%{_bindir}/sslget
%{_bindir}/tkstool
%{_datadir}/pki/native-tools/
%{_bindir}/AtoB
%{_bindir}/AuditVerify
%{_bindir}/BtoA
%{_bindir}/CMCEnroll
%{_bindir}/CMCRequest
%{_bindir}/CMCResponse
%{_bindir}/CMCRevoke
%{_bindir}/CRMFPopClient
%{_bindir}/DRMTool
%{_bindir}/ExtJoiner
%{_bindir}/GenExtKeyUsage
%{_bindir}/GenIssuerAltNameExt
%{_bindir}/GenSubjectAltNameExt
%{_bindir}/HttpClient
%{_bindir}/OCSPClient
%{_bindir}/PKCS10Client
%{_bindir}/PKCS12Export
%{_bindir}/PrettyPrintCert
%{_bindir}/PrettyPrintCrl
%{_bindir}/TokenInfo
%{_javadir}/pki/pki-tools.jar
%{_datadir}/pki/java-tools/
%{_mandir}/man1/pki.1*
%{_mandir}/man1/pki-audit.1*
%{_mandir}/man1/pki-cert.1*
%{_mandir}/man1/pki-client.1*
%{_mandir}/man1/pki-group.1*
%{_mandir}/man1/pki-group-member.1*
%{_mandir}/man1/pki-key.1*
%{_mandir}/man1/pki-securitydomain.1*
%{_mandir}/man1/pki-user.1*
%{_mandir}/man1/pki-user-cert.1*
%{_mandir}/man1/pki-user-membership.1*
%{_mandir}/man1/pki-ca-profile.1*
%{_mandir}/man1/pki-tps-profile.1*

%if %{with server}

%files -n pki-server
%doc base/common/THIRD_PARTY_LICENSES
%doc base/server/LICENSE
%doc base/server/README
%{_sysconfdir}/pki/default.cfg
%{_sbindir}/pkispawn
%{_sbindir}/pkidestroy
%{_sbindir}/pki-server
%{_sbindir}/pki-server-nuxwdog
%{_sbindir}/pki-server-upgrade
%{python_sitelibdir_noarch}/pki/server/
%dir %{_datadir}/pki/deployment
%{_datadir}/pki/deployment/config/
%dir %{_datadir}/pki/scripts
%{_datadir}/pki/scripts/operations
%{_bindir}/pkidaemon
%dir %{_sysconfdir}/systemd/system/pki-tomcatd.target.wants
%{_unitdir}/pki-tomcatd@.service
%{_unitdir}/pki-tomcatd.target
%dir %{_sysconfdir}/systemd/system/pki-tomcatd-nuxwdog.target.wants
%{_unitdir}/pki-tomcatd-nuxwdog@.service
%{_unitdir}/pki-tomcatd-nuxwdog.target
%{_javadir}/pki/pki-cms.jar
%{_javadir}/pki/pki-cmsbundle.jar
%{_javadir}/pki/pki-cmscore.jar
%{_javadir}/pki/pki-tomcat.jar
%dir %{_sharedstatedir}/pki
%{_mandir}/man1/pkidaemon.1*
%{_mandir}/man5/pki_default.cfg.5*
%{_mandir}/man8/pki-server-upgrade.8*
%{_mandir}/man8/pkidestroy.8*
%{_mandir}/man8/pkispawn.8*
%{_mandir}/man8/pki-server.8*
%{_mandir}/man8/pki-server-instance.8*
%{_mandir}/man8/pki-server-subsystem.8*
%{_mandir}/man8/pki-server-nuxwdog.8*
%{_mandir}/man8/pki-server-migrate.8*

%{_datadir}/pki/setup/
%{_datadir}/pki/server/


%files -n pki-ca
%doc base/ca/LICENSE
%{_javadir}/pki/pki-ca.jar
%dir %{_datadir}/pki/ca
%{_datadir}/pki/ca/conf/
%{_datadir}/pki/ca/emails/
%dir %{_datadir}/pki/ca/profiles
%{_datadir}/pki/ca/profiles/ca/
%{_datadir}/pki/ca/setup/
%{_datadir}/pki/ca/webapps/

%files -n pki-kra
%doc base/kra/LICENSE
%{_javadir}/pki/pki-kra.jar
%dir %{_datadir}/pki/kra
%{_datadir}/pki/kra/conf/
%{_datadir}/pki/kra/setup/
%{_datadir}/pki/kra/webapps/

%files -n pki-ocsp
%doc base/ocsp/LICENSE
%{_javadir}/pki/pki-ocsp.jar
%dir %{_datadir}/pki/ocsp
%{_datadir}/pki/ocsp/conf/
%{_datadir}/pki/ocsp/setup/
%{_datadir}/pki/ocsp/webapps/

%files -n pki-tks
%doc base/tks/LICENSE
%{_javadir}/pki/pki-tks.jar
%dir %{_datadir}/pki/tks
%{_datadir}/pki/tks/conf/
%{_datadir}/pki/tks/setup/
%{_datadir}/pki/tks/webapps/

%files -n pki-tps
%doc base/tps/LICENSE
%{_javadir}/pki/pki-tps.jar
%dir %{_datadir}/pki/tps
%{_datadir}/pki/tps/applets/
%{_datadir}/pki/tps/conf/
%{_datadir}/pki/tps/setup/
%{_datadir}/pki/tps/webapps/
%{_mandir}/man5/pki-tps-connector.5*
%{_mandir}/man5/pki-tps-profile.5*
%{_mandir}/man1/tpsclient.1*
# files for native 'tpsclient'
# REMINDER:  Remove this comment once 'tpsclient' is rewritten as a Java app
%{_bindir}/tpsclient
%{_libdir}/tps/libtps.so
%{_libdir}/tps/libtokendb.so

%if %{with javadoc}
%files -n pki-javadoc
%{_javadocdir}/pki-%{version}/
%endif

%endif # %{with server}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt3_19jpp8
- cleanup: removed conflict glitch and selinux dependency

* Mon Nov 21 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt2_19jpp8
- bugfix thanks to @sem

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt2_16jpp8
- added sem@ patch

* Fri Apr 29 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt1_16jpp8
- new version
- TODO: %{_datadir}/pki/tks/* not packaged
