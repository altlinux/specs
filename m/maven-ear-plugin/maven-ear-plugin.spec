# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-ear-plugin
Version:        2.8
Release:        alt1_2jpp7
Summary:        Maven EAR Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-ear-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven
BuildRequires: maven-archiver
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-verifier
BuildRequires: maven-surefire-plugin
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils
BuildRequires: xmlunit

Requires:       maven
Requires:       jpackage-utils
Requires:       maven-plugin-annotations
Requires:       plexus-archiver
Requires:       plexus-containers-container-default
Requires:       plexus-utils

Obsoletes: maven2-plugin-ear <= 0:2.0.8
Provides: maven2-plugin-ear = 0:%{version}-%{release}
Source44: import.info

%description
Generates a J2EE Enterprise Archive (EAR) file.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

# Was missing
%pom_add_dep org.codehaus.plexus:plexus-container-default:1.0

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_2jpp7
- fixed build

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_2jpp7
- new fc release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_1jpp7
- complete build

