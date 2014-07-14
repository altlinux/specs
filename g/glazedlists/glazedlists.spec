# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           glazedlists
Version:        1.8.0
Release:        alt2_3jpp7
Summary:        A toolkit for transformations in Java
License:        (LGPLv2+ or MPLv1.1+) and ASL 2.0
Group:          Development/Java
Url:            http://publicobject.com/glazedlists/
BuildArch:      noarch

Source0:        http://java.net/downloads/glazedlists/glazedlists-1.8.0/glazedlists-1.8.0-source_java15.zip
# Build against system jars instead of downloaded ones
Patch0:         %{name}-1.8.0-build_xml.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant

BuildRequires:  dos2unix
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  aqute-bnd
BuildRequires:  eclipse-rcp
BuildRequires:  eclipse-swt
BuildRequires:  icu4j
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  jgoodies-forms
BuildRequires:  swingx

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
%patch0 -p1
dos2unix license

%build
# System jars from /usr/share/java
export CLASSPATH=`build-classpath aqute-bnd jgoodies-forms swingx icu4j jcommon jfreechart hsqldb`
# Additional Eclipse/SWT jars
for package in org.eclipse.core.commands_ org.eclipse.equinox.common_ \
        org.eclipse.jface_ org.eclipse.swt.gtk.linux
do
    jar=`ls %{_libdir}/eclipse/plugins/${package}*.jar`
    export CLASSPATH=${CLASSPATH}:${jar}
done
# This ant task also creates the correct pom.xml
ant -Dversion=%{version} maven-bundle

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 target/maven_bundle/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 target/%{name}_java15.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r target/docs ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_3jpp7
- new version

