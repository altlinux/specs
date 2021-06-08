Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xsom
Summary:        XML Schema Object Model (XSOM)
Version:        20140514
Release:        alt3_3jpp11
License:        CDDL-1.1 or GPLv2 with exceptions

# java.net is dead; upstream sources have been imported to GitHub though
URL:            https://github.com/kohsuke/xsom
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# We need this because one of the original tests tries to download
# it from the website, but that doesn't work in Koji:
Source1: http://docs.oasis-open.org/regrep/v3.0/schema/lcm.xsd

# patch POM to drop tasks that rely on bundled JARs
Patch0:         00-pom-changes.patch
Patch33:	xsom-no-target-15.patch

BuildRequires:  relaxngcc
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype:20020414)

BuildArch:      noarch
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
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch33 -p1

find -name "*.class" -print -delete
find -name "*.jar" -print -delete

# parent POM is not necessary
%pom_remove_parent

# Replace the URL of the XSD file used by the tests with its
# absolute filesystem location:
sed -i \
  's|http://docs.oasis-open.org/regrep/v3.0/schema/lcm.xsd|file://%{SOURCE1}|' \
  test/XSOMParserTest.java

pushd lib
ln -sf `build-classpath relaxngcc` relaxngcc.jar
popd

%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8 -Dproject.build.sourceEncoding=UTF-8 -P regenerate-sources

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference license.txt copyright.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt copyright.txt

%changelog
* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 20140514-alt3_3jpp11
- build with compat relaxngDatatype

* Sun May 30 2021 Igor Vlasenko <viy@altlinux.org> 20140514-alt2_3jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 20140514-alt1_3jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt2_21.20110809svnjpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt2_19.20110809svnjpp8
- java update

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

