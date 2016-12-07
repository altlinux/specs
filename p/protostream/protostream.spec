Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: protobuf-c-compiler
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name protostream
%define version 1.0.0
%global namedreltag .Alpha7
%global namedversion %{version}%{?namedreltag}

%global debug_package %{nil}

Name:             protostream
Version:          1.0.0
Release:          alt1_0.10.Alpha7jpp8
Summary:          Infinispan ProtoStream
License:          ASL 2.0 and BSD
Url:              http://infinispan.org/
Source0:          https://github.com/infinispan/protostream/archive/%{namedversion}.tar.gz
Source1:          LICENSE.txt

BuildRequires:    maven-local
BuildRequires:    mvn(com.google.protobuf:protobuf-java)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires:    mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    protobuf-compiler
Source44: import.info
Patch33: protostream-1.0.0.Alpha7-alt-protoc-c.patch
BuildArch: noarch

%description
The Infinispan ProtoStream project

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n protostream-%{namedversion}

cp %{SOURCE1} .

%pom_xpath_set "pom:properties/pom:version.log4j" 12 parent
%pom_xpath_inject "pom:dependency[pom:artifactId = 'log4j']" '<version>${version.log4j}</version>' core
%pom_remove_plugin -r :maven-source-plugin
# Break build, use system setting
%pom_remove_plugin -r :maven-compiler-plugin
%patch33 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.10.Alpha7jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.8.Alpha7jpp8
- new version

