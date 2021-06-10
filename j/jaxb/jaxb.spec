Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionally build with a minimal dependency set
%bcond_with jp_minimal

Name:           jaxb
Version:        2.3.3
Release:        alt1_6jpp11
Summary:        JAXB Reference Implementation
# EDL-1.0 license is BSD-3-clause
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-ri
Source0:        https://github.com/eclipse-ee4j/jaxb-ri/archive/%{version}-RI.tar.gz

# Avoid hard runtime dep on istack-commons from the main implementation jar
Patch0:         0001-Avoid-runtime-dependency-on-istack-commons-from-main.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%if %{without jp_minimal}
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(xmlunit:xmlunit)
%endif

%global obs_vr 2.3.3-1

BuildArch:      noarch
Source44: import.info

%description
GlassFish JAXB Reference Implementation.

%package runtime
Group: Development/Java
Summary:        JAXB Runtime
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb = %{version}-%{release}
Obsoletes:      glassfish-jaxb < %{obs_vr}
Provides:       glassfish-jaxb-runtime = %{version}-%{release}
Obsoletes:      glassfish-jaxb-runtime < %{obs_vr}
# -core subpackage was merged into -runtime during F33
Provides:       glassfish-jaxb-core = %{version}-%{release}
Obsoletes:      glassfish-jaxb-core < %{obs_vr}
# Obsolete module gone away for good
Obsoletes:      glassfish-jaxb1-impl < %{obs_vr}
# Unable to ship any longer due to missing dep: org.checkerframework:compiler
Obsoletes:      glassfish-jaxb-jxc < %{obs_vr}
# Disable javadocs for now, due to https://github.com/fedora-java/xmvn/issues/58
Obsoletes:      glassfish-jaxb-javadoc < %{obs_vr}
# No longer shipping parent pom packages
Obsoletes:      glassfish-jaxb-codemodel-parent < %{obs_vr}
Obsoletes:      glassfish-jaxb-external-parent < %{obs_vr}
Obsoletes:      glassfish-jaxb-parent < %{obs_vr}
Obsoletes:      glassfish-jaxb-runtime-parent < %{obs_vr}
Obsoletes:      glassfish-jaxb-txw-parent < %{obs_vr}

%if %{with jp_minimal}
# Obsolete packages that are not shipped in the minimal build
Obsoletes:      glassfish-jaxb-bom                           < %{obs_vr}
Obsoletes:      glassfish-jaxb-bom-ext                       < %{obs_vr}
Obsoletes:      glassfish-jaxb-codemodel                     < %{obs_vr}
Obsoletes:      glassfish-jaxb-codemodel-annotation-compiler < %{obs_vr}
Obsoletes:      glassfish-jaxb-rngom                         < %{obs_vr}
Obsoletes:      glassfish-jaxb-txwc2                         < %{obs_vr}
Obsoletes:      glassfish-jaxb-xjc                           < %{obs_vr}
Obsoletes:      %{name}-bom                           < %{obs_vr}
Obsoletes:      %{name}-bom-ext                       < %{obs_vr}
Obsoletes:      %{name}-codemodel                     < %{obs_vr}
Obsoletes:      %{name}-codemodel-annotation-compiler < %{obs_vr}
Obsoletes:      %{name}-rngom                         < %{obs_vr}
Obsoletes:      %{name}-txwc2                         < %{obs_vr}
Obsoletes:      %{name}-xjc                           < %{obs_vr}
Obsoletes:      %{name}-xsom                          < %{obs_vr}
Obsoletes:      %{name}-relaxng-datatype              < %{obs_vr}
%endif

%description runtime
JAXB (JSR 222) Reference Implementation

%package txw2
Group: Development/Java
Summary:        TXW2 Runtime
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-txw2 = %{version}-%{release}
Obsoletes:      glassfish-jaxb-txw2 < %{obs_vr}

%description txw2
TXW is a library that allows you to write XML documents.

%package impl
Group: Development/Java
Summary:        Old JAXB Runtime

%description impl
Old JAXB Runtime module. Contains sources required for runtime processing.
Standalone bundle suitable for use in OSGi runtimes.

%if %{without jp_minimal}
%package codemodel
Group: Development/Java
Summary:        Codemodel Core
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-codemodel = %{version}-%{release}
Obsoletes:      glassfish-jaxb-codemodel < %{obs_vr}

