%define oldname mockito
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mockito1
Version:        1.10.19
Release:        alt2_17jpp8
Summary:        A Java mocking framework

License:        MIT
URL:            http://%{oldname}.org
Source0:        %{oldname}-%{version}.tar.xz
Source1:        make-%{oldname}-sourcetarball.sh
Patch0:         fixup-ant-script.patch
Patch1:         fix-bnd-config.patch
Patch2:         %{oldname}-matcher.patch
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
Summary:        Javadocs for %{oldname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%pom_add_dep net.sf.cglib:cglib:3.1 maven/mockito-core.pom
find . -name "*.java" -exec sed -i "s|org\.%{oldname}\.cglib|net\.sf\.cglib|g" {} +
mkdir -p lib/compile

%pom_xpath_remove 'target[@name="javadoc"]/copy' build.xml
%mvn_compat_version : %{version} 1

%build
build-jar-repository lib/compile objenesis cglib junit hamcrest/core
ant jar javadoc

# Convert to OSGi bundle
pushd target
bnd wrap \
 --version %{version} \
 --output %{oldname}-core-%{version}.bar \
 --properties ../conf/%{oldname}-core.bnd \
 %{oldname}-core-%{version}.jar
mv %{oldname}-core-%{version}.bar %{oldname}-core-%{version}.jar

# Explicit Require-Bundle on hamcrest
unzip mockito-core-%{version}.jar META-INF/MANIFEST.MF
sed -i -e '2iRequire-Bundle: org.hamcrest.core' META-INF/MANIFEST.MF
jar umf META-INF/MANIFEST.MF mockito-core-%{version}.jar
popd

sed -i -e "s|@version@|%{version}|g" maven/%{oldname}-core.pom
%mvn_artifact maven/%{oldname}-core.pom target/%{oldname}-core-%{version}.jar
%mvn_alias org.%{oldname}:%{oldname}-core org.%{oldname}:%{oldname}-all

%install
%mvn_install -J target/javadoc

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt2_17jpp8
- compat package

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_17jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_10jpp8
- new fc release

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

