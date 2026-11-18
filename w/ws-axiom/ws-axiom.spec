%define _unpackaged_files_terminate_build 1

Name: ws-axiom
Version: 2.0.0
Release: alt1

Summary: Apache Axiom XML object model
License: Apache-2.0 AND W3C
Group: Development/Java
URL: https://ws.apache.org/axiom/
VCS: https://github.com/apache/ws-axiom.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-system.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: jaxb-xjc
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: mvn(com.github.veithen:jrel)
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.auto.service:auto-service-annotations)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api:1.2.2)
BuildRequires: mvn(jakarta.mail:jakarta.mail-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api:2.3.3)
BuildRequires: mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires: mvn(jaxen:jaxen)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.saxon:Saxon-HE)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.james:apache-mime4j-core)
BuildRequires: mvn(org.apache.james:apache-mime4j-dom)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.eclipse.angus:angus-mail)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.jacoco:org.jacoco.agent::runtime:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.osgi:org.osgi.util.tracker)
BuildRequires: mvn(org.osgi:osgi.core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.ow2.asm:asm-util)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.xmlunit:xmlunit-assertj3)
BuildRequires: mvn(xalan:serializer)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(xerces:xercesImpl)

%description
Apache Axiom provides an XML object model, StAX processing, SOAP support,
DOM and linked-list implementations, activation/JAXB bridges and its
bytecode weaver with Maven integration.

%package buildutils
Summary: Apache Axiom buildutils module
Group: Development/Java

%description buildutils
This package provides the Apache Axiom buildutils module.

%package weaver-maven-plugin
Summary: Apache Axiom axiom weaver maven plugin module
Group: Development/Java

%description weaver-maven-plugin
This package provides the Apache Axiom axiom weaver maven plugin module.

%package buildutils-maven-plugin
Summary: Apache Axiom buildutils maven plugin module
Group: Development/Java

%description buildutils-maven-plugin
This package provides the Apache Axiom buildutils maven plugin module.

%package shade-axiom-xml
Summary: Apache Axiom shade axiom xml module
Group: Development/Java

%description shade-axiom-xml
This package provides the Apache Axiom shade axiom xml module.

%package api
Summary: Apache Axiom axiom api module
Group: Development/Java

%description api
This package provides the Apache Axiom axiom api module.

%package compat
Summary: Apache Axiom axiom compat module
Group: Development/Java

%description compat
This package provides the Apache Axiom axiom compat module.

%package jakarta-jaxb
Summary: Apache Axiom axiom jakarta jaxb module
Group: Development/Java

%description jakarta-jaxb
This package provides the Apache Axiom axiom jakarta jaxb module.

%package javax-jaxb
Summary: Apache Axiom axiom javax jaxb module
Group: Development/Java

%description javax-jaxb
This package provides the Apache Axiom axiom javax jaxb module.

%package systests
Summary: Apache Axiom systests module
Group: Development/Java

%description systests
This package provides the Apache Axiom systests module.

%package testing
Summary: Apache Axiom testing module
Group: Development/Java

%description testing
This package provides the Apache Axiom testing module.

%package testsuite
Summary: Apache Axiom axiom testsuite module
Group: Development/Java

%description testsuite
This package provides the Apache Axiom axiom testsuite module.

%package truth
Summary: Apache Axiom axiom truth module
Group: Development/Java

%description truth
This package provides the Apache Axiom axiom truth module.

%package dom-testsuite
Summary: Apache Axiom dom testsuite module
Group: Development/Java

%description dom-testsuite
This package provides the Apache Axiom dom testsuite module.

%package jaxen-testsuite
Summary: Apache Axiom jaxen testsuite module
Group: Development/Java

%description jaxen-testsuite
This package provides the Apache Axiom jaxen testsuite module.

%package multiton
Summary: Apache Axiom multiton module
Group: Development/Java

%description multiton
This package provides the Apache Axiom multiton module.

%package saaj-testsuite
Summary: Apache Axiom saaj testsuite module
Group: Development/Java

%description saaj-testsuite
This package provides the Apache Axiom saaj testsuite module.

%package soap-testsuite
Summary: Apache Axiom soap testsuite module
Group: Development/Java

%description soap-testsuite
This package provides the Apache Axiom soap testsuite module.

%package testutils
Summary: Apache Axiom testutils module
Group: Development/Java

%description testutils
This package provides the Apache Axiom testutils module.

%package xml-testsuite
Summary: Apache Axiom xml testsuite module
Group: Development/Java

%description xml-testsuite
This package provides the Apache Axiom xml testsuite module.

%package xml-truth
Summary: Apache Axiom xml truth module
Group: Development/Java

%description xml-truth
This package provides the Apache Axiom xml truth module.

%package jaxp-testsuite
Summary: Apache Axiom jaxp testsuite module
Group: Development/Java

