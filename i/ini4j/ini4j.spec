# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ini4j
Version:        0.5.1
Release:        alt2_7jpp7
Summary:        Java API for handling files in Windows .ini format
Group:          Development/Java
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

BuildArch:      noarch

# See http://ini4j.sourceforge.net/dependencies.html
BuildRequires:  jpackage-utils

BuildRequires:  maven

BuildRequires:  javamail
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-changes-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  plexus-mail-sender
BuildRequires:  xmlrpc-client
BuildRequires:  xmlrpc-common

Requires:       jpackage-utils
Source44: import.info


%description
%{name} is a simple Java API for handling configuration files in Windows 
.ini format. Additionally, the library includes Java Preferences API 
implementation based on the .ini file.


%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
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


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

# Tests require easymock2 class extension to compile. This package is not
# available in fedora yet. So disable tests for now.
# Will also need to add the correct depmap for jetty when tests are enabled.

mvn-rpmbuild \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        install javadoc:aggregate


%install
# jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt NOTICE.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*


%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_7jpp7
- fixed deps

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_7jpp7
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2jpp6
- new version

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_4jpp6
- converted from JPackage by jppimport script

