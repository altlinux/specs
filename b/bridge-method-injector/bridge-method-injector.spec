Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           bridge-method-injector
Version:        1.14
Release:        alt1_5jpp8
Summary:        Evolve Java classes without breaking compatibility
# License is specified in pom file
License:        MIT
URL:            https://github.com/infradna/bridge-method-injector
BuildArch:      noarch

Source0:        https://github.com/infradna/%{name}/archive/%{name}-parent-%{version}.tar.gz
# License text copied from http://www.opensource.org/licenses/mit-license.php
# Upstream doesn't care about license texts in repository
Source1:        LICENSE.txt

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
BuildRequires:  mvn(org.jenkins-ci:annotation-indexer)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
Source44: import.info

%description
This package contains small Java library for generating
synthetic bridge methods with different return types
to help backward compatibility.

%package -n bridge-method-annotation
Group: Development/Java
Summary:        Bridge method injection annotations

%description -n bridge-method-annotation
This package contains annotations for injecting bridge methods.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{name}-parent-%{version}

cp %{SOURCE1} LICENSE

%mvn_package :bridge-method-annotation bridge-method-annotation

# We don't have this extension
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-svn']]"
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-svn']]" injector
%pom_remove_plugin :nexus-staging-maven-plugin

# We don't have asm-all with debug information
%pom_change_dep :asm-debug-all :asm-all injector

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE
%files -n bridge-method-annotation -f .mfiles-bridge-method-annotation
%doc LICENSE
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_3jpp8
- java 8 mass update

