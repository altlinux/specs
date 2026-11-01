%define _unpackaged_files_terminate_build 1

Name: groovy
Version: 6.0.0
Release: alt1

Summary: Groovy programming language
License: Apache-2.0 and BSD-3-Clause
Group: Development/Java
Url: https://groovy.apache.org
VCS: https://github.com/apache/groovy.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: jackson-dataformat-csv
BuildRequires: jackson-dataformat-yaml
BuildRequires: jakarta-servlet
BuildRequires: java-21-openjdk-devel
BuildRequires: jline4-builtins
BuildRequires: jline4-console
BuildRequires: jline4-core
BuildRequires: jline4-jansi
BuildRequires: jline4-reader
BuildRequires: jline4-shell
BuildRequires: jline4-terminal
BuildRequires: jline4-terminal-jni
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires: mvn(bsf:bsf)
BuildRequires: mvn(com.carrotsearch:hppc)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-toml)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-jsr310)
BuildRequires: mvn(com.formdev:flatlaf)
BuildRequires: mvn(com.formdev:flatlaf-extras)
BuildRequires: mvn(com.github.javaparser:javaparser-core)
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(com.gradleup.shadow:shadow-gradle-plugin)
BuildRequires: mvn(com.thoughtworks.qdox:qdox)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(info.picocli:picocli)
BuildRequires: mvn(io.projectreactor:reactor-core)
BuildRequires: mvn(io.reactivex.rxjava3:rxjava)
BuildRequires: mvn(jakarta.servlet.jsp:jakarta.servlet.jsp-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(me.champeau.openbeans:openbeans)
BuildRequires: mvn(me.sunlan:antlr4)
BuildRequires: mvn(me.sunlan:antlr4-runtime)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-antlr)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.ivy:ivy)
BuildRequires: mvn(org.commonmark:commonmark)
BuildRequires: mvn(org.commonmark:commonmark-ext-gfm-tables)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.jboss.bridger:bridger)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-analysis)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.ow2.asm:asm-util)
BuildRequires: mvn(org.pantsbuild:jarjar)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.vafer:jdependency)

%description
Groovy is a programming language for the Java platform with optional
static typing and compilation. It integrates with Java libraries and
provides closures, metaprogramming and support for scripting and
domain-specific languages.

%package all
Summary: Aggregate Maven POM for the Groovy modules
License: Apache-2.0
Group: Development/Java

%description all
Aggregate Maven POM for the Groovy modules.

%package ant
Summary: Groovy ant module
License: Apache-2.0
Group: Development/Java

%description ant
Groovy ant module.

%package astbuilder
Summary: Groovy astbuilder module
License: Apache-2.0
Group: Development/Java

%description astbuilder
Groovy astbuilder module.

%package bom
Summary: Maven bill of materials for the Groovy modules
License: Apache-2.0
Group: Development/Java

%description bom
Maven bill of materials for the Groovy modules.

%package callsite
Summary: Groovy callsite module
License: Apache-2.0
Group: Development/Java

%description callsite
Groovy callsite module.

%package cli-commons
Summary: Groovy cli commons module
License: Apache-2.0
Group: Development/Java

%description cli-commons
Groovy cli commons module.

%package cli-picocli
Summary: Groovy cli picocli module
License: Apache-2.0
Group: Development/Java

%description cli-picocli
Groovy cli picocli module.

%package concurrent-java
Summary: Groovy concurrent java module
License: Apache-2.0
Group: Development/Java

%description concurrent-java
Groovy concurrent java module.

%package console
Summary: Groovy console module
License: Apache-2.0
Group: Development/Java

%description console
Groovy console module.

%package contracts
Summary: Groovy contracts module
License: Apache-2.0
Group: Development/Java

%description contracts
Groovy contracts module.

%package csv
Summary: Groovy csv module
License: Apache-2.0
Group: Development/Java

%description csv
Groovy csv module.

%package datetime
Summary: Groovy datetime module
License: Apache-2.0
Group: Development/Java

%description datetime
Groovy datetime module.

%package dateutil
Summary: Groovy dateutil module
License: Apache-2.0
Group: Development/Java

%description dateutil
Groovy dateutil module.

%package docgenerator
Summary: Groovy docgenerator module
License: Apache-2.0
Group: Development/Java

%description docgenerator
Groovy docgenerator module.

%package ginq
Summary: Groovy ginq module
License: Apache-2.0
Group: Development/Java

%description ginq
Groovy ginq module.

