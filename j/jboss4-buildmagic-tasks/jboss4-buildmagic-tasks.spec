BuildRequires: /proc
BuildRequires: jpackage-1.4-compat
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


Summary:        JBoss buildmagic tasks module
Name:           jboss4-buildmagic-tasks
Version:        2.0
Release:        alt1_4jpp1.7
Epoch:          0
License:        LGPL
URL:            http://www.jboss.org/
Group:          Development/Java
Source0:        jboss-buildmagic-2.0.tar.gz
Source1:        jboss-common-4.0.0.DR4.tar.gz
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/jboss login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/jboss export -r buildmagic-2_0 buildmagic
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/jboss export -r Rel_4_0_0_DR4 jboss-common
Patch0:         jboss4-buildmagic-tasks-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: bsf
BuildRequires: log4j
Requires: bsf
Requires: log4j
BuildArch:      noarch

%description
Buildmagic tasks module of JBoss

%prep
%setup -q -n buildmagic
gzip -dc %{SOURCE1} | tar -xf -
find . -name "*.jar" -exec rm {} \;
#cp tasks/build.xml tasks/build.xml.sav
for f in `find tasks/src -name "*.java"`; do
    sed -e 's|com\.ibm\.bsf|org\.apache\.bsf|' $f > temp.java
    cp temp.java $f
done
rm temp.java
mkdir -p tasks/src/main/org/jboss/util/file
mkdir -p tasks/src/main/org/jboss/util/platform
mkdir -p tasks/src/main/org/jboss/util/stream
mkdir -p tasks/src/main/org/jboss/logging
cp jboss-common/src/main/org/jboss/util/DirectoryBuilder.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/Strings.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/NestedError.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/NestedThrowable.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/ThrowableHandler.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/ThrowableListener.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/NullArgumentException.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/EmptyStringException.java tasks/src/main/org/jboss/util
cp jboss-common/src/main/org/jboss/util/file/Files.java tasks/src/main/org/jboss/util/file
cp jboss-common/src/main/org/jboss/util/platform/Java.java tasks/src/main/org/jboss/util/platform
cp jboss-common/src/main/org/jboss/util/stream/Streams.java tasks/src/main/org/jboss/util/stream
cp jboss-common/src/main/org/jboss/logging/Logger.java tasks/src/main/org/jboss/logging
cp jboss-common/src/main/org/jboss/logging/LoggerPlugin.java tasks/src/main/org/jboss/logging
cp jboss-common/src/main/org/jboss/logging/NullLoggerPlugin.java tasks/src/main/org/jboss/logging

%patch0 -b .sav

%build
export CLASSPATH=$(build-classpath \
bsf \
log4j)
cd tasks
ant \
        -Djavac.optimize=off \
        -Djavac.target=1.4 \
        -Djavac.debug=off \
        -Djavac.depend=no \
        -Djavac.verbose=no \
        -Djavac.deprecation=on \
        -Djavac.include.ant.runtime=yes \
        -Djavac.include.java.runtime=no \
        -Djavac.fail.onerror=true \
	-Djavac.includes=**/*.java \
	-Dsource.java=src \
	-Dsource.etc=src/etc \
	-Dsource.resources=src/resources \
	-Dbuild.classes=output/classes \
	-Dbuild.gen.classes=output/gen/classes \
	-Dbuild.etc=output/etc \
	-Dbuild.resources=output/resources \
	-Dbuild.lib=output/lib \
	-Dinit.disable=true \
	-Ddependency-manager.offline=true \
	-Dbuild.sysclasspath=only \
	output

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/jboss4
cp -p tasks/output/lib/buildmagic-tasks.jar \
  $RPM_BUILD_ROOT%{_javadir}/jboss4/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/jboss4 && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)


%files
#%doc LICENSE.txt
%{_javadir}/jboss4/*.jar

%changelog
* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_4jpp1.7
- converted from JPackage by jppimport script

