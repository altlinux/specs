%define _unpackaged_files_terminate_build 1

Name: beust-jcommander
Version: 3.0
Release: alt1

Summary: Java framework for parsing command line parameters
License: Apache-2.0
Group: Development/Java
Url: http://jcommander.org
Vcs: https://github.com/cbeust/jcommander.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Unicode-fix-for-tests-with-java-17.patch
Patch1: 0002-Disable-signing-with-key.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: jackson-core
BuildRequires: jackson-annotations
BuildRequires: testng

Provides: mvn(com.beust:jcommander) = %EVR
Provides: mvn(org.jcommander:jcommander) = %EVR

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Group: Development/Java
Summary: API documentation for %name
BuildArch: noarch

%description javadoc
This package contains the %summary.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
# Alias for backward compatibility (changed groupId).
%mvn_alias org.jcommander:jcommander com.beust:jcommander

%gradle_register
%gradle_register_javadoc

%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Mon Oct 27 2025 Ivan Khanas <xeno@altlinux.org> 3.0-alt1
- New version.

* Thu Oct 23 2025 Ivan Khanas <xeno@altlinux.org> 1.78-alt2
- Create symlink to maintain the naming of artifacts.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.78-alt1_7jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 1.78-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_6jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1_1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_4jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

