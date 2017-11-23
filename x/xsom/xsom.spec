Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global checkout 20110809

Name: xsom
Version: 0
Release: alt2_18.20110809svnjpp8
Summary: XML Schema Object Model (XSOM)
License: CDDL-1.1 or GPLv2 with exceptions
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

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  relaxngcc

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
  ln -sf `build-classpath relaxngcc` relaxngcc.jar
popd

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt2_18.20110809svnjpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt2_17.20110809svnjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt2_16.20110809svnjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_15.20110809svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_14.20110809svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_10.20110809svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_9.20110809svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_6.20110809svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_6.20110809svnjpp7
- new version

