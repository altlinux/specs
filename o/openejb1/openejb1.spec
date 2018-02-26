BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2012, JPackage Project
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

%define gcj_support 0

%define bname openejb

Name:           openejb1
Summary:        EJB Container System and EJB Server
Url:            http://openejb.apache.org/
Version:        1.0
Release:        alt6_3jpp6
Epoch:          0
License:        Apache Software License 2
Group:          Development/Java
#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
Source0:        http://dist.codehaus.org/openejb/distributions/openejb-1.0-src.tar.gz

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        openejb1-1.0-jpp-depmap.xml
Source5:        openejb1.conf
Source6:        openejb1.default.cmp_local_tx_database.xml
Source7:        openejb1-core-1.0.pom
Source8:        openejb1-itests-1.0.pom
Source9:        openejb1-loader-1.0.pom
Source10:       openejb1-webadmin-1.0.pom



Patch0:         openejb1-moviefun-project_xml.patch
Patch1:         openejb1-etc-project_xml.patch
Patch2:         openejb1-JdbcConnection.patch
Patch3:         openejb1-JdbcConnectionFactory.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit
BuildRequires:  maven1 >= 0:1.1
BuildRequires:  maven1-plugins-base
BuildRequires:  maven1-plugin-changelog
BuildRequires:  maven1-plugin-checkstyle
BuildRequires:  maven1-plugin-developer-activity
BuildRequires:  maven1-plugin-file-activity
BuildRequires:  maven1-plugin-html2xdoc
BuildRequires:  maven1-plugin-jdepend
BuildRequires:  maven1-plugin-jxr
BuildRequires:  maven1-plugin-license
BuildRequires:  maven1-plugin-multiproject
BuildRequires:  maven1-plugin-pmd
BuildRequires:  maven1-plugin-test
BuildRequires:  maven1-plugin-war
BuildRequires:  maven1-plugin-xdoc
BuildRequires:  saxon
BuildRequires:  saxon-scripts
#
BuildRequires:  backport-util-concurrent
BuildRequires:  castor0
BuildRequires:  apache-commons-fileupload
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-ejb-2.1-api
BuildRequires:  geronimo-j2ee-connector-1.5-api
BuildRequires:  geronimo-jta-1.0.1B-api
BuildRequires:  geronimo-servlet-2.4-api
BuildRequires:  geronimo-ejb-2.1-api
BuildRequires:  hsqldb
BuildRequires:  log4j
BuildRequires:  jakarta-oro
BuildRequires:  regexp
#BuildRequires:  xalan-j2
#BuildRequires:  xerces-j2
#BuildRequires:  xml-commons-jaxp-1.3-apis

#
# modules
Requires:       backport-util-concurrent
Requires:       castor0
Requires:       geronimo-ejb-2.1-api
Requires:       geronimo-j2ee-connector-1.5-api
Requires:       geronimo-jta-1.0.1B-api
Requires:       geronimo-servlet-2.4-api
Requires:       apache-commons-fileupload
Requires:       apache-commons-logging
Requires:       junit
Requires:       log4j
Requires:       regexp
#Requires:       xerces-j2
#Requires:       xml-commons-jaxp-1.3-apis

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
OpenEJB is an open source, modular, configurable, and 
extendable EJB Container System and EJB Server.
OpenEJB comes with fast, lightweight EJB Servers for 
both Local and Remote access. 
That's right, deploy your EJBs into the container system, 
then just start the Remote EJB Server from the command 
line! Or, put OpenEJB in your class path and use it as 
an embedded library through the Local EJB Server.
As a container system, OpenEJB works like a big plug-in for
middleware servers like Web servers, CORBA servers, and 
application servers. By plugging in OpenEJB these servers 
obtain instant EJB compliance for hosting 
Enterprise JavaBeans! 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%prep
%setup -q -n %{bname}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

export DEPCAT=$(pwd)/openejb1-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > openejb1-1.0-depmap.new.xml

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

sed -i -e 's|^OPENEJB_HOME=.*|OPENEJB_HOME=/usr/share/openejb1; cd $OPENEJB_HOME|' modules/core/src/bin/openejb

%build
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        default 

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        -Dgoal=javadoc:generate,xdoc:transform \
        multiproject:goal


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 \
        modules/core/target/%{bname}-core-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 \
        modules/core/target/%{bname}-loader-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/loader-%{version}.jar
