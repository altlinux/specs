%define _unpackaged_files_terminate_build 1

Name: webauthn4j
Version: 0.30.0
Release: alt1

Summary: A portable Java library for WebAuthn(Passkeys) server side verification
License: Apache-2.0
Group: Development/Java
Url: https://webauthn4j.github.io/webauthn4j/en
Vcs: https://github.com/webauthn4j/webauthn4j.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-unwanted-dependencies-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
# Although webauthn4j uses JDK 15+ API to support EdDSA.
BuildRequires: jpackage-17-compat
BuildRequires: jetbrains-annotations
BuildRequires: jackson-databind
BuildRequires: jackson-datatype-jsr310
BuildRequires: jackson-dataformat-cbor
BuildRequires: jackson-core
BuildRequires: slf4j

%description
WebAuthn4J is a comprehensive Java library implementing the W3C Web
Authentication (WebAuthn) and FIDO2 server-side standards. It provides the core
functionality for registration and authentication ceremonies, attestation and
assertion verification, and credential metadata validation.

This library includes support for both synchronous and asynchronous operations,
integration with reactive frameworks, and extensions such as Apple App Attest
verification. Additionally, it provides utilities for data encoding,
cryptography, and JSON handling, ensuring developers can easily integrate
WebAuthn/FIDO2 functionality into Java server applications.

WebAuthn4J is suitable for secure passwordless authentication, multi-factor
authentication, and modern identity management solutions, providing a robust
foundation for WebAuthn/FIDO2-compliant services.

%package core
Summary: Core library for WebAuthn4J
Group: Development/Java
BuildArch: noarch

%description core
The core module of WebAuthn4J.  It implements the main logic for WebAuthn/FIDO2
attestation and assertion verification, including credential parsing, signature
validation, challenge handling, and data structures for server-side
authentication flows.

%package core-async
Summary: Asynchronous WebAuthn core library
Group: Development/Java
BuildArch: noarch
Requires: webauthn4j-core

%description core-async
Asynchronous extension of WebAuthn4J Core.  Provides non-blocking
implementations of the WebAuthn core operations, enabling integration with
reactive or asynchronous Java frameworks such as Spring WebFlux or Vert.x.

%package metadata
Summary: WebAuthn4J Metadata Service client
Group: Development/Java
BuildArch: noarch
Requires: webauthn4j-core

%description metadata
The metadata module for WebAuthn4J.  Implements support for the FIDO Metadata
Service (MDS), enabling validation of authenticator attestation statements
against metadata entries. Provides APIs for parsing and managing FIDO MDS
payloads and trust anchors.

%package metadata-async
Summary: Asynchronous WebAuthn4J Metadata Service client
Group: Development/Java
BuildArch: noarch
Requires: webauthn4j-core-async
Requires: webauthn4j-metadata

%description metadata-async
Asynchronous version of the WebAuthn4J Metadata module.  Offers non-blocking
interfaces for retrieving and validating metadata entries, suitable for
reactive and high-throughput WebAuthn server environments.

%package appattest
Summary: Apple App Attest extension for WebAuthn4J
Group: Development/Java
BuildArch: noarch
Requires: webauthn4j-core

%description appattest
The App Attest module for WebAuthn4J.  Adds support for Apple App Attest
attestation format, allowing verification of credentials issued by iOS
applications via Apple's App Attest service. Integrates seamlessly with the
core WebAuthn verification pipeline.

%package util
Summary: Common utilities for WebAuthn4J
Group: Development/Java
BuildArch: noarch
Requires: webauthn4j-core

%description util
Utility module providing shared components used across WebAuthn4J modules,
including data encoding, cryptographic helpers, JSON utilities, and type
definitions. This package is a lightweight dependency required by other
WebAuthn4J modules.

%package javadoc
Group: Development/Java
Summary: Javadoc for webauthn4j

%description javadoc
This package contains javadoc for webauthn4j.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%files core
%_mavenmetadatadir/webauthn4j.xml
%_javadir/webauthn4j/webauthn4j-core.jar
%_mavenpomdir/webauthn4j/webauthn4j-core.pom

%files core-async
%_javadir/webauthn4j/webauthn4j-core-async.jar
%_mavenpomdir/webauthn4j/webauthn4j-core-async.pom

%files metadata
%_javadir/webauthn4j/webauthn4j-metadata.jar
%_mavenpomdir/webauthn4j/webauthn4j-metadata.pom

%files metadata-async
%_javadir/webauthn4j/webauthn4j-metadata-async.jar
%_mavenpomdir/webauthn4j/webauthn4j-metadata-async.pom

%files appattest
%_javadir/webauthn4j/webauthn4j-appattest.jar
%_mavenpomdir/webauthn4j/webauthn4j-appattest.pom

%files util
%_javadir/webauthn4j/webauthn4j-util.jar
%_mavenpomdir/webauthn4j/webauthn4j-util.pom

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 0.30.0-alt1
- First build for ALT.
