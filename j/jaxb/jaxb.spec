Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
Name:           jaxb
Version:        2.3.5
Release:        alt1_5jpp11
Summary:        JAXB Reference Implementation
# EDL-1.0 license is BSD-3-clause
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-ri
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-ri/archive/%{version}-RI/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(xmlunit:xmlunit)
Source44: import.info

%description
GlassFish JAXB Reference Implementation.

%package runtime
Group: Development/Java
Summary:        JAXB Runtime
%description runtime
JAXB (JSR 222) Reference Implementation

%package txw2
Group: Development/Java
Summary:        TXW2 Runtime
%description txw2
TXW is a library that allows you to write XML documents.

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

%package txwc2
Group: Development/Java
Summary:        TXW2 Compiler
%description txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package xsom
Group: Development/Java
Summary:        XML Schema Object Model
%description xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package relaxng-datatype
Group: Development/Java
Summary:        RelaxNG Datatype
%description relaxng-datatype
RelaxNG Datatype library.

%prep
%setup -q -n jaxb-ri-%{version}-RI
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git config gc.auto 0
git add --force .
git commit -q --allow-empty -a --author "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"

# Delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cd jaxb-ri
# Remove unnecessary dep on ee4j parent pom (it adds nothing to our downstream builds)
%pom_remove_parent boms/bom external xsom codemodel
# SCM from parent: org.eclipse.ee4j:project:1.0.7
%pom_xpath_inject 'pom:project' \
    '<scm>
      <connection>scm:git:git@github.com:eclipse-ee4j/ee4j.git</connection>
      <developerConnection>scm:git:git@github.com:eclipse-ee4j/ee4j.git</developerConnection>
      <url>https://github.com/eclipse-ee4j/ee4j</url>
    </scm>' external
# Fix dep on xml resolver
%pom_change_dep com.sun.org.apache.xml.internal:resolver xml-resolver:xml-resolver:1.2 xjc jxc
sed -i -e 's/com\.sun\.org\.apache\.xml\.internal\.resolver/org.apache.xml.resolver/' xjc/src/main/java/com/sun/tools/xjc/CatalogUtil.java
# Missing dep in Fedora: org.checkerframework:compiler
%pom_disable_module jxc
# Disable unneeded extra OSGi bundles
%pom_disable_module jxc bundles
%pom_disable_module osgi bundles
%pom_disable_module ri bundles
%pom_disable_module runtime bundles
%pom_disable_module xjc bundles
# Ignore osgi tests
%pom_disable_module tools/osgi_tests
# lack of dependency when building documentation
%pom_disable_module release-documentation docs
# Compatibility
%mvn_alias com.sun.xml.bind.external:relaxng-datatype com.github.relaxng:relaxngDatatype relaxngDatatype:relaxngDatatype
%mvn_alias org.glassfish.jaxb:jaxb-runtime org.glassfish.jaxb:jaxb-core
%mvn_alias org.glassfish.jaxb:jaxb-xjc com.sun.xml.bind:jaxb-xjc
%mvn_alias org.glassfish.jaxb:xsom com.sun.xsom:xsom
# Don't install aggregator and parent poms
%mvn_package :jaxb-bom __noinstall
%mvn_package :jaxb-bom-ext __noinstall
%mvn_package :jaxb-bundles __noinstall
%mvn_package :jaxb-codemodel-parent __noinstall
%mvn_package :jaxb-docs-parent __noinstall
%mvn_package :jaxb-external-parent __noinstall
%mvn_package :jaxb-parent __noinstall
%mvn_package :jaxb-runtime-parent __noinstall
%mvn_package :jaxb-samples __noinstall
%mvn_package :jaxb-txw-parent __noinstall
%mvn_package :jaxb-www __noinstall
cd -

%build
cd jaxb-ri
%mvn_build -s -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
cd -

%install
cd jaxb-ri
%mvn_install
cd -

%files codemodel -f jaxb-ri/.mfiles-codemodel
%doc --no-dereference LICENSE.md NOTICE.md
%files codemodel-annotation-compiler -f jaxb-ri/.mfiles-codemodel-annotation-compiler
%doc --no-dereference LICENSE.md NOTICE.md
%files relaxng-datatype -f jaxb-ri/.mfiles-relaxng-datatype
%doc --no-dereference LICENSE.md NOTICE.md
%files rngom -f jaxb-ri/.mfiles-rngom
%doc --no-dereference LICENSE.md NOTICE.md
%files runtime -f jaxb-ri/.mfiles-jaxb-runtime
%doc --no-dereference LICENSE.md NOTICE.md
%files txw2 -f jaxb-ri/.mfiles-txw2
%doc --no-dereference LICENSE.md NOTICE.md
%files txwc2 -f jaxb-ri/.mfiles-txwc2
%doc --no-dereference LICENSE.md NOTICE.md
%files xjc -f jaxb-ri/.mfiles-jaxb-xjc
%doc --no-dereference LICENSE.md NOTICE.md
%files xsom -f jaxb-ri/.mfiles-xsom
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Thu Jun 09 2022 Igor Vlasenko <viy@altlinux.org> 2.3.5-alt1_5jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_6jpp11
- new version

