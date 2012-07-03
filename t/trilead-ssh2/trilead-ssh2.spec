# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

%bcond_without repolib


%if 0
%define reltag _redhat_1
%define namedreltag -redhat-1
%endif
%global namedversion build213-svnkit-1.3-patch%{?namedreltag}

Name:           trilead-ssh2
Version:        213
Release:        alt2_10_redhat_1jpp6
Epoch:          0
Summary:        SSH-2 protocol implementation in pure Java
Group:          Development/Java
License:        BSD
URL:            http://www.trilead.com/Products/Trilead-SSH-2-Java/
Source0:        %{name}-build%{version}.zip
Source1:        build.xml
Source2:        trilead-ssh2-build213.pom
Patch0:         trilead-ssh2-build213-svnkit-1.3-patch.patch
Patch1:         trilead-ssh2-build213-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  maven2-plugin-deploy
BuildArch:      noarch
Source44: import.info

%description
Ganymed SSH-2 for Java is a library which implements the SSH-2 protocol in pure
Java (tested on J2SE 1.4.2 and 5.0). It allows one to connect to SSH servers
from within Java programs. It supports SSH sessions (remote command execution
and shell access), local and remote port forwarding, local stream forwarding,
X11 forwarding and SCP. There are no dependencies on any JCE provider, as all
crypto functionality is included.

NB: This version contains the svnkit-1.3 patch for Trilead SSH.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

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
%setup -q -n %{name}-build%{version}
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__cp} -p %{SOURCE1} build.xml
%{__cp} -p %{SOURCE2} trilead-ssh2-build%{version}.pom
%patch0 -p1 -b .sav0
%if 0
%patch1 -p1 -b .sav1
%endif

# fix file-not-utf8 warnings
%{_bindir}/iconv -f iso88591 -t utf8 HISTORY.txt > HISTORY.txt.new
%{__mv} HISTORY.txt.new HISTORY.txt

# fix wrong-file-end-of-line-encoding warnings
%{__sed} -i 's/\r$//g;' LICENSE.txt README.txt HISTORY.txt faq/FAQ.html
%{_bindir}/find examples -name \*.java | %{_bindir}/xargs -t %{__sed} -i 's/\r$//g'

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%if %with repolib
# repolib
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export URL=file://`pwd`/maven2-brew
export MAVEN_OPTS=""
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=trilead-ssh2-build%{version}.pom -Dfile=dist/lib/trilead-ssh2.jar -DrepositoryId=jboss-releases-repository -Durl=${URL}
%endif

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/lib/trilead-ssh2.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
%{__ln_s} %{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
%{__mkdir_p} %{buildroot}%{_mavenpomdir}
%{__cp} -p trilead-ssh2-build%{version}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.trilead trilead-ssh2 %{namedversion} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
%{__ln_s} %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
# repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com
%{__cp} -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%doc LICENSE.txt HISTORY.txt README.txt faq examples
%{_javadir}*/%{name}-%{namedversion}.jar
%{_javadir}*/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_10_redhat_1jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:213-alt2_5jpp6
- added pom

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 213-alt1_6jpp6
- new version

