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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           dtddoc
Version:        1.1.0
Release:        alt2_3jpp6
Epoch:          0
Summary:        DTD Documentation Tool
License:        X11 License
Url:            http://dtddoc.sourceforge.net/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/dtddoc/DTDDoc_1_1_0.zip
Source1:        empty.zip
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Patch0:         dtddoc-dtdencoding.patch
Requires(post): jpackage-utils
Requires(postun):  jpackage-utils
Requires:       dtdparser
Requires:       jpackage-utils
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  dtdparser
BuildRequires:  jhighlight
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
This little tool is here to help you to document your DTD's
efficiently. It is a straightforward extension of the 
avadoc concept and a not so straightforward implementation 
of some of the concepts solidified by Donald E. Knuth.
Advantages of DTDDoc over competition (let's do some 
marketing :))
* DTDDoc builds documentation for collections of DTD's, not 
  for single ones.
* DTDDoc gives easy to read cardinality information (it's a 
  little more clever than it seems).
* DTDDoc supports multiple character encodings, so you can 
  write your documentation in polish or greek if you want.
The secret aim of this project is also to figure out a 
proper way to document DTD's... That's a little bit more 
philosophical and that's what is really interesting here. 
All contributions are welcome. My current ideas are :
* Programmers read/write the DTD. Therefore the documentation 
  should be easy to read/write for them.
* Documentation should be automatically checkable because we 
  are merely humans. The "tag" (like in javadoc tags) idea 
  works fine for that.
* Documentation should be easy to navigate. HTML presentation 
  might help.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n DTDDoc
%patch0 -p0 -b .sav0
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

cp -p %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export LANG=en_US.ISO8859-1
export M2SETTINGS=`pwd`/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
#mkdir -p $MAVEN_REPO_LOCAL/org.apache.bsf/
#ln -sf bsf-engines/target/bsf-engines-3.0.jar $MAVEN_REPO_LOCAL/org.apache.bsf/bsf-engines.jar

#mkdir -p $MAVEN_REPO_LOCAL
#ln -sf $(build-classpath retroweaver) $MAVEN_REPO_LOCAL
#ln -sf $(build-classpath retroweaver-rt) $MAVEN_REPO_LOCAL
#ln -sf $(build-classpath objectweb-asm/asm-all) $MAVEN_REPO_LOCAL
#ln -sf $(build-classpath backport-util-concurrent) $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install javadoc:javadoc

%install
%{__rm} -fr %{buildroot}
%{__install} -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-dtddoc.pom
%add_to_maven_depmap net.sf.dtddoc DTDDoc %{version} JPP %{name}
%{__install} -p -m 644 target/DTDDoc-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -s %{name}-%{version} %{name})

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc license.txt
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_3jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp6
- new jpp relase

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- first build

