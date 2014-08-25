# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-gpg-plugin
Version:        1.4
Release:        alt3_7jpp7
Summary:        Maven GPG Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-gpg-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Add-support-for-maven-3.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant-nodeps
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Obsoletes: maven2-plugin-gpg <= 0:2.0.8
Provides: maven2-plugin-gpg = 1:%{version}-%{release}
Source44: import.info

%description
This plugin signs all of the project's attached artifacts with
GnuPG. It adds goals gpg:sign and gpg:sign-and-deploy-file.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

# migrate to maven 3.x 
%patch0 -p1
sed -i 's/${mavenVersion}/3.0.4/' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- fixed build

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- new fc release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

