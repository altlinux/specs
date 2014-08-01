Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jettison
Version:        1.3.3
Release:        alt1_1jpp7
Summary:        A JSON StAX implementation
Group:          Development/Java
License:        ASL 2.0
URL:            http://jettison.codehaus.org/
# svn export http://svn.codehaus.org/jettison/tags/jettison-1.3.3 jettison-1.3.3
# rm -rf jettison-1.3.3/trunk
# tar cvJf jettison-1.3.3.tar.xz jettison-1.3.3
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

# Change the POM to use the version of woodstox that we have available:
Patch0: %{name}-update-woodstox-version.patch

%if 0%{?rhel} <= 5
%else
%endif
BuildRequires:     jpackage-utils
BuildRequires:     maven-local
BuildRequires:     maven-compiler-plugin
BuildRequires:     maven-install-plugin
BuildRequires:     maven-jar-plugin
BuildRequires:     maven-javadoc-plugin
BuildRequires:     maven-release-plugin
BuildRequires:     maven-resources-plugin
BuildRequires:     woodstox-core
BuildRequires:     stax2-api
Requires:          jpackage-utils
Source44: import.info


%description
Jettison is a collection of Java APIs (like STaX and DOM) which read
and write JSON. This allows nearly transparent enablement of JSON based
web services in services frameworks like CXF or XML serialization
frameworks like XStream.


%package javadoc
Summary:           Javadocs for %{name}
Group:             Development/Java
Requires:          %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:          jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
# We don't need wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%build
# Disable the tests until BZ#796739 is fixed:
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true install javadoc:aggregate


%install
# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
cp -p target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc src/main/resources/META-INF/LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%files javadoc
%doc src/main/resources/META-INF/LICENSE
%{_javadocdir}/%{name}


%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_1jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp7
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc2.1jpp5
- jpp5 build

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc1.1jpp1.7
- added dependency on new excalibur

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.rc1.1jpp1.7
- converted from JPackage by jppimport script

