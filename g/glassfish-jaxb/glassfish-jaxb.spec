Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           glassfish-jaxb
Version:        2.2.11
Release:        alt1_4jpp8
Summary:        JAXB Reference Implementation

License:        CDDL and GPLv2 with exceptions
URL:            http://jaxb.java.net

Source0:        https://jaxb.java.net/%{version}/jaxb-ri-%{version}.src.zip
Patch0:         txw2-args4j.patch

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.javaparser:javaparser)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(com.sun.xsom:xsom)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(xmlunit:xmlunit)

Requires:       glassfish-jaxb1-impl = %{version}
Requires:       %{name}-bom = %{version}
Requires:       %{name}-bom-ext = %{version}
Requires:       %{name}-codemodel = %{version}
Requires:       %{name}-codemodel-annotation-compiler = %{version}
Requires:       %{name}-codemodel-parent = %{version}
Requires:       %{name}-core = %{version}
Requires:       %{name}-external-parent = %{version}
Requires:       %{name}-jxc = %{version}
Requires:       %{name}-parent = %{version}
Requires:       %{name}-rngom = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       %{name}-runtime-parent = %{version}
Requires:       %{name}-txw2 = %{version}
Requires:       %{name}-txwc2 = %{version}
Requires:       %{name}-txw-parent = %{version}
Requires:       %{name}-xjc = %{version}

BuildArch:      noarch
Source44: import.info

%description
GlassFish JAXB Reference Implementation.

%package codemodel
Group: Development/Java
Summary:        Codemodel Core

%description codemodel
The core functionality of the CodeModel java source code generation
library.

%package codemodel-annotation-compiler
Group: Development/Java
Summary:        Codemodel Annotation Compiler

%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package -n glassfish-jaxb1-impl
Group: Development/Java
Summary:        JAXB1 Runtime

%description -n glassfish-jaxb1-impl
Runtime classes for JAXB1 runtime implementation.

%package bom
Group: Development/Java
Summary:        JAXB BOM

%description bom
JAXB Bill of Materials (BOM)

%package bom-ext
Group: Development/Java
Summary:        JAXB BOM with all dependencies

%description bom-ext
JAXB Bill of Materials (BOM) with all dependencies.

%package codemodel-parent
Group: Development/Java
Summary:        Codemodel parent POM

%description codemodel-parent
This package contains codemodel parent POM.

%package core
Group: Development/Java
Summary:        JAXB Core

%description core
JAXB Core module. Contains sources required by XJC, JXC and Runtime
modules.

%package external-parent
Group: Development/Java
Summary:        JAXB External parent POM

%description external-parent
JAXB External parent POM.

%package jxc
Group: Development/Java
Summary:        JAXB schema generator

%description jxc
The tool to generate XML schema based on java classes.

%package parent
Group: Development/Java
Summary:        JAXB parent POM

%description parent
This package contains parent POM.

%package runtime
Group: Development/Java
Summary:        JAXB Runtime

%description runtime
JAXB (JSR 222) Reference Implementation

%package runtime-parent
Group: Development/Java
Summary:        JAXB Runtime parent POM

%description runtime-parent
This package contains Runtime parent POM.

%package txw-parent
Group: Development/Java
Summary:        JAXB TXW parent POM

%description txw-parent
This package contains TXW parent POM.

%package xjc
Group: Development/Java
Summary:        JAXB XJC

%description xjc
JAXB Binding Compiler. Contains source code needed for binding
customization files into java sources. In other words: the tool to
generate java classes for the given xml representation.

%package rngom
Group: Development/Java
Summary:        RELAX NG Object Model/Parser

%description rngom
This package contains RELAX NG Object Model/Parser.

%package txw2
Group: Development/Java
Summary:        TXW2 Runtime

%description txw2
TXW is a library that allows you to write XML documents.

%package txwc2
Group: Development/Java
Summary:        TXW2 Compiler

%description txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c

%patch0 -p1

%pom_disable_module bundles

%pom_remove_dep com.sun:tools
%pom_add_dep_mgmt com.sun:tools
%pom_remove_dep com.sun:tools jxc
%pom_add_dep com.sun:tools jxc

%pom_remove_dep com.sun.xml.bind:jaxb-release-documentation bundles/ri
%pom_remove_dep com.sun.xml.bind:jaxb-samples bundles/ri

%pom_remove_plugin :gfnexus-maven-plugin
%pom_remove_plugin :maven-site-plugin

%mvn_alias org.glassfish.jaxb:jaxb-runtime "com.sun.xml.bind:jaxb-impl"
%mvn_alias org.glassfish.jaxb:jaxb-xjc "com.sun.xml.bind:jaxb-xjc"

%build
%mvn_build -f -s -- -Ddev

%install
%mvn_install

%files
%doc License.txt licenceheader.txt License.html

%files codemodel -f .mfiles-codemodel
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files codemodel-annotation-compiler -f .mfiles-codemodel-annotation-compiler
%dir %{_javadir}/%{name}

%files -n glassfish-jaxb1-impl -f .mfiles-jaxb1-impl
%dir %{_javadir}/%{name}

%files bom -f .mfiles-jaxb-bom
%doc License.txt licenceheader.txt License.html

%files bom-ext -f .mfiles-jaxb-bom-ext

%files codemodel-parent -f .mfiles-jaxb-codemodel-parent

%files core -f .mfiles-jaxb-core
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files external-parent -f .mfiles-jaxb-external-parent

%files jxc -f .mfiles-jaxb-jxc
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files parent -f .mfiles-jaxb-parent

%files runtime -f .mfiles-jaxb-runtime
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files runtime-parent -f .mfiles-jaxb-runtime-parent

%files txw-parent -f .mfiles-jaxb-txw-parent

%files xjc -f .mfiles-jaxb-xjc
%dir %{_javadir}/%{name}

%files rngom -f .mfiles-rngom
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files txw2 -f .mfiles-txw2
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files txwc2 -f .mfiles-txwc2
%dir %{_javadir}/%{name}
%doc License.txt licenceheader.txt License.html

%files javadoc -f .mfiles-javadoc
%doc License.txt licenceheader.txt License.html


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_3jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt1_3jpp7
- fc version
- jaxb 2.2 api
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt3_7jpp6
- built with java 6

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt2_7jpp6
- removed compat symlink

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt1_7jpp6
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_7jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_6jpp5
- converted from JPackage by jppimport script

