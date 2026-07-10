Name:           miglayout
Version:        11.4.2
Release:        alt1

Summary:        Official MiG Layout for Swing, SWT and JavaFX
License:        BSD
Group:          Development/Java
URL:            http://www.miglayout.com/
VCS:            https://github.com/mikaelgrev/miglayout

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch

%description
Official MiG Layout for Swing, SWT and JavaFX

For Java developers writing GUI layouts by hand that wants simplicity, power and
automatic per platform fidelity, that are dissatisfied with the current layout
managers in Swing, JavaFX and SWT, MigLayout solves your layout problems. User
interfaces created with MigLayout is easy to maintain, you will understand how
the layout will look like just by looking at the source code.

MigLayout is a superbly versatile JavaFX/SWT/Swing layout manager that makes
layout problems trivial. It is using String or API type-checked constraints to
format the layout. MigLayout can produce flowing, grid based, absolute (with
links), grouped and docking layouts. You will never have to switch to another
layout manager ever again! MigLayout is created to be to manually coded layouts
what Matisse/GroupLayout is to IDE supported visual layouts.

For documentation see http://miglayout.com

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_disable_module nbm
%pom_disable_module swt
%pom_disable_module javafx
%pom_disable_module demo
%pom_disable_module examples

# Disable Error Prone
sed -i '/<annotationProcessorPaths>/,/<\/annotationProcessorPaths>/d; /Xplugin:ErrorProne/,/<\/arg>/d' pom.xml

rm -f swing/src/test/java/net/miginfocom/swing/MigLayoutTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Tue Jul 07 2026 Evgeniy Serov <scala@altlinux.org> 11.4.2-alt1
- Updated to 11.4.2 (core and swing only).

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_12jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_10jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_7jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2jpp7
- new version

