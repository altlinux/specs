%define _unpackaged_files_terminate_build 1
%def_with check

Name: objectweb-asm
Version: 9.9
Release: alt1

Summary: Java bytecode manipulation and analysis framework
License: BSD
Group: Development/Java
Url: https://asm.ow2.org
Vcs: https://gitlab.ow2.org/asm/asm.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-all-external-gradle-plugins-alt-patch.patch
Patch1: 0002-Janino-3.1.7-compatibility-for-tests-alt-patch.patch
%if_with check
# Fix warnings "unknown enum constant Status.STABLE".
Patch2: 0003-Add-an-explicit-dependency-on-apiguardian-alt-patch.patch
%endif

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: xgradle
%if_with check
BuildRequires: junit5
BuildRequires: janino
BuildRequires: apiguardian
%endif

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package javadoc
Group: Development/Java
Summary: API documentation for %name
BuildArch: noarch

%description javadoc
This package provides %summary.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Prelease

%install
%gradle_register_bom --remove-parent=all
%gradle_register --exclude-artifacts=asm-test --remove-parent=all
%gradle_register_javadoc --exclude-artifacts=asm-test

%gradle_install

%check
# We must explicitly specify the encoding when building in hasher
# if it is not explicitly specified by upstream in the build file.
%gradle_check -Dfile.encoding=UTF-8

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Nov 13 2025 Ivan Khanas <xeno@altlinux.org> 9.9-alt1
- New version.
- Switch to xgradle.
- Add JPMS support by compiling module-info.java.
- Add asm-bom installation to include as a platform in Gradle.

* Sun Feb 23 2025 Andrey Cherepanov <cas@altlinux.org> 0:9.7.1-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:9.3-alt1_2jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:9.2-alt1_3jpp11
- new version

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 0:9.1-alt1_3jpp11
- new version

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:8.0.1-alt1_1jpp8
- new version, use jvm8

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:7.0-alt1_4jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.0-alt1_2jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.2.1-alt1_1jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.1.1-alt1_1jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.0-alt1_1jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_4jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.4-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_7jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp7
- update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp6
- updated OSGi manifest to match version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

