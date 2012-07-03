# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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


Name:           gjt-jpl-util
Version:        0.6
Release:        alt1_6jpp6
Epoch:          0
Summary:        Miscellaneous utility classes and methods
License:        GPL
Group:          Development/Java
URL:            http://www.gjt.org/pkgdoc/org/gjt/lindfors/util/index.html
Source0:        gjt-jpl-util-source.zip
# download http://www.gjt.org/servlets/JCVSlet/zip/gjt/org/gjt/lindfors/util/util.zip
Source1:        http://repository.jboss.com/maven2/jpl-util/jpl-util/1.0/jpl-util-1.0.pom
Patch0:         gjt-jpl-util-build_xml.patch

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant
Requires(post):   jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildArch:      noarch
Source44: import.info

%description
A collection of miscellaneous classes and methods that 
generally come in handy in all sorts of situations. 

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

%prep
%setup -q -c -n %{name}-%{version}
cp -p util/build/build.xml util/build/build.xml.sav
mkdir util/classes
%patch0 -p0 -b .sav0

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f util/build/build.xml lib javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 util/build/jpl-util-0_6.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jpl-util jpl-util %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr util/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr util/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_docdir}/%{name}-%{version}/License
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_6jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_4jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_3jpp5
- fixed repocop warnings

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_3jpp1.7
- converted from JPackage by jppimport script

