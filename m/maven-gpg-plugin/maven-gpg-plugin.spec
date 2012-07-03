# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-gpg-plugin
Version:        1.4
Release:        alt1_2jpp7
Summary:        Maven GPG Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-gpg-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Add-support-for-maven-3.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant-nodeps
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
Requires: maven
Requires: jpackage-utils
Requires: gnupg2

Obsoletes: maven2-plugin-gpg <= 0:2.0.8
Provides: maven2-plugin-gpg = 1:%{version}-%{release}
Source44: import.info

%description
This plugin signs all of the project's attached artifacts with
GnuPG. It adds goals gpg:sign and gpg:sign-and-deploy-file.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%patch0 -p1

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

