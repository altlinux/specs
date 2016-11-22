# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           ini4j
Version:        0.5.1
Release:        alt2_15jpp8
Summary:        Java API for handling files in Windows .ini format
Group:          Development/Other
License:        ASL 2.0
URL:            http://www.ini4j.org/

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.zip
# maven-changes-plugin requires javax-activation (which is part of JRE)
Source1:        %{name}.depmap

Patch0:         %{name}-remove-translator.patch
Patch1:         %{name}-remove-wagon.patch
Patch2:         %{name}-fix-maven-license-plugin.patch
Patch3:         %{name}-remove-test-dependencies.patch
# disable checkstyle and pmd; both fail when running over the release
# thanks to heffer for pointing this out
Patch4:         %{name}-remove-checkstyle-and-pmd-checks.patch
Patch5:         %{name}-encoding.patch
# removing maven-license-plugin BR
Patch6:         %{name}-remove-license-plugin.patch
# need to specify version explicitly for maven-dependency-plugin:unpack
# the normal version a specified in the dependency elment is ignored by maven
Patch7:         %{name}-add-version-bsh.patch
# build with java8. technically, this is an api change
Patch8:         %{name}-java8-compat.patch

BuildArch:      noarch

# See http://ini4j.sourceforge.net/dependencies.html
BuildRequires: javapackages-tools rpm-build-java

BuildRequires:  maven-local

BuildRequires:  bsh
BuildRequires:  javamail
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  xmlrpc3-client
BuildRequires:  xmlrpc3-common

Requires: javapackages-tools rpm-build-java
Source44: import.info


%description
%{name} is a simple Java API for handling configuration files in Windows 
.ini format. Additionally, the library includes Java Preferences API 
implementation based on the .ini file.


%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

# remove existing binaries
find . -type f \( -iname "*.jar" -o -iname "*.class" -o -iname "*.exe" -o -iname "*.so" \) | \
  xargs -t rm -f

%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# maven-changes-plugin was retired
%pom_remove_plugin :maven-changes-plugin


%build
# Tests require easymock2 class extension to compile. This package is not
# available in fedora yet. So disable tests for now.
# Will also need to add the correct depmap for jetty when tests are enabled.
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_9jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_7jpp7
- fixed deps

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_7jpp7
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2jpp6
- new version

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_4jpp6
- converted from JPackage by jppimport script

