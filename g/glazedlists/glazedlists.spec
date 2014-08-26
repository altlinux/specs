# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Work around koji build issues on ppc64
# See https://www.redhat.com/archives/fedora-devel-list/2009-March/msg00022.html
%global eclipse_dir $(ls -d /usr/lib*/eclipse)

Name:           glazedlists
Version:        1.9.0
Release:        alt1_1jpp7
Summary:        A toolkit for transformations in Java
License:        (LGPLv2+ or MPLv1.1+) and ASL 2.0
Group:          Development/Java
Url:            http://publicobject.com/glazedlists/
BuildArch:      noarch

Source0:        http://search.maven.org/remotecontent?filepath=net/java/dev/glazedlists/glazedlists_java15/1.9.0/glazedlists_java15-1.9.0-dist.zip
# Build against system jars instead of downloaded ones, and don't build things we don't
# have requirements for
Patch0:         %{name}-1.9.0-build.xml.patch
# Use the new Hibernate API
Patch1:         %{name}-1.9.0-hibernate.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant

BuildRequires:  dos2unix
BuildRequires:  aqute-bnd
BuildRequires:  eclipse-swt
BuildRequires:  icu4j
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  jgoodies-forms
BuildRequires:  hibernate
BuildRequires:  hsqldb

Requires:       jpackage-utils
Source44: import.info

# Adapted from http://www.javaworld.com/javaworld/jw-10-2004/jw-1025-glazed.html
# because the project website doesn't have a good description
%description
Glazed Lists is an open source toolkit for list transformations. If a
developer is already familiar with ArrayList or Vector, he or she will feel
at home with Glazed Lists.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch
%description javadoc
Documentation for the %{name} Java library.

%prep
%setup -q -c %{name}-%{version}
# Build against system jars, and disable unavailable extensions
%patch0 -p1
rm -rf extensions/ktable extensions/swinglabs extensions/nachocalendar \
        extensions/japex extensions/issuesbrowser 
# Use correct libdir for this build architecture
sed -i "s#ECLIPSE_DIR#%{eclipse_dir}#" build.xml

# Use new hibernate API
%patch1 -p1

# Clean up line endings
dos2unix license

%build
ant jar docs

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 target/%{name}_java15-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r target/docs/api ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc license readme.html
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc license
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1_1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_3jpp7
- new version

