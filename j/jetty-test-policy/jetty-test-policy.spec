Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jetty-test-policy
Version:        1.2
Release:        alt3_15jpp8
Summary:        Jetty test policy files
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
Source2:        http://www.eclipse.org/legal/epl-v10.html
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         0001-Sign-JAR-with-maven-jarsigner-plugin.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-jarsigner-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
Source44: import.info

%description
Jetty test policy files

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE2} %{SOURCE3} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new version

