BuildRequires: /proc
BuildRequires: jpackage-compat
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

%global arch_name %{_target_os}_%{_target_cpu}


Name:           jansi-native
Version:        1.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        jansi-native
License:        ASL 2.0
URL:            http://jansi-native.fusesource.org
Group:          Development/Java
# git clone git://forge.fusesource.com/jansinative.git && cd jansinative && git checkout jansi-native-1.1 && rm -rf .git && cd .. && mv jansinative jansi-native-1.1
# tar cjf jansi-native-1.1.tar.bz2 jansi-native-1.1
Source0:        jansi-native-1.1.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         jansi-native-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires: %{name}-native = %{epoch}:%{version}-%{release}
BuildRequires: apache-commons-parent
BuildRequires: maven-surefire-provider-junit4
BuildRequires: hawtjni
Source44: import.info

%description
Jansi is a java library for generating and interpreting ANSI escape sequences.

%if 0
%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.
%endif

%package %{arch_name}
Summary:        Native jar for %{name}
Group:          Development/Documentation
Provides:       %{name}-native = %{epoch}:%{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description %{arch_name}
%{summary}.

%if 0
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

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
%patch0 -p0

%build
export CLASSPATH=
export MAVEN_OPTS="-Xbootclasspath/p:$(build-classpath objectweb-asm)"
%{_bindir}/mvn-jpp \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$(pwd)/maven2-brew \
        -Dmaven.test.skip=true \
	-Daggregate=true \
        install \
        javadoc:javadoc \
%if 0
        javadoc:aggregate \
        site
%endif

%install

mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/maven2/poms

cp -p maven2-brew/org/fusesource/jansi/jansi-native/%{version}/jansi-native-%{version}-linux*.jar %{buildroot}%{_javadir}/
cp maven2-brew/org/fusesource/jansi/jansi-native/%{version}/jansi-native-%{version}-native-src.zip %{buildroot}%{_javadir}/
cp maven2-brew/org/fusesource/jansi/jansi-native/%{version}/jansi-native-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp maven2-brew/org/fusesource/jansi/jansi-native/%{version}/jansi-native-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.fusesource.jansi jansi-native %{version} JPP %{name}

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

%if 0
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

%if 0
# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%doc license.txt
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_javadir}*/jansi-native-%{version}-native-src.zip
%{_javadir}*/jansi-native-native-src.zip
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files %{arch_name}
%{_javadir}*/jansi-native-%{version}-linux*.jar
%{_javadir}*/jansi-native-linux*.jar

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%if 0
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp6
- fixed build

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

