%define _unpackaged_files_terminate_build 1

Name: jaxb
Version: 4.0.9
Release: alt1

Summary: JAXB Reference Implementation
License: BSD-3-Clause
Group: Development/Java
URL: https://eclipse-ee4j.github.io/jaxb-ri/
VCS: https://github.com/eclipse-ee4j/jaxb-ri.git

Source: %name-%version.tar
Patch: %name-%version-security.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(com.sun.istack:istack-commons-runtime)
BuildRequires: mvn(com.github.relaxng:relaxngDatatype:2011.1)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.jvnet.staxex:stax-ex)
BuildRequires: mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires: mvn(net.java.dev.msv:xsdlib)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires: mvn(com.sun.istack:istack-commons-tools)
BuildRequires: mvn(xmlunit:xmlunit)
BuildRequires: mvn(com.github.javaparser:javaparser-core)
BuildRequires: mvn(org.eclipse.angus:angus-activation)
BuildRequires: junit

BuildArch: noarch

%description
Jakarta XML Binding gives Java developers an efficient and standard way of
mapping between XML and Java code. Java developers using Jakarta XML Binding
are more productive because they can write less code themselves and do not
have to be experts in XML. Jakarta XML Binding makes it easier for developers
to extend their applications with XML and Web Services technologies.

%package        codemodel
Group: Development/Java
Summary: Codemodel Core

%description    codemodel
The core functionality of the CodeModel java source code generation
library.

%package        codemodel-annotation-compiler
Group: Development/Java
Summary: Codemodel Annotation Compiler

%description    codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package        bom
Group: Development/Java
Summary: JAXB BOM

%description    bom
JAXB Bill of Materials (BOM)

%package        bom-ext
Group: Development/Java
Summary: JAXB BOM with ALL dependencies

%description    bom-ext
%summary.
If you are not sure - DON'T USE THIS BOM. Use com.sun.xml.bind:jaxb-bom instead.

%package        codemodel-parent
Group: Development/Java
Summary: Codemodel

%description    codemodel-parent
Java source code generation library.

%package        core
Group: Development/Java
Summary: JAXB Core

%description    core
JAXB Core module. Contains sources required by XJC, JXC and Runtime modules.

%package        external-parent
Group: Development/Java
Summary: JAXB External parent

%description    external-parent
JAXB External parent module. Contains sources for external components.

%package        jxc
Group: Development/Java
Summary: JAXB JXC

%description    jxc
JAXB schema generator.The *tool* to generate XML schema based on java classes.

%package        runtime-parent
Group: Development/Java
Summary: JAXB Runtime parent

%description    runtime-parent
JAXB Runtime parent module. Contains sources used during runtime processing.

%package        runtime
Group: Development/Java
Summary: JAXB Runtime

%description    runtime
JAXB (JSR 222) Reference Implementation.

%package        parent
Group: Development/Java
Summary: Jakarta XML Binding Implementation

%description    parent
Open source Implementation of Jakarta XML Binding (formerly JSR-222)

%package        txw-parent
Group: Development/Java
Summary: JAXB TXW parent

%description    txw-parent
JAXB TXW parent module. Contains sources for TXW component.

%package        xjc
Group: Development/Java
Summary: JAXB XJC

%description    xjc
JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources.
In other words: the *tool* to generate java classes for the given xml
representation.

%package        relaxng-datatype
Group: Development/Java
Summary: RelaxNG Datatype

%description    relaxng-datatype
RelaxNG Datatype library.

%package        rngom
Group: Development/Java
Summary: RELAX NG Object Model/Parser

%description    rngom
This package contains RELAX NG Object Model/Parser.

%package        txw2
Group: Development/Java
Summary: TXW2 Runtime

%description    txw2
TXW is a library that allows you to write XML documents.

%package        txwc2
Group: Development/Java
Summary: TXW2 Compiler

%description    txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package        xsom
Group: Development/Java
Summary: XML Schema Object Model

%description    xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package        legacy-core
Group: Development/Java
Summary: Legacy JAXB Core

%description    legacy-core
Old JAXB Core module. Contains sources required by XJC, JXC and Runtime modules
with dependencies.

%package        legacy-runtime
Group: Development/Java
Summary: Legacy JAXB Runtime

%description    legacy-runtime
Old JAXB Runtime module. Contains sources required for runtime processing.

%package        legacy-xjc
Group: Development/Java
Summary: Legacy JAXB XJC

%description    legacy-xjc
Old JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources.
In other words: the *tool* to generate java classes for the given xml
representation.

%package        legacy-jxc
Group: Development/Java
Summary: Legacy JAXB JXC

%description    legacy-jxc
Old JAXB schema generator.The *tool* to generate XML schema based on java
classes.

%package        osgi
Group: Development/Java
Summary: JAXB OSGi bundle

%description    osgi
Parent module of JAXB OSGI bundle.

%prep
%setup -n %name-%version
%autopatch -p1
cd jaxb-ri


%pom_remove_parent boms/bom external xsom codemodel

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep :compiler jxc bundles/jxc bundles/osgi/osgi
%pom_remove_dep :jaxb-release-documentation bundles/ri
%pom_remove_dep :jaxb-samples bundles/ri

