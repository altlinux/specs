# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             maven-checkstyle-plugin
Version:          2.8
Release:          alt1_2jpp7
Summary:          Plugin that generates a report regarding the code style used by the developers
Group:            Development/Java
License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{name}

Source0:          http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:           %{name}-maven-core-dep.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-plugin-plugin >= 2.5.1
BuildRequires:    plexus-containers-component-metadata >= 1.5.1
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-compiler-plugin >= 2.0.2
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-jar-plugin >= 2.2
BuildRequires:    maven-install-plugin >= 2.2
BuildRequires:    checkstyle >= 5.0
BuildRequires:    plexus-cli >= 1.2
BuildRequires:    maven-artifact-manager
BuildRequires:    plexus-resources

Requires:         maven
Requires:         maven-shared-reporting-impl >= 2.0.4.3
Requires:         maven-doxia >= 1.0
Requires:         maven-doxia-sitetools >= 1.0
Requires:         maven-doxia-tools >= 1.0.2
Requires:         plexus-containers-container-default
Requires:         plexus-resources
Requires:         plexus-utils >= 1.5.6
Requires:         plexus-velocity >= 1.1.7
Requires:         checkstyle >= 5.0
Requires:         velocity >= 1.5
Requires:         apache-commons-collections >= 3.2.1
Requires:         junit >= 3.8.2
Requires:         maven-plugin-testing-harness >= 1.2

Requires:         jpackage-utils

Provides:         maven2-plugin-checkstyle = %{version}-%{release}
Obsoletes:        maven2-plugin-checkstyle <= 0:2.0.8
Source44: import.info

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 
#adapt to upstream checkstyle groupId
sed -i -e "s|<groupId>checkstyle|<groupId>com.puppycrawl.tools|g" pom.xml

%build
# During testing, component descriptors can't be found. 
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.failure.ignore

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

