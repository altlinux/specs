BuildRequires: maven-enforcer-plugin
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           janino-parent
Version:        2.6.1
Release:        alt3_3jpp7
Summary:        Parent POM for Janino

License:        BSD
URL:            http://docs.codehaus.org/display/JANINO/Home
Source0:        http://repo1.maven.org/maven2/org/codehaus/janino/janino-parent/2.6.1/janino-parent-2.6.1.pom
Source1:        http://dist.codehaus.org/janino/new_bsd_license.txt

# Remove sub-modules from the POM; they are built as
# separate RPMs that depend on this one
Patch0:         %{name}-remove-modules.patch

BuildRequires:  codehaus-parent
BuildRequires:  maven-local
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  jpackage-utils

BuildArch:      noarch

Requires:       jpackage-utils
Source44: import.info

%description
%{summary}.


%prep
%setup -q -c -T
cp %{SOURCE0} ./pom.xml
%patch0 -p0
cp %{SOURCE1} ./

%build
mvn-rpmbuild install

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom


%files
%doc new_bsd_license.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt3_3jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_3jpp7
- fc release

