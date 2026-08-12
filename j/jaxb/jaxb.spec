Name:           jaxb
Version:        4.0.6
Release:        alt2

Summary:        JAXB Reference Implementation
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://eclipse-ee4j.github.io/jaxb-ri/
VCS:            https://github.com/eclipse-ee4j/jaxb-ri

Source:         %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.github.relaxng:relaxngDatatype:2011.1)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(xmlunit:xmlunit)
BuildRequires:  mvn(com.google.code.javaparser:javaparser)
BuildRequires:  mvn(org.eclipse.angus:angus-activation)

BuildArch:      noarch

%description
Jakarta XML Binding gives Java developers an efficient and standard way of
mapping between XML and Java code. Java developers using Jakarta XML Binding
are more productive because they can write less code themselves and do not
have to be experts in XML. Jakarta XML Binding makes it easier for developers
to extend their applications with XML and Web Services technologies.

%package        codemodel
Group:          Development/Java
Summary:        Codemodel Core

%description    codemodel
The core functionality of the CodeModel java source code generation
library.

%package        codemodel-annotation-compiler
Group:          Development/Java
Summary:        Codemodel Annotation Compiler

%description    codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package        bom
Group:          Development/Java
Summary:        JAXB BOM

%description    bom
JAXB Bill of Materials (BOM)

%package        bom-ext
Group:          Development/Java
Summary:        JAXB BOM with ALL dependencies

%description    bom-ext
%summary.
If you are not sure - DON'T USE THIS BOM. Use com.sun.xml.bind:jaxb-bom instead.

%package        codemodel-parent
Group:          Development/Java
Summary:        Codemodel

%description    codemodel-parent
Java source code generation library.

%package        core
Group:          Development/Java
Summary:        JAXB Core

%description    core
JAXB Core module. Contains sources required by XJC, JXC and Runtime modules.

%package        external-parent
Group:          Development/Java
Summary:        JAXB External parent

%description    external-parent
JAXB External parent module. Contains sources for external components.

%package        jxc
Group:          Development/Java
Summary:        JAXB JXC

%description    jxc
JAXB schema generator.The *tool* to generate XML schema based on java classes.

%package        runtime-parent
Group:          Development/Java
Summary:        JAXB Runtime parent

%description    runtime-parent
JAXB Runtime parent module. Contains sources used during runtime processing.

%package        runtime
Group:          Development/Java
Summary:        JAXB Runtime

%description    runtime
JAXB (JSR 222) Reference Implementation.

%package        parent
Group:          Development/Java
Summary:        Jakarta XML Binding Implementation

%description    parent
Open source Implementation of Jakarta XML Binding (formerly JSR-222)

%package        txw-parent
Group:          Development/Java
Summary:        JAXB TXW parent

%description    txw-parent
JAXB TXW parent module. Contains sources for TXW component.

%package        xjc
Group:          Development/Java
Summary:        JAXB XJC

%description    xjc
JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources.
In other words: the *tool* to generate java classes for the given xml
representation.

%package        relaxng-datatype
Group:          Development/Java
Summary:        RelaxNG Datatype

%description    relaxng-datatype
RelaxNG Datatype library.

%package        rngom
Group:          Development/Java
Summary:        RELAX NG Object Model/Parser

%description    rngom
This package contains RELAX NG Object Model/Parser.

%package        txw2
Group:          Development/Java
Summary:        TXW2 Runtime

%description    txw2
TXW is a library that allows you to write XML documents.

%package        txwc2
Group:          Development/Java
Summary:        TXW2 Compiler

%description    txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package        xsom
Group:          Development/Java
Summary:        XML Schema Object Model

%description    xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package        legacy-core
Group:          Development/Java
Summary:        Legacy JAXB Core

%description    legacy-core
Old JAXB Core module. Contains sources required by XJC, JXC and Runtime modules
with dependencies.

%package        legacy-runtime
Group:          Development/Java
Summary:        Legacy JAXB Runtime

%description    legacy-runtime
Old JAXB Runtime module. Contains sources required for runtime processing.

%package        legacy-xjc
Group:          Development/Java
Summary:        Legacy JAXB XJC

%description    legacy-xjc
Old JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources.
In other words: the *tool* to generate java classes for the given xml
representation.

%package        legacy-jxc
Group:          Development/Java
Summary:        Legacy JAXB JXC

%description    legacy-jxc
Old JAXB schema generator.The *tool* to generate XML schema based on java
classes.

%package        osgi
Group:          Development/Java
Summary:        JAXB OSGi bundle

%description    osgi
Parent module of JAXB OSGI bundle.

%prep
%setup -n %name-%version/jaxb-ri

rm xsom/src/test/java/com/sun/xml/xsom/test/XSOMParserTest.java
rm codemodel/codemodel/src/test/java/com/sun/codemodel/tests/JDefinedClassInstanceInitTest.java

%pom_remove_parent boms/bom external xsom codemodel

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep :compiler jxc bundles/jxc bundles/osgi/osgi
%pom_remove_dep :jaxb-release-documentation bundles/ri
%pom_remove_dep :jaxb-samples bundles/ri

%pom_remove_plugin :maven-junit4osgi-plugin bundles/core

# missing docbkx-maven-plugin
%pom_disable_module docs

%pom_disable_module tools/osgi_tests

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
%mvn_package com.sun.xml.bind.mvn:tests __noinstall
%mvn_package com.sun.xml.bind.mvn:jaxb-bundles __noinstall
%mvn_package com.sun.xml.bind.mvn:jaxb-osgi __noinstall

%build
%mvn_build -j -s -f -- -Dproject.build.sourceEncoding=UTF-8 -Dproject.reporting.outputEncoding=UTF-8

%install
%mvn_install

%files core -f .mfiles-jaxb-core
%doc ../LICENSE.md ../NOTICE.md

%files codemodel -f .mfiles-codemodel
%files codemodel-annotation-compiler -f .mfiles-codemodel-annotation-compiler
%files bom -f .mfiles-jaxb-bom
%files bom-ext -f .mfiles-jaxb-bom-ext
%files codemodel-parent -f .mfiles-jaxb-codemodel-parent
%files external-parent -f .mfiles-jaxb-external-parent
%files jxc -f .mfiles-jaxb-jxc
%files runtime-parent -f .mfiles-jaxb-runtime-parent
%files runtime -f .mfiles-jaxb-runtime
%files parent -f .mfiles-jaxb-parent
%files txw-parent -f .mfiles-jaxb-txw-parent
%files xjc -f .mfiles-jaxb-xjc
%files relaxng-datatype -f .mfiles-relaxng-datatype
%files rngom -f .mfiles-rngom
%files txw2 -f .mfiles-txw2
%files txwc2 -f .mfiles-txwc2
%files xsom -f .mfiles-xsom
%files legacy-core -f .mfiles-legacy-core
%files legacy-runtime -f .mfiles-legacy-runtime
%files legacy-xjc -f .mfiles-legacy-xjc
%files legacy-jxc -f .mfiles-legacy-jxc
%files osgi -f .mfiles-osgi

%changelog
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
