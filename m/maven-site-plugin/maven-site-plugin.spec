# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-site-plugin
Version:        3.1
Release:        alt2_2jpp7
Summary:        Maven Site Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-site-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Set-source-encoding-property-to-UTF8.patch
Patch1:         0002-Port-to-jetty-8.x.patch

BuildArch: noarch

BuildRequires: maven
BuildRequires: maven-artifact-manager
BuildRequires: maven-plugin-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-doxia-tools
BuildRequires: maven-project
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-shade-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-wagon
BuildRequires: maven-reporting-exec
BuildRequires: plexus-containers-component-metadata
BuildRequires: jetty >= 8.1.0-0.1.rc5
BuildRequires: servlet3
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-i18n
BuildRequires: plexus-velocity
BuildRequires: plexus-utils
BuildRequires: jetty-parent

Requires: maven
Requires: jetty >= 8.1.0-0.1.rc5
Requires: jpackage-utils
Requires: maven-artifact-manager
Requires: maven-doxia-tools
Requires: maven-project
Requires: maven-shared-reporting-api
Requires: maven-wagon
Requires: maven-reporting-exec
Requires: servlet3
Requires: plexus-archiver
Requires: plexus-containers-container-default
Requires: plexus-i18n
Requires: plexus-velocity
Requires: plexus-utils
Requires: jetty-parent

Provides:       maven2-plugin-site = %{version}-%{release}
Obsoletes:      maven2-plugin-site <= 0:2.0.8
Source44: import.info

%description
The Maven Site Plugin is a plugin that generates a site for the current project.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# skipping tests because we need to fix them first for jetty update
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp7
- new version

* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.3jpp
- added obsoletes on maven2-plugin-site

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.2jpp
- added oro dependency to pom

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

