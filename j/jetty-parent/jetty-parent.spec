Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-parent
Version:        19
Release:        alt2_17jpp8
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
Source44: import.info

%description
Jetty parent POM file

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE2} %{SOURCE3} .

%pom_remove_plugin :maven-release-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 19-alt2_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 19-alt2_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 19-alt2_15jpp8
- new jpp release

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

