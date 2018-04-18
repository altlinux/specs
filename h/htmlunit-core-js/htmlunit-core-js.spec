Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Getopt/Mixed.pm) rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global rhino_fork_githash ef0faa3e34ef6c3b42c1be4474d0252d96eb4535

Name:          htmlunit-core-js
Version:       2.23
Release:       alt1_4jpp8
Summary:       Rhino fork for htmlunit
License:       MPLv2.0
URL:           http://htmlunit.sourceforge.net/
Source0:       https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-%{version}.tar.gz
Source1:       https://github.com/HtmlUnit/htmlunit-rhino-fork/archive/%{rhino_fork_githash}/htmlunit-rhino-fork-%{rhino_fork_githash}.tar.gz

Patch0:        %{name}-2.23-build.patch


BuildRequires: ant
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: junit

%if 0
# Test use
BuildRequires: ant-junit
BuildRequires: bea-stax-api
BuildRequires: emma
BuildRequires: hamcrest
BuildRequires: xmlbeans
%endif

# Modified version of Mozilla Rhino 1.7.7
# see http://central.maven.org/maven2/net/sourceforge/htmlunit/htmlunit-core-js/2.23/htmlunit-core-js-2.23-sources.jar#rhinoDiff.txt
# https://fedorahosted.org/fpc/ticket/538
Provides:      bundled(rhino) = 1.7.7

BuildArch:     noarch
Source44: import.info

%description
This is a fork of Rhino to support HtmlUnit.
Everyone hopes it will go away someday.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-core-js-%{version} -a1
mv htmlunit-rhino-fork-%{rhino_fork_githash} htmlunit-rhino-fork

# Cleanup
find . -name "*.class"  -print -delete
find . -name "*.jar" -print -delete
find . -name "*.tar.*" -print -delete
find . -name '*.zip' -print -delete

%patch0 -p1

cp -p htmlunit-rhino-fork/LICENSE.txt LICENSE-MPL.txt

%build

%ant jar-all

%install
%mvn_artifact pom.xml target/%{name}-%{version}.jar
%mvn_file net.sourceforge.htmlunit:%{name} %{name}
%mvn_install -J target/javadoc

%files -f .mfiles
%doc README.html
%doc --no-dereference LICENSE.txt LICENSE-MPL.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt LICENSE-MPL.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.23-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.23-alt1_3jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.23-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.17-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.17-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt1_3jpp7
- new release

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_3jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp6
- new version

