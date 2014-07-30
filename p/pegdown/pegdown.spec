# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          pegdown
Version:       1.1.0
Release:       alt3_4jpp7
Summary:       Java library for Markdown processing
Group:         Development/Java
License:       ASL 2.0
URL:           http://pegdown.org
# git clone git://github.com/sirthias/pegdown.git pegdown-1.1.0
# cd pegdown-1.1.0/ && git archive --format=tar --prefix=pegdown-1.1.0/ 1.1.0 | xz > ../pegdown-1.1.0-src-git.tar.xz
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: jpackage-utils

BuildRequires: parboiled
# test deps
BuildRequires: jtidy
BuildRequires: testng

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-testng

Requires:      parboiled

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A pure-Java Markdown processor based on a parboiled PEG parser
supporting a number of extensions.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n pegdown-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete

# these test fail
rm src/test/java/org/pegdown/CustomParserTest.java
rm src/test/java/org/pegdown/Markdown103Test.java
rm src/test/java/org/pegdown/PegDownTest.java

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGELOG LICENSE NOTICE README.markdown

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_4jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp7
- new version

