BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       lang
%global short_name      commons-%{base_name}3

Name:           apache-%{short_name}
Version:        3.1
Release:        alt2_3jpp7
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-site-plugin
BuildRequires:  maven
BuildRequires:  apache-commons-parent
BuildRequires:  apache-commons-io
BuildRequires:  junit4
%if 0%{?rhel} <= 0
BuildRequires:  easymock3
%endif

BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils >= 0:1.6
Source44: import.info


%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

With version of commons-lang 3.x, developers decided to change API and
therefore created differently named artifact and jar files. This is
the new version, while apache-commons-lang is the compatibility
package.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

%build
mvn-rpmbuild \
%if 0%{?rhel}
    -Dmaven.test.skip=true \
%endif
    install javadoc:aggregate

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_3jpp7
- new release

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp7
- new version

