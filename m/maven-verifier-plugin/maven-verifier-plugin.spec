Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-verifier-plugin
Version:        1.1
Release:        alt1_1jpp11
Summary:        Maven Verifier Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-verifier-plugin/
Source0:        http://www.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-parent
BuildRequires: modello
BuildRequires: plexus-utils
Source44: import.info

%description
Assists in integration testing by means of evaluating 
success/error conditions read from a configuration file.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%mvn_file :%{name} %{name}
%pom_remove_parent
%pom_add_parent org.apache.maven.plugins:maven-plugins:34
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='maven-plugin-api']" '<scope>provided</scope>'

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_1jpp11
- new version

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt4_28jpp11
- fixed build with new maven-parent

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_23jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_21jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_17jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_15jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_14jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp7
- new fc release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- new version

