BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          tuscany-parent
Version:       2
Release:       alt1_2jpp7
Summary:       Apache Tuscany Project Parent
Group:         Development/Java
License:       ASL 2.0
Url:           http://tuscany.apache.org/
# svn export http://svn.apache.org/repos/asf/tuscany/tags/java/pom/parent/2 tuscany-parent-2
# tar czf tuscany-parent-2-src-svn.tar.gz tuscany-parent-2
Source0:       %{name}-%{version}-src-svn.tar.gz

BuildRequires: jpackage-utils

BuildRequires: maven
BuildRequires: maven-install-plugin

Requires:      maven-checkstyle-plugin
Requires:      maven-compiler-plugin
Requires:      maven-pmd-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Parent POM defining settings that can be used across Tuscany.

%prep
%setup -q

%build

mvn-rpmbuild install

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp7
- new version

