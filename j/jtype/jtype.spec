# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jtype
Version:        0.1.2
Release:        alt1_5jpp7
Summary:        A small library for working with the Java 5 type system

Group:          Development/Java
License:        ASL 2.0 
# svn export http://jtype.googlecode.com/svn/tags/0.1.2 jtype-0.1.2
# tar caf jtype-0.1.2.tar.xz jtype-0.1.2
URL:            http://code.google.com/p/jtype/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-disable-wagon-svn.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin

Requires:       jpackage-utils
Source44: import.info

%description
Java 5 introduced a richer type system for generics with Type and its various
sub-types, but lacks any easy way to perform common operations on these types.
JType aims to fill this gap. 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p 0

%build
# Tests require jmock, so skip them for now
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:javadoc

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_5jpp7
- new release

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3jpp7
- new version

