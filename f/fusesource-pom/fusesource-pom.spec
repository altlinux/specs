Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             fusesource-pom
Version:          1.9
Release:          alt1_13jpp8
Summary:          Parent POM for FuseSource Maven projects
License:          ASL 2.0
URL:              http://fusesource.com/
Source0:          http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/%{version}/fusesource-pom-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.maven.plugins:maven-scm-plugin)
BuildRequires:    mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
Source44: import.info

%description
This is a shared POM parent for FuseSource Maven projects

%prep
%setup -c -T
cp %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_remove_plugin :clirr-maven-plugin

# WebDAV wagon is not available in Fedora.
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_12jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_10jpp8
- new release

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_4jpp7
- new release

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt4_1jpp6
- dropped unused plexus-maven-plugin dependencies

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt3_1jpp6
- build w/o plexus-maven-plugin

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_1jpp6
- fixed build with maven3; disabled repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp6
- new jpp relase

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_3jpp6
- maven1 translation

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_3jpp6
- fixed modello plugin dependency

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp6
- new version

