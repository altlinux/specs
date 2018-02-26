BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.apache.felix.shell
Name:           felix-shell
Version:        1.4.2
Release:        alt2_3jpp6
Summary:        Apache Felix Shell Service

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.picvi.com/external/apache/felix/org.apache.felix.shell-1.4.2-project.tar.gz
#Fixed org.osgi.core and org.osgi.compendium's groupId
Patch0:        felix-shell-pom.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven2
BuildRequires: felix-osgi-core
BuildRequires: felix-osgi-compendium
BuildRequires: maven-plugin-bundle
BuildRequires: felix-parent

Requires: jpackage-utils
Requires: felix-osgi-core
Requires: felix-osgi-compendium

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info


%description
A simple OSGi command shell service.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p0

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository

mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install

# jars
install -Dpm 644 target/%{bundle}-%{version}.jar   %{buildroot}%{_javadir}/felix/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir}/felix && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.apache.felix %{bundle} %{version} JPP/felix %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.felix-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE NOTICE
%{_javadir}/felix/*
%{_mavenpomdir}/JPP.felix-%{name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2_3jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

