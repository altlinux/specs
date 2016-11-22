Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-release
Version:        2.2.1
Release:        alt6_15jpp8
Summary:        Release a project updating the POM and tagging in the SCM
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-release-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/release/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Remove deps needed for tests, till jmock gets packaged
Patch1:         002-mavenrelease-fixbuild.patch
Patch2:         003-fixing-migration-to-component-metadata.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1015123
Patch3:         %{name}-ftbfs.patch
# Maven's Setting.getRuntimeInfo() was removed, see https://issues.apache.org/jira/browse/MNG-3954
Patch4:         %{name}-MNG-3954.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-scm
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  modello
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-utils
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  jaxen
Source44: import.info

%description
This plugin is used to release a project with Maven, saving a lot of 
repetitive, manual work. Releasing a project is made in two steps: 
prepare and perform.

%package manager
Group: Development/Java
Summary:        Release a project updating the POM and tagging in the SCM

%description manager
This package contains %{name}-manager needed by %{name}-plugin.

%package plugin
Group: Development/Java
Summary:        Release a project updating the POM and tagging in the SCM

%description plugin
This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Provides:       %{name}-manager-javadoc = %{version}-%{release}
Obsoletes:      %{name}-manager-javadoc <= 2.0-1
Provides:       %{name}-plugin-javadoc = %{version}-%{release}
Obsoletes:      %{name}-plugin-javadoc <= 2.0-1
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

cat > README << EOT
%{name}-%{version}

This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.
EOT


%build

%mvn_file :%{name}-manager %{name}-manager
%mvn_file :%{name}-plugin %{name}-plugin
%mvn_package :%{name}-manager manager
%mvn_package :%{name}-plugin plugin
# Skip tests because we don't have dependencies (jmock)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README

%files manager -f .mfiles-manager
%doc LICENSE NOTICE

%files plugin -f .mfiles-plugin
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt6_15jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt6_14jpp8
- java8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt4_9jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt4_7jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt3_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt3_4jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt2_4jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt2_2jpp7
- applied repocop patches

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt1_2jpp7
- complete build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

