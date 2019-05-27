Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsilver
Version:        1.0.0
Release:        alt2_17jpp8
Summary:        A pure-Java implementation of Clearsilver

License:        ASL 2.0 

URL:            http://code.google.com/p/jsilver/
# svn export http://jsilver.googlecode.com/svn/tags/jsilver-1.0.0 jsilver-1.0.0
# tar caf jsilver-1.0.0.tar.xz jsilver-1.0.0
Source0:        jsilver-1.0.0.tar.xz
# javascript not allowed in javadoc.
Patch0:         jsilver-1.0.0-javascript.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  sablecc
Source44: import.info

%description
A pure-Java implementation of Clearsilver, an HTML template system.

%package javadoc
Group: Development/Java
Summary:        API docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

find . -name *.jar -exec rm -f {} \;
ln -s $(build-classpath sablecc) sablecc/

%pom_change_dep :guava "com.google.guava:guava:15.0"

%mvn_file : jsilver

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_17jpp8
- new version

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- fixed build with new guava

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_12jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

