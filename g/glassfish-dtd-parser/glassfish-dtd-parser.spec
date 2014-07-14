BuildRequires: /proc
BuildRequires: jpackage-compat
Name: glassfish-dtd-parser
Version: 1.2
Release: alt2_0.4.20120120svnjpp7
Summary: Library for parsing XML DTDs
Group: Development/Java
License: CDDL 1.1 and GPLv2 with exceptions
Url: http://java.net/projects/dtd-parser

# svn export https://svn.java.net/svn/dtd-parser~svn/trunk/dtd-parser glassfish-dtd-parser-1.2-SNAPSHOT
# find glassfish-dtd-parser-1.2-SNAPSHOT/ -name '*.jar' -delete
# tar czf glassfish-dtd-parser-1.2-SNAPSHOT-src-svn.tar.gz glassfish-dtd-parser-1.2-SNAPSHOT
Source0: %{name}-%{version}-SNAPSHOT-src-svn.tar.gz

BuildRequires: jpackage-utils
BuildRequires: bsf
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: sonatype-oss-parent

Requires: jpackage-utils

BuildArch: noarch
Source44: import.info


%description
Library for parsing XML DTDs.


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n glassfish-dtd-parser-1.2-SNAPSHOT


%build
mvn-rpmbuild install javadoc:aggregate


%install
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# JAR
install -m 644 target/dtd-parser-1.2-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

# JAVADOC
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# POM
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.4.20120120svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.4.20120120svnjpp7
- new version

