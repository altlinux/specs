Group: Databases
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(DBD/ODBC.pm) perl(DBI.pm) rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           hsqldb
Version:        2.4.0
Release:        alt1_5jpp8
Epoch:          1
Summary:        HyperSQL Database Engine
License:        BSD
URL:            http://hsqldb.sourceforge.net/

BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/hsqldb/%{name}-%{version}.zip
Source1:        %{name}.cfg
Source2:        %{name}-server.properties
Source3:        %{name}-webserver.properties
Source4:        %{name}-sqltool.rc
Source5:        http://www.hsqldb.org/repos/org/hsqldb/hsqldb/%{version}/hsqldb-%{version}.pom
# Custom systemd files - talking with upstream about incorporating them, see
# http://sourceforge.net/projects/hsqldb/forums/forum/73673/topic/5367103
Source6:        %{name}.systemd
Source7:        %{name}-wrapper
Source8:        %{name}-post
Source9:        %{name}-stop

# Javadoc fails to create since apidocs folder is deleted and not recreated
Patch0:         0001-Fix-javadoc-build.patch
# Package org.hsqldb.cmdline was only compiled with java 1.5
Patch1:         0002-Build-cmdline-classes.patch

BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  glassfish-servlet-api

Requires:       %{name}-lib = %{epoch}:%{version}-%{release}
Requires:       glassfish-servlet-api
Requires(pre):  shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
Source44: import.info
Source45: hsqldb.init


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

%package lib
Group: Development/Java
Summary:    HyperSQL Database Engine library

%description lib
Library part of %{name}.

%package manual
Group: Development/Java
Summary:    Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group: Development/Java
Summary:    Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Group: Development/Java
Summary:    Demo for %{name}
Requires:   %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%patch0 -p1
%patch1 -p1

# set right permissions
find . -name "*.sh" -exec chmod 755 \{\} \;

# remove all _notes directories
for dir in `find . -name _notes`; do rm -rf $dir; done

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;
find . -name "*.war" -exec rm -f {} \;
find . -name "*.zip" -exec rm -f {} \;

# correct silly permissions
chmod -R go=u-w *

# Fix doc location
sed -i -e 's/doc-src/doc/g' build/build.xml
sed -i -e 's|doc/apidocs|%{_javadocdir}/%{name}|g' index.html

%build
pushd build
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
ant hsqldb javadoc -Dservletapi.lib=$(build-classpath glassfish-servlet-api)
popd

%install
%mvn_file :%{name} %{name}
%mvn_artifact %{SOURCE5} lib/%{name}.jar
%mvn_install -J doc/apidocs

# systemd
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_prefix}/lib/%{name}
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
install -m 755 %{SOURCE7} %{buildroot}%{_prefix}/lib/%{name}/%{name}-wrapper
install -m 755 %{SOURCE8} %{buildroot}%{_prefix}/lib/%{name}/%{name}-post
install -m 755 %{SOURCE9} %{buildroot}%{_prefix}/lib/%{name}/%{name}-stop
# config
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
# serverconfig
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_localstatedir}/lib/%{name}/server.properties
install -m 644 %{SOURCE3} %{buildroot}%{_localstatedir}/lib/%{name}/webserver.properties
install -m 600 %{SOURCE4} %{buildroot}%{_localstatedir}/lib/%{name}/sqltool.rc
# lib
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/lib
# data
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/data
# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -r doc index.html %{buildroot}%{_docdir}/%{name}

pushd %{buildroot}%{_localstatedir}/lib/%{name}/lib
    # build-classpath can not be used as the jar is not
    # yet present during the build
    ln -s %{_javadir}/hsqldb.jar hsqldb.jar
    ln -s $(build-classpath glassfish-servlet-api) servlet.jar
popd
# sysv init
install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
#install -m 755 bin/%{name} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -m 755 %{SOURCE45} $RPM_BUILD_ROOT%{_initrddir}/%{name}


%preun
%preun_service hsqldb

%pre
%{_sbindir}/groupadd  -f -r %{name} 2> /dev/null || :
%{_sbindir}/useradd  -g %{name} -s /sbin/nologin \
    -d %{_localstatedir}/lib/%{name} -r %{name} 2> /dev/null || :

%post
%post_service hsqldb

%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_prefix}/lib/%{name}/%{name}-wrapper
%{_prefix}/lib/%{name}/%{name}-post
%{_prefix}/lib/%{name}/%{name}-stop
%attr(0700,hsqldb,hsqldb) %{_localstatedir}/lib/%{name}/data
%{_localstatedir}/lib/%{name}/lib
%{_localstatedir}/lib/%{name}/server.properties
%{_localstatedir}/lib/%{name}/webserver.properties
%attr(0600,hsqldb,hsqldb) %{_localstatedir}/lib/%{name}/sqltool.rc
%dir %{_localstatedir}/lib/%{name}
%dir %{_prefix}/lib/%{name}
%{_initrddir}/%{name}

%files lib -f .mfiles

%files manual
%doc %{_docdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt1_5jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.3.4-alt1_4jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.3.4-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.3.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.3.3-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.3.3-alt1_1jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1.3-alt3_10jpp7
- new release

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1.3-alt3_9jpp7
- fixed init script

* Sun Mar 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1.3-alt2_9jpp7
- fixed scripts (closes: 28719)

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.8.1.3-alt1_9jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.10-alt2_3jpp6
- built with java 6

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.10-alt1_3jpp6
- new jpp relase

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.10-alt1_2jpp6
- new jpackage release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.8-alt3_2.patch01.7jpp5
- selected java5 compiler explicitly

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.8-alt2_2.patch01.7jpp5
- fixed postinstall script

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.8-alt1_2.patch01.7jpp5
- fixed repolib

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.8-alt1_2.patch01.2jpp5
- converted from JPackage by jppimport script

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0.7-alt2_2jpp1.7
- updated to new jpackage release

* Mon Apr 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.8.0.7-alt2
- Built with java-1.4.0 to maintain backward compatibility

* Thu Apr 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.8.0.7-alt1
- 1.8.0.7 version
- Built with java-1.5.0

* Thu Apr 21 2005 Vladimir Lettiev <crux@altlinux.ru> 1.7.3.3-alt1
- Initial build for ALT Linux Sisyphus

