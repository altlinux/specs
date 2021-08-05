Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           tomcat-taglibs-parent
Version:        3
Release:        alt1_16jpp11
Summary:        Apache Taglibs Parent

License:        ASL 2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        https://github.com/apache/tomcat-taglibs-parent/raw/master/pom.xml
BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
Apache Taglibs Parent pom used for building purposes.

%prep
%setup -q -c -T
cp -p %{SOURCE0} .

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%dir %{_mavenpomdir}/%{name}

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3-alt1_16jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 3-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_3jpp8
- new version

