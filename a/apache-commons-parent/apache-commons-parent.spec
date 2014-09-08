Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       parent
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          26
Release:          alt1_5jpp7
Summary:          Apache Commons Parent Pom
Group:            Development/Java
License:          ASL 2.0
URL:              http://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-26
# tar caf commons-parent-26.tar.xz commons-parent-26
Source0:          %{short_name}-%{version}.tar.xz

#common-build-plugin not in fedora yet
Patch1:           %{name}-remove-build-plugin.patch
BuildArch:        noarch

BuildRequires:    maven-local

BuildRequires:    mvn(org.apache:apache)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:    mvn(org.apache.rat:apache-rat-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)

Requires:         mvn(org.apache:apache)
Requires:         mvn(org.apache.felix:maven-bundle-plugin)
Requires:         mvn(org.apache.maven.plugins:maven-antrun-plugin)
Requires:         mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires:         mvn(org.apache.maven.plugins:maven-jar-plugin)
Requires:         mvn(org.apache.maven.plugins:maven-surefire-plugin)
Requires:         mvn(org.apache.rat:apache-rat-plugin)
Requires:         mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Source44: import.info


%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}
%patch1 -p0

%build
mvn-rpmbuild install

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom

%add_maven_depmap JPP-%{short_name}.pom

%files
%doc LICENSE.txt NOTICE.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:26-alt1_5jpp7
- fc update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:22-alt2_4jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:22-alt1_4jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt6_2jpp6
- build with maven-jxr

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt5_2jpp6
- dropped commons-build-plugin dependency

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt4_2jpp6
- added maven-plugin-bundle as replacement for felix-maven

* Wed Sep 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt3_2jpp6
- removed felix-maven from requires

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt2_2jpp6
- removed mojo-maven2-plugin-* from requires

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_2jpp6
- new jpp release

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_1jpp6
- fixed init script