%description codemodel
The core functionality of the CodeModel java source code generation
library.

%package codemodel-annotation-compiler
Group: Development/Java
Summary:        Codemodel Annotation Compiler
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-codemodel-annotation-compiler = %{version}-%{release}
Obsoletes:      glassfish-jaxb-codemodel-annotation-compiler < %{obs_vr}

%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package bom
Group: Development/Java
Summary:        JAXB BOM
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-bom = %{version}-%{release}
Obsoletes:      glassfish-jaxb-bom < %{obs_vr}

%description bom
JAXB Bill of Materials (BOM)

%package bom-ext
Group: Development/Java
Summary:        JAXB BOM with all dependencies
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-bom-ext = %{version}-%{release}
Obsoletes:      glassfish-jaxb-bom-ext < %{obs_vr}

%description bom-ext
JAXB Bill of Materials (BOM) with all dependencies.

%package xjc
Group: Development/Java
Summary:        JAXB XJC
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-xjc = %{version}-%{release}
Obsoletes:      glassfish-jaxb-xjc < %{obs_vr}

%description xjc
JAXB Binding Compiler. Contains source code needed for binding
customization files into java sources. In other words: the tool to
generate java classes for the given xml representation.

%package rngom
Group: Development/Java
Summary:        RELAX NG Object Model/Parser
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-rngom = %{version}-%{release}
Obsoletes:      glassfish-jaxb-rngom < %{obs_vr}

%description rngom
This package contains RELAX NG Object Model/Parser.

%package txwc2
Group: Development/Java
Summary:        TXW2 Compiler
# Package renamed from glassfish-jaxb with version 2.3.3-1 in F33
Provides:       glassfish-jaxb-txwc2 = %{version}-%{release}
Obsoletes:      glassfish-jaxb-txwc2 < %{obs_vr}

%description txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package xsom
Group: Development/Java
Summary:        XML Schema Object Model
# Xsom package was merged upstream into jaxb
Provides:       xsom = %{version}-%{release}
Obsoletes:      xsom < 20140514-7
Provides:       xsom-javadoc = %{version}-%{release}
Obsoletes:      xsom-javadoc < 20140514-7

%description xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package relaxng-datatype
Group: Development/Java
Summary:        RelaxNG Datatype
# RelaxNG was subsumed into jaxb upstream
Provides:       relaxngDatatype = 1:%{version}-%{release}
Obsoletes:      relaxngDatatype < 2011.1-16
Provides:       relaxngDatatype-javadoc = 1:%{version}-%{release}
Obsoletes:      relaxngDatatype-javadoc < 2011.1-16

%description relaxng-datatype
RelaxNG Datatype library.
%endif

%prep
%setup -q -n jaxb-ri-%{version}-RI

# Avoid unnecessary runtime dependency on istack commons
%patch0 -p1

pushd jaxb-ri

# Remove unnecessary dep on ee4j parent pom (it adds nothing to our downstream builds)
%pom_remove_parent boms/bom codemodel external xsom

# Fix dep on xml resolver
%pom_change_dep -r com.sun.org.apache.xml.internal:resolver xml-resolver:xml-resolver:1.2
sed -i -e 's/com\.sun\.org\.apache\.xml\.internal\.resolver/org.apache.xml.resolver/' xjc/src/main/java/com/sun/tools/xjc/CatalogUtil.java

# Plug-ins not useful for RPM builds
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Disable unneeded extra OSGi bundles
%pom_disable_module xjc bundles
%pom_disable_module jxc bundles
%pom_disable_module ri bundles
%pom_disable_module osgi bundles

# Missing dep in Fedora: org.checkerframework:compiler
%pom_disable_module jxc

%if %{with jp_minimal}
# For minimal build disable all modules with extra deps
%pom_disable_module external
%pom_disable_module compiler txw
%pom_disable_module xjc
%pom_disable_module xsom
%pom_disable_module codemodel
# Don't run tests for minimal build
%pom_remove_plugin -r :maven-failsafe-plugin
# Remove optional extra marshaller implementations for minimal build
%pom_remove_dep org.jvnet.staxex:stax-ex runtime/impl bundles/runtime
%pom_remove_dep com.sun.xml.fastinfoset:FastInfoset runtime/impl bundles/runtime
rm runtime/impl/src/main/java/com/sun/xml/bind/v2/runtime/unmarshaller/{FastInfoset,StAXEx}Connector.java
rm runtime/impl/src/main/java/com/sun/xml/bind/v2/runtime/output/{FastInfoset,StAXEx}StreamWriterOutput.java
sed -i -e '/org.jvnet.staxex/d' -e '/com.sun.xml.fastinfoset/d' runtime/impl/src/main/java/module-info.java bundles/runtime/src/main/java/module-info.java
%endif

