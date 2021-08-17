Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           plexus-cipher
Version:        1.7
Release:        alt3_24jpp11
Summary:        Plexus Cipher: encryption/decryption Component
License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch

# git clone https://github.com/sonatype/plexus-cipher.git
# cd plexus-cipher/
# note this is version 1.7 + our patches which were incorporated by upstream maintainer
# git archive --format tar --prefix=plexus-cipher-1.7/ 0cff29e6b2e | gzip -9 > plexus-cipher-1.7.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.sonatype.plugins:sisu-maven-plugin)
%endif
Source44: import.info

%description
Plexus Cipher: encryption/decryption Component

%{?javadoc_package}

%prep
%setup -q

%pom_remove_parent
%pom_xpath_inject "pom:dependency[pom:artifactId='junit']" "<scope>test</scope>"

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_replace pom:project/pom:version "<version>%{version}</version>"

# fedora moved from sonatype sisu to eclipse sisu. sisu-inject-bean artifact
# doesn't exist in eclipse sisu. this artifact contains nothing but
# bundled classes from atinject, cdi-api, aopalliance and maybe others.
%pom_remove_dep org.sonatype.sisu:sisu-inject-bean
%pom_add_dep javax.inject:javax.inject:1:provided
%pom_add_dep javax.enterprise:cdi-api:1.0:provided

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.6

%mvn_file : plexus/%{name}

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1.7-alt3_24jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.7-alt3_21jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_18jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_16jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_11jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_10jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3_11jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

