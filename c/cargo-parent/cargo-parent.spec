BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cargo-parent
Version:        4.11
Release:        alt2_2jpp7
Summary:        Parent pom file for cargo.codehaus.org project

Group:          Development/Java
License:        ASL 2.0
URL:            http://cargo.codehaus.org/
#svn export http://svn.codehaus.org/cargo/pom/tags/cargo-parent-4.11/
Source0:        %{name}-%{version}.tar.gz
# Remove wagon-webdav
Patch0:         cargo-parent-wagon-webdav.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:  codehaus-parent

Requires:       jpackage-utils
Requires:       codehaus-parent
Source44: import.info

%description
This package contains the cargo parent pom.

%prep
%setup -q
%patch0 -p1 -b .wagon-webdav


%build
mvn-rpmbuild install


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.11-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1_2jpp7
- new release

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7-alt1_1jpp7
- new version

