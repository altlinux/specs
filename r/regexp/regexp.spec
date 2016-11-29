Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
Obsoletes: jakarta-regexp = 1.4-alt1
Obsoletes: jakarta-regexp = 1.4-alt2
Obsoletes: jakarta-regexp = 1.4-alt3
Obsoletes: jakarta-regexp = 1.4-alt4
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           regexp
Epoch:          1
Version:        1.5
Release:        alt1_23jpp8
Summary:        Simple regular expressions API
License:        ASL 2.0
URL:            http://jakarta.apache.org/%{name}/
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/jakarta/%{name}/jakarta-%{name}-%{version}.tar.gz
Source2:        jakarta-%{name}-osgi-manifest.MF
Patch0:         jakarta-%{name}-attach-osgi-manifest.patch

BuildRequires:  ant
BuildRequires:  javapackages-local
Source44: import.info
Provides: jakarta-regexp = %{version}-%{release}


%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up quite
well to the test of time.
It includes complete Javadoc documentation as well as a simple Applet
for visual debugging and testing suite for compatibility.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n jakarta-%{name}-%{version}
%patch0
cp -p %{SOURCE2} MANIFEST.MF
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

cat > pom.xml << EOF
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>jakarta-%{name}</groupId>
  <artifactId>jakarta-%{name}</artifactId>
  <version>%{version}</version>
</project>
EOF

%mvn_file : %{name}

%mvn_alias jakarta-%{name}:jakarta-%{name} %{name}:%{name}

%build
mkdir lib
%ant -Djakarta-site2.dir=. jar javadocs

%mvn_artifact pom.xml build/*.jar

%install
%mvn_install -J docs/api

%check
%ant -Djakarta-site2.dir=. test

# Workaround for RPM bug #646523 - can't change symlink to directory
# TODO: Remove this in F-23
%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_23jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_20jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_10jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_9jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_2jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp5
- new version

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_3jpp1.7
- resurrected from misplaced in obsolete

* Wed Jun 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_3jpp1.7
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

