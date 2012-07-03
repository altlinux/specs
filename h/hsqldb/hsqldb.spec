# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 1.8.0.10
%define name hsqldb
# Copyright (c) 2000-2010, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define version_full %{version}

%define repodir %{_javadir}/repository.jboss.com/hsqldb/%{version_full}
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag patch01

%define cvs_version 1_8_0_10

Name:           hsqldb
Version:        1.8.0.10
Release:        alt2_3jpp6
Epoch:          1
Summary:        Hsqldb Database Engine
Group:          Development/Java
License:        BSD
URL:            http://hsqldb.sourceforge.net/
# http://downloads.sourceforge.net/hsqldb/hsqldb_1_8_0_10.zip
Source0:        %{name}_%{cvs_version}.zip
Source1:        %{name}-1.8.0-standard.cfg
Source2:        %{name}-1.8.0-standard-server.properties
Source3:        %{name}-1.8.0-standard-webserver.properties
Source4:        %{name}-1.8.0-standard-sqltool.rc
Source5:        hsqldb-component-info.xml
Source6:        http://repository.jboss.org/maven2/hsqldb/hsqldb/1.8.0.8patch01-brew/hsqldb-1.8.0.8patch01-brew.pom
Patch0:         hsqldb-1.8.0-scripts.patch
Patch1:         hsqldb-tmp.patch
Patch2:         hsqldb-1.8.0.8-backport.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires(pre):  shadow-utils
Requires:       jpackage-utils
Requires:       servlet_2_5_api
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  jpackage-utils
BuildRequires:  servlet_2_5_api
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
Buildarch:      noarch
%endif
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

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}

perl -pi -e 's/\r$//g' doc/*.txt doc/src/hsqldbstylesheet.css

cp -p %{SOURCE6} hsqldb.pom
perl -pi -e 's|<version>.*</version>|<version>%{version}</version>|' hsqldb.pom

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

%patch0 -p0
%patch1 -p1
%patch33 -p1
#%%patch2 -p1

%build
export CLASSPATH=$(build-classpath \
jsse/jsse \
jsse/jnet \
jsse/jcert \
jdbc-stdext \
servlet_2_5_api \
junit)
export OPT_JAR_LIST=:
pushd build
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first jar javadoc
popd

%install

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)
# bin
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 bin/runUtil.sh $RPM_BUILD_ROOT%{_bindir}/%{name}RunUtil
# sysv init
install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 bin/%{name} $RPM_BUILD_ROOT%{_initrddir}/%{name}
# config
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
# serverconfig
install -d -m 755 $RPM_BUILD_ROOT%{_var}/lib/%{name}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_var}/lib/%{name}/server.properties
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_var}/lib/%{name}/webserver.properties
install -m 600 %{SOURCE4} $RPM_BUILD_ROOT%{_var}/lib/%{name}/sqltool.rc
# lib
install -d -m 755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/lib
install -m 644 lib/functions         $RPM_BUILD_ROOT%{_var}/lib/%{name}/lib
# data
install -d -m 755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/data
# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/demo
install -m 755 demo/*.sh         $RPM_BUILD_ROOT%{_datadir}/%{name}/demo
install -m 644 demo/*.html         $RPM_BUILD_ROOT%{_datadir}/%{name}/demo
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r doc/src/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/src

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p hsqldb.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap hsqldb hsqldb %{version_full} JPP %{name}

(cd %{buildroot}%{_var}/lib/%{name}/lib
    ln -s $(build-classpath hsqldb) hsqldb.jar
    ln -s $(build-classpath servlet_2_5_api) servlet.jar
) 2>/dev/null || :

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version_full}/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/hsqldb.jar $RPM_BUILD_ROOT%{repodirlib}/hsqldb.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom $RPM_BUILD_ROOT%{repodirlib}/hsqldb.pom
%endif

%pre
%{_sbindir}/groupadd -g 96 -f -r %{name} 2> /dev/null || :
%{_sbindir}/useradd -u 96 -g %{name} -s /sbin/nologin \
    -d %{_var}/lib/%{name} -r %{name} 2> /dev/null || :

%files
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/hsqldb_lic.txt
%attr(0755,root,root) %{_bindir}/hsqldbRunUtil
%attr(0755,root,root) %{_initrddir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,hsqldb,hsqldb) %{_var}/lib/%{name}/data
%dir %{_var}/lib/%{name}/lib
%{_var}/lib/%{name}/lib/functions
%{_var}/lib/%{name}/lib/hsqldb.jar
%{_var}/lib/%{name}/lib/servlet.jar
%attr(0644,root,root) %{_var}/lib/%{name}/server.properties
%attr(0644,root,root) %{_var}/lib/%{name}/webserver.properties
%attr(0600,hsqldb,hsqldb) %{_var}/lib/%{name}/sqltool.rc
%dir %{_var}/lib/%{name}
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj
%{_libdir}/gcj/%{name}/*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%exclude %{_javadir}/repository.jboss.com/*
%exclude %{_javadir}/repository.jboss.com

%files manual
%doc %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
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

