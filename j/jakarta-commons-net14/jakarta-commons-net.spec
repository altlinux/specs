%define oldname jakarta-commons-net
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define _without_maven 1

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define gcj_support 0

%define without_tests %{?_without_tests:1}%{!?_without_tests:%{?_with_tests:0}%{!?_with_tests:%{?_tests:%{_tests}}%{!?_tests:0}}}


%define base_name       net
%define short_name      commons-%{base_name}

Name:           jakarta-commons-net14
Version:        1.4.1
Release:        alt6_4jpp5
Epoch:          0
Summary:        Jakarta Commons Net Package
License:        Apache Software License
Group:          Development/Java
Url:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/jakarta/commons/net/source/commons-net-1.4.1-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        commons-net-1.4.1-jpp-depmap.xml
Source5:        commons-build.tar.gz
Source6:        commons-net-1.4.1.pom

Patch0:         %{oldname}-crosslink.patch
Patch1:         %{short_name}-%{version}-project_xml.patch
Patch2:         %{short_name}-%{version}-project_properties.patch
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
%if ! %{without_tests}
BuildRequires: ant-junit >= 0:1.6
%endif
BuildRequires: junit >= 3.8.1
BuildRequires: java-javadoc
BuildRequires: oro >= 2.0.8
%if %{with_maven}
BuildRequires: maven-plugins >= 0:1.1
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-changes
BuildRequires: maven-plugin-checkstyle
BuildRequires: maven-plugin-jcoverage
BuildRequires: maven-plugin-jdepend
BuildRequires: maven-plugin-jxr
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-tasklist
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc

BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires: oro >= 2.0.8
#Provides:       %{short_name}
#Obsoletes:      %{short_name}
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions. 

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation

%description javadoc
Javadoc for %{oldname}.

%if %{with_maven}
%package manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}
gzip -dc %{SOURCE5} | tar xf -

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
%if %{with_maven}
export DEPCAT=$(pwd)/commons-net-1.4.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > commons-net-1.4.1-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

#        -Dmaven.test.failure.ignore=true \
maven -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate site
%else
mkdir -p target/lib
ln -s %{_javadir}/oro.jar target/lib
ln -s %{_javadir}/junit.jar target/lib

%if %{without_tests}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget=true -Dfinal.name=commons-net-%{version} -Dj2se.api=%{_javadocdir}/java jar javadoc
%else
export OPT_JAR_LIST="ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget=true -Dfinal.name=commons-net-%{version} -Dj2se.api=%{_javadocdir}/java jar test javadoc
%endif
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}14
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/docs/apidocs
# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt6_4jpp5
- fixed build with moved maven1

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt5_4jpp5
- removed commons-net provides

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt4_4jpp5
- compat version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_4jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_4jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_3jpp1.7
- rebuilt with maven1

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 07 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- New upstream release

* Thu Dec 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0-alt1
- New upstream release
- Use rpm-build-java macros
- Updated Patch0

* Sat Jun 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.2-alt1
- New upstream release

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.1-alt1
- New upstream release

* Tue May 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt1
- New upstream release

* Sun Feb 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.0-alt1
- Adapted for Sisyphus from the JPackage project
