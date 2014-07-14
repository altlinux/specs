BuildRequires: /proc
BuildRequires: jpackage-compat
%global checkout 20110809

Name: xsom
Version: 0
Release: alt2_6.20110809svnjpp7
Summary: XML Schema Object Model (XSOM)
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://xsom.java.net

# svn export https://svn.java.net/svn/xsom~sources/tags/xsom-20110809 xsom-20110809svn
# find xsom-20110809svn/ -name '*.class' -delete
# find xsom-20110809svn/ -name '*.class' -delete
# tar czf xsom-20110809svn.tar.gz xsom-20110809svn
Source0: %{name}-%{checkout}svn.tar.gz

# We need this because one of the original tests tries to download
# it from the website, but that doesn't work in Koji:
Source1: http://docs.oasis-open.org/regrep/v3.0/schema/lcm.xsd

Patch0: %{name}-%{checkout}svn-pom.patch

BuildRequires: jpackage-utils
BuildRequires: junit4
BuildRequires: maven
BuildRequires: maven-antrun-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: relaxngDatatype
BuildRequires: relaxngcc
BuildRequires: sonatype-oss-parent
BuildRequires: forge-parent

Requires: jpackage-utils
Requires: relaxngDatatype
BuildArch: noarch
Source44: import.info


%description
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.  The library is a straight-forward implement of "schema components" as
defined in the XML Schema spec part 1.  Refer to this specification of how this
object model works. 


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{name}-%{checkout}svn
%patch0 -p1

# Replace the URL of the XSD file used by the tests with its
# absolute filesystem location:
sed -i \
  's|http://docs.oasis-open.org/regrep/v3.0/schema/lcm.xsd|file://%{SOURCE1}|' \
  test/XSOMParserTest.java

pushd lib
  ln -sf $(build-classpath relaxngcc) relaxngcc.jar
popd


%build

mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
cp -p target/xsom-%{checkout}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/*
%doc license.txt


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_6.20110809svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_6.20110809svnjpp7
- new version

