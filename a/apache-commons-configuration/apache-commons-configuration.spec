Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       configuration
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.9
Release:        alt3_4jpp7
Summary:        Commons Configuration Package

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  jpackage-utils
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  javacc-maven-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit

BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-jexl
BuildRequires:  apache-commons-jxpath
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-vfs
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  xml-commons-resolver


Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < 0:%{version}-%{release}
Source44: import.info


%description
Configuration is a project to provide a generic Configuration
interface and allow the source of the values to vary. It
provides easy typed access to single, as well as lists of
configuration values based on a 'key'.
Right now you can load properties from a simple properties
file, a properties file in a jar, an XML file, JNDI settings,
as well as use a mix of different sources using a
ConfigurationFactory and CompositeConfiguration.
Custom configuration objects are very easy to create now
by just subclassing AbstractConfiguration. This works
similar to how AbstractList works.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

Provides:       jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < 0:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q -n %{short_name}-%{version}-src
%{__sed} -i 's/\r//' LICENSE.txt NOTICE.txt

%build
%mvn_file   : %{short_name} %{name}
%mvn_alias  : org.apache.commons:%{short_name}
# We skip tests because we don't have test deps (dbunit in particular).
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt3_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt3_1jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new version

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp6
- new version

