%define _unpackaged_files_terminate_build 1

Name: plexus-interpolation
Version: 1.28
Release: alt1

Summary: Plexus Interpolation API
License: Apache-2.0
Group: Development/Java
Url: https://github.com/codehaus-plexus/plexus-interpolation
Vcs: https://github.com/codehaus-plexus/plexus-interpolation.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Use-PATH-env-variable-instead-of-JAVA_HOME.patch

BuildRequires: maven-local
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-default
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%pom_add_dep junit:junit:4.13.1:test
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-publish-plugin

%build
%mvn_file : plexus/plexus-interpolation plexus/interpolation

%mvn_build -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Aug 15 2025 Ivan Khanas <xeno@altlinux.org> 1.28-alt1
- New version.
- Rename artifact.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:1.26-alt1_12jpp11
- update

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:1.26-alt1_8jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.26-alt1_2jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_11jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_4jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.15-alt1_2jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_1jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp6
- new version

