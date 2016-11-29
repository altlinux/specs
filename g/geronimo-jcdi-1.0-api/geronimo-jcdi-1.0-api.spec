Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spec_ver 1.0
%global spec_name geronimo-jcdi_%{spec_ver}_spec
Name:          geronimo-jcdi-1.0-api
Version:       1.0
Release:       alt1_6jpp8
Summary:       Apache Geronimo Java Contexts and Dependency Injection (JSR-299) Spec API
License:       ASL 2.0
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz

BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-annotation_1.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
# bundle-plugin requires
#BuildRequires: mvn(org.sonatype.aether:aether)

BuildArch:     noarch
Source44: import.info

%description
Apache Geronimo implementation of the JSR-299 Context and
Dependency Injection for the Java EE Platform.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{version}

%pom_xpath_set "pom:project/pom:parent/pom:groupId" org.apache.geronimo.specs
%pom_xpath_set "pom:project/pom:parent/pom:artifactId" specs
%pom_xpath_set "pom:project/pom:parent/pom:version" 1.4
%pom_xpath_inject "pom:project/pom:parent" "<relativePath>../pom.xml</relativePath>"

%pom_remove_dep org.apache.geronimo.specs:geronimo-el_2.2_spec
%pom_add_dep org.jboss.spec.javax.el:jboss-el-api_2.2_spec::provided

%pom_remove_dep org.apache.geronimo.specs:geronimo-atinject_1.0_spec
%pom_add_dep javax.inject:javax.inject::provided

%pom_remove_dep org.apache.geronimo.specs:geronimo-interceptor_1.1_spec
%pom_add_dep org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.1_spec::provided

for s in src/main/java/javax/enterprise/inject/spi/BeanManager.java \
  src/main/java/javax/enterprise/context/RequestScoped.java \
  src/main/java/javax/enterprise/context/spi/Context.java \
  src/main/java/javax/enterprise/util/AnnotationLiteral.java; do
 native2ascii -encoding UTF8 ${s} ${s}
done

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp8
- new fc release

