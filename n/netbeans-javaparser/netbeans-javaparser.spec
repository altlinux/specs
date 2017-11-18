BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}
%global namedtag RELEASE801

Name:           netbeans-javaparser
Version:        8.0.1
Release:        alt2_4jpp8
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            http://netbeans.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# hg clone http://hg.netbeans.org/main/nb-javac/
# cd nb-javac/
# hg update -r release801_base
# hg archive ../netbeans-javaparser-8.0.1.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  jpackage-utils

Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Java parser to analyze Java source files inside of the NetBeans IDE

%prep
%setup -q
# remove all binary libs
find . -name "*.class" -delete
find . -name "*.jar" -delete

%build
%ant -f make/netbeans/nb-javac/build.xml jar

%install

# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%add_maven_depmap org.netbeans.external:nb-javac-api:%{namedtag} %{name}-api.jar
%add_maven_depmap org.netbeans.external:nb-javac-impl:%{namedtag} %{name}-impl.jar

%files -f .mfiles
%doc ASSEMBLY_EXCEPTION LICENSE README
%{_javadir}/*.jar

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 8.0.1-alt2_4jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 8.0.1-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8.0.1-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 8.0.1-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.1-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.1-alt1_4jpp7
- new release

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 7.0.1-alt1_3jpp7
- new version

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 6.9-alt1_2jpp6
- update to new release by jppimport

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 6.9-alt1_1jpp6
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.8-alt1_1jpp6
- new version

* Thu Apr 30 2009 Igor Vlasenko <viy@altlinux.ru> 6.5-alt1_2jpp6
- new version

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_2jpp6
- converted from JPackage by jppimport script

