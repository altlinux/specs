# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ perl(DBI.pm) swig
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Webapp is disabled, since Fedora does not have the Java Webapp guidelines
# finished yet: http://fedoraproject.org/wiki/PackagingDrafts/JavaWebApps
#def_with webapp
%bcond_with webapp

Name:           opengrok
Version:        0.11.1
Release:        alt1_1jpp7
Summary:        Source browser and indexer

Group:          Development/Java
License:        CDDL
URL:            http://opengrok.github.io/OpenGrok/
Source0:        https://java.net/downloads/opengrok/%{name}-%{version}-src.tar.gz
Source1:        opengrok
Source2:        configuration.xml
Source3:        opengrok-README.Fedora.webapp
Source4:        opengrok-README.Fedora.nowebapp
Patch1:         opengrok-0.11.1-nocplib.patch
Patch3:         opengrok-0.11.1-manifest-classpath.patch
Patch6:         opengrok-0.11.1-jflex.patch
Patch7:         opengrok-0.11.1-lucene35.patch

BuildArch:      noarch

%define common_reqs jakarta-oro ant bcel servlet lucene > 3.5 lucene-contrib > 3.5 swing-layout jpackage-utils javacc
Requires:       %{common_reqs}
Requires:       ctags
BuildRequires:  %{common_reqs}
BuildRequires:  jflex >= 1.4
BuildRequires:  java_cup
BuildRequires:  ant
BuildRequires:  unzip
BuildRequires:  junit4
BuildRequires:  ant-junit
BuildRequires:  ctags
BuildRequires:  docbook2X
Source44: import.info

%description
OpenGrok is a fast and usable source code search and cross reference
engine, written in Java. It helps you search, cross-reference and navigate
your source tree. It can understand various program file formats and
version control histories like SCCS, RCS, CVS, Subversion and Mercurial.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.


%if %with webapp
%package tomcat5
Summary:        Source browser web application
Group:          Development/Java
Requires:       %{name} tomcat5

%description tomcat5
OpenGrok web application
%endif


%prep
%setup -q -n %{name}-%{version}-src
%patch1 -p1 -b .nocplib
%patch3 -p1 -b .manifest-classpath
%patch6 -p1 -b .jflex
%patch7 -p1 -b .lucene35

# This is not strictly needed, but to nuke prebuilt stuff
# makes us feel warmer while building
find \( -name '*.jar' -o -name '*.class' -o -name '*.war' \) -delete

# Default war configuration
sed 's,/var/opengrok/etc/configuration.xml,%{_sysconfdir}/%{name}/configuration.xml,' \
        -i web/WEB-INF/web.xml

# README.Fedora
%if %with webapp
cp %{SOURCE3} README.Fedora
%else
cp %{SOURCE4} README.Fedora
%endif


%build
CLASSPATH=$(build-classpath jflex java_cup junit4) %{ant} -v jar javadoc                               \
        -Dfile.reference.org.apache.commons.jrcs.diff.jar=jrcs/lib/org.apache.commons.jrcs.diff.jar \
        -Dfile.reference.org.apache.commons.jrcs.rcs.jar=jrcs/lib/org.apache.commons.jrcs.rcs.jar \
        -Dfile.reference.lucene-core-3.0.2.jar=$(build-classpath lucene)                        \
        -Dfile.reference.lucene-spellchecker-3.0.2.jar=$(build-classpath lucene-contrib/lucene-spellchecker) \
        -Dfile.reference.ant.jar=$(build-classpath ant)                                         \
        -Dfile.reference.bcel-5.2.jar=$(build-classpath bcel)                                   \
        -Dfile.reference.jakarta-oro-2.0.8.jar=$(build-classpath jakarta-oro)                   \
        -Dfile.reference.servlet-api.jar=$(build-classpath servlet)                             \
        -Dfile.reference.swing-layout-0.9.jar=$(build-classpath swing-layout)

# SolBook is more-or-less DocBook subset, so this can be done safely
# FIXME: db2x_docbook2man output is not as nice as it should be
sed '
        s,^<!DOCTYPE.*,<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN" "docbookx.dtd">,
        s,^<?Pub Inc>,,
' dist/opengrok.1 |db2x_docbook2man -


%install
# directories

%if %with webapp
%define webappdir %{_var}/lib/tomcat5/webapps/source
install -d %{buildroot}%{webappdir}/WEB-INF/lib
%endif

install -d %{buildroot}%{_javadir}
install -d %{buildroot}%{_javadocdir}/%{name}
install -d %{buildroot}%{_javadocdir}/%{name}-jrcs
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_var}/lib/%{name}/data
install -d %{buildroot}%{_var}/lib/%{name}/src
install -d %{buildroot}%{_datadir}/pixmaps

# jar
install -p -m 644 dist/opengrok.jar %{buildroot}%{_javadir}/opengrok-%{version}.jar
ln -sf opengrok-%{version}.jar %{buildroot}%{_javadir}/opengrok.jar

# jrcs
install -p -m 644 lib/jrcs.jar \
        %{buildroot}%{_javadir}/opengrok-jrcs-%{version}.jar
ln -sf opengrok-jrcs-%{version}.jar \
        %{buildroot}%{_javadir}/opengrok-jrcs.jar

# bin
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}

# man
install -p -m 644 opengrok.1 %{buildroot}%{_mandir}/man1

# javadoc
cp -pR dist/javadoc/. %{buildroot}%{_javadocdir}/%{name}

# Configuration file configuration.xml
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}

%if %with webapp
# Make love, not war!
unzip -q dist/source.war -d %{buildroot}%{webappdir}
(IFS=:; for file in $(build-classpath                   \
        bcel jakarta-oro swing-layout                   \
        lucene lucene-contrib/lucene-spellchecker)      \
        %{_javadir}/opengrok.jar                        \
        %{_javadir}/opengrok-jrcs.jar
do
        ln -sf $file %{buildroot}%{webappdir}/WEB-INF/lib
done)
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/opengrok.conf`
touch $RPM_BUILD_ROOT/etc/opengrok.conf


%files
%{_javadir}/*
%{_bindir}/opengrok
%{_mandir}/man1/opengrok.1*
%{_var}/lib/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/configuration.xml
%doc CHANGES.txt LICENSE.txt README.txt doc/EXAMPLE.txt README.Fedora
%config(noreplace,missingok) /etc/opengrok.conf


%files javadoc
%{_javadocdir}/*


%if %with webapp
%files tomcat5
%{webappdir}
%config(noreplace) %{webappdir}/WEB-INF/web.xml
%config(noreplace) %{webappdir}/index_body.html
%endif


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_5jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_4jpp7
- new version

