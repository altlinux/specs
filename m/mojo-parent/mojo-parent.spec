Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           mojo-parent
Version:        32
Release:        alt1_2jpp7
Summary:        Codehaus MOJO parent project pom file

License:        ASL 2.0
URL:            http://mojo.codehaus.org/
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  codehaus-parent
BuildRequires:  maven-enforcer-plugin
Source44: import.info

%description
Codehaus MOJO parent project pom file

%prep
%setup -q
# Cobertura plugin is executed only during clean Maven phase.
%pom_remove_plugin :cobertura-maven-plugin
# wagon-webdav-jackrabbit is not available in Fedora
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%build
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:32-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt4_2jpp7
- rebuild with maven-local

* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt3_2jpp7
- fixed 1.4 java mojo target in pom

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:30-alt1_1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp6
- new version

