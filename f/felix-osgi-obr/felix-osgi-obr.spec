Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.osgi.service.obr

Name:           felix-osgi-obr
Version:        1.0.2
Release:        alt2_9jpp7
Summary:        Felix OSGi OBR Service API

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
Source0:        http://www.apache.org/dist/felix/org.osgi.service.obr-%{version}-project.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  felix-osgi-core

Requires:       jpackage-utils
Requires:       felix-osgi-core
Source44: import.info

%description
OSGi OBR Service API.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}/felix
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

install -p -m 644 target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/felix/%{bundle}.jar
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.felix-%{bundle}.pom
%add_maven_depmap JPP.felix-%{bundle}.pom felix/%{bundle}.jar

cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/felix/%{bundle}.jar
%{_mavenpomdir}/JPP.felix-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_9jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp7
- new release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp7
- fc package

