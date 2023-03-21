Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xvfb-run
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           stringtemplate4
Version:        4.3.3
Release:        alt1_3jpp11
Summary:        A Java template engine
License:        BSD
URL:            http://www.stringtemplate.org/
BuildArch:      noarch

Source0:        https://github.com/antlr/stringtemplate4/archive/%{version}/%{name}-%{version}.tar.gz
# Adapt to JDK 11
Patch0:         %{name}-java11.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime) >= 3.5.2
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin) >= 3.5.2
BuildRequires:  fonts-type1-xorg
BuildRequires:  xorg-xvfb xvfb-run
Source44: import.info

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1


# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

%build
xvfb-run -a -n 1 %mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 4.3.3-alt1_3jpp11
- new version

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 4.3.1-alt1_9jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 4.3.1-alt1_4jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 4.3-alt1_2jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt1_2jpp8
- java8 mass update

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_4jpp7
- new version

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

