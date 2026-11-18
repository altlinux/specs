%define _unpackaged_files_terminate_build 1

Name: xmlutil
Version: 1.0.2.1
Release: alt1

Summary: Kotlin Multiplatform XML serialization library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/pdvrieze/xmlutil
VCS: https://github.com/pdvrieze/xmlutil.git

BuildArch: noarch
Source: %name-%version.tar
Source1: %name-xsdtests-3d686a51975b4136fc957e1f006aefbe85a8a410.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.apache.httpcomponents.client5:httpclient5)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-datetime-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:atomicfu-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-io-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)
BuildRequires: mvn(net.sf.kxml:kxml2)
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-benchmark-runtime-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx.benchmark:org.jetbrains.kotlinx.benchmark.gradle.plugin:pom:)

%description
Core XML processing library for Kotlin Multiplatform.
This package provides the JVM implementation.

%package core-compat
Summary: XML core relocation metadata
Group: Development/Java

%description core-compat
Compatibility relocation metadata for the upstream core-compat module.

%package core-jdk
Summary: XML processing with the JDK StAX provider
Group: Development/Java

%description core-jdk
JDK StAX integration for the XMLUtil core module.

%package core-android
Summary: XML processing with an Android-compatible provider
Group: Development/Java

%description core-android
Android-compatible XML processing provider for XMLUtil.

%package core-io
Summary: Kotlinx IO integration for XMLUtil
Group: Development/Java

%description core-io
Kotlinx IO integration for the XMLUtil core module.

%package serialization
Summary: Kotlin XML serialization integration
Group: Development/Java

%description serialization
XML serialization integration for kotlinx.serialization.

%package serialization-io
Summary: Kotlinx IO integration for XML serialization
Group: Development/Java

%description serialization-io
Kotlinx IO integration for XMLUtil serialization.

%package serialutil
Summary: Kotlin serialization utility library
Group: Development/Java

%description serialutil
Serialization utilities shared by XMLUtil modules.

%package xmlserializable
Summary: XML serializable interfaces for Kotlin
Group: Development/Java

%description xmlserializable
XML serializable interfaces for the XMLUtil modules.

%package testutil
Summary: XMLUtil test utility library
Group: Development/Java

%description testutil
Reusable test support for XMLUtil modules and their consumers.

%package xmlschema
Summary: Kotlin XML Schema library
Group: Development/Java

%description xmlschema
XML Schema serialization and validation support for XMLUtil.

%package bom
Summary: XMLUtil dependency management BOM
Group: Development/Java

%description bom
Maven dependency management for the XMLUtil modules.

%prep
%setup -q
mkdir -p schemaTests/src/commonMain/resources/xsts
tar -xf %SOURCE1 --strip-components=1 -C schemaTests/src/commonMain/resources/xsts
%autopatch -p1

# Leave room for the JVM outside the heap in a 32-bit address space.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx3072M/-Xmx2048M/' gradle.properties
fi

%build
%gradle_publish -Pnative.deploy=disabled -Pxmlutil.jvmOnly=true

%install
%mvn_package io.github.pdvrieze.xmlutil:core-jvm
%mvn_package io.github.pdvrieze.xmlutil:core-jvmcommon core-compat
%mvn_package io.github.pdvrieze.xmlutil:core-jdk core-jdk
%mvn_package io.github.pdvrieze.xmlutil:core-android core-android
%mvn_package io.github.pdvrieze.xmlutil:core-io-jvm core-io
%mvn_package io.github.pdvrieze.xmlutil:serialization-jvm serialization
%mvn_package io.github.pdvrieze.xmlutil:serialization-android serialization
%mvn_package io.github.pdvrieze.xmlutil:serialization-io-jvm serialization-io
%mvn_package io.github.pdvrieze.xmlutil:serialutil-jvm serialutil
%mvn_package io.github.pdvrieze.xmlutil:serialutil-android serialutil
%mvn_package io.github.pdvrieze.xmlutil:xmlserializable-jvm xmlserializable
%mvn_package io.github.pdvrieze.xmlutil:xmlserializable-android xmlserializable
%mvn_package io.github.pdvrieze.xmlutil:testutil-jvm testutil
%mvn_package io.github.pdvrieze.xmlutil:xmlschema-jvm xmlschema
%mvn_package io.github.pdvrieze.xmlutil:xmlutil-bom bom
%gradle_register --exclude-artifacts=xmlutil-bom-,core-jvmcommon-,serialization-android-,serialutil-android-,xmlserializable-android-
%gradle_register_bom --artifacts=xmlutil-bom-
%mvn_artifact %_mavenrepolocal/repository/io/github/pdvrieze/xmlutil/core-jvmcommon/%version/core-jvmcommon-%version.pom
%mvn_artifact %_mavenrepolocal/repository/io/github/pdvrieze/xmlutil/serialization-android/%version/serialization-android-%version.pom
%mvn_artifact %_mavenrepolocal/repository/io/github/pdvrieze/xmlutil/serialutil-android/%version/serialutil-android-%version.pom
%mvn_artifact %_mavenrepolocal/repository/io/github/pdvrieze/xmlutil/xmlserializable-android/%version/xmlserializable-android-%version.pom
%gradle_install

%check
%gradle_check --continue -Pnative.deploy=disabled -Pxmlutil.jvmOnly=true

%files -f .mfiles
%doc COPYING

%files core-compat -f .mfiles-core-compat

%files core-jdk -f .mfiles-core-jdk

%files core-android -f .mfiles-core-android

%files core-io -f .mfiles-core-io

%files serialization -f .mfiles-serialization

%files serialization-io -f .mfiles-serialization-io

%files serialutil -f .mfiles-serialutil

%files xmlserializable -f .mfiles-xmlserializable

%files testutil -f .mfiles-testutil

%files xmlschema -f .mfiles-xmlschema

%files bom -f .mfiles-bom

%changelog
* Fri Nov 13 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2.1-alt1
- Initial build for ALT.