# Felix JUnit4OSGi providers are unavailable; retain normal bundle tests.
%pom_remove_plugin -r :maven-junit4osgi-plugin bundles
%pom_remove_dep -r org.glassfish.jaxb:osgi-test-core bundles
%pom_remove_dep -r org.glassfish.jaxb:osgi-test-runtime bundles
%pom_remove_dep -r org.glassfish.jaxb:osgi-test-xjc bundles
%pom_remove_dep -r org.glassfish.jaxb:osgi-test-jxc bundles
%pom_remove_dep -r org.glassfish.jaxb:osgi-test-parent bundles
%pom_disable_module tests bundles/osgi

# missing docbkx-maven-plugin
%pom_disable_module docs

%pom_disable_module tools/osgi_tests

# Source classifier exclusion must precede legacy artifact mappings.
%mvn_package :::sources: __noinstall

# legacy
%mvn_package com.sun.xml.bind:jaxb-core legacy-core
%mvn_package com.sun.xml.bind:jaxb-impl legacy-runtime
%mvn_package com.sun.xml.bind:jaxb-xjc legacy-xjc
%mvn_package com.sun.xml.bind:jaxb-jxc legacy-jxc

%mvn_file com.sun.xml.bind:jaxb-core jaxb/legacy-jaxb-core
%mvn_file com.sun.xml.bind:jaxb-xjc  jaxb/legacy-jaxb-xjc
%mvn_file com.sun.xml.bind:jaxb-jxc  jaxb/legacy-jaxb-jxc

%mvn_file com.sun.xml.bind:jaxb-osgi jaxb/legacy-jaxb-osgi
%mvn_package com.sun.xml.bind:jaxb-osgi osgi

%mvn_package com.sun.xml.bind:jaxb-ri __noinstall
%mvn_package org.glassfish.jaxb:tests __noinstall
%mvn_package org.glassfish.jaxb:jaxb-bundles __noinstall
%mvn_package org.glassfish.jaxb:jaxb-osgi __noinstall

%build
cd jaxb-ri
%mvn_build -j -s -- \
    -Dproject.build.sourceEncoding=UTF-8 \
    -Dproject.reporting.outputEncoding=UTF-8

%install
cd jaxb-ri
%mvn_install

%jpackage_script com.sun.tools.xjc.XJCFacade "" "" "jaxb/jaxb-xjc:jaxb/jaxb-core:jaxb/jaxb-runtime:jaxb/xsom:jaxb/codemodel:jaxb/rngom:jaxb/relaxng-datatype:jaxb/txw2:jaxb-istack-commons/istack-commons-runtime:jaxb-istack-commons/istack-commons-tools:jaxb-dtd-parser/dtd-parser:jaxb-api:jakarta-activation" xjc true

%files core -f jaxb-ri/.mfiles-jaxb-core
%doc LICENSE.md NOTICE.md

%files codemodel -f jaxb-ri/.mfiles-codemodel
%files codemodel-annotation-compiler -f jaxb-ri/.mfiles-codemodel-annotation-compiler
%files bom -f jaxb-ri/.mfiles-jaxb-bom
%files bom-ext -f jaxb-ri/.mfiles-jaxb-bom-ext
%files codemodel-parent -f jaxb-ri/.mfiles-jaxb-codemodel-parent
%files external-parent -f jaxb-ri/.mfiles-jaxb-external-parent
%files jxc -f jaxb-ri/.mfiles-jaxb-jxc
%files runtime-parent -f jaxb-ri/.mfiles-jaxb-runtime-parent
%files runtime -f jaxb-ri/.mfiles-jaxb-runtime
%files parent -f jaxb-ri/.mfiles-jaxb-parent
%files txw-parent -f jaxb-ri/.mfiles-jaxb-txw-parent
%files xjc -f jaxb-ri/.mfiles-jaxb-xjc
%_bindir/xjc

%files relaxng-datatype -f jaxb-ri/.mfiles-relaxng-datatype
%files rngom -f jaxb-ri/.mfiles-rngom
%files txw2 -f jaxb-ri/.mfiles-txw2
%files txwc2 -f jaxb-ri/.mfiles-txwc2
%files xsom -f jaxb-ri/.mfiles-xsom
%files legacy-core -f jaxb-ri/.mfiles-legacy-core
%files legacy-runtime -f jaxb-ri/.mfiles-legacy-runtime
%files legacy-xjc -f jaxb-ri/.mfiles-legacy-xjc
%files legacy-jxc -f jaxb-ri/.mfiles-legacy-jxc
%files osgi -f jaxb-ri/.mfiles-osgi

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 4.0.9-alt1
- New version.
- Backport upstream XML parser hardening (CVE-2026-92877).

* Fri Aug 14 2026 Evgeniy Serov <scala@altlinux.org> 4.0.6-alt3
- Added XJC command-line launcher.

* Wed Aug 12 2026 Evgeniy Serov <scala@altlinux.org> 4.0.6-alt2
- Added legacy JAXB artifacts.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 4.0.6-alt1.1
- Cosmetic fixes.

* Fri Jan 16 2026 Evgeniy Serov <scala@altlinux.org> 4.0.6-alt1
- Updated to 4.0.6.
- Removed import.info.

* Thu Jun 09 2022 Igor Vlasenko <viy@altlinux.org> 2.3.5-alt1_5jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_6jpp11
- new version
