BuildRequires: /proc
BuildRequires: jpackage-compat
%global project_version 1.0-beta-2

Name:           plexus-active-collections
Version:        1.0
Release:        alt1_0.7.beta2jpp7
Summary:        Plexus Container-Backed Active Collections

Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/
#svn export http://svn.codehaus.org/plexus/tags/plexus-active-collections-1.0-beta-2/
#tar zcf plexus-active-collections-1.0-beta-2.tar.gz plexus-active-collections-1.0-beta-2/
Source0:        plexus-active-collections-1.0-beta-2.tar.gz

Patch0:         %{name}-migration-to-component-metadata.patch

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  maven
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-component-api
BuildRequires:  plexus-container-default
BuildRequires:  junit

Requires:          plexus-component-api
Requires:          plexus-container-default
Requires:          plexus-utils
Requires:          junit
Requires:          jpackage-utils
Source44: import.info


%description
Plexus Container-Backed Active Collections

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}
%patch0 -p1

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/plexus
install -m 644 target/%{name}-%{project_version}.jar %{buildroot}%{_javadir}/plexus/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom 
%add_maven_depmap JPP.plexus-%{name}.pom plexus/%{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}/

%files
%{_javadir}/plexus/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/plexus/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.beta2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

