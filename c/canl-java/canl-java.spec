Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		canl-java
Version:	2.2.1
Release:	alt1_1jpp8
Summary:	EMI Common Authentication library - bindings for Java

#		The main parts of the code are BSD
#		Parts derived from glite security utils java are Apache 2.0
#		Parts derived from bouncycastle are MIT
#		Parts derived from Apache Commons IO are Apache 2.0
#		See LICENSE.txt for details
License:	BSD and ASL 2.0 and MIT
URL:		https://github.com/eu-emi/%{name}/
Source0:	https://github.com/eu-emi/%{name}/archive/canl-%{version}.tar.gz
#		Disable tests that require network connections
Patch0:		%{name}-test.patch
#		https://github.com/eu-emi/canl-java/pull/86
Patch1:		%{name}-javadoc.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.52
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on) >= 1.52
Source44: import.info

%description
This is the Java part of the EMI caNl -- the Common Authentication Library.

%package javadoc
Group: Development/Java
Summary:	Javadoc documentation for %{name}
BuildArch: noarch

%description javadoc
Javadoc documentation for EMI caNl.

%prep
%setup -q -n %{name}-canl-%{version}
%patch0 -p1
%patch1 -p1

# Remove maven-wagon-webdav-jackrabbit dependency
%pom_xpath_remove pom:build/pom:extensions

# GPG signing requires a GPG key
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

# Avoid build dependency bloat
%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%doc API-Changes.txt README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp8
- new version

