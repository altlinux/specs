Name:           yecht
Version:        1.1
Release:        alt1

Summary:        The "Yecht" implementation of Ruby 1.8's yaml parser "Syck"
License:        MIT
Group:          Development/Java
URL:            https://github.com/jruby/yecht
VCS:            https://github.com/jruby/yecht

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:      noarch

%description
%summary.

%javadoc_package

%prep
%setup

%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_dep :jruby-core

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Jul 07 2026 Evgeniy Serov <scala@altlinux.org> 1.1-alt1
- Updated to 1.1.

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt1_16jpp11
- fc34 update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_6jpp7
- new version

