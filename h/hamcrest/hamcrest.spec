%define _unpackaged_files_terminate_build 1
%def_with check

Name: hamcrest
Version: 3.0
Release: alt1

Summary: Library of matchers for building test expressions
License: BSD-3-Clause
Group: Development/Java
Url: http://hamcrest.org
Vcs: https://github.com/hamcrest/JavaHamcrest.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-unwanted-gradle-plugins-alt-patch.patch

Provides: hamcrest-core = %EVR
Provides: hamcrest-library = %EVR

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: biz-aQute-bnd-gradle-plugins
%if_with check
BuildRequires: junit5
%endif

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

# Disable the hamcrest-integration module as very obsolete.
sed -i '/^[[:space:]]*'\''hamcrest-integration'\''/d' settings.gradle

# Aliases for compatibility.
%mvn_alias org.hamcrest:hamcrest \
  org.hamcrest:hamcrest-core \
  org.hamcrest:hamcrest-library \
  #

%build
%gradle_publish

%install
# Hamcrest library and core have almost empty jars and were deprecated
# use org.hamcrest:hamcrest as a dependency instead.
%gradle_register --artifacts=hamcrest-%version
%gradle_register_javadoc --artifacts=hamcrest-%version

%gradle_install

%check
%gradle_check -Dfile.encoding=UTF-8

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Fri Nov 14 2025 Ivan Khanas <xeno@altlinux.org> 3.0-alt1
- New version.
- Switch to xgradle.

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2-alt1_5jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt3_30jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_27jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_25jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_23jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_22jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_13jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp7
- new release

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp7
- new version

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_21jpp7
- source and target to 1.5

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_21jpp7
- fix for arm

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp7
- java6 build for jmock2

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_19jpp7
- fc release

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9.2jpp6
- added OSGi manifest for eclipse

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp5
- rebuild to fix jmock2

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

