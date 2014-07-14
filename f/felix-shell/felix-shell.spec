BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.apache.felix.shell
Name:           felix-shell
Version:        1.4.2
Release:        alt3_7jpp7
Summary:        Apache Felix Shell Service

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.picvi.com/external/apache/felix/org.apache.felix.shell-1.4.2-project.tar.gz
#Fixed org.osgi.core and org.osgi.compendium's groupId
Patch0:        felix-shell-pom.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: felix-osgi-core
BuildRequires: felix-osgi-compendium
BuildRequires: maven-plugin-bundle
BuildRequires: felix-parent

Requires:       jpackage-utils
Requires: felix-osgi-core
Requires: felix-osgi-compendium
Source44: import.info


%description
A simple OSGi command shell service.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p0

%build
mvn-rpmbuild -e -Dmaven.test.skip=true install javadoc:javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/felix
install -Dpm 644 target/%{bundle}-%{version}.jar   %{buildroot}%{_javadir}/felix/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.felix-%{name}.pom
%add_maven_depmap JPP.felix-%{name}.pom felix/%{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}
 
%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE NOTICE
%{_javadir}/felix/*
%{_mavenpomdir}/JPP.felix-%{name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2_7jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2_3jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

