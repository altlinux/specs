Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-release
Version:        2.2.1
Release:        alt1_2jpp7
Summary:        Release a project updating the POM and tagging in the SCM

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-release-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/release/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Remove deps needed for tests, till jmock gets packaged
Patch1:         002-mavenrelease-fixbuild.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-scm
BuildRequires:  maven-scm-test
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-utils
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  jaxen

Requires:       jpackage-utils
Source44: import.info

%description
This plugin is used to release a project with Maven, saving a lot of 
repetitive, manual work. Releasing a project is made in two steps: 
prepare and perform.


%package manager
Summary:        Release a project updating the POM and tagging in the SCM
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description manager
This package contains %{name}-manager needed by %{name}-plugin.


%package plugin
Summary:        Release a project updating the POM and tagging in the SCM
Group:          Development/Java
Requires:       %{name}-manager = %{version}-%{release}
Requires:       jpackage-utils
Provides: maven2-plugin-release = %version

%description plugin
This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
Obsoletes:      %{name}-manager-javadoc <= 2.0-1
Obsoletes:      %{name}-plugin-javadoc <= 2.0-1
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
cat > README << EOT
%{name}-%{version}

This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.
EOT


%build
mvn-rpmbuild -e -Dmaven.test.skip=true install javadoc:aggregate


%install
# jars
install -Dp -m 644 %{name}-manager/target/%{name}-manager-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-manager.jar
install -Dp -m 644 %{name}-plugin/target/%{name}-plugin-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-plugin.jar

# javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/
cp -rp target/site/apidocs  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}
install -pm 644 pom.xml  \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 %{name}-manager/pom.xml  \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-manager.pom
install -pm 644 %{name}-plugin/pom.xml  \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-plugin.pom

%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-manager.pom %{name}-manager.jar
%add_maven_depmap JPP-%{name}-plugin.pom %{name}-plugin.jar

%files
%doc README
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/*

%files manager
%{_javadir}/*manager*
%{_mavenpomdir}/JPP-%{name}-manager.pom

%files plugin
%{_javadir}/*plugin*
%{_mavenpomdir}/JPP-%{name}-plugin.pom

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt1_2jpp7
- complete build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

