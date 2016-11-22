# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(DBD/ODBC.pm) perl(DBI.pm) unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global pomversion 2.3.0

Name:           hsqldb
Version:        2.3.3
Release:        alt1_4jpp8
Epoch:          1
Summary:        HyperSQL Database Engine
License:        BSD
URL:            http://hsqldb.sourceforge.net/
Group:          Databases

BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/hsqldb/%{name}-%{version}.zip
Source1:        %{name}-1.8.0-standard.cfg
Source2:        %{name}-1.8.0-standard-server.properties
Source3:        %{name}-1.8.0-standard-webserver.properties
Source4:        %{name}-1.8.0-standard-sqltool.rc
Source5:        http://www.hsqldb.org/repos/org/hsqldb/hsqldb/%{pomversion}/hsqldb-%{pomversion}.pom
# Custom systemd files - talking with upstream about incorporating them, see
# http://sourceforge.net/projects/hsqldb/forums/forum/73673/topic/5367103
Source6:        %{name}.systemd
Source7:        %{name}-wrapper
Source8:        %{name}-post
Source9:        %{name}-stop

# Javadoc fails to create since apidocs folder is deleted and not recreated
Patch0:         %{name}-apidocs.patch
# Package org.hsqldb.cmdline was only compiled with java 1.5
Patch1:         %{name}-cmdline.patch

BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  glassfish-servlet-api

Requires:       %{name}-lib = %{epoch}:%{version}
Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
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
Summary:    HyperSQL Database Engine library
Group:      Development/Java

%description lib
Library part of %{name}.

%package manual
Summary:    Manual for %{name}
Group:      Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:    Demo for %{name}
Group:      Development/Java
Requires:   %{name} = %{epoch}:%{version}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}
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

# Fix doc location
sed -i -e 's/doc-src/doc/g' build/build.xml
sed -i -e 's|doc/apidocs|%{_javadocdir}/%{name}|g' index.html

%patch0 -p1
%patch1 -p1

%build
export CLASSPATH=$(build-classpath \
servlet \
junit)
pushd build
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8
ant hsqldb javadoc
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# bin
install -d -m 755 %{buildroot}%{_bindir}
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
install -d -m 755 %{buildroot}%{_var}/lib/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_var}/lib/%{name}/server.properties
install -m 644 %{SOURCE3} %{buildroot}%{_var}/lib/%{name}/webserver.properties
install -m 600 %{SOURCE4} %{buildroot}%{_var}/lib/%{name}/sqltool.rc
# lib
install -d -m 755 %{buildroot}%{_var}/lib/%{name}/lib
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}
mv doc/apidocs %{buildroot}%{_javadocdir}/%{name}
# data
install -d -m 755 %{buildroot}%{_var}/lib/%{name}/data
# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -r doc index.html %{buildroot}%{_docdir}/%{name}

# Maven metadata
install -pD -T -m 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

pushd %{buildroot}%{_var}/lib/%{name}/lib
    # build-classpath can not be used as the jar is not
    # yet present during the build
    ln -s %{_javadir}/hsqldb.jar hsqldb.jar
    ln -s $(build-classpath servlet) servlet.jar
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
    -d %{_var}/lib/%{name} -r %{name} 2> /dev/null || :

%post
%post_service hsqldb

%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_prefix}/lib/%{name}/%{name}-wrapper
%{_prefix}/lib/%{name}/%{name}-post
%{_prefix}/lib/%{name}/%{name}-stop
%attr(0700,hsqldb,hsqldb) %{_var}/lib/%{name}/data
%{_var}/lib/%{name}/lib
%{_var}/lib/%{name}/server.properties
%{_var}/lib/%{name}/webserver.properties
%attr(0600,hsqldb,hsqldb) %{_var}/lib/%{name}/sqltool.rc
%dir %{_var}/lib/%{name}
%dir %{_prefix}/lib/%{name}
%{_initrddir}/%{name}

%files lib -f .mfiles

%files manual
%doc %{_docdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo

%changelog
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

