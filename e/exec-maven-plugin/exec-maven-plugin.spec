# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           exec-maven-plugin
Version:        1.2.1
Release:        alt4_10jpp7
Summary:        Exec Maven Plugin

Group:          Development/Java
# Most of the files are under ASL 2.0 license, but there are some files
# with no license specified. The project contains MIT license text,
# but there is no file which uses such a license.
License:        ASL 2.0 and MIT
URL:            http://mojo.codehaus.org/exec-maven-plugin
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.2.1/exec-maven-plugin-1.2.1-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  plexus-utils
BuildRequires:  maven-shared-plugin-testing-harness
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-plugin-cobertura
BuildRequires:  mojo-signatures
BuildRequires:  maven-invoker-plugin
BuildRequires:  apache-commons-exec
BuildRequires:  plexus-containers-container-default

Obsoletes:      maven-plugin-exec < %{version}-%{release}
Provides:       maven-plugin-exec = %{version}-%{release}
Source44: import.info

%description
A plugin to allow execution of system and Java programs

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n exec-maven-plugin-%{version}

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

cp -p %{SOURCE1} .

%pom_add_dep org.apache.maven:maven-compat pom.xml
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml

%build
# There are missing dependencies for tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_3jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp7
- new version

