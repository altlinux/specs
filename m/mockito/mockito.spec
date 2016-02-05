Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           mockito
Version:        1.10.19
Release:        alt1_4jpp8
Summary:        A Java mocking framework

License:        MIT
URL:            http://mockito.org
Source0:        mockito-%{version}.tar.xz
Source1:        make-mockito-sourcetarball.sh
Patch0:         fixup-ant-script.patch
Patch1:         fix-bnd-config.patch
Patch2:         mockito-matcher.patch
# Workaround for NPE in setting NamingPolicy in cglib
Patch3:         setting-naming-policy.patch
# because we have old objenesis
Patch4:         fix-incompatible-types.patch

BuildArch:      noarch
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  objenesis
BuildRequires:  cglib
BuildRequires:  junit
BuildRequires:  hamcrest
BuildRequires:  aqute-bnd

Requires:       objenesis
Requires:       cglib
Requires:       junit
Requires:       hamcrest
Source44: import.info

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%pom_add_dep net.sf.cglib:cglib maven/mockito-core.pom
find . -name "*.java" -exec sed -i "s|org\.mockito\.cglib|net\.sf\.cglib|g" {} +
mkdir -p lib/compile

%build
build-jar-repository lib/compile objenesis cglib junit hamcrest/core
ant jar javadoc
# Convert to OSGi bundle
pushd target
bnd wrap --output mockito-core-%{version}.bar --properties ../conf/mockito-core.bnd \
    --version %{version} mockito-core-%{version}.jar
mv mockito-core-%{version}.bar mockito-core-%{version}.jar
popd

sed -i -e "s|@version@|%{version}|g" maven/mockito-core.pom
%mvn_artifact maven/mockito-core.pom target/mockito-core-%{version}.jar
%mvn_alias org.mockito:mockito-core org.mockito:mockito-all

%install
%mvn_install -J target/javadoc

%files -f .mfiles
%doc NOTICE
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc NOTICE

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_4jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt1_9jpp7
- new version

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt5_0.1jpp6
- fixed build

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

