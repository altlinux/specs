Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# Work around koji build issues on ppc64
# See https://www.redhat.com/archives/fedora-devel-list/2009-March/msg00022.html
%global eclipse_dir $(ls -d /usr/lib*/eclipse)

Name:           glazedlists
Version:        1.9.1
Release:        alt1_1jpp8
Summary:        A toolkit for transformations in Java
License:        (LGPLv2+ or MPLv1.1+) and ASL 2.0
Url:            http://www.glazedlists.com/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/net/java/dev/glazedlists/%{name}_java15/%{version}/glazedlists_java15-%{version}-dist.zip
# Build against system jars instead of downloaded ones, and don't build things we don't
# have requirements for
Patch0:         %{name}-1.9.1-build.xml.patch
# Use the new Hibernate API
Patch1:         %{name}-1.9.1-hibernate.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  aqute-bnd
BuildRequires:  aqute-bndlib
BuildRequires:  eclipse-swt
BuildRequires:  icu4j
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  jgoodies-forms
BuildRequires:  hibernate-core
BuildRequires:  hsqldb
BuildRequires:  jvnet-parent
Source44: import.info

# Adapted from http://www.javaworld.com/javaworld/jw-10-2004/jw-1025-glazed.html
# because the project website doesn't have a good description
%description
Glazed Lists is an open source toolkit for list transformations. If a
developer is already familiar with ArrayList or Vector, he or she will feel
at home with Glazed Lists.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Documentation for the %{name} Java library.

%prep
%setup -q -c %{name}-%{version}
# Build against system jars, and disable unavailable extensions
%patch0 -b .build-xml -p0
rm -rf extensions/ktable extensions/swinglabs extensions/nachocalendar \
        extensions/japex extensions/issuesbrowser 
# Use correct libdir for this build architecture
sed -i.eclipse_dir "s#ECLIPSE_DIR#%{_jnidir}#" build.xml

%if 0%{?fedora} >= 23
%global taskdef_classpath /usr/share/java/aqute-bnd/biz.aQute.bnd.jar:/usr/share/java/aqute-bnd/biz.aQute.bndlib.jar
%else
%global taskdef_classpath /usr/share/java/aqute-bnd.jar
%endif

sed -i.taskdef_classpath "s#TASKDEF_CLASSPATH#%{taskdef_classpath}#" build.xml

# Use new hibernate API
%patch1 -b .hibernate -p0

# Clean up line endings
dos2unix license

# Don't download ant tasks
sed -i -e '/"deploy-init"/ s/download-mavenanttasks,//' build.xml

%build
ant -v dist jar sourcejar javadocjar deploy-init -DartifactId=%{name}

# Maven artifact installation
%mvn_artifact target/deploy/pom.xml target/deploy/%{name}-%{version}.jar

%install
%mvn_install -J target/docs/api

%files -f .mfiles
%doc license readme.html
%dir %{_javadir}/glazedlists
%dir %{_mavenpomdir}/glazedlists

%files javadoc -f .mfiles-javadoc
%doc license

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_1jpp8
- new version

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_7jpp8
- unbootstrap build

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_2jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_3jpp7
- new version

