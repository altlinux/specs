Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           felix-parent
Version:        1.2.1
Release:        alt5_11jpp7
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

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: easymock2
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-project-info-reports-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-jxr

Requires: junit
Requires: easymock2
Requires: maven
Requires: maven-plugin-plugin
Requires: maven-compiler-plugin
Requires: maven-install-plugin
Requires: maven-jar-plugin
Requires: maven-javadoc-plugin
Requires: maven-resources-plugin
Requires: maven-assembly-plugin
Requires: maven-source-plugin
Requires: maven-deploy-plugin
Requires: maven-gpg-plugin
Requires: maven-project-info-reports-plugin
Requires: maven-release-plugin
Requires: maven-surefire-plugin
Requires: maven-surefire-report-plugin
Requires: maven-plugin-build-helper
Requires: maven-plugin-jxr

Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Source44: import.info


%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q 
%patch0 -p0 -b .sav

%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin

%build
mvn-rpmbuild \
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
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_8jpp7
- new release

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

