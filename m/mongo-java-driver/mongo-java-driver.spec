# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mongo-java-driver
%define version 2.13.2
%{?scl:%scl_package mongo-java-driver}
%{!?scl:%global pkg_name %{name}}

%if 0%{?rhel}
# Use java common's requires/provides generator
%{?java_common_find_provides_and_requires}
%endif

Name:		%{?scl_prefix}mongo-java-driver
Version:	2.13.2
Release:	alt1_5jpp8
Summary:	A Java driver for MongoDB

Group:		Development/Java
BuildArch:	noarch
License:	ASL 2.0
URL:		http://www.mongodb.org/display/DOCS/Java+Language+Center
Source0:	https://github.com/mongodb/%{pkg_name}/archive/r%{version}.tar.gz

%{!?scl:
}
BuildRequires:  maven-local
BuildRequires:  %{?scl_prefix_java_common}javapackages-local
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  %{?scl_prefix_maven}ant-contrib
BuildRequires:  %{?scl_prefix_maven}testng
BuildRequires:  git


%{!?scl:
Requires:	maven-local
}
%{?scl:
Requires:       %{scl_runtime}
}
Source44: import.info

%description
This is the Java driver for MongoDB.

%package bson
Summary:	A Java-based BSON implementation
Group:		Development/Java
%{!?scl:
Requires:	maven-local
}
%{?scl:
Requires:       %{scl_runtime}
}

%description bson
This is the Java implementation of BSON that the Java driver for
MongoDB ships with.  It can be used separately by Java applications
that require BSON.
# Upstream has hinted that eventually, their bson implementation will
# be better separated out: http://bsonspec.org/#/implementation
# To make things easier for when that does happen, for now the jar
# and javadocs for this are in separate subpackages.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
%{!?scl:
Requires:	maven-local
}
%{?scl:
Requires:       %{scl_runtime}
}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package bson-javadoc
Summary:	Javadoc for %{name}-bson
Group:		Development/Java
%{!?scl:
Requires:	maven-local
}
%{?scl:
Requires:       %{scl_runtime}
}

%description bson-javadoc
This package contains the API documentation for %{name}-bson.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -qn %{pkg_name}-r%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed -i -e "s|@VERSION@|%{version}|g" maven/maven-bson.xml maven/maven-mongo-java-driver.xml
set -ex
%mvn_package org.mongodb:bson:* %{pkg_name}-bson
%mvn_package org.mongodb:%{pkg_name}:* %{pkg_name}
%mvn_file org.mongodb:bson:* %{pkg_name}/bson
%mvn_file org.mongodb:%{pkg_name}:* %{pkg_name}/mongo
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
(
  ln -s $(build-classpath testng) lib/testng-6.3.1.jar
  ant -Dfile.encoding=UTF-8 -Denv.JAVA_HOME=/usr/lib/jvm/java -Dplatforms.JDK_1.5.home=/usr/lib/jvm/java jar javadocs
)
%mvn_artifact maven/maven-bson.xml bson.jar
%mvn_artifact maven/maven-mongo-java-driver.xml mongo.jar
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
# Java-docs
install -d -m 755                 %{buildroot}%{_javadocdir}/%{pkg_name}
install -d -m 755                 %{buildroot}%{_javadocdir}/%{pkg_name}-bson
cp -r -p docs/mongo-java-driver/* %{buildroot}%{_javadocdir}/%{pkg_name}
cp -r -p docs/bson/*              %{buildroot}%{_javadocdir}/%{pkg_name}-bson
%{?scl:EOF}

%files -f .mfiles-%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_datadir}/maven-metadata
%doc README.md LICENSE.txt

%files bson -f .mfiles-%{pkg_name}-bson
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_datadir}/maven-metadata
%doc README.md LICENSE.txt

%files javadoc
%{_javadocdir}/%{pkg_name}
%doc README.md LICENSE.txt

%files bson-javadoc
%{_javadocdir}/%{pkg_name}-bson
%doc README.md LICENSE.txt

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.13.2-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.11.3-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.3-alt1_2jpp7
- full version

