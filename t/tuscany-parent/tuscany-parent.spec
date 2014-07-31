# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          tuscany-parent
Version:       2
Release:       alt1_6jpp7
Summary:       Apache Tuscany Project Parent
Group:         Development/Java
License:       ASL 2.0
Url:           http://tuscany.apache.org/
# svn export http://svn.apache.org/repos/asf/tuscany/tags/java/pom/parent/2 tuscany-parent-2
# tar czf tuscany-parent-2-src-svn.tar.gz tuscany-parent-2
Source0:       %{name}-%{version}-src-svn.tar.gz
# tuscany-parent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-install-plugin

# required by remote-resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

Requires:      maven-checkstyle-plugin
Requires:      maven-compiler-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Parent POM defining settings that can be used across Tuscany.

%prep
%setup -q

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin

%build

mvn-rpmbuild install

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp7
- new version

