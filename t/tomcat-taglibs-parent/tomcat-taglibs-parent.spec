# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           tomcat-taglibs-parent
Version:        3
Release:        alt1_6jpp8
Summary:        Apache Taglibs Parent

Group:          Development/Other
License:        ASL 2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        http://svn.apache.org/repos/asf/tomcat/taglibs/taglibs-parent/tags/taglibs-parent-3/pom.xml
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
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_mavenpomdir}/%{name}

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_3jpp8
- new version

