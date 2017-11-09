Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          tuscany-parent
Version:       2
Release:       alt1_15jpp8
Summary:       Apache Tuscany Project Parent
License:       ASL 2.0
Url:           http://tuscany.apache.org/
# svn export http://svn.apache.org/repos/asf/tuscany/tags/java/pom/parent/2 tuscany-parent-2
# tar czf tuscany-parent-2-src-svn.tar.gz tuscany-parent-2
Source0:       %{name}-%{version}-src-svn.tar.gz
# tuscany-parent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: maven-install-plugin

# required by remote-resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch
Source44: import.info

%description
Parent POM defining settings that can be used across Tuscany.

%prep
%setup -q

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_14jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_12jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp7
- new version

