BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 3.2.1
%define name apache-commons-collections
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without maven
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name       collections
%define short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.2.1
Release:        alt5_6jpp6
Epoch:          0
Summary:        Apache Commons Collections Package
License:        ASL 2.0
Group:          Development/Java
Url:            http://commons.apache.org/collections
Source0:        http://www.apache.org/dist/jakarta/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        collections-tomcat5-build.xml
Patch0:         %{name}-javadoc-nonet.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.1
%if %with maven
BuildRequires:  apache-commons-parent >= 0:12
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
%endif
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package testframework
Summary:        Testframework for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-testframework = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-testframework < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-testframework = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-testframework < %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description testframework
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package tomcat5
Summary:        Collection dependency for Tomcat5
Group:          Development/Java
Provides:       jakarta-%{short_name}-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-tomcat5 < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-tomcat5 < %{epoch}:%{version}-%{release}

%description tomcat5
Collections dependency for Tomcat5

%package testframework-javadoc
Summary:        Javadoc for %{name}-testframework
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-testframework-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-testframework-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-testframework-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-testframework-javadoc < %{epoch}:%{version}-%{release}

%description testframework-javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -p1 -b .sav0

cp %{SOURCE4} .

cp -p %{SOURCE1} settings.xml

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif


%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dproject.build.directory=$(pwd)/target"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 tf.javadoc
%else
#FIXME Enabling tests with gcj causes memory leaks!
# See http://gcc.gnu.org/bugzilla/show_bug.cgi?id=28423
%if %{gcj_support}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djava.io.tmpdir=. jar javadoc tf.validate tf.jar dist.bin dist.src tf.javadoc
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djava.io.tmpdir=. test dist tf.javadoc
%endif
%endif

# commons-collections-tomcat5
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f collections-tomcat5-build.xml

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -p -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 target/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%else
install -p -m 644 build/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 build/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%endif

#tomcat5
install -p -m 644 collections-tomcat5/%{short_name}-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5-%{version}.jar

%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap %{short_name} %{short_name}-testframework %{version} JPP %{short_name}-testframework
%add_to_maven_depmap org.apache.commons %{short_name}-testframework %{version} JPP %{short_name}-testframework

ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar
ln -s %{name}-testframework-%{version}.jar %{buildroot}%{_javadir}/%{name}-testframework.jar
ln -s %{name}-testframework-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-testframework-%{version}.jar
ln -s %{name}-testframework-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-testframework.jar
ln -s %{name}-testframework-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-testframework-%{version}.jar
ln -s %{name}-testframework-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-testframework.jar
ln -s %{name}-tomcat5-%{version}.jar %{buildroot}%{_javadir}/%{name}-tomcat5.jar
ln -s %{name}-tomcat5-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-tomcat5-%{version}.jar
ln -s %{name}-tomcat5-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-tomcat5.jar
ln -s %{name}-tomcat5-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-tomcat5-%{version}.jar
ln -s %{name}-tomcat5-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-tomcat5.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -p *.txt target/site
cp -p *.html target/site
%else
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}
ln -s jakarta-%{short_name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{short_name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}

# testframework-javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
cp -pr build/docs/testframework/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-testframework-%{version}
ln -s jakarta-%{short_name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-testframework
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-testframework-%{version}
ln -s %{short_name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-testframework

# manual
%if %with maven
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/jakarta-%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{short_name}-%{version}
%endif

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/project name=""/project name="%{name}"/;s/id="commons-collections"/id="apache-collections"/' %{buildroot}%{repodir}/component-info.xml

%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc PROPOSAL.html README.txt LICENSE.txt RELEASE-NOTES.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/jakarta-%{short_name}-%{version}.jar
%{_javadir}/jakarta-%{short_name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files testframework
%{_javadir}/%{name}-testframework-%{version}.jar
%{_javadir}/%{name}-testframework.jar
%{_javadir}/%{short_name}-testframework-%{version}.jar
%{_javadir}/%{short_name}-testframework.jar
%{_javadir}/jakarta-%{short_name}-testframework-%{version}.jar
%{_javadir}/jakarta-%{short_name}-testframework.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-testframework-%{version}.jar.*
%endif

%files tomcat5
%{_javadir}/*-tomcat5*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/*-tomcat5*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jakarta-%{short_name}-%{version}
%{_javadocdir}/jakarta-%{short_name}
%{_javadocdir}/%{short_name}-%{version}
%{_javadocdir}/%{short_name}

%files testframework-javadoc
%{_javadocdir}/%{name}-testframework-%{version}
%{_javadocdir}/%{name}-testframework
%{_javadocdir}/jakarta-%{short_name}-testframework-%{version}
%{_javadocdir}/jakarta-%{short_name}-testframework
%{_javadocdir}/%{short_name}-testframework-%{version}
%{_javadocdir}/%{short_name}-testframework

%if %with maven
%files manual
%{_docdir}/%{name}-%{version}
%{_docdir}/jakarta-%{short_name}-%{version}
%{_docdir}/%{short_name}-%{version}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_6jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_5jpp6
- fixed conflicts/obsoletes (closes: #24858)

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt4_5jpp6
- fixed repolib id

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_5jpp6
- fixed repolib

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_5jpp6
- add obsoletes

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp6
- new version

