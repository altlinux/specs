Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash cb6709646eed97c271d73f50ad750cc43c8e052a
Name:             paranamer
Version:          2.8
Release:          alt1_2jpp8
Summary:          Library for accessing non-private method parameter names at run-time
License:          BSD
URL:              https://github.com/paul-hammant/paranamer
Source0:          https://github.com/paul-hammant/paranamer/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(com.thoughtworks.qdox:qdox)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:    mvn(org.mockito:mockito-all)
BuildRequires:    mvn(org.ow2.asm:asm)

BuildArch:        noarch
Source44: import.info

%description
It is a library that allows the parameter names of non-private methods
and constructors to be accessed at run-time.

%package ant
Group: Development/Java
Summary:          ParaNamer Ant

%description ant
This package contains the ParaNamer Ant tasks.

%package generator
Group: Development/Java
Summary:          ParaNamer Generator

%description generator
This package contains the ParaNamer Generator.

%package integration-tests
Group: Development/Java
Summary:          ParaNamer Integration Test Parent POM

%description integration-tests
ParaNamer Integration Test Parent POM.

%package it-011
Group: Development/Java
Summary:          ParaNamer Integration Test 011

%description it-011
ParaNamer IT 011: can use maven plugin defaults.

%package maven-plugin
Group: Development/Java
Summary:          ParaNamer Maven plugin

%description maven-plugin
This package contains the ParaNamer Maven plugin.

%package parent
Group: Development/Java
Summary:          ParaNamer Parent POM

%description parent
This package contains the ParaNamer Parent POM.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{githash}
# Cleanup
find -name "*.class" -print -delete
# Do not erase test resources
find -name "*.jar" -print ! -name "test.jar" -delete

chmod -x LICENSE.txt

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# Disable distribution module
%pom_disable_module %{name}-distribution

# Unavailable test deps
%pom_remove_dep -r net.sourceforge.f2j:
%pom_xpath_remove -r "pom:dependency[pom:classifier = 'javadoc' ]"
# package org.netlib.blas does not exist
rm -r %{name}/src/test/com/thoughtworks/paranamer/JavadocParanamerTest.java
# testRetrievesParameterNamesFromBootstrapClassLoader java.lang.AssertionError:
#       Should not find names for classes loaded by the bootstrap class loader.
rm -r %{name}/src/test/com/thoughtworks/paranamer/BytecodeReadingParanamerTestCase.java

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc LICENSE.txt

%files ant -f .mfiles-%{name}-ant

%files generator -f .mfiles-%{name}-generator
%doc LICENSE.txt

%files integration-tests -f .mfiles-%{name}-integration-tests
%doc LICENSE.txt

%files it-011 -f .mfiles-%{name}-it-011
%doc LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_2jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_1jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_5jpp7
- fixed build

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_5jpp7
- converted from JPackage by jppimport script

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_1jpp6
- use jmock1 (TODO: try jmock2)

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_1jpp6
- fixed build

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build (added BR: sun-annotation-1.0-api)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