# Fastinfoset and Staxex are optional deps, reflect that in OSGi metadata
sed -i -e '/<Import-Package>/aorg.jvnet.staxex;resolution:=optional,org.jvnet.fastinfoset.stax;resolution:=optional,com.sun.xml.fastinfoset.stax;resolution:=optional,' bundles/runtime/pom.xml

# Ignore tests that require Internet connections
sed -i -e 's/void testParse/void ignoreTestParse/' xsom/src/test/java/XSOMParserTest.java
# Ignore tests that require an ancient version of javaparser (version in Fedora is too new)
%pom_remove_dep com.google.code.javaparser:javaparser codemodel/codemodel
rm codemodel/codemodel/src/test/java/com/sun/codemodel/tests/JDefinedClassInstanceInitTest.java
# Ignore tests requiring org.jmockit:jmockit which is not in Fedora
%pom_remove_dep -r org.jmockit:jmockit
rm xjc/src/test/java/com/sun/tools/xjc/addon/code_injector/PluginImplTest.java
# Missing test dep for OSGi tests
%pom_remove_plugin org.apache.felix:maven-junit4osgi-plugin bundles/runtime

# Compatibility aliases
%mvn_alias org.glassfish.jaxb:jaxb-xjc "com.sun.xml.bind:jaxb-xjc"
%mvn_alias org.glassfish.jaxb:jaxb-runtime org.glassfish.jaxb:jaxb-core
%mvn_alias org.glassfish.jaxb:xsom com.sun.xsom:xsom
%mvn_alias com.sun.xml.bind.external:relaxng-datatype com.github.relaxng:relaxngDatatype relaxngDatatype:relaxngDatatype

# Don't install aggregator and parent poms
%mvn_package com.sun.xml.bind.mvn: __noinstall
%mvn_package :::sources __noinstall

%if %{with jp_minimal}
# Don't install aggregator poms or boms for minimal build
%mvn_package :jaxb-bom* __noinstall
%endif
popd

%build
pushd jaxb-ri
%if %{with jp_minimal}
# Don't run tests for minimal build
%mvn_build -j -s -f -- -Ddev -DbuildNumber=unknown -Drelaxng.version=%{version}
%else
%mvn_build -j -s -- -Ddev -DbuildNumber=unknown -Drelaxng.version=%{version}
%endif
popd

%install
pushd jaxb-ri
%mvn_install
popd

%files runtime -f jaxb-ri/.mfiles-jaxb-runtime
%doc --no-dereference LICENSE.md NOTICE.md

%files txw2 -f jaxb-ri/.mfiles-txw2
%doc --no-dereference LICENSE.md NOTICE.md

%files impl -f jaxb-ri/.mfiles-jaxb-impl
%doc --no-dereference LICENSE.md NOTICE.md

%if %{without jp_minimal}
%files codemodel -f jaxb-ri/.mfiles-codemodel
%doc --no-dereference LICENSE.md NOTICE.md

%files codemodel-annotation-compiler -f jaxb-ri/.mfiles-codemodel-annotation-compiler

%files bom -f jaxb-ri/.mfiles-jaxb-bom
%doc --no-dereference LICENSE.md NOTICE.md

%files bom-ext -f jaxb-ri/.mfiles-jaxb-bom-ext

%files xjc -f jaxb-ri/.mfiles-jaxb-xjc

%files rngom -f jaxb-ri/.mfiles-rngom
%doc --no-dereference LICENSE.md NOTICE.md

%files txwc2 -f jaxb-ri/.mfiles-txwc2
%doc --no-dereference LICENSE.md NOTICE.md

%files xsom -f jaxb-ri/.mfiles-xsom

%files relaxng-datatype -f jaxb-ri/.mfiles-relaxng-datatype
%endif

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_6jpp11
- new version

