Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          javaparser
Version:       1.0.11
Release:       alt1_2jpp8
Summary:       Java 1.7 Parser and AST
License:       GPLv3+ and LGPLv3+
# https://github.com/before/javaparser/
URL:           http://javaparser.github.io/javaparser/
Source0:       https://github.com/javaparser/javaparser/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
A Java 1.7 Parser with AST generation and visitor support.
The AST records the source code structure, java doc and
comments. It is also possible to change the AST nodes or
create new ones to modify the source code.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' readme.md

%mvn_file :%{name} %{name}

%build

# test skip http://code.google.com/p/javaparser/issues/detail?id=43
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc readme.md
%doc COPYING COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%doc COPYING COPYING.LESSER

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp7
- new version

