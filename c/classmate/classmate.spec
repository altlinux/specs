# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          classmate
Version:       0.5.4
Release:       alt2_2jpp7
Summary:       Java introspection library
Group:         Development/Java
License:       ASL 2.0
Url:           http://github.com/cowtowncoder/java-classmate/
# git clone git://github.com/cowtowncoder/java-classmate.git classmate-0.5.4
# cd classmate-0.5.4/ && git archive --format=tar --prefix=classmate-0.5.4/ classmate-0.5.4 | xz > ../classmate-0.5.4.tar.xz
Source0:       %{name}-%{version}.tar.xz
# classmate package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: jpackage-utils
BuildRequires: sonatype-oss-parent

BuildRequires: junit4

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Library for introspecting types with full generic information
including resolving of field and method types.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %%{name}.

%prep
%setup -q

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

mvn-rpmbuild install javadoc:aggregate

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
%doc LICENSE-2.0.txt README release-notes.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt2_2jpp7
- fixed maven1 dependency

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_2jpp7
- initial build

