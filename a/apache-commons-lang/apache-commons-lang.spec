Epoch: 0
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       lang
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.6
Release:        alt3_12jpp7
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch1:         0002-Fix-FastDateFormat-for-Java-7-behaviour.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit

Provides:       jakarta-commons-lang = 0:%{version}-%{release}
Obsoletes:      jakarta-commons-lang <= 0:2.4
Source44: import.info
Provides:       %{short_name} = %{epoch}:%{version}-%{release}

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

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Obsoletes:      jakarta-%{short_name}-javadoc <= 0:2.4
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch1 -p1
sed -i 's/\r//' *.txt *.html

# "enum" is used as a Java identifier, which is prohibited in Java >= 1.5
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . "
    <configuration><source>1.3</source></configuration>"


%mvn_file  : %{name} %{short_name}
%mvn_alias : org.apache.commons: %{base_name}:%{base_name}
# this package needs to be compiled with -source 1.3 option
%mvn_config buildSettings/compilerSource 1.3

%build
%mvn_build

%install
%mvn_install
ln -sf %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

%files -f .mfiles
%doc PROPOSAL.html LICENSE.txt RELEASE-NOTES.txt NOTICE.txt
%{_javadir}/jakarta-%{short_name}.jar

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_12jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_7jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt3_7jpp6
- restored javadoc

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_7jpp6
- fixed build

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp6
- renamed

