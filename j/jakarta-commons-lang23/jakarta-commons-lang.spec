%define oldname jakarta-commons-lang
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: sf-cobertura-maven-plugin
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven 0

%define base_name       lang
%define short_name      commons-%{base_name}

Name:           jakarta-commons-lang23
Version:        2.3
Release:        alt3_2.3jpp5
Epoch:          0
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/lang/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{short_name}-%{version}-jpp-depmap.xml
Source5:        %{short_name}-%{version}.pom
Patch0:         %{oldname}-notarget.patch
Patch1:         %{oldname}-addosgimanifest.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: %{__perl}
%if %{with_maven}
BuildRequires: maven-plugins >= 0:1.1
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: maven-plugin-changelog
BuildRequires: maven-plugin-changes
BuildRequires: maven-plugin-xdoc
%endif
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc

%description    javadoc
Javadoc for %{name}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%{__perl} -pi -e 's/\r//g' *.txt
%{__sed} -i 's/\r//' STATUS.html

if [ ! -f %{SOURCE4} ]; then
export DEPCAT=$(pwd)/%{short_name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > %{short_name}-%{version}-depmap.new.xml
fi
%patch0
%patch1

%build
%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done


mkdir -p .maven/repository/JPP/plugins/
ln -s \
/usr/share/java/maven-plugins/maven-cobertura-plugin.jar \
.maven/repository/JPP/plugins/
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.javadoc.source=1.4 \
    -Dmaven.repo.remote=file:/usr/share/maven1/repository \
    -Dmaven.home.local=$(pwd)/.maven \
    jar javadoc xdoc:transform
%else

# FIXME: There are failures with gcj. Ignore them for now.
%if %{gcj_support}
  %ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Djunit.jar=$(find-jar junit) \
    -Dfinal.name=%{short_name} \
    -Djdk.javadoc=%{_javadocdir}/java \
    -Dtest.failonerror=false \
    jar javadoc
%else
  %ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Djunit.jar=$(find-jar junit) \
    -Dfinal.name=%{short_name} \
    -Djdk.javadoc=%{_javadocdir}/java \
    jar javadoc
%endif
#    test dist
%endif

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
%if %{with_maven}
cp -p target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap %{base_name} %{base_name} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

## manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p STATUS.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/docs/apidocs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/STATUS.html
%doc %{_docdir}/%{name}-%{version}/*.txt
#%doc PROPOSAL.html STATUS.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_2.3jpp5
- fixed build with moved maven1

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_2.3jpp5
- compat build

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2.3jpp5
- updated OSGi manifest from 2.3-2.3.fc10

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp1.7
- built with maven; new version

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_6jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 14 2005 Vladimir Lettiev <crux@altlinux.ru> 2.1-alt1
- 2.1

* Wed Mar 30 2005 Vladimir Lettiev <crux@altlinux.ru> 2.1-alt0.1
- Initial build for ALT Linux Sisyphus

