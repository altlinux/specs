Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jetty-parent
Version:        19
Release:        alt2_14jpp8
Summary:        Jetty parent POM file
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/eclipse/jetty/%{name}/%{version}/%{name}-%{version}.pom
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
Source2:        http://www.eclipse.org/legal/epl-v10.html
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  maven-release-plugin
Source44: import.info

%description
Jetty parent POM file

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE2} %{SOURCE3} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 19-alt2_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 19-alt2_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 19-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp7
- new version

