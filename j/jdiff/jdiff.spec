BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%bcond_with repolib


Name:           jdiff
Version:        1.1.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        HTML Report of API Differences
License:        LGPLv2+
URL:            http://javadiff.sourceforge.net/
Group:          Development/Java
# cvs -z3 -d:pserver:anonymous@javadiff.cvs.sourceforge.net:/cvsroot/javadiff export -D 20100703 -d jdiff-1.1.1 jdiff && tar cjf jdiff-1.1.1.tar.bz2 jdiff-1.1.1
Source0:        jdiff-1.1.1.tar.bz2
Source1:        jdiff-1.1.1.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  maven2-plugin-deploy
BuildRequires:  xerces-j2
BuildArch:      noarch
Source44: import.info

%description
JDiff is a Javadoc doclet which generates an HTML 
report of all the packages, classes, constructors, 
methods, and fields which have been removed, added 
or changed in any way, including their documentation, 
when two APIs are compared. This is very useful for 
describing exactly what has changed between two 
releases of a product. Only the API (Application 
Programming Interface) of each version is compared. 
It does not compare what the source code does when 
executed. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Docs and examples for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__ln_s} `%{_bindir}/build-classpath xerces-j2` lib/xerces.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first
%{javadoc} -classpath lib/jdiff.jar:${JAVA_HOME}/lib/tools.jar -d apidocs -sourcepath src -subpackages jdiff

%install

#install
#%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
#-DpomFile=%{SOURCE1} -Dfile=build/lib/jdiff.jar


# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/lib/jdiff.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p build/lib/antjdiff.jar %{buildroot}%{_javadir}/ant%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jdiff jdiff %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual and examples
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%if 0
%{__cp} -p build/%{name}-%{version}/*.txt %{buildroot}%{_docdir}/%{name}-%{version}
%endif
%{__cp} -p build/%{name}-%{version}/*.xml %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -p build/%{name}-%{version}/*.html %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -p build/%{name}-%{version}/*.gif %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -p build/%{name}-%{version}/*.java %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr examples %{buildroot}%{_docdir}/%{name}-%{version}

%if %without repolib
%{__rm} -r %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%doc *.txt
%{_javadir}*/ant%{name}-%{version}.jar
%{_javadir}*/ant%{name}.jar
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_1jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_1jpp6
- new jpp relase

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt1_2jpp1.7
- converted from JPackage by jppimport script

