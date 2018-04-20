Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-emacs
BuildRequires: /usr/bin/desktop-file-install rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without desktop
%bcond_without emacs

Summary:        Fast Scanner Generator
Name:           jflex
Version:        1.6.1
Release:        alt1_10jpp8
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
BuildRequires:  ant
BuildRequires:  jflex
BuildRequires:  junit
BuildRequires:  sonatype-oss-parent
BuildRequires:  java-devel
BuildRequires:  java_cup
%if %{with desktop}
BuildRequires:  desktop-file-utils
%endif
%if %{with emacs}
BuildRequires:  emacs
%endif
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

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :jflex-maven-plugin

# Tests fail with 320k stacks (default on i686), so lets increase
# stack to 16M to avoid stack overflows.  See rhbz#1119308
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" "<argLine>-Xss16384k</argLine>"

%build
java -jar $(find-jar java_cup) -parser LexParse -interface -destdir src/main/java src/main/cup/LexParse.cup
jflex -d src/main/java/jflex --skel src/main/jflex/skeleton.nested src/main/jflex/LexScan.flex
%mvn_build

%if %{with emacs}
# Compile Emacs jflex-mode source
%byte_compile_file lib/jflex-mode.el
%endif

%install
%mvn_install

# wrapper script for direct execution
%jpackage_script jflex.Main "" "" jflex:java_cup jflex true

# manpage
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man1

# .desktop + icons
%if %{with desktop}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif

# Emacs files
%if %{with emacs}
install -d -m 755 %{buildroot}%{_emacslispdir}/%{name}
install -p -m 644 lib/jflex-mode.el %{buildroot}%{_emacslispdir}/%{name}
install -p -m 644 lib/jflex-mode.elc %{buildroot}%{_emacslispdir}/%{name}
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc doc
%doc COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%if %{with desktop}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%endif
%if %{with emacs}
%{_emacslispdir}/%{name}
%endif
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%doc COPYRIGHT
%doc %{_javadocdir}/%{name}


%changelog
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

