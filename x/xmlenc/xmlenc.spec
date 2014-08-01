# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xmlenc
Version:       0.53
Release:       alt1_4jpp7
Summary:       Light-weight XML output library for Java
Group:         Development/Java
License:       BSD
#  http://xmlenc.sourceforge.net/
URL:           https://github.com/znerd/xmlenc/
# git clone git://github.com/znerd/xmlenc.git xmlenc-0.53
# (cd xmlenc-0.53/ && git archive --format=tar --prefix=xmlenc-0.53/ xmlenc-0.53 | xz > ../xmlenc-0.53-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: jpackage-utils
BuildRequires: znerd-oss-parent

# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
This library is a fast stream-based XML output library for Java. 
Main design goals are performance, simplicity and pureness. 

%package javadoc
Summary:       Javadoc for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q
find . -name "*.class" -delete
find . -name ".*" -delete
find . -name "*.jar" -type f -delete

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGES.txt COPYRIGHT.txt README.txt THANKS.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYRIGHT.txt

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_4jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_10jpp7
- new version

