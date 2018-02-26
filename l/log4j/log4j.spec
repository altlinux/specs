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

%bcond_without repolib
#def_with bootstrap
%bcond_with bootstrap

%define repodir %{_javadir}/repository.jboss.com/apache-log4j/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           log4j
Version:        1.2.15
Release:        alt2_7jpp6
Epoch:          0
Summary:        Java logging package
License:        ASL 2.0
Group:          Development/Java
URL:            http://logging.apache.org/log4j/
Source0:        http://www.apache.org/dist/logging/log4j/1.2.15/apache-log4j-1.2.15.tar.gz
# Converted from src/java/org/apache/log4j/lf5/viewer/images/lf5_small_icon.gif
Source1:        %{name}-logfactor5.png
Source2:        %{name}-logfactor5.sh
Source3:        %{name}-logfactor5.desktop
# Converted from docs/images/logo.jpg
Source4:        %{name}-chainsaw.png
Source5:        %{name}-chainsaw.sh
Source6:        %{name}-chainsaw.desktop
Source7:        %{name}.catalog
Source8:        log4j-component-info.xml
Source9:        http://repo1.maven.org/maven2/log4j/log4j/1.2.15/log4j-1.2.15.pom
Patch0:         %{name}-logfactor5-userdir.patch
Patch1:         %{name}-javadoc-xlink.patch
Patch2:         %{name}-mx4j-tools.patch
Patch3:         %{name}-jmx-Agent.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: jpackage-utils >= 0:1.7.3
%if %without bootstrap
Requires: jaf_1_0_2_api
Requires: jaxp_parser_impl
%if 0
Requires: javamail_1_4_api
%else
# XXX: needed for correct pom
Requires: glassfish-javamail >= 0:1.4
%endif
Requires: jms_1_1_api
Requires: mx4j
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant
%if %without bootstrap
BuildRequires: jaf_1_0_2_api
BuildRequires: javamail_1_4_api
BuildRequires: jms_1_1_api
BuildRequires: mx4j
%endif
BuildRequires: java-javadoc
BuildRequires: jaxp_parser_impl
BuildRequires: jndi
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%if %{with_repolib}
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
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%{__perl} -pi -e 's/\r$//g' LICENSE NOTICE

for file in contribs/JimMoore/mail-2001-03-12T1454 contribs/JimMoore/mail-2001-03-13T0646; do
    %{__mv} ${file} ${file}.orig
    %{_bindir}/iconv -f iso-8859-1 -t utf8 -o ${file} ${file}.orig
    %{__rm} ${file}.orig
done

# remove all the stuff we'll build ourselves
find . -name "*.jar" -o -name "*.class" | xargs %{__rm}
#%__rm -r docs/api

# fix perl location
%__perl -p -i -e 's|/opt/perl5/bin/perl|%{__perl}|' \
contribs/KitchingSimon/udpserver.pl

%build
# javac.source=1.1 doesn't work with Sun's 1.4.2_09/1.5.0_05
# Provide -Djmx-present="true" option to build Patch02 to enable HtmlAdaptor
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Djavamail.jar=$(build-classpath javamail_1_4_api) \
        -Dactivation.jar=$(build-classpath jaf_1_0_2_api) \
        -Djaxp.jaxp.jar=$(build-classpath jaxp_parser_impl) \
        -Djms.jar=$(build-classpath jms_1_1_api) \
        -Djmx.jar=$(build-classpath mx4j/mx4j) \
        -Djmx-extra.jar=$(build-classpath mx4j/mx4j-tools) \
        -Djndi.jar=$(build-classpath jndi) \
        -Djavac.source=1.2 \
        -Djdk.javadoc=%{_javadocdir}/java \
        jar javadoc

%install
%__rm -rf %{buildroot}

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -a dist/lib/%{name}-%{version}.jar %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__cp -a %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})
# FIXME: (dwalluck) This breaks -bi --short-circuit
%__rm -rf docs/api
ln -s %{_javadocdir}/log4j docs/api

# scripts
%__mkdir_p %{buildroot}%{_bindir}
%__install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/logfactor5
%__install -p -m 755 %{SOURCE5} %{buildroot}%{_bindir}/chainsaw

# freedesktop.org menu entries and icons
%__mkdir_p %{buildroot}%{_datadir}/{applications,pixmaps}
%__cp -a %{SOURCE1} \
  %{buildroot}%{_datadir}/pixmaps/logfactor5.png
%__cp -a %{SOURCE3} \
  %{buildroot}%{_datadir}/applications/jpackage-logfactor5.desktop
%__cp -a %{SOURCE4} \
  %{buildroot}%{_datadir}/pixmaps/chainsaw.png
%__cp -a %{SOURCE6} \
  %{buildroot}%{_datadir}/applications/jpackage-chainsaw.desktop

# DTD and the SGML catalog (XML catalog handled in scriptlets)
%__mkdir_p %{buildroot}%{_datadir}/sgml/%{name}
%__cp -a src/main/resources/org/apache/log4j/xml/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/%{name}
%__cp -a %{SOURCE7} \
  %{buildroot}%{_datadir}/sgml/%{name}/catalog

%__mkdir_p %{buildroot}%{_sysconfdir}/sgml
/bin/touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
%__install -d -m 755 $RPM_BUILD_ROOT%{repodir}
%__install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
%__install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %__sed 's|\.|_|g'`
%__sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/1.2.14-brew/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%__sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
%__install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
%__install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
%__install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
%__install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
%__cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/log4j.jar
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/chainsaw.conf`
touch $RPM_BUILD_ROOT/etc/chainsaw.conf

%post
/bin/touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat 2>/dev/null
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null 2>&1 || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system log4j.dtd \
    file://%{_datadir}/sgml/%{name}/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del log4j.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null 2>&1 || :
  fi
fi


%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null 2>&1 || :
fi


%files
%doc LICENSE NOTICE
%attr(0755,root,root) %{_bindir}/chainsaw
%attr(0755,root,root) %{_bindir}/logfactor5
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_datadir}/applications/*chainsaw.desktop
%{_datadir}/applications/*logfactor5.desktop
%{_datadir}/pixmaps/chainsaw.png
%{_datadir}/pixmaps/logfactor5.png
%{_datadir}/sgml/%{name}
#%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.db
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.so
%endif
%config(noreplace,missingok) /etc/chainsaw.conf

%files manual
# FIXME: (dwalluck) Manuals are usually installed at an absolute location inside %%{_docdir}
%doc --no-dereference docs/* contribs

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt2_7jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt1_7jpp6
- new version

* Sun Mar 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt8_15jpp5
- fixed missing org.apache.log4j.jmx

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_15jpp5
- new version

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_4jpp5
- fixed missing org.apache.log4j.jmx

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt6_4jpp5
- removed obsolete update_menus

