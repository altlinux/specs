Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           easymock
Version:        3.3.1
Release:        alt1_4jpp8
Summary:        Easy mock objects
License:        ASL 2.0
URL:            http://www.easymock.org

Source0:        https://github.com/easymock/easymock/archive/easymock-%{version}.tar.gz

Patch5:         %{name}-remove-android-support.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.mycila.maven-license-plugin:maven-license-plugin)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.cglib:cglib)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

Obsoletes:      %{name}3 < %{version}-%{release}
Provides:       %{name}3 = %{version}-%{release}
Obsoletes:      %{name}2 < 2.5.2-10
Source44: import.info


%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
# Unpack the sources:
%setup -q -n easymock-easymock-%{version}

find . -name "*.zip" -delete

# remove android support
rm -fr easymock/src/main/java/org/easymock/internal/Android*.java
%patch5 -p1 -b .sav
%pom_xpath_remove "pom:profile[pom:id[text()='android']]"
%pom_remove_dep :dexmaker easymock

# fix cglib aId and gId
%pom_remove_dep :cglib easymock
%pom_add_dep net.sf.cglib:cglib easymock

# remove some warning caused by unavailable plugin
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin

# retired
%pom_remove_plugin :maven-timestamp-plugin

%pom_disable_module easymock-test-integration
%pom_disable_module easymock-test-osgi

# For compatibility reasons
%mvn_file ":easymock{*}" easymock@1 easymock3@1

# ssh not needed during our builds 
%pom_xpath_remove pom:extensions

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc easymock/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc easymock/LICENSE.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_3jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_20jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_18jpp7
- fc update

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_8jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- new jpackage release

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