install -m 644 \
        modules/itests/target/%{bname}-itests-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/itests-%{version}.jar
install -m 644 \
        modules/itests/target/%{bname}-itests-beans.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/itests-beans-%{version}.jar
install -m 644 \
        modules/itests/target/%{bname}-itests-client.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/itests-client-%{version}.jar
install -m 644 \
        modules/webadmin/target/%{bname}-webadmin-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webadmin-%{version}.jar
install -m 644 \
        modules/webadmin/target/%{bname}-webadmin-clienttools.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webadmin-clienttools-%{version}.jar
install -m 644 \
        modules/webadmin/target/%{bname}-webadmin-ejbgen.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webadmin-ejbgen-%{version}.jar
install -m 644 \
        modules/webadmin/target/%{bname}-webadmin-main.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webadmin-main-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap openejb openejb-core %{version} JPP/%{name} core
%add_to_maven_depmap openejb openejb-loader %{version} JPP/%{name} loader
%add_to_maven_depmap openejb openejb-itests %{version} JPP/%{name} itests
%add_to_maven_depmap openejb openejb-webadmin %{version} JPP/%{name} webadmin

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-itests.pom
install -pm 644 %{SOURCE9} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-loader.pom
install -pm 644 %{SOURCE10} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webadmin.pom

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

# server
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/beans
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/beans
ln -sf %{_javadir}/%{name}/webadmin-main.jar openejb-webadmin-main.jar
ln -sf %{_javadir}/%{name}/webadmin-clienttools.jar openejb-webadmin-clienttools.jar
ln -sf %{_javadir}/%{name}/webadmin-ejbgen.jar openejb-webadmin-ejbgen.jar
ln -sf %{_javadir}/%{name}/itests-beans.jar openejb-itests-beans.jar
popd
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install -m 755 target/%{bname}-%{version}/bin/openejb \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 644 target/%{bname}-%{version}/conf/*.xml \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 644 target/%{bname}-%{version}/conf/*.conf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/openejb.conf
install -m 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/default.cmp_local_tx_database.xml

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
ln -sf $(build-classpath geronimo-j2ee-connector-1.5-api)
ln -sf $(build-classpath geronimo-ejb-2.1-api)
ln -sf $(build-classpath xerces-j2)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath oro)
ln -sf %{_javadir}/%{name}/core.jar openejb-core-%{version}.jar
ln -sf $(build-classpath geronimo-jta-1.0.1B-api)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath commons-fileupload)
ln -sf $(build-classpath backport-util-concurrent)
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis)
ln -sf %{_javadir}/%{name}/loader.jar openejb-loader-%{version}.jar
ln -sf $(build-classpath regexp)
ln -sf $(build-classpath castor0) castor.jar
ln -sf %{_javadir}/%{name}/itests-client.jar openejb-itests-client.jar
ln -sf $(build-classpath log4j)
popd 

install -d -m 755 $RPM_BUILD_ROOT%{_var}/log/%{name}
ln -sf %{_var}/log/%{name} \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/logs

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/war
install -m 644 target/%{bname}-%{version}/war/openejb-itests-webapp.war \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/war
install -m 644 target/%{bname}-%{version}/war/moviefun.war \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/war
install -m 644 target/%{bname}-%{version}/war/openejb-loader-1.0.war \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/war
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/moviefun
cp -pr target/%{bname}-%{version}/moviefun/* \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/moviefun

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

for md in core itests loader webadmin; do
        install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$md
        cp -pr modules/$md/target/docs/apidocs/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$md
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf modules/core/target/docs/apidocs
cp -pr modules/core/target/docs/* \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm \
    --exclude /usr/share/openejb1/moviefun/moviefun.war \
    --exclude /usr/share/openejb1/war/moviefun.war \
    --exclude /usr/share/openejb1/war/openejb-itests-webapp.war
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%preun
(cd %{_datadir}/%{name}/lib
rm -f *.jar
)

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/beans
%{_datadir}/%{name}/bin
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/logs
%{_datadir}/%{name}/war
%{_var}/log/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%files demo
%doc %{_datadir}/%{name}/moviefun

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_3jpp6
- built with java 6 due to abstract getParentLogger

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_3jpp6
- fixed build with moved maven1

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_3jpp6
- converted from JPackage by jppimport script

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Thu Oct 09 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- fixed broken symlink

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