%description jaxp-testsuite
This package provides the Apache Axiom jaxp testsuite module.

%package url-registry
Summary: Apache Axiom url registry module
Group: Development/Java

%description url-registry
This package provides the Apache Axiom url registry module.

%package blob-testutils
Summary: Apache Axiom blob testutils module
Group: Development/Java

%description blob-testutils
This package provides the Apache Axiom blob testutils module.

%package mixins
Summary: Apache Axiom mixins module
Group: Development/Java

%description mixins
This package provides the Apache Axiom mixins module.

%package core-mixins
Summary: Apache Axiom core mixins module
Group: Development/Java

%description core-mixins
This package provides the Apache Axiom core mixins module.

%package dom-mixins
Summary: Apache Axiom dom mixins module
Group: Development/Java

%description dom-mixins
This package provides the Apache Axiom dom mixins module.

%package om-mixins
Summary: Apache Axiom om mixins module
Group: Development/Java

%description om-mixins
This package provides the Apache Axiom om mixins module.

%package implementations
Summary: Apache Axiom implementations module
Group: Development/Java

%description implementations
This package provides the Apache Axiom implementations module.

%package impl
Summary: Apache Axiom axiom impl module
Group: Development/Java

%description impl
This package provides the Apache Axiom axiom impl module.

%package dom
Summary: Apache Axiom axiom dom module
Group: Development/Java

%description dom
This package provides the Apache Axiom axiom dom module.

%package components
Summary: Apache Axiom components module
Group: Development/Java

%description components
This package provides the Apache Axiom components module.

%package base64-utils
Summary: Apache Axiom base64 utils module
Group: Development/Java

%description base64-utils
This package provides the Apache Axiom base64 utils module.

%package blob
Summary: Apache Axiom blob module
Group: Development/Java

%description blob
This package provides the Apache Axiom blob module.

%package core-streams
Summary: Apache Axiom core streams module
Group: Development/Java

%description core-streams
This package provides the Apache Axiom core streams module.

%package io
Summary: Apache Axiom io module
Group: Development/Java

%description io
This package provides the Apache Axiom io module.

%package xml-utils
Summary: Apache Axiom xml utils module
Group: Development/Java

%description xml-utils
This package provides the Apache Axiom xml utils module.

%package weaver
Summary: Apache Axiom axiom weaver module
Group: Development/Java

%description weaver
This package provides the Apache Axiom axiom weaver module.

%package weaver-annotations
Summary: Apache Axiom axiom weaver annotations module
Group: Development/Java

%description weaver-annotations
This package provides the Apache Axiom axiom weaver annotations module.

%package jakarta-activation
Summary: Apache Axiom axiom jakarta activation module
Group: Development/Java

%description jakarta-activation
This package provides the Apache Axiom axiom jakarta activation module.

%package javax-activation
Summary: Apache Axiom axiom javax activation module
Group: Development/Java

%description javax-activation
This package provides the Apache Axiom axiom javax activation module.

%package legacy-attachments
Summary: Apache Axiom axiom legacy attachments module
Group: Development/Java

%description legacy-attachments
This package provides the Apache Axiom axiom legacy attachments module.

%package javax-bom
Summary: Apache Axiom javax bom module
Group: Development/Java

%description javax-bom
This package provides the Apache Axiom javax bom module.

%package jakarta-bom
Summary: Apache Axiom jakarta bom module
Group: Development/Java

%description jakarta-bom
This package provides the Apache Axiom jakarta bom module.

%javadoc_package

%prep
%setup
%autopatch -p1
# Keep compiler coordinates explicit for the POM-only RPM dependency generator.
%pom_xpath_inject \
    "/pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']" \
    "<groupId>org.apache.maven.plugins</groupId><version>3.13.0</version>"
sed -n '1,/-->/p' \
    testing/soap-testsuite/src/main/resources/org/apache/axiom/ts/soap/xsd/soap-1.1.xsd \
    > W3C-soap-1.1-LICENSE.txt
sed -n '1,/-->/p' \
    testing/soap-testsuite/src/main/resources/org/apache/axiom/ts/soap/xsd/soap-1.2.xsd \
    > W3C-soap-1.2-LICENSE.txt
# Source classifiers are genuine intermediate inputs for the javax bridges.
%mvn_package ::jar:sources: __noinstall
# Integration modules contain tests only, without production JAR contents.
%mvn_package :samples __noinstall
%mvn_package :cross-om-tests __noinstall
%mvn_package :old-tests __noinstall
%mvn_package :jaxb-tests __noinstall

