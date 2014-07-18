BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          activemq-protobuf
Version:       1.1
Release:       alt3_2jpp7
Summary:       ActiveMQ Protocol Buffers
Group:         Development/Java
License:       ASL 2.0
Url:           http://activemq.apache.org/
# svn export http://svn.apache.org/repos/asf/activemq/activemq-protobuf/tags/activemq-protobuf-1.1
# tar czf activemq-protobuf-1.1-src-svn.tar.gz activemq-protobuf-1.1
Source0:       activemq-protobuf-1.1-src-svn.tar.gz
# remove ianal-maven-plugin
# remove assembly-plugin and its deps (org.apache.geronimo.genesis apache-source-release-assembly-descriptor)
# fix rat-plugin groupId artifactId version
Patch0:        activemq-protobuf-1.1-parent-pom.patch

BuildRequires: jpackage-utils

BuildRequires: junit4

BuildRequires: maven
BuildRequires: javacc-maven-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      maven

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A Simpler Protocol Buffer Java API.
Comes with a built in proto file
compiler and Java source code generator.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
chmod 644 LICENSE

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-pom.pom
%add_maven_depmap JPP.%{name}-pom.pom

mkdir -p %{buildroot}%{_javadir}/activemq
for m in protobuf protobuf-test; do
  install -m 644 activemq-${m}/target/activemq-${m}-%{version}.jar %{buildroot}%{_javadir}/activemq/${m}.jar
  install -pm 644 activemq-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.activemq-${m}.pom
%add_maven_depmap JPP.activemq-${m}.pom activemq/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/activemq
%{_javadir}/activemq/*.jar
%{_mavenpomdir}/JPP.%{name}*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new version

