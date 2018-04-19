Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global spec_ver 3.0
%global spec_name geronimo-jpa_%{spec_ver}_spec

Name:           geronimo-jpa
Version:        1.1.1
Release:        alt3_21jpp8
Summary:        Java persistence API implementation

License:        ASL 2.0
URL:            http://geronimo.apache.org/
# Unfortunately no source release was created in
# http://repo2.maven.org/maven2/org/apache/geronimo/specs/geronimo-jpa_3.0_spec/1.1.1/
# so we do:
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_3.0_spec-1.1.1
# tar caf geronimo-jpa_3.0_spec-1.1.1.tar.xz geronimo-jpa_3.0_spec-1.1.1
Source0:       %{spec_name}-%{version}.tar.xz

BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.geronimo.specs:specs:pom:)

Provides:       jpa_api = %{spec_ver}
Provides:       javax.persistence = %{spec_ver}
Source44: import.info


%description
The Java Persistence API is a new programming model under EJB 3.0
specification (JSR220) for the management of persistence and
object/relational mapping with Java EE and Java SE. Geronimo JPA is
one implementation of this specification.


%package javadoc
Group: Development/Java
Summary:   API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{spec_name}-%{version}

%build
%mvn_file  : %{name}/%{name} %{name} jpa
%mvn_alias : javax.persistence:persistence-api
%mvn_build

%install
%mvn_install

install -d -m 755 %{buildroot}%{_javadir}/javax.persistence/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.persistence/

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%{_javadir}/javax.persistence/

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_21jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_20jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_19jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_17jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_13jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_11jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_8jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8jpp7
- new version

