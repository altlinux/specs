Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       beanutils
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.8.3
Release:        alt3_11jpp7
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-collections:commons-collections-testframework)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent)

Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} <= 0:1.7.0
Source44: import.info

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

Provides:       jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc <= 0:1.7.0
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-assembly-plugin

%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : %{short_name} %{short_name}-core %{short_name}-bean-collections

%build
# Some tests fail in Koji
%mvn_build -f

%install
%mvn_install

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_9jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_7jpp7
- fc update

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_4jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_4jpp6
- fixed repolib

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp6
- new version

