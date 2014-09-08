Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name commons-digester

Name:          apache-%{short_name}
Version:       2.1
Release:       alt1_1jpp7
Summary:       XML to Java object mapping module
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/digester/
Source0:       http://archive.apache.org/dist/commons/digester/source/%{short_name}-%{version}-src.tar.gz
BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: apache-commons-beanutils >= 1.8
BuildRequires: apache-commons-logging >= 1.1.1
BuildRequires: maven-local

Provides:      jakarta-%{short_name} = %{version}-%{release}
Obsoletes:     jakarta-%{short_name} < %{version}-%{release}
Source44: import.info

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

%package javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
Obsoletes:     jakarta-%{short_name}-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

# Build rss -- needed by struts
export CLASSPATH=$(build-classpath commons-beanutils commons-collections commons-logging junit)
CLASSPATH=${CLASSPATH}:`pwd`/target/%{short_name}-%{version}.jar
pushd src/examples/rss
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist
popd


%install
%mvn_install
# rss -- needed by struts
cp -p src/examples/rss/dist/%{short_name}-rss.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss.jar


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
#%{_javadir}/*-rss*.jar

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_14jpp7
- new release

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp7
- fc update

* Tue Mar 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp6
- bumped release to fix obsoletes

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt2_11jpp6
- fixed repolib version

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_11jpp6
- new version

