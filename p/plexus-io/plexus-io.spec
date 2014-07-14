Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           plexus-io
Version:        2.0.4
Release:        alt2_2jpp7
Summary:        Plexus IO Components

Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/plexus-components/plexus-io
# fetched from https://github.com/sonatype/plexus-io/tarball/plexus-io-2.0.4
Source0:        sonatype-plexus-io-plexus-io-2.0.4-0-g2767dfe.tar.gz
BuildArch: noarch

BuildRequires:  jpackage-utils

BuildRequires: plexus-utils
BuildRequires: plexus-container-default
BuildRequires: maven
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
Requires:  jpackage-utils
Requires: plexus-utils
Requires: plexus-container-default
Source44: import.info

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n sonatype-plexus-io-fd7f1a8

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/plexus
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/plexus/io.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom

%add_maven_depmap JPP.%{name}.pom plexus/io.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/


%files
%doc NOTICE.txt
%{_javadir}/plexus/io.jar
%{_mavenpomdir}/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

