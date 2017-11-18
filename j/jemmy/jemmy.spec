BuildRequires: javapackages-local
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jemmy
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

# Install time macros
%global target_jar build/%{name}.jar
%global target_javadoc build/javadoc/*


Name:           jemmy
Version:        2.3.0.0
Release:        alt3_14jpp8
Summary:        Java UI testing library

Group:          Development/Other
License:        CDDL
URL:            https://jemmy.dev.java.net

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#
# svn export https://jemmy.dev.java.net/svn/jemmy/trunk/Jemmy2 jemmy-2.3.0.0 --username <username>
# tar -czvf jemmy-2.3.0.0.tar.gz jemmy-2.3.0.0
#
# where <username> is a name of the user registered here: https://www.dev.java.net/servlets/Join
Source0:        jemmy-2.3.0.0.tar.gz

# POM based on one from maven.org, with version and license info modified:
# http://central.maven.org/maven2/org/netbeans/jemmy/2.2.7.5/jemmy-2.2.7.5.pom
Source1:        %{name}.pom

BuildRequires:  ant >= 1.6.5
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  jpackage-utils

Requires:       java >= 1.6.0
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Jemmy is a Java UI testing library. Jemmy represents the most natural way to 
test Java UI - perform the testing right from the Java code. Jemmy is a Java 
library which provides clear and straightforward API to access Java UI. Tests 
are then just java programs, which use the API. Having the tests in Java allows 
to use all the flexibility of high level language to capture test logic and 
also do any other operations needed to be done from test.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find . -type f -name '*.jar' | xargs -t rm
echo "Please, visit http://jemmy.java.net for more info about Jemmy." > README.txt

%build
%ant jar javadoc

%install
# jar
%__mkdir_p %{buildroot}%{_javadir}
%__cp -a %{target_jar} %{buildroot}%{_javadir}/%{name}.jar

# POM
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}
%__cp -a %{target_javadoc} %{buildroot}%{_javadocdir}/%{name}


%files -f .mfiles
%doc README.txt
%{_javadir}/*.jar
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt3_14jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt1_8jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt1_6jpp7
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt1_5jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.0.0-alt1_4jpp5
- new version

