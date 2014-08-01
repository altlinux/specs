# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cargo-parent
Version:        4.12
Release:        alt1_3jpp7
Summary:        Parent pom file for cargo.codehaus.org project

Group:          Development/Java
License:        ASL 2.0
URL:            http://cargo.codehaus.org/
#svn export http://svn.codehaus.org/cargo/pom/tags/cargo-parent-4.12/
Source0:        %{name}-%{version}.tar.gz
# cargo-parent package don't include the license file
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:  codehaus-parent

Requires:       jpackage-utils
Requires:       codehaus-parent
Source44: import.info

%description
This package contains the cargo parent pom.

%prep
%setup -q

# remove org.apache.maven.wagon wagon-webdav
%pom_xpath_remove "pom:build/pom:extensions"

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build
# Nothing to do
%install

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml  \
        %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1_3jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.11-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1_2jpp7
- new release

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7-alt1_1jpp7
- new version

