%define _unpackaged_files_terminate_build 1

Name: svgsalamander
Version: 1.1.5.5
Release: alt1

Summary: An SVG engine for Java
Group: Development/Other
License: LGPLv2+ or BSD
Url: https://github.com/blackears/svgSalamander/
Vcs: https://github.com/blackears/svgSalamander/
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: javacc-maven-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-source-plugin

%{?javadoc_package}

%description
SVG Salamander is an SVG engine for Java that's designed to be small, fast, 
and allow programmers to use it with a minimum of fuss. It's in particular 
targeted for making it easy to integrate SVG into Java games and making it 
much easier for artists to design 2D game content - from rich interactive 
menus to charts and graphcs to complex animations.

%prep
%setup
%autopatch -p1

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

%pom_disable_module svg-example
%pom_remove_plugin :central-publishing-maven-plugin svg-core
%pom_remove_plugin :maven-gpg-plugin svg-core
%pom_remove_plugin :maven-javadoc-plugin svg-core

%build
%mvn_build

%install
%mvn_alias io.github.blackears:svg-salamander com.kitfox.svg:svg-salamander
%mvn_alias io.github.blackears:svg-salamander com.formdev:svgSalamander
%mvn_install

%files -f .mfiles
%doc www/docs/exampleCode/
%doc www/docs/use.html
%doc www/license/*

%changelog
* Mon Apr 20 2026 Arseniy Kostevich <faux@altlinux.org> 1.1.5.5-alt1
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_9jpp11
- fc34 update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_5jpp11
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.39-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.33-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.19-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_3jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.10-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2jpp7
- new version
