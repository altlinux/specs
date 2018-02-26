BuildRequires: ecj3
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%global parent  plexus
%global dirhash 8b4d9ed
%global githash gef6142f

Name:       plexus-compiler
Version:    1.8.3
Release:    alt1_1jpp7
Epoch:      0
Summary:    Compiler call initiators for Plexus
License:    MIT
Group:      Development/Java
URL:        http://plexus.codehaus.org/

# wget  https://github.com/sonatype/plexus-compiler/tarball/plexus-compiler-1.8.3
Source0:    sonatype-plexus-compiler-plexus-compiler-1.8.3-0-%{githash}.tar.gz

Patch0:     0001-Remove-aspecj-support.patch

BuildArch:      noarch
BuildRequires:  maven
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  classworlds
BuildRequires:  eclipse-ecj
BuildRequires:  plexus-container-default
BuildRequires:  plexus-utils
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  junit4

Requires:       classworlds
Requires:       plexus-container-default
Requires:       plexus-utils
Requires:       junit4
Source44: import.info

%description
Plexus Compiler adds support for using various compilers from a
unified api. Support for javac is available in main package. For
additional compilers see %{name}-extras package.

%package extras
Summary:        Extra compiler support for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       eclipse-ecj
Requires:       %{name} = %{version}-%{release}

%description extras
Additional support for csharp, eclipse and jikes compilers

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n sonatype-plexus-compiler-%{dirhash}
%patch0 -p1


# don't build/install compiler-test module, it needs maven2 test harness
sed -i 's:<module>plexus-compiler-test</module>::' pom.xml

%build
mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        install javadoc:aggregate


%install
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{parent}
install -d -m 755 %{buildroot}%{_mavenpomdir}

for mod in plexus-compiler-{api,manager}; do
    jarname=${mod/plexus-}
    install -pm 644 $mod/target/${mod}-%{version}.jar \
                    %{buildroot}%{_javadir}/%{parent}/$jarname.jar

    install -pm 644 $mod/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-$jarname.pom
    %add_maven_depmap JPP.%{parent}-$jarname.pom %{parent}/$jarname.jar
done

pushd plexus-compilers
for mod in plexus-compiler-{csharp,eclipse,jikes,javac}; do
    jarname=${mod/plexus-}
    install -pm 644 $mod/target/${mod}-%{version}.jar \
                    %{buildroot}%{_javadir}/%{parent}/$jarname.jar

    install -pm 644 $mod/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-$jarname.pom
    %add_maven_depmap JPP.%{parent}-$jarname.pom %{parent}/$jarname.jar -f extras
done

install -pm 644 plexus-compiler-javac/target/plexus-compiler-javac-%{version}.jar \
                    %{buildroot}%{_javadir}/%{parent}/compiler-javac.jar

install -pm 644 plexus-compiler-javac/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-compiler-javac.pom
%add_maven_depmap JPP.%{parent}-compiler-javac.pom %{parent}/compiler-javac.jar

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-compilers.pom
%add_maven_depmap JPP.%{parent}-compilers.pom
popd

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{parent}-compiler.pom
%add_maven_depmap JPP.%{parent}-compiler.pom


# javadocs
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# compat pom
%add_to_maven_depmap plexus plexus-compiler-api %{version} JPP/plexus compiler-api


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%{_javadir}/%{parent}/compiler-api.jar
%{_javadir}/%{parent}/compiler-manager.jar
%{_javadir}/%{parent}/compiler-javac.jar
%{_mavenpomdir}/JPP.%{parent}-compilers.pom
%{_mavenpomdir}/JPP.%{parent}-compiler.pom
%{_mavenpomdir}/JPP.%{parent}-compiler-api.pom
%{_mavenpomdir}/JPP.%{parent}-compiler-manager.pom
%{_mavenpomdir}/JPP.%{parent}-compiler-javac.pom
%{_mavendepmapfragdir}/%{name}

%files extras
%{_mavendepmapfragdir}/%{name}-extras
%{_javadir}/%{parent}/compiler-csharp.jar
%{_javadir}/%{parent}/compiler-eclipse.jar
%{_javadir}/%{parent}/compiler-jikes.jar
%{_mavenpomdir}/JPP.%{parent}-compiler-jikes.pom
%{_mavenpomdir}/JPP.%{parent}-compiler-eclipse.pom
%{_mavenpomdir}/JPP.%{parent}-compiler-csharp.pom

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

