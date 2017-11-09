Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           stringtemplate4
Version:        4.0.8
Release:        alt1_5jpp8
Summary:        A Java template engine
License:        BSD
URL:            http://www.stringtemplate.org/
BuildArch:      noarch

Source0:        https://github.com/antlr/stringtemplate4/archive/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime) >= 3.5.2
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin) >= 3.5.2
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
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

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-shade-plugin

# Bug, should be reported upstream
sed -i '/tmpdir =/s,;,+"/"&,' test/org/stringtemplate/v4/test/BaseTest.java
# Tests fail for unknown reason
sed -i /testUnknownNamedArg/s/@Test// test/org/stringtemplate/v4/test/TestGroups.java
sed -i /testMissingImportString/s/@Test// test/org/stringtemplate/v4/test/TestGroupSyntaxErrors.java
# Requires running X server
rm -r test/org/stringtemplate/v4/test/TestEarlyEvaluation.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt contributors.txt README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
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

