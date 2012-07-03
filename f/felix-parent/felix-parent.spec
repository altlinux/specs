BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           felix-parent
Version:        1.2.1
Release:        alt4_5jpp6
Epoch:          0
Summary:        Parent POM file for Apache Felix Specs

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org/
#svn export http://svn.apache.org/repos/asf/felix/releases/felix-parent-1.2.1/
#tar -jcf felix-parent-1.2.1.tar.bz2 felix-parent-1.2.1/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-depmap.xml
#Remove mockito-all dependency which is not in koji
Patch0:        %{name}-%{version}-pom.patch
Patch33:	felix-parent-1.2.1-alt-pom-fix-target.patch

BuildArch: noarch

BuildRequires: apache-commons-parent >= 0:9
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: easymock2
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-gpg
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-release
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: maven-plugin-build-helper

Requires: apache-commons-parent >= 0:9
Requires: junit
Requires: easymock2
Requires: maven2-plugin-plugin
Requires: maven2-plugin-compiler
Requires: maven2-plugin-install
Requires: maven2-plugin-jar
Requires: maven2-plugin-javadoc
Requires: maven2-plugin-resources
Requires: maven2-plugin-assembly
Requires: maven2-plugin-source
Requires: maven2-plugin-deploy
Requires: maven2-plugin-gpg
Requires: maven2-plugin-site
Requires: maven2-plugin-project-info-reports
Requires: maven2-plugin-release
Requires: maven-surefire-plugin
Requires: maven-surefire-report-maven-plugin
Requires: maven-plugin-build-helper


Requires: jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info


%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q #You may need to update this according to your Source0
%patch0 -p0
%patch33 -p0

%build
#mvn-jpp call is not really needed for the pom file. 
#But it's good to have it there to see changes in dependencies when new version is released
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# depmap
%add_to_maven_depmap org.apache.felix %{name} %{version} JPP/felix %{name}

# legacy depmap
# (some upstream packages haven't caught up with the "felix" -> "felix-parent" rename yet)
%add_to_maven_depmap org.apache.felix felix %{version} JPP/felix %{name}

# poms
install -pD -T -m 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.felix-%{name}.pom

%files
%doc LICENSE NOTICE
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*


%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_5jpp6
- use maven-plugin-build-helper

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_5jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_5jpp6
- new jpp release

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_3jpp6
- dropped mojo-maven2-* dependency

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_3jpp6
- fixed repolib