# Keep every output of each independent Maven module in its own RPM.
%mvn_package :axiom
%mvn_package :buildutils buildutils
%mvn_package :axiom-weaver-maven-plugin weaver-maven-plugin
%mvn_package :buildutils-maven-plugin buildutils-maven-plugin
%mvn_package :shade-axiom-xml shade-axiom-xml
%mvn_package :axiom-api api
%mvn_package :axiom-compat compat
%mvn_package :axiom-jakarta-jaxb jakarta-jaxb
%mvn_package :axiom-javax-jaxb javax-jaxb
%mvn_package :systests systests
%mvn_package :testing testing
%mvn_package :axiom-testsuite testsuite
%mvn_package :axiom-truth truth
%mvn_package :dom-testsuite dom-testsuite
%mvn_package :jaxen-testsuite jaxen-testsuite
%mvn_package :multiton multiton
%mvn_package :saaj-testsuite saaj-testsuite
%mvn_package :soap-testsuite soap-testsuite
%mvn_package :testutils testutils
%mvn_package :xml-testsuite xml-testsuite
%mvn_package :xml-truth xml-truth
%mvn_package :jaxp-testsuite jaxp-testsuite
%mvn_package :url-registry url-registry
%mvn_package :blob-testutils blob-testutils
%mvn_package :mixins mixins
%mvn_package :core-mixins core-mixins
%mvn_package :dom-mixins dom-mixins
%mvn_package :om-mixins om-mixins
%mvn_package :implementations implementations
%mvn_package :axiom-impl impl
%mvn_package :axiom-dom dom
%mvn_package :components components
%mvn_package :base64-utils base64-utils
%mvn_package :blob blob
%mvn_package :core-streams core-streams
%mvn_package :io io
%mvn_package :xml-utils xml-utils
%mvn_package :axiom-weaver weaver
%mvn_package :axiom-weaver-annotations weaver-annotations
%mvn_package :axiom-jakarta-activation jakarta-activation
%mvn_package :axiom-javax-activation javax-activation
%mvn_package :axiom-legacy-attachments legacy-attachments
%mvn_package :javax-bom javax-bom
%mvn_package :jakarta-bom jakarta-bom

%build
%mvn_build -s -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%doc NOTICE
%doc W3C-soap-1.1-LICENSE.txt W3C-soap-1.2-LICENSE.txt
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%doc legal/apache-mime4j-core-LICENSE.txt
%doc legal/commons-logging-LICENSE.txt
%doc legal/jakarta.activation-api-LICENSE.txt
%doc legal/jakarta.xml.bind-api-LICENSE.txt
%doc legal/jaxen-LICENSE.txt
%doc legal/stax2-api-LICENSE.txt
%doc legal/woodstox-core-asl-LICENSE.txt

%files buildutils -f .mfiles-buildutils

%files weaver-maven-plugin -f .mfiles-weaver-maven-plugin

%files buildutils-maven-plugin -f .mfiles-buildutils-maven-plugin

%files shade-axiom-xml -f .mfiles-shade-axiom-xml

%files api -f .mfiles-api

%files compat -f .mfiles-compat

%files jakarta-jaxb -f .mfiles-jakarta-jaxb

%files javax-jaxb -f .mfiles-javax-jaxb

%files systests -f .mfiles-systests

%files testing -f .mfiles-testing

%files testsuite -f .mfiles-testsuite

%files truth -f .mfiles-truth

%files dom-testsuite -f .mfiles-dom-testsuite

%files jaxen-testsuite -f .mfiles-jaxen-testsuite

%files multiton -f .mfiles-multiton

%files saaj-testsuite -f .mfiles-saaj-testsuite

%files soap-testsuite -f .mfiles-soap-testsuite

%files testutils -f .mfiles-testutils

%files xml-testsuite -f .mfiles-xml-testsuite

%files xml-truth -f .mfiles-xml-truth

%files jaxp-testsuite -f .mfiles-jaxp-testsuite

%files url-registry -f .mfiles-url-registry

%files blob-testutils -f .mfiles-blob-testutils

%files mixins -f .mfiles-mixins

%files core-mixins -f .mfiles-core-mixins

%files dom-mixins -f .mfiles-dom-mixins

%files om-mixins -f .mfiles-om-mixins

%files implementations -f .mfiles-implementations

%files impl -f .mfiles-impl

%files dom -f .mfiles-dom

%files components -f .mfiles-components

%files base64-utils -f .mfiles-base64-utils

%files blob -f .mfiles-blob

%files core-streams -f .mfiles-core-streams

%files io -f .mfiles-io

%files xml-utils -f .mfiles-xml-utils

%files weaver -f .mfiles-weaver

%files weaver-annotations -f .mfiles-weaver-annotations

%files jakarta-activation -f .mfiles-jakarta-activation

%files javax-activation -f .mfiles-javax-activation

%files legacy-attachments -f .mfiles-legacy-attachments

%files javax-bom -f .mfiles-javax-bom

%files jakarta-bom -f .mfiles-jakarta-bom

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.0.0-alt1
- Initial build for ALT.
