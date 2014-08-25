Epoch: 0
BuildRequires: tomcat6-jsp-2.1-api
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       jxpath
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.3
Release:          alt3_15jpp7
Summary:          Simple XPath interpreter

Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:           %{short_name}-mockrunner.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-assembly-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-idea-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    servlet
BuildRequires:    jsp
BuildRequires:    el_api

Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:%{version}-%{release}
Source44: import.info

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils

Provides:         jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name}-javadoc < 0:%{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

%build
# we are skipping tests because we don't have com.mockrunner in repos yet
%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:%{short_name}
%mvn_build -f

%install
%mvn_install

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_15jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_11jpp7
- rebuild with maven-local

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_9jpp7
- fixed build

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_9jpp7
- fc release

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp6
- new version

