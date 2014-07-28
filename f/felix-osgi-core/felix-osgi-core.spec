Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.osgi.core

Name:    felix-osgi-core
Version: 1.4.0
Release: alt3_12jpp7
Summary: Felix OSGi R4 Core Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org/site/apache-felix-osgi-core.html
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: felix-parent
BuildRequires: maven-surefire-provider-junit4
BuildRequires: jpackage-utils
Source44: import.info


%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

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
export LC_ALL=en_US.UTF-8
mvn-rpmbuild package javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/felix/%{bundle}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.felix-%{bundle}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%add_maven_depmap -a "org.osgi:%{bundle}" JPP.felix-%{bundle}.pom felix/%{bundle}.jar

%files
%doc LICENSE
%{_javadir}/felix
%{_mavenpomdir}/JPP.felix-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_10jpp7
- new release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_6jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_6jpp6
- new version

