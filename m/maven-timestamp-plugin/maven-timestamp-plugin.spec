Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-timestamp-plugin
Version:        1.1
Release:        alt3_9jpp7
Summary:        Provides formatted timestamps for maven builds
License:        ASL 2.0
URL:            http://code.google.com/p/maven-timestamp-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-timestamp-plugin.googlecode.com/svn/tags/maven-timestamp-plugin-1.1 maven-timestamp-plugin
# tar caf maven-timestamp-plugin-1.1.tar.xz maven-timestamp-plugin 
Source0:        maven-timestamp-plugin-1.1.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-project)
Source44: import.info

%description
There are a few ways to get a timestamp in your maven build. Unfortunately 
most of them make you jump through giant hoops. This maven plugin makes it 
as simple as 1-2-3 to create a timestamp at your disposal.
Also, it enables you to use the syntax of SimpleDateFormat to form custom 
formatted dates. 

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc readme.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp7
- full version

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

