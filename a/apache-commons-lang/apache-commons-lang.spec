Epoch: 0
Group: Development/Other
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name       lang
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.6
Release:        alt5_32jpp11
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0

URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         0000-Fix-FastDateFormat-for-Java-7-behaviour.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit
Source44: import.info
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}

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
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

sed -i 's/\r//' *.txt *.html

%mvn_file  : %{name} %{short_name}
%mvn_alias : org.apache.commons: %{base_name}:%{base_name}

# remove org.apache.commons.lang.enum package
# "enum" is a keyword since Java 4 and cannot be used as an identifier
rm -r src/main/java/org/apache/commons/lang/enum/
rm -r src/test/java/org/apache/commons/lang/enum/
rm src/test/java/org/apache/commons/lang/enums/EnumTest.java

# convert some stray ISO-8859-1 characters to UTF-8
iconv -f ISO-8859-1 -t UTF-8 \
    src/main/java/org/apache/commons/lang/Entities.java > \
    src/main/java/org/apache/commons/lang/Entities.java.utf-8
mv src/main/java/org/apache/commons/lang/Entities.java.utf-8 \
    src/main/java/org/apache/commons/lang/Entities.java

%build
%mvn_build -f -- \
    -Dcommons.osgi.symbolicName=org.apache.commons.lang \
    -Dmaven.compiler.source=1.8 \
    -Dmaven.compiler.target=1.8 \
    -Dsource=1.8

%install
%mvn_install

%files -f .mfiles
%doc PROPOSAL.html RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:2.6-alt5_32jpp11
- fixed build

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_24jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_22jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_21jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_20jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_19jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_18jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_17jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_13jpp7
- new release

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

