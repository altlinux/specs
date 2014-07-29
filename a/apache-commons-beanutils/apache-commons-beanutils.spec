Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name       beanutils
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.8.3
Release:        alt3_9jpp7
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# this will not be needed after commons-collections have proper pom

BuildRequires:  apache-commons-logging >= 0:1.0
BuildRequires:  jpackage-utils > 0:1.7.2
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
#change to apache-commons-collections once transition is done
BuildRequires:  apache-commons-collections-testframework >= 0:2.0
BuildRequires:  apache-commons-collections >= 0:2.0
Requires:       apache-commons-collections >= 0:2.0
Requires:       apache-commons-logging >= 0:1.0


# This should go away with F-17
Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} <= 0:1.7.0
Source44: import.info

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils

Provides:       jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc <= 0:1.7.0
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt


%build

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
# test failures ignored because they are caused by mock
mvn-rpmbuild -Dmaven.test.failure.ignore=true \
             install javadoc:javadoc


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# main jar created from these, we install them just for safe measure
install -m 644 target/%{short_name}-bean-collections-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bean-collections.jar
install -m 644 target/%{short_name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *.jar; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
done
popd # come back from javadir

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{short_name}:%{short_name}-core,%{short_name}:%{short_name}-bean-collections"
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name},org.apache.commons:%{short_name}-core,org.apache.commons:%{short_name}-bean-collections"


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc *.txt
%{_javadir}/%{short_name}.jar
%{_javadir}/%{short_name}-core.jar
%{_javadir}/%{short_name}-bean-collections.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-bean-collections.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadocdir}/%{name}


%changelog
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

