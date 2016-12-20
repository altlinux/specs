Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging-tools1
%define version 1.2.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging-tools1
Version:          1.2.1
Release:          alt1_1jpp8
Summary:          JBoss Logging I18n Annotation Processor
# ASL 2.0: ./annotations/src/main/java/org/jboss/logging/annotations/*.java
# Source files without license headers https://issues.jboss.org/browse/LOGTOOL-113
License:          ASL 2.0 and LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logging-tools
Source0:          https://github.com/jboss-logging/jboss-logging-tools/archive/%{namedversion}.tar.gz
# Not available license file https://issues.jboss.org/browse/LOGTOOL-107 thanks to jamezp
Patch0:           https://github.com/jboss-logging/jboss-logging-tools/commit/9a07a05d8437948c353fd13ce3311d0c5c4c0a79.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.jdeparser:jdeparser:1)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.testng:testng)
Source44: import.info

%description
This package contains JBoss Logging I18n Annotation Processor

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-tools-%{namedversion}
%patch0 -p1

cp -p annotations/src/main/resources/META-INF/LICENSE.txt LICENSE-ASL.txt
cp -p processor/src/main/resources/META-INF/LICENSE.txt LICENSE-LGPL.txt

%pom_disable_module processor-tests

%pom_xpath_set pom:properties/pom:version.org.jboss.jdeparser 1
%pom_xpath_inject pom:project "<version>%{namedversion}</version>" annotations
%pom_xpath_inject pom:project "<version>%{namedversion}</version>" processor
%pom_change_dep :jdeparser ::1 processor
%pom_change_dep :jboss-logging-annotations ::'%{namedversion}' processor

%mvn_compat_version : %{namedversion} %{version} 1

%build
# @ random java.lang.ArrayIndexOutOfBoundsException: 1
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-ASL.txt LICENSE-LGPL.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-LGPL.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1jpp8
- new version

