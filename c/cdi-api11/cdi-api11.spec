# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global majorversion 1
Name:          cdi-api11
Version:       1.1
Release:       alt1_1jpp7
Summary:       CDI APIs
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.seamframework.org/Weld

Source0:       http://repo1.maven.org/maven2/javax/enterprise/cdi-api/%{version}/cdi-api-%{version}-sources.jar
Source1:       http://repo1.maven.org/maven2/javax/enterprise/cdi-api/%{version}/cdi-api-%{version}.pom

BuildRequires: geronimo-parent-poms
BuildRequires: weld-parent

BuildRequires: atinject
BuildRequires: geronimo-annotation
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-interceptors-1.1-api

# test deps
BuildRequires: testng
#BuildRequires: maven-surefire-provider-testng

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      atinject
Requires:      geronimo-annotation
Requires:      jboss-el-2.2-api
Requires:      jboss-ejb-3.1-api
Requires:      jboss-interceptors-1.1-api

BuildArch:     noarch
Source44: import.info

%description
APIs for CDI (Contexts and Dependency Injection for Java EE).

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -T -q -c

# fixing incomplete source directory structure
mkdir -p src/main/{java,resources}

(
  cd src/main/java
  unzip -qq %{SOURCE0}
  mv META-INF/LICENSE.txt ../../../
  rm -rf META-INF
)

# clone source directory structure
find src/main/java/ -type d | while read dirname ; do
  newdirname=`echo $dirname | sed "s:src/main/java:src/main/resources:g"`
  mkdir -p $newdirname
done

# copy everything except *.java sources
find src/main/java/ -type f | grep -v "\.java" | while read cpfrom ; do
  cpto=`echo $cpfrom | sed "s:src/main/java:src/main/resources:g"`
  cp $cpfrom $cpto
done

cp -p %{SOURCE1} pom.xml

%build

mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 target/cdi-api-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -v "%{majorversion}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-%{majorversion}.jar
%{_mavenpomdir}/JPP-%{name}-%{version}.pom
%{_mavenpomdir}/JPP-%{name}-%{majorversion}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new release

