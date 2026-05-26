Name:           apache-commons-beanutils
Version:        1.11.0
Release:        alt1

Summary:        Apache Commons Beanutils
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/beanutils/
VCS:            https://github.com/apache/commons-beanutils

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-collections:commons-collections-testframework)

BuildArch:      noarch

%description
Apache Commons BeanUtils provides an easy-to-use but flexible wrapper around
reflection and introspection.

%javadoc_package

%prep
%setup

%mvn_alias :commons-beanutils org.apache.commons:commons-beanutils

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Wed May 20 2026 Evgeniy Serov <scala@altlinux.org> 1.11.0-alt1
- Updated to 1.11.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_10jpp11
- update

* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_6jpp11
- quick fix (closes: #40375)

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_5jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt5_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt5_4jpp8
- java 8 mass update

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_9jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_7jpp7
- fc update

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_4jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_4jpp6
- fixed repolib

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp6
- new version

