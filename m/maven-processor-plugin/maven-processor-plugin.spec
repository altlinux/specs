# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          maven-processor-plugin
Version:       2.1.1
Release:       alt1_1jpp7
Summary:       Maven Processor Plugin
Group:         Development/Java
# some classes and pom file are annotated with ASL 2.0
# and the site here it is hosted says "GNU Lesser GPL"
# contacted the project owner (available in POM) and clarified the license status in LGPLv3
License:       LGPLv3 and ASL 2.0
Url:           http://code.google.com/p/maven-annotation-plugin/
# git clone https://code.google.com/p/maven-annotation-plugin/ maven-processor-plugin-2.1.1
# (cd maven-processor-plugin-2.1.1/ && git archive --format=tar --prefix=maven-processor-plugin-2.1.1/ maven-processor-plugin-2.1.1 | xz > ../maven-processor-plugin-2.1.1-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: jpackage-utils

# test deps
BuildRequires: junit

BuildRequires: maven-local

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      maven

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A maven plugin to process annotation for jdk6 at compile time

This plugin helps to use from maven the new annotation processing
provided by JDK6 integrated in java compiler

This plugin could be considered the 'alter ego' of maven apt plugin.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_xpath_remove pom:project/pom:profiles
%pom_xpath_remove pom:build/pom:extensions

cp -p src/main/resources/COPYING.LESSER .

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc COPYING.LESSER

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.LESSER

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_1jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp7
- new version

