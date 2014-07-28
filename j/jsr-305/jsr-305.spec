Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jsr-305
Version:        0
Release:        alt2_0.13.20090319svnjpp7
Summary:        Correctness annotations for Java code

Group:          Development/Java
# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD and CC-BY
URL:            http://jsr-305.googlecode.com/
# There has been no official release yet.  This is a snapshot of the Subversion
# repository as of 19 Mar 2009.  Use the following commands to generate the
# tarball:
#   svn export -r 49 http://jsr-305.googlecode.com/svn/trunk jsr-305
#   tar -cvf jsr-305-0.4.20090319.tar jsr-305
#   xz jsr-305-0.4.20090319.tar
Source0:        jsr-305-0.4.20090319.tar.xz

BuildRequires:  jpackage-utils maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
sed -i 's/\r//' sampleUses/pom.xml

# do not build sampleUses module - it causes Javadoc generation to fail
sed -i '/<module>sampleUses<\/module>/d' pom.xml

%build
mvn-rpmbuild install javadoc:aggregate

%install

# JAR files
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ri/target/ri-0.1-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

# pom
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 ri/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a 'com.google.code.findbugs:jsr305'

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-parent.pom


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc ri/LICENSE sampleUses
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.13.20090319svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.10.20090319svnjpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.10.20090319svnjpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp6
- jpp 6 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_1jpp5
- converted from JPackage by jppimport script