%package grape-ivy
Summary: Groovy grape ivy module
License: Apache-2.0
Group: Development/Java

%description grape-ivy
Groovy grape ivy module.

%package groovydoc
Summary: Groovy groovydoc module
License: Apache-2.0 and MIT
Group: Development/Java

%description groovydoc
Groovy groovydoc module.

%package groovysh
Summary: Groovy groovysh module
License: Apache-2.0 and BSD-3-Clause
Group: Development/Java

%description groovysh
Groovy groovysh module.

%package http-builder
Summary: Groovy http builder module
License: Apache-2.0
Group: Development/Java

%description http-builder
Groovy http builder module.

%package jmx
Summary: Groovy jmx module
License: Apache-2.0
Group: Development/Java

%description jmx
Groovy jmx module.

%package json
Summary: Groovy json module
License: Apache-2.0
Group: Development/Java

%description json
Groovy json module.

%package jsr223
Summary: Groovy jsr223 module
License: Apache-2.0 and BSD-3-Clause
Group: Development/Java

%description jsr223
Groovy jsr223 module.

%package macro-library
Summary: Groovy macro library module
License: Apache-2.0
Group: Development/Java

%description macro-library
Groovy macro library module.

%package macro
Summary: Groovy macro module
License: Apache-2.0
Group: Development/Java

%description macro
Groovy macro module.

%package markdown
Summary: Groovy markdown module
License: Apache-2.0
Group: Development/Java

%description markdown
Groovy markdown module.

%package nio
Summary: Groovy nio module
License: Apache-2.0
Group: Development/Java

%description nio
Groovy nio module.

%package reactor
Summary: Groovy reactor module
License: Apache-2.0
Group: Development/Java

%description reactor
Groovy reactor module.

%package rxjava
Summary: Groovy rxjava module
License: Apache-2.0
Group: Development/Java

%description rxjava
Groovy rxjava module.

%package servlet
Summary: Groovy servlet module
License: Apache-2.0
Group: Development/Java

%description servlet
Groovy servlet module.

%package sql
Summary: Groovy sql module
License: Apache-2.0
Group: Development/Java

%description sql
Groovy sql module.

%package swing
Summary: Groovy swing module
License: Apache-2.0
Group: Development/Java

%description swing
Groovy swing module.

%package templates
Summary: Groovy templates module
License: Apache-2.0
Group: Development/Java

%description templates
Groovy templates module.

%package test-junit5
Summary: Groovy test junit5 module
License: Apache-2.0
Group: Development/Java

%description test-junit5
Groovy test junit5 module.

%package test
Summary: Groovy test module
License: Apache-2.0
Group: Development/Java

%description test
Groovy test module.

%package testng
Summary: Groovy testng module
License: Apache-2.0
Group: Development/Java

%description testng
Groovy testng module.

%package toml
Summary: Groovy toml module
License: Apache-2.0
Group: Development/Java

%description toml
Groovy toml module.

%package typecheckers
Summary: Groovy typecheckers module
License: Apache-2.0
Group: Development/Java

%description typecheckers
Groovy typecheckers module.

%package xml
Summary: Groovy xml module
License: Apache-2.0
Group: Development/Java

%description xml
Groovy xml module.

%package yaml
Summary: Groovy yaml module
License: Apache-2.0
Group: Development/Java

%description yaml
Groovy yaml module.

%{?javadoc_package}

%prep
%setup -q
%autopatch -p1

