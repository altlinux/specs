Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm) rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2005, JPackage Project
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

Summary:        High-performance, full-featured text search engine
Name:           lucene4
Version:        4.10.4
Release:        alt1_12jpp8
Epoch:          0
License:        ASL 2.0
URL:            http://lucene.apache.org/
Source0:        http://www.apache.org/dist/lucene/java/%{version}/lucene-%{version}-src.tgz
#svn export http://svn.apache.org/repos/asf/lucene/dev/tags/lucene_solr_4_10_4/dev-tools/
#tar caf dev-tools-4.10.4.tar.xz dev-tools/
Source1:        dev-tools-%{version}.tar.xz

Patch0:         0001-disable-ivy-settings.patch
Patch1:         0001-dependency-generation.patch

# Build fix for morfologik-stemming 2.x
Patch2:         lucene-4.10.4-morfologik-stemming.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1501841
Patch3:         0001-SOLR-11477-Disallow-resolving-of-external-entities-i.patch

BuildRequires:  git
BuildRequires:  subversion subversion-server-common
BuildRequires:  ant
BuildRequires:  ivy-local
BuildRequires:  apache-ivy
BuildRequires:  icu4j
BuildRequires:  httpcomponents-client
BuildRequires:  jetty-continuation
BuildRequires:  jetty-http
BuildRequires:  jetty-io
BuildRequires:  jetty-server
BuildRequires:  jetty-servlet
BuildRequires:  jetty-util
BuildRequires:  morfologik-stemming
BuildRequires:  uimaj
BuildRequires:  uima-addons
BuildRequires:  spatial4j
BuildRequires:  nekohtml
BuildRequires:  xerces-j2
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  maven-local
BuildRequires:  apache-parent
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  regexp

# test-framework deps
BuildRequires:  junit
BuildRequires:  randomizedtesting-junit4-ant
BuildRequires:  randomizedtesting-runner

Provides:       %{name}-core = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package javadoc
Group: Development/Java
Summary:        Javadoc for Lucene
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n lucene-%{version}

# dependency generator expects that the directory name is just lucene
mkdir lucene
find -maxdepth 1 \
    ! -name CHANGES.txt ! -name LICENSE.txt ! -name README.txt \
    ! -name NOTICE.txt ! -name MIGRATE.txt  ! -name ivy-settings.xml \
    ! -path ./lucene -exec mv \{} lucene/ \;

tar xf %{SOURCE1}

pushd lucene
%patch0 -p1
%patch1 -p1
%patch3 -p1

# remove all binary libs
find . -name "*.jar" -delete

rm sandbox/src/test/org/apache/lucene/sandbox/queries/regex/TestJakartaRegexpCapabilities.java

# old API
rm -r replicator/src/test/*

rm -r analysis/common/src/test/*

# Because ivy-local is not available before F21
ln -s %{_sysconfdir}/ivy/ivysettings.xml

popd

%patch2 -p1

# Ensure OSGi package imports are versioned correctly
sed -i -e '/Export-Package/a<Import-Package>org.apache.lucene*;version="[${project.version},5.0.0)",org.tartarus*;version="[${project.version},5.0.0)",*</Import-Package>' \
  dev-tools/maven/pom.xml.template

# suggest provides spellchecker
%mvn_alias :lucene-suggest :lucene-spellchecker
# compatibility with existing packages
%mvn_alias :lucene-analyzers-common :lucene-analyzers
%mvn_compat_version : 4 %{version}

%build
pushd lucene
# generate dependencies
ant filter-pom-templates -Divy.mode=local -Dversion=%{version}

# fix source dir + move to expected place
for pom in `find build/poms/lucene -name pom.xml`; do
    sed 's/\${module-path}/${basedir}/g' "$pom" > "${pom##build/poms/lucene/}"
done

%pom_disable_module src/test core
%pom_disable_module src/test codecs

# test deps
%pom_add_dep org.ow2.asm:asm::test demo
%pom_add_dep org.ow2.asm:asm-commons::test demo
%pom_add_dep org.antlr:antlr-runtime::test demo

popd

mv lucene/build/poms/pom.xml .

%pom_disable_module solr
%pom_remove_plugin :gmaven-plugin
%pom_remove_plugin -r :forbiddenapis
# Duplicate pom entries is not allowed in maven 3.4+
%pom_remove_dep org.eclipse.jetty.orbit:javax.servlet
%pom_change_dep org.eclipse.jetty.orbit:javax.servlet javax.servlet:javax.servlet-api:3.1.0 lucene/replicator
%pom_change_dep -r :servlet-api javax.servlet:javax.servlet-api:3.1.0
# Prevent build failure
%pom_remove_plugin -r :maven-enforcer-plugin

# For some reason TestHtmlParser.testTurkish fails when building inside SCLs
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.txt MIGRATE.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.10.4-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.10.4-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.10.4-alt1_8jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.10.4-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.10.4-alt1_3jpp8
- new version

