BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           netbeans-javaparser
Version:        6.9
Release:        alt1_2jpp6
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            http://java.netbeans.org/javaparser/
Group:          Development/Java
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# hg clone http://hg.netbeans.org/main/nb-javac/
# cd nb-javac/
# hg update -r release69_base
# tar -czvf ../nb-javac-6.9.tar.gz .
Source0:        nb-javac-%{version}.tar.gz

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  jpackage-utils

Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Java parser to analyze Java source files inside of the NetBeans IDE

%prep
%setup -q -c
# remove all binary libs
find . -name "*.jar" -exec %__rm -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
%ant -f make/netbeans/nb-javac/build.xml jar

%install
%__rm -fr %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}
%__install -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%__ln_s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%__install -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl-%{version}.jar
%__ln_s %{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%files
%doc ASSEMBLY_EXCEPTION LICENSE README
%{_javadir}/*


%changelog
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

