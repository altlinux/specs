Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jsilver
Version:        1.0.0
Release:        alt1_11jpp8
Summary:        A pure-Java implementation of Clearsilver

License:        ASL 2.0 

URL:            http://code.google.com/p/jsilver/
# svn export http://jsilver.googlecode.com/svn/tags/jsilver-1.0.0 jsilver-1.0.0
# tar caf jsilver-1.0.0.tar.xz jsilver-1.0.0
Source0:        jsilver-1.0.0.tar.xz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  exec-maven-plugin
BuildRequires:  maven-antrun-plugin
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
find . -name *.jar -exec rm -f {} \;
ln -s %{_javadir}/sablecc.jar sablecc/

%mvn_file : jsilver

%build
%mvn_build

# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1106598
mkdir target
mv build/site target

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
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

