Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name seam-solder
%define version 3.1.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          seam-solder
Version:       3.1.1
Release:       alt1_6jpp7
Summary:       A portable CDI extensions library
License:       ASL 2.0 and LGPLv2+
URL:           http://seamframework.org/Seam3/Solder
# git clone git://github.com/seam/solder seam-solder-3.1.1.Final
# (cd seam-solder-3.1.1.Final/ && git archive --format=tar --prefix=seam-solder-3.1.1.Final/ 3.1.1.Final | xz > ../seam-solder-3.1.1.Final.tar.xz)
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: seam-parent
BuildRequires: weld-parent
BuildRequires: geronimo-parent-poms

BuildRequires: cdi-api
BuildRequires: javassist
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-servlet-3.0-api
BuildRequires: log4j
BuildRequires: slf4j

%if 0
# testsuite module deps
BuildRequires: mvn(org.jboss.arquillian.junit:arquillian-junit-container)
BuildRequires: mvn(org.jboss.seam.test:weld-ee-embedded)
# docs (solder-reference-guide) module deps
# https://github.com/pressgang
BuildRequires: mvn(org.jboss.maven.plugins:maven-jdocbook-plugin)
%endif

# test deps
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: mockito

BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
A portable CDI extensions library for developing CDI applications,
frameworks or other extensions.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin org.codehaus.mojo:emma-maven-plugin
%pom_remove_plugin org.sonatype.maven.plugin:emma4it-maven-plugin

# unavailable deps
# org.jboss.seam.test:weld-ee-embedded-1.1
%pom_disable_module testsuite

# disabled, this module is jboss-logging re-packaged library, with shade plugin. use jboss-logging directly
%pom_disable_module logging
%pom_remove_dep org.jboss.solder:solder-logging api
%pom_add_dep org.jboss.logging:jboss-logging api
sed -i "s|org.jboss.solder.logging.internal|org.jboss.logging|" $(find api -name "*.java") \
  tooling/src/main/java/org/jboss/solder/tooling/SolderLoggers.java

# unavailable pom
%pom_remove_dep org.jboss.seam:seam-bom

# TODO require jboss-logging-tools <= 1.0.3
%pom_disable_module tooling
%pom_remove_dep :solder-tooling impl

%pom_remove_dep org.jboss.logging:jboss-logging-generator tooling
%pom_add_dep org.jboss.logging:jboss-logging-processor tooling

sed -i "s|org.jboss.logging.generator|org.jboss.logging.processor|" \
  tooling/src/main/java/org/jboss/solder/tooling/SolderLoggers.java \
  tooling/src/main/java/org/jboss/solder/tooling/SolderAnnotations.java \
  tooling/src/main/java/org/jboss/solder/tooling/AptHelperImpl.java \
  tooling/src/main/resources/META-INF/services/javax.annotation.processing.Processor

cp -p tooling/src/main/resources/META-INF/services/org.jboss.logging.generator.Annotations \
  tooling/src/main/resources/META-INF/services/org.jboss.logging.processor.Annotations
cp -p tooling/src/main/resources/META-INF/services/org.jboss.logging.generator.Loggers \
  tooling/src/main/resources/META-INF/services/org.jboss.logging.processor.Loggers
cp -p tooling/src/main/resources/META-INF/services/org.jboss.logging.generator.apt.AptHelper \
  tooling/src/main/resources/META-INF/services/org.jboss.logging.processor.apt.AptHelper

# this test fails
rm -r impl/src/test/java/org/jboss/solder/test/reflection/annotated/AnnotatedTypeBuilderTest.java

cp -p dist/src/main/assembly/license.txt .
cp -p dist/src/main/assembly/notice.txt .
sed -i 's/\r//' license.txt notice.txt

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc license.txt notice.txt readme.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_6jpp7
- new release

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp7
- new release

