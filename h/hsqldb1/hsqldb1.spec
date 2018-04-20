Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%global cvs_version 1_8_1_3
%global majorversion 1
Name:          hsqldb1
Version:       1.8.1.3
Release:       alt1_14jpp8
Summary:       HyperSQL Database Engine
License:       BSD
URL:           http://hsqldb.sourceforge.net/
Source0:       http://downloads.sourceforge.net/hsqldb/hsqldb_%{cvs_version}.zip
Source1:       http://mirrors.ibiblio.org/pub/mirrors/maven2/hsqldb/hsqldb/1.8.0.10/hsqldb-1.8.0.10.pom
Patch0:        hsqldb-jdbc-4.1.patch

BuildRequires: ant
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: junit
BuildRequires: glassfish-servlet-api

Requires:      glassfish-servlet-api

BuildArch:     noarch
Source44: import.info

%description
HSQLdb is a relational database engine written in JavaTM , with a JDBC
driver, supporting a subset of ANSI-92 SQL. It offers a small (about
100k), fast database engine which offers both in memory and disk based
tables. Embedded and server modes are available. Additionally, it
includes tools such as a minimal web server, in-memory query and
management tools (can be run as applets or servlets, too) and a number
of demonstration examples.
Downloaded code should be regarded as being of production quality. The
product is currently being used as a database and persistence engine in
many Open Source Software projects and even in commercial projects and
products! In it's current version it is extremely stable and reliable.
It is best known for its small size, ability to execute completely in
memory and its speed. Yet it is a completely functional relational
database management system that is completely free under the Modified
BSD License. Yes, that's right, completely free of cost or restrictions!

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n hsqldb

# set right permissions
find . -name "*.sh" -exec chmod 755 \{\} \;
# remove all _notes directories
for dir in `find . -name _notes`; do rm -rf $dir; done
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;
find . -name "*.war" -exec rm -f {} \;
# correct silly permissions
chmod -R go=u-w *

%patch0 -p1

cp %{SOURCE1} ./pom.xml

%mvn_file hsqldb:hsqldb %{name}

%mvn_compat_version : %{majorversion}

%build
export CLASSPATH=$(build-classpath glassfish-servlet-api junit)
pushd build
ant jar javadoc
popd

%install
%mvn_artifact pom.xml lib/hsqldb.jar
%mvn_install -J doc/src

%files -f .mfiles
%doc --no-dereference doc/hsqldb_lic.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference doc/hsqldb_lic.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_12jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1.3-alt1_8jpp8
- new version

