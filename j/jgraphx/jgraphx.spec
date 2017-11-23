# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jgraphx
%{?scl:%scl_package jgraphx}
%{!?scl:%global pkg_name %{name}}

%if 0%{?rhel}
# Use java common's requires/provides generator
%{?java_common_find_provides_and_requires}
%endif

Name:           %{?scl_prefix}jgraphx
Version:        3.6.0.0
Release:        alt1_3jpp8
Summary:        Java Graph Drawing Component

Group:          Development/Other
License:        BSD
URL:            http://www.jgraph.com/jgraph.html
Source0:        http://www.jgraph.com/downloads/jgraphx/archive/%{pkg_name}-%(echo %{version} |sed 's/\./_/g').zip
Source1:        bnd.properties

BuildRequires:  %{?scl_prefix_java_common}javapackages-local
BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  %{?scl_prefix_maven}aqute-bnd
%{!?scl:
Requires:       jpackage-utils
}
%{?scl:Requires: %scl_runtime}

BuildArch:      noarch
Source44: import.info

%description
JGraphX is the a powerful, easy-to-use and feature-rich graph drawing
component for Java. It is a rewrite of JGraph, also known as JGraph 6.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
%{!?scl:
Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
}
%{?scl:Requires: %scl_runtime}
BuildArch: noarch

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n %{pkg_name}
find -name '*.jar' -delete
rm -rf docs/api

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
ant build maven-jar

#Convert to OSGi bundle
pushd lib
%if 0%{?fedora} >= 23
  bnd wrap --output %{pkg_name}.bar --properties %{SOURCE1} \
           --version %{version} %{pkg_name}.jar
%else
  java -jar $(build-classpath aqute-bnd) wrap -output jgraphx.bar -properties %{SOURCE1} %{pkg_name}.jar
%endif
mv %{pkg_name}.bar %{pkg_name}.jar
popd
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_artifact pom.xml lib/%{pkg_name}.jar
%mvn_install -J docs/api/
%{?scl:EOF}

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%if 0%{?rhel} <= 6
  %doc license.txt
%else
  %doc license.txt
%endif

%files javadoc -f .mfiles-javadoc
%if 0%{?rhel} <= 6
  %doc license.txt
%else
  %doc license.txt
%endif

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.0.0-alt1_3jpp8
- new version

* Mon Apr 14 2014 Andrey Cherepanov <cas@altlinux.org> 2.5.1.0-alt1
- New version (ALT #30003)

* Tue May 28 2013 Andrey Cherepanov <cas@altlinux.org> 1.9.2.5-alt1_2jpp6.M60P.1
- Backport new version to p6 branch

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.2.5-alt1_2jpp7
- new version