%mvn_package org.apache.groovy:groovy
%mvn_package org.apache.groovy:groovy-all all
%mvn_package org.apache.groovy:groovy-ant ant
%mvn_package org.apache.groovy:groovy-astbuilder astbuilder
%mvn_package org.apache.groovy:groovy-bom bom
%mvn_package org.apache.groovy:groovy-callsite callsite
%mvn_package org.apache.groovy:groovy-cli-commons cli-commons
%mvn_package org.apache.groovy:groovy-cli-picocli cli-picocli
%mvn_package org.apache.groovy:groovy-concurrent-java concurrent-java
%mvn_package org.apache.groovy:groovy-console console
%mvn_package org.apache.groovy:groovy-contracts contracts
%mvn_package org.apache.groovy:groovy-csv csv
%mvn_package org.apache.groovy:groovy-datetime datetime
%mvn_package org.apache.groovy:groovy-dateutil dateutil
%mvn_package org.apache.groovy:groovy-docgenerator docgenerator
%mvn_package org.apache.groovy:groovy-ginq ginq
%mvn_package org.apache.groovy:groovy-grape-ivy grape-ivy
%mvn_package org.apache.groovy:groovy-groovydoc groovydoc
%mvn_package org.apache.groovy:groovy-groovysh groovysh
%mvn_package org.apache.groovy:groovy-http-builder http-builder
%mvn_package org.apache.groovy:groovy-jmx jmx
%mvn_package org.apache.groovy:groovy-json json
%mvn_package org.apache.groovy:groovy-jsr223 jsr223
%mvn_package org.apache.groovy:groovy-macro-library macro-library
%mvn_package org.apache.groovy:groovy-macro macro
%mvn_package org.apache.groovy:groovy-markdown markdown
%mvn_package org.apache.groovy:groovy-nio nio
%mvn_package org.apache.groovy:groovy-reactor reactor
%mvn_package org.apache.groovy:groovy-rxjava rxjava
%mvn_package org.apache.groovy:groovy-servlet servlet
%mvn_package org.apache.groovy:groovy-sql sql
%mvn_package org.apache.groovy:groovy-swing swing
%mvn_package org.apache.groovy:groovy-templates templates
%mvn_package org.apache.groovy:groovy-test-junit5 test-junit5
%mvn_package org.apache.groovy:groovy-test test
%mvn_package org.apache.groovy:groovy-testng testng
%mvn_package org.apache.groovy:groovy-toml toml
%mvn_package org.apache.groovy:groovy-typecheckers typecheckers
%mvn_package org.apache.groovy:groovy-xml xml
%mvn_package org.apache.groovy:groovy-yaml yaml

%build
%gradle_publish --no-daemon --dependency-verification=off \
    -PskipQuality=true -PskipAsciidoc=true

%install
# Restrict registration to Groovy publications in the builder Maven repository.
%gradle_register --artifacts=groovy-
%gradle_register_bom --artifacts=groovy-
# The aggregate POM has neither a JAR nor dependencyManagement.
%mvn_artifact \
    %_mavenrepolocal/repository/org/apache/groovy/groovy-all/%version/groovy-all-%version.pom
%gradle_install
%gradle_register_javadoc --artifacts=groovy-

%files -f .mfiles
%doc LICENSE NOTICE licenses notices build/docs/javadoc/legal

%files all -f .mfiles-all

%files ant -f .mfiles-ant

%files astbuilder -f .mfiles-astbuilder

%files bom -f .mfiles-bom

%files callsite -f .mfiles-callsite

%files cli-commons -f .mfiles-cli-commons

%files cli-picocli -f .mfiles-cli-picocli

%files concurrent-java -f .mfiles-concurrent-java

%files console -f .mfiles-console

%files contracts -f .mfiles-contracts

%files csv -f .mfiles-csv

%files datetime -f .mfiles-datetime

%files dateutil -f .mfiles-dateutil

%files docgenerator -f .mfiles-docgenerator

%files ginq -f .mfiles-ginq

%files grape-ivy -f .mfiles-grape-ivy

%files groovydoc -f .mfiles-groovydoc

%files groovysh -f .mfiles-groovysh

%files http-builder -f .mfiles-http-builder

%files jmx -f .mfiles-jmx

%files json -f .mfiles-json

%files jsr223 -f .mfiles-jsr223

%files macro-library -f .mfiles-macro-library

%files macro -f .mfiles-macro

%files markdown -f .mfiles-markdown

%files nio -f .mfiles-nio

%files reactor -f .mfiles-reactor

%files rxjava -f .mfiles-rxjava

%files servlet -f .mfiles-servlet

%files sql -f .mfiles-sql

%files swing -f .mfiles-swing

%files templates -f .mfiles-templates

%files test-junit5 -f .mfiles-test-junit5

%files test -f .mfiles-test

%files testng -f .mfiles-testng

%files toml -f .mfiles-toml

%files typecheckers -f .mfiles-typecheckers

%files xml -f .mfiles-xml

%files yaml -f .mfiles-yaml

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 6.0.0-alt1
- Reintroduce into Sisyphus.
- New version.
- Build with xgradle.

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4.8-alt1_9jpp8
- build with new gradle

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4.8-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.8-alt1_5jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4.8-alt1_4jpp8
- new version

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.5-alt1_7jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.4-alt1_1jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_5jpp7
- new release

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_2jpp7
- update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.7-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt2_2jpp7
- applied repocop patches

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt1_2jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- disabled rebuild-java-repository

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script
