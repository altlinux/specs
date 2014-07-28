Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name digester
%global short_name commons-%{base_name}

Name:          apache-%{short_name}
Version:       1.8.1
Release:       alt3_14jpp7
Summary:       XML to Java object mapping module
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: apache-commons-beanutils >= 1.8
BuildRequires: apache-commons-logging >= 1.1.1
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
Requires:      jpackage-utils
Requires:      apache-commons-beanutils >= 1.8
Requires:      apache-commons-logging >= 1.1.1

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
Requires:      jpackage-utils
Obsoletes:     jakarta-%{short_name}-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%build
mvn-rpmbuild install javadoc:aggregate

# Build rss -- needed by struts
export CLASSPATH=$(build-classpath commons-beanutils commons-collections commons-logging junit)
CLASSPATH=${CLASSPATH}:`pwd`/target/%{short_name}-%{version}.jar
pushd src/examples/rss
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist
popd


%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{short_name}.jar %{buildroot}/%{_javadir}/%{name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "%{short_name}:%{short_name}"
# rss -- needed by struts
cp -p src/examples/rss/dist/%{short_name}-rss.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss.jar


%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES*
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_javadir}/*
#%{_javadir}/*-rss*.jar

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
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

