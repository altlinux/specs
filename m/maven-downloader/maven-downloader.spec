Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-downloader
Version:        1.1
Release:        alt1_10jpp8
# Maven-shared defines maven-downloader version as 1.2
Epoch:          1
Summary:        Maven artifact downloader
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-downloader
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-downloader-1.1 maven-downloader-1.1
# tar caf maven-downloader-1.1.tar.xz maven-downloader-1.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  plexus-containers-component-metadata

Obsoletes:      maven-shared-downloader < %{epoch}:%{version}-%{release}
Provides:       maven-shared-downloader = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Provide a super simple interface for downloading a single artifact.

This is a replacement package for maven-shared-downloader

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

%pom_add_dep org.apache.maven:maven-compat

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

cp %{SOURCE1} LICENSE.txt

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_10jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_4jpp7
- new release

