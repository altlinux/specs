Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global tarball_name RELEASE_3_2_4

Name:           cglib
Version:        3.2.4
Release:        alt1_7jpp8
Summary:        Code Generation Library for Java
License:        ASL 2.0 and BSD
Url:            https://github.com/cglib/cglib
Source0:        https://github.com/cglib/cglib/archive/%{tarball_name}.tar.gz

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  javapackages-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch
Source44: import.info

%description
cglib is a powerful, high performance and quality code generation library
for Java. It is used to extend Java classes and implements interfaces
at run-time.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Documentation for the cglib code generation library.

%prep
%setup -q -n %{name}-%{tarball_name}

%pom_disable_module cglib-nodep
%pom_disable_module cglib-integration-test
%pom_disable_module cglib-jmh
%pom_xpath_set pom:packaging 'bundle' cglib
%pom_xpath_inject pom:build/pom:plugins '<plugin>
                                           <groupId>org.apache.felix</groupId>
                                           <artifactId>maven-bundle-plugin</artifactId>
                                           <version>1.4.0</version>
                                           <extensions>true</extensions>
                                           <configuration>
                                             <instructions>
                                               <Bundle-SymbolicName>net.sf.cglib.core</Bundle-SymbolicName>
                                               <Export-Package>net.*</Export-Package>
                                               <Import-Package>org.apache.tools.*;resolution:=optional,*</Import-Package>
                                             </instructions>
                                           </configuration>
                                         </plugin>' cglib
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-jarsigner-plugin cglib-sample
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_inject "pom:dependency[pom:artifactId='ant']" "<optional>true</optional>" cglib

%mvn_alias :cglib "net.sf.cglib:cglib" "cglib:cglib-full" "cglib:cglib-nodep" "org.sonatype.sisu.inject:cglib"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_6jpp8
- fc27 update

* Tue Oct 31 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_4jpp8
- new version
- manually added compat symlink for hadoop

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_10jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_7jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_17jpp7
- new release

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_15jpp7
- fc update

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_4jpp6
- added net.sf.cglib group id

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- added pom

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_3jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_2jpp1.7
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_2jpp1.7
- fixed provides to avoid unmets on cglib

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_2jpp1.7
- imported with jppimport script; note: bootstrapped version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp1.7
- fixed cglib provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp1.7
- imported with jppimport script; note: bootstrapped version

