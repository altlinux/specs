Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
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

Summary:        Fast Scanner Generator
Name:           jflex
Version:        1.7.0
Release:        alt1_7jpp11
License:        BSD
URL:            http://jflex.de/
BuildArch:      noarch

# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}-clean.tar.gz
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        %{name}.1
Source5:        create-tarball.sh

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(java_cup:java_cup)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
%endif

%if %{without bootstrap}
BuildRequires:  jflex
%endif

# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

%description
JFlex is a lexical analyzer generator (also known as scanner
generator) for Java, written in Java.  It is also a rewrite of the
very useful tool JLex which was developed by Elliot Berk at Princeton
University.  As Vern Paxson states for his C/C++ tool flex: They do
not share any code though.  JFlex is designed to work together with
the LALR parser generator CUP by Scott Hudson, and the Java
modification of Berkeley Yacc BYacc/J by Bob Jamison.  It can also be
used together with other parser generators like ANTLR or as a
standalone tool.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q
%mvn_file : %{name}
%pom_add_dep java_cup:java_cup

%pom_remove_plugin :jflex-maven-plugin
%pom_remove_plugin :cup-maven-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_dep :cup_runtime

# Tests fail with 320k stacks (default on i686), so lets increase
# stack to 16M to avoid stack overflows.  See rhbz#1119308
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" "<argLine>-Xss16384k</argLine>"

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-site-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='fmt-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='cup-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-shade-plugin']" parent.xml

%pom_xpath_remove "pom:dependency[pom:artifactId='plexus-compiler-javac-errorprone']" parent.xml
%pom_xpath_remove "pom:dependency[pom:artifactId='error_prone_core']" parent.xml
%pom_xpath_remove "pom:compilerId" parent.xml
%pom_xpath_remove "pom:compilerArgs" parent.xml

sed -i /%%inputstreamctor/d src/main/jflex/LexScan.flex

%build
%{?jpb_env}
cup -parser LexParse -interface -destdir src/main/java src/main/cup/LexParse.cup
jflex -d src/main/java/jflex --skel src/main/jflex/skeleton.nested src/main/jflex/LexScan.flex
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install

# wrapper script for direct execution
%jpackage_script jflex.Main "" "" jflex:java_cup jflex true

# manpage
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man1

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

# .desktop + icons

# Emacs files

%files -f .mfiles
%doc doc
%doc COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%doc COPYRIGHT
%doc %{_javadocdir}/%{name}


%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.7.0-alt1_7jpp11
- update

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:1.7.0-alt1_5jpp11
- rebuild with java11 and use jvm_run

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt1_1jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_13jpp8
- new version

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_10jpp8.qa1
- NMU: applied repocop patch

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_2jpp8
- java 8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_16jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_10jpp7
- fc release

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_1jpp6
- fixed build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt4_1jpp6
- fixed build with java 7

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_1jpp6
- added maven2-plugin-resources dep

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_1jpp6
- new version (full build)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_1jpp6
- new version (bootstrap build)

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_3jpp5
- new jpp release

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp5
- fixed classpath

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp5
- jpp5 build

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.5-alt1_2jpp1.7
- converted from JPackage by jppimport script

