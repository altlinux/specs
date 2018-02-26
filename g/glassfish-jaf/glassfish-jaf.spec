Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/sun-jaf/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define jafver  1.1
%define jar_name activation

Name:           glassfish-jaf
Version:        1.1.0
Release:        alt3_6jpp6
Epoch:          0
Summary:        Glassfish - JavaBeans Activation Framework
License:        CDDL
Group:          Development/Java
URL:            http://glassfish.dev.java.net/
Source0:        %{name}-%{version}.tar.gz
#cvs -d :pserver:guest@cvs.dev.java.net:/cvs checkout glassfish/activation
Source1:        %{name}-%{version}-LICENCE.tar.gz
#cvs -d :pserver:guest@cvs.dev.java.net:/cvs checkout glassfish/bootstrap ... this tar is a tar of the legal folder under glassfish/bootstrap
Source2:        activation-1.1.pom
Source3:        %{name}-component-info.xml
Patch0:                %{name}-%{version}-ant-hack.patch
BuildRequires: ant >= 0:1.6.5
BuildRequires: jpackage-utils >= 0:1.7.3
Provides:       jaf = 0:%{jafver}
Provides:       jaf_api = 0:%{jafver}
Provides:       jaf_1_1_api
Provides:        activation
BuildArch:      noarch
Source44: import.info

%description
JavaBeans Activation Framework. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jaf-javadoc = 0:%{jafver}
BuildArch: noarch

%description javadoc
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
%setup -q -n %{name}
%setup -q -n %{name} -T -D -a 1
%patch0 -p1

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 release

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 build/release/%{jar_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.activation activation %{version} JPP %{name}

pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar %{name}.jar
popd

#(cd $RPM_BUILD_ROOT%{_javadir}
#ln -s %{name}-%{version}.jar jaf-%{jafver}.jar
#ln -s %{name}-%{version}.jar jaf_api.jar
#ln -s %{name}-%{version}.jar jaf_1_1_api.jar
#ln -s %{name}-%{version}.jar jaf.jar
#)

# Do not ghost (which would be the right thing) because of a bug in the
# classpathx-jaf package and some RPM bug with ghosts (already fixed in RHEL-5)
#touch $RPM_BUILD_ROOT%{_javadir}/activation.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaf.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaf_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaf_1_1_api.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/%{jar_name}.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_%{name}<<EOF
%{_javadir}/jaf.jar	%{_javadir}/%{name}.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/activation_%{name}<<EOF
%{_javadir}/activation.jar	%{_javadir}/%{name}.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_api_%{name}<<EOF
%{_javadir}/jaf_api.jar	%{_javadir}/%{name}.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_1_1_api_%{name}<<EOF
%{_javadir}/jaf_1_1_api.jar	%{_javadir}/%{name}.jar	10100
EOF

%if %with repolib
%define compatrepodir %{_javadir}/repository.jboss.com/glassfish/jaf/%{version}-brew
install -d -m 755 $RPM_BUILD_ROOT%{compatrepodir}/
ln -s $(relative %{repodir}/lib %{compatrepodir}/lib) $RPM_BUILD_ROOT%{compatrepodir}/lib
ln -s $(relative %{repodir}/src %{compatrepodir}/src) $RPM_BUILD_ROOT%{compatrepodir}/src
cp -a $RPM_BUILD_ROOT%{repodir}/component-info.xml $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
sed -i s,sun-jaf,glassfish/jaf, $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
%endif

%files
%_altdir/jaf_1_1_api_%{name}
%_altdir/jaf_api_%{name}
%_altdir/activation_%{name}
%_altdir/jaf_%{name}
%doc build/META-INF/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
#%{_javadir}/jaf-%{jafver}.jar
%exclude %{_javadir}/jaf.jar
# Do not ghost (which would be the right thing) because of a bug in the
# classpathx-jaf package and some RPM bug with ghosts (already fixed in RHEL-5)
#%ghost %{_javadir}/activation.jar
%exclude %{_javadir}/jaf_api.jar
%exclude %{_javadir}/jaf_1_1_api.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt3_6jpp6
- jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_6jpp6
- new jpackage release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_5jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_5jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- converted from JPackage by jppimport script

