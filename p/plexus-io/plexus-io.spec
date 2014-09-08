Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           plexus-io
Version:        2.0.5
Release:        alt1_8jpp7
Summary:        Plexus IO Components

Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/plexus-components/plexus-io
Source0:        https://github.com/sonatype/plexus-io/tarball/plexus-io-%{version}#/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch: noarch

BuildRequires: jpackage-utils

BuildRequires: plexus-utils
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-components-pom
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n sonatype-plexus-io-1a0010b
cp %{SOURCE1} .

%build
export XMVN_COMPILER_SOURCE="1.5"
%mvn_file  : plexus/io
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc NOTICE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE-2.0.txt


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

