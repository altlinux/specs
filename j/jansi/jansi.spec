Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
Requires: fusesource-pom
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             jansi
Version:          1.11
Release:          alt1_10jpp8
Summary:          Jansi is a java library for generating and interpreting ANSI escape sequences
License:          ASL 2.0
URL:              http://jansi.fusesource.org/

# git clone git://github.com/fusesource/jansi.git
# cd jansi && git archive --format=tar --prefix=jansi-1.11/ jansi-project-1.11 | xz > jansi-1.11.tar.xz
Source0:          jansi-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jansi-native
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-site-plugin
BuildRequires:    fusesource-pom
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences. 

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%pom_disable_module jansi-website
%pom_xpath_remove "pom:build/pom:extensions"

# No org.fusesource.mvnplugins:fuse-javadoc-skin available
%pom_remove_plugin "org.apache.maven.plugins:maven-dependency-plugin"

# No maven-uberize-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-uberize-plugin']" jansi/pom.xml

# Remove unnecessary deps for jansi-native builds
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'jansi-native' and pom:classifier != '']" jansi/pom.xml

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin jansi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc readme.md license.txt changelog.md

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_10jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_9jpp8
- unbootsrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_4jpp7
- added Requires: fusesource-pom

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added jansi:jansi depmap for jpp packages

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- fixed pom

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- fc version

* Sat Feb 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp6
- new version

