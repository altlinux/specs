BuildRequires: /proc
BuildRequires: jpackage-compat
%define project_version 1.0-alpha-15

Name:           plexus-component-api
Version:        1.0
Release:        alt1_0.7.alpha15jpp7
Summary:        Plexus Component API

Group:          Development/Java
License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        plexus-component-api-1.0-alpha-15.tar.gz

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant ant-nodeps
BuildRequires:  maven >= 0:2.0.4-9
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  plexus-digest
BuildRequires:  plexus-classworlds

Requires:          plexus-digest
Requires:          plexus-classworlds
Requires:          jpackage-utils
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2
Source44: import.info

%description
Plexus Component API

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install


# jars
install -d -m 0755 %{buildroot}%{_javadir}/plexus
install -m 644 target/%{name}-%{project_version}.jar %{buildroot}%{_javadir}/plexus

(cd %{buildroot}%{_javadir}/plexus && for jar in *-%{project_version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{project_version}||g"`; done)

%add_to_maven_depmap org.codehaus.plexus %{name} %{project_version} JPP/plexus %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/plexus/%{name}
rm -rf target/site/api*

%files
%{_javadir}/plexus/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/plexus/%{name}-%{version}
%{_javadocdir}/plexus/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.alpha15jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

