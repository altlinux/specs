# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global cvs_version 1_8_1_3

Name:           hsqldb
Version:        1.8.1.3
Release:        alt3_10jpp7
Epoch:          1
Summary:        HyperSQL Database Engine
License:        BSD
URL:            http://hsqldb.sourceforge.net/
Group:          Databases

BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/hsqldb/%{name}_%{cvs_version}.zip
Source1:        %{name}-1.8.0-standard.cfg
Source2:        %{name}-1.8.0-standard-server.properties
Source3:        %{name}-1.8.0-standard-webserver.properties
Source4:        %{name}-1.8.0-standard-sqltool.rc
Source5:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/1.8.0.10/%{name}-1.8.0.10.pom
# Custom systemd files - talking with upstream about incorporating them, see
# http://sourceforge.net/projects/hsqldb/forums/forum/73673/topic/5367103
Source6:        %{name}.systemd
Source7:        %{name}-wrapper
Source8:        %{name}-post
Source9:        %{name}-stop

Patch0:         %{name}-1.8.0-scripts.patch
Patch1:         hsqldb-tmp.patch
Patch2:         %{name}-1.8.0-specify-su-shell.patch
Patch3:         %{name}-jdbc-4.1.patch

BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  junit
BuildRequires:  tomcat-servlet-3.0-api

Requires:       tomcat-servlet-3.0-api
Requires(pre):  shadow-utils
Source44: import.info
Patch33: hsqldb-1.8.0.7-alt-init.patch


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

%package manual
Summary:    Manual for %{name}
Group:      Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:    Demo for %{name}
Group:      Development/Java
Requires:   %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -T -c -n %{name}
(cd ..
unzip -q %{SOURCE0} 
)
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

%patch0
%patch1 -p1
%patch2
%patch3 -p1

cp %{SOURCE5} ./pom.xml
%patch33 -p1

%build
export CLASSPATH=$(build-classpath \
servlet \
junit)
pushd build
ant jar javadoc
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# bin
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 bin/runUtil.sh %{buildroot}%{_bindir}/%{name}RunUtil
# systemd
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_prefix}/lib/%{name}
install -m 755 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
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
install -m 644 lib/functions %{buildroot}%{_var}/lib/%{name}/lib
# data
install -d -m 755 %{buildroot}%{_var}/lib/%{name}/data
# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/demo
install -m 755 demo/*.sh %{buildroot}%{_datadir}/%{name}/demo
install -m 644 demo/*.html %{buildroot}%{_datadir}/%{name}/demo
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r doc/src/* %{buildroot}%{_javadocdir}/%{name}
rm -rf doc/src
# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -r doc/* %{buildroot}%{_docdir}/%{name}-%{version}
cp index.html %{buildroot}%{_docdir}/%{name}-%{version}

# Maven metadata
install -pD -T -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

pushd %{buildroot}%{_var}/lib/%{name}/lib
    # build-classpath can not be used as the jar is not
    # yet present during the build
    ln -s %{_javadir}/hsqldb.jar hsqldb.jar
    ln -s $(build-classpath servlet) servlet.jar
popd
# sysv init
install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 bin/%{name} $RPM_BUILD_ROOT%{_initrddir}/%{name}

%preun
%preun_service hsqldb

%pre
%{_sbindir}/groupadd  -f -r %{name} 2> /dev/null || :
%{_sbindir}/useradd  -g %{name} -s /sbin/nologin \
    -d %{_var}/lib/%{name} -r %{name} 2> /dev/null || :

%post
%post_service hsqldb

%files
%doc doc/hsqldb_lic.txt
%{_javadir}/*
%attr(0755,root,root) %{_bindir}/*
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
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_initrddir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}
%doc doc/hsqldb_lic.txt

%files javadoc
%{_javadocdir}/%{name}
%doc doc/hsqldb_lic.txt

%files demo
%{_datadir}/%{name}

%changelog
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

