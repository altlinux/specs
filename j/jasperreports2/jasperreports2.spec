# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define oname jasperreports

Summary:        Report-generating tool
Name:           jasperreports2
Version:        2.0.5
Release:        alt1_1jpp6
Epoch:          0
License:        Apache-style Software License & LGPL
URL:            http://www.jasperforge.org/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/%{oname}/%{oname}-%{version}-project.zip
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  junit
BuildRequires:  ecj3
BuildRequires:  hsqldb
BuildRequires:  itext
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  jakarta-commons-javaflow
BuildRequires:  apache-commons-logging
BuildRequires:  apache-poi
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  servlet_2_3_api
Requires:       ecj3
Requires:       hsqldb
Requires:       itext
Requires:       apache-commons-beanutils
Requires:       apache-commons-collections
Requires:       apache-commons-digester
Requires:       apache-commons-logging
Requires:       apache-poi
Requires:       jcommon
Requires:       jfreechart
Requires:       servlet_api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


%description
JasperReports is a powerful open source 
report-generating tool that has the ability 
to deliver rich content onto the screen, to 
the printer or into PDF, HTML, XLS, CSV and 
XML files. It is entirely written in Java 
and can be used in a variety of Java enabled 
applications, including J2EE or Web 
Its main purpose is to help creating page 
oriented, ready to print documents in a 
simple and flexible manner. 

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

%description demo
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done

%build
export OPT_JAR_LIST="ant/ant-trax ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath bcel)
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath commons-javaflow)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath commons-logging-api)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath itext)
ln -sf $(build-classpath jcommon)
ln -sf $(build-classpath ecj3)
ln -sf $(build-classpath jfreechart)
ln -sf $(build-classpath poi)
ln -sf $(build-classpath servlet_2_3_api)
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar docs

cat > demo/samples/webapp/applets/PUT.jasperreports-applet.jar.HERE.txt << EOT
Copy or symlink the jasperreports-applet-2.0.4.jar to this location.
EOT

cat > demo/samples/webapp/WEB-INF/lib/PUT.required.jars.HERE.txt << EOT
Copy or symlink the bsh.jar to this location.
Copy or symlink the commons-beanutils.jar to this location.
Copy or symlink the commons-collections.jar to this location.
Copy or symlink the commons-digester.jar to this location.
Copy or symlink the commons-logging.jar to this location.
Copy or symlink the itext.jar to this location.
Copy or symlink the jasperreports-2.0.4.jar to this location.
EOT

cat > demo/samples/jcharts/GET.jCharts-0.6.0.jar.HERE.txt << EOT
Get and copy or symlink jCharts-0.6.0.jar to this location.
EOT

cat > demo/samples/jfreechart/PUT.jfreechart.jar.HERE.txt << EOT
Copy or symlink the jfreechart.jar (from jfreechart0-1.0.9) to this location.
Copy or symlink the jcommon.jar (from jcommon0-1.0.12) to this location.
EOT


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{oname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{oname}-%{version}-javaflow.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-javaflow-%{version}.jar
install -m 644 dist/%{oname}-%{version}-applet.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-applet-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{oname} %{oname} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr dist/*.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p license.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr demo/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version} -name "*.jar.no" -exec rm -f {} \;

%if %{gcj_support}
%{_bindir}/aot-compile-rpm --exclude /usr/share/java/%{name}-applet-%{version}.jar
%endif

%files
%doc %{_docdir}/%{name}-%{version}/license.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}/quick.reference-%{version}.html
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files demo
%doc %{_datadir}/%{name}-%{version}

%changelog
* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_1jpp6
- jpp6 release

