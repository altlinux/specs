Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:         jgroups212
Version:      2.12.3
Release:      alt1_12jpp8
Summary:      A toolkit for reliable multicast communication
License:      LGPLv2
URL:          http://www.jgroups.org
# git clone git://github.com/belaban/JGroups.git
# cd JGroups && git checkout Branch_JGroups_2_12 && git checkout-index -f -a --prefix=jgroups212-2.12.3.Final
# find jgroups212-2.12.3.Final/ -name '*.jar' -type f -delete
# tar -cJf jgroups212-2.12.3.Final.tar.xz jgroups212-2.12.3.Final
Source0:       %{name}-%{version}.Final.tar.xz
Patch0:        %{name}-groupid.patch
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(bsh:bsh)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(xalan:serializer)
Source44: import.info

%description
A toolkit for reliable multicast communication.
It allows developers to create reliable multipoint (multicast) applications
where reliability is a deployment issue, and does not have to be implemented
by the application developer. This saves application developers significant
amounts of time, and allows for the application to be deployed in different
environments, without having to change code.

%package javadoc
Group: Development/Java
Summary:    Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.Final
# Cleanup
find . -name '*.jar' -delete
find . -name '*.class' -delete

%patch0 -p1

%pom_remove_plugin :maven-source-plugin
%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17

# Fix incorrect permissions on documentation
chmod 644 README

%mvn_file org.%{name}:jgroups %{name}

%build
# Tests to not current run under maven for this project
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README INSTALL.html
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_5jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_3jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.12.3-alt1_2jpp7
- new version

