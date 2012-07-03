# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-remote-resources-plugin
Version:        1.2.1
Release:        alt1_4jpp7
Summary:        Maven Remote Resources Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-remote-resources-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#Class org.apache.maven.shared.artifact.filter.collection.TransitivityFilter which ProcessRemoteResourcesMojo.java imports
#is renamed as org.apache.maven.shared.artifact.filter.collection.ProjectTransitivityFilter in
#the version 1.3 of maven-shared-common-artifact-filters package.
Patch0:        ProcessRemoteResourcesMojo.java.patch

BuildArch: noarch

BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-shared-filtering
BuildRequires: plexus-container-default
BuildRequires: velocity
BuildRequires: maven-shared-artifact-resolver
BuildRequires: maven-shared-common-artifact-filters
BuildRequires: maven-shared-downloader
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: plexus-resources
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-wagon
BuildRequires: maven-shared-verifier
BuildRequires: maven-surefire-provider-junit
BuildRequires: modello

Requires:       maven
Requires:       jpackage-utils
Requires:       maven-wagon
Requires:       maven-shared-artifact-resolver
Requires:       maven-shared-downloader
Requires:       plexus-resources

Obsoletes:      maven2-plugin-remote-resources <= 0:2.0.8
Provides:       maven2-plugin-remote-resources = 1:%{version}-%{release}
Source44: import.info

%description
Process resources packaged in JARs that have been deployed to
a remote repository. The primary use case being satisfied is
the consistent inclusion of common resources in a large set of
projects. Maven projects at Apache use this plug-in to satisfy
licensing requirements at Apache where each project much include
license and notice files for each release.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p0

%build
# fix 613582
# we now use plexus-velocity which has the correct descriptor with a hint.
rm -f src/main/resources/META-INF/plexus/components.xml

mvn-rpmbuild -Dmaven.test.skip=true install javadoc:javadoc

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
%doc DEPENDENCIES LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc DEPENDENCIES LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
- new version

