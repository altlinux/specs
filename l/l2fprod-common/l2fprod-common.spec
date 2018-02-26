Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define reldate 20090428
%define cvstag %{reldate}cvs

Name:           l2fprod-common
Version:        7.3
Release:        alt1_0.20090428cvs.7jpp6
Summary:        In JavaSE missing Swing components, inspired from modern user interfaces
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.l2fprod.com/common/
# cvs -d:pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d:pserver:guest@cvs.dev.java.net:/cvs co l2fprod-common
# tar -cjf l2fprod-common-%{version}-%{cvstag}.tar.bz2 l2fprod-common
Source0:        %{name}-%{version}-%{cvstag}.tar.bz2
BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: jcalendar
BuildRequires: nachocalendar
Requires: jpackage-utils >= 0:5.0.0

%description
Swing has lot of components built-in but still some are missing. This
provides the developer community with these missing components,
components inspired from modern user interfaces.


%package javadoc
Summary:           Javadocs for l2fprod-common
Group:             Development/Java
Requires: %name = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
l2fprod-common development documentation.


%prep
%setup -q -n %{name}

# Clean up the CVS directories contained in the cvs-snapshot tarball
find . -type d -name CVS | xargs rm -rf

# Change the line endings but preserve the timestamp
%{__sed} -i.tmp 's/\r//' LICENSE.txt
touch -r LICENSE.txt.tmp LICENSE.txt

# We can't build this module without the spring framework.
# The spring framework is not yet in the Fedora repos.
rm -rf docs lib src/java/springrcp

# The only file with another license. We don't need/use it, therefore we delete it to keep this ASL 2.0 only.
rm -f src/tests/com/l2fprod/common/demo/MainUnitTest.java


%build
mkdir target

cp -a src/java target
find target -name '*.java' -exec rm -f {} \;

find src/java -name '*.java' -print0 | xargs -0 javac -d target -cp `build-classpath nachocalendar jcalendar`
jar -cf %{name}-%{version}.jar -C target .

find src/java -name '*.java' -print0 | xargs -0 javadoc -d doc -classpath `build-classpath nachocalendar jcalendar`


%install

# jar
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-all-%{version}.jar
ln -s %{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-all.jar
for dir in src/java/*/; do
 subname=$(basename $dir)
 for exception in demo springrcp; do
  if [ $subname = $exception ] ; then continue 2 ; fi
 done
 ln -sf %{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${subname}.jar
 ln -sf %{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${subname}-%{version}.jar
done

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rp doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-*.jar

%files javadoc
%{_javadocdir}/%{name}*


%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 7.3-alt1_0.20090428cvs.7jpp6
- new version

