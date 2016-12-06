# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mongo-java-driver
%define version 3.2.1
%{?scl:%scl_package mongo-java-driver}
%{!?scl:%global pkg_name %{name}}

%if 0%{?rhel}
# Use java common's requires/provides generator
%{?java_common_find_provides_and_requires}
%endif

Name:		%{?scl_prefix}mongo-java-driver
Version:	3.2.1
Release:	alt1_2jpp8
Summary:	A Java driver for MongoDB

Group:		Development/Other
BuildArch:	noarch
License:	ASL 2.0
URL:		http://www.mongodb.org/display/DOCS/Java+Language+Center
Source0:	https://github.com/mongodb/%{pkg_name}/archive/r%{version}.tar.gz
Patch0:         %{pkg_name}-gradle-local-fixes.patch

%{!?scl:
BuildRequires:	java-devel
}
BuildRequires:  %{?scl_prefix_java_common}gradle-local
BuildRequires:  maven-local
BuildRequires:  %{?scl_prefix_java_common}javapackages-local
BuildRequires:  mvn(io.netty:netty-buffer)
BuildRequires:  mvn(io.netty:netty-transport)
BuildRequires:  mvn(io.netty:netty-handler)
BuildRequires:  mvn(org.slf4j:slf4j-api)


%{!?scl:
}
%{?scl:
Requires:       %{scl_runtime}
}
Source44: import.info

%description
This is an ueber jar for the MongoDB Java driver.

%package bson
Summary:	A Java-based BSON implementation
Group:		Development/Other
%{!?scl:
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

%package driver
Summary:	The MongoDB Java Driver
Group:		Development/Other
%{!?scl:
}
%{?scl:
Requires:       %{scl_runtime}
}

%description driver
The MongoDB Java Driver

%package driver-core
Summary:	The MongoDB Java Operations Layer
Group:		Development/Other
%{!?scl:
}
%{?scl:
Requires:       %{scl_runtime}
}

%description driver-core
The Java operations layer for the MongoDB Java Driver. Third
parties can wrap this layer to provide custom higher-level APIs

%package driver-async
Summary:	The MongoDB Java Async Driver
Group:		Development/Other
%{!?scl:
}
%{?scl:
Requires:       %{scl_runtime}
}

%description driver-async
The MongoDB Asynchronous Driver.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -qn %{pkg_name}-r%{version}

%patch0 -p2

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

set -ex
%mvn_package org.mongodb:bson:* %{pkg_name}-bson
%mvn_package org.mongodb:%{pkg_name}:* %{pkg_name}
%mvn_package org.mongodb:mongodb-driver-core:* %{pkg_name}-driver-core
%mvn_package org.mongodb:mongodb-driver-async:* %{pkg_name}-driver-async
%mvn_package org.mongodb:mongodb-driver:* %{pkg_name}-driver
%mvn_package org.mongodb:mongodb-javadoc-utils:* __noinstall
%mvn_file org.mongodb:bson:* %{pkg_name}/bson
%mvn_file org.mongodb:%{pkg_name}:* %{pkg_name}/mongo
%mvn_file org.mongodb:mongodb-driver-core:* %{pkg_name}/driver-core
%mvn_file org.mongodb:mongodb-driver-async:* %{pkg_name}/driver-async
%mvn_file org.mongodb:mongodb-driver:* %{pkg_name}/driver
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%gradle_build -f -- -s -i
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles-%{pkg_name}
%doc README.md LICENSE.txt

%files bson -f .mfiles-%{pkg_name}-bson
%doc README.md LICENSE.txt

%files driver -f .mfiles-%{pkg_name}-driver
%doc README.md LICENSE.txt

%files driver-core -f .mfiles-%{pkg_name}-driver-core
%doc README.md LICENSE.txt

%files driver-async -f .mfiles-%{pkg_name}-driver-async
%doc README.md LICENSE.txt

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2jpp8
- new version

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.13.2-alt2_5jpp8
- new version

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

