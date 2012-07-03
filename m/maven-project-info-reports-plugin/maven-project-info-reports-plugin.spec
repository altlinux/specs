# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-project-info-reports-plugin
Version:        2.4
Release:        alt1_5jpp7
Summary:        Maven Project Info Reports Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-project-info-reports-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#- Removed junit-addons dependency as there is no junit-addons available in koji, meanwhile set test skip as true.
Patch0:        %{name}-pom.patch
BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: apache-commons-parent
BuildRequires: maven-plugin-plugin
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-shared-dependency-tree
BuildRequires: maven-doxia-tools
BuildRequires: maven-shared-jar
BuildRequires: maven-wagon
BuildRequires: maven-scm
BuildRequires: maven-doxia
BuildRequires: plexus-container-default
BuildRequires: plexus-component-api
BuildRequires: plexus-i18n
BuildRequires: plexus-utils
BuildRequires: apache-commons-validator
BuildRequires: httpunit
BuildRequires: maven-plugin-testing-harness
BuildRequires: servlet25
BuildRequires: netbeans-cvsclient
BuildRequires: maven-jarsigner-plugin
BuildRequires: keytool-maven-plugin
BuildRequires: joda-time

Requires:       maven
Requires:       jpackage-utils
Requires:       plexus-container-default
Requires:       plexus-component-api
Requires:       plexus-i18n
Requires:       plexus-utils
Requires:       apache-commons-validator
Requires:       httpunit
Requires:       servlet25
Requires:       maven-shared-jar
Requires:       maven-scm
Requires:       joda-time

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-project-info-reports <= 0:2.0.8
Provides: maven2-plugin-project-info-reports = 0:%{version}-%{release}
Source44: import.info

%description
The Maven Project Info Reports Plugin is a plugin 
that generates standard reports for the specified project.
  

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -c
%patch0 -p0 -b .sav

%build
pushd %{name}-%{version}
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc
popd

%install
pushd %{name}-%{version}
# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
popd

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

