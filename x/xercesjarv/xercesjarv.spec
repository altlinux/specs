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

%define srcname XercesJARV

%define	cvs_version 20030530

Summary:        JARV driver for Xerces-2
Name:           xercesjarv
Version:        0.1
Release:        alt1_0.20030530.6jpp1.7
Epoch:          0
License:        MIT-style License
URL:            http://www.kohsuke.org/jarv/xerces/
Group:          Development/Java
Source0:        %{srcname}.src.zip
Patch0:         xercesjarv-build_xml.patch
Patch1:         xercesjarv-XercesConstants.patch
Patch2:         xercesjarv-XercesVerifier.patch
Patch3:         xercesjarv-XercesVerifierFactory.patch
Patch4:         xercesjarv-LocatorAdaptor.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: isorelax
BuildRequires: xerces-j2 >= 0:2.6.0
BuildRequires: xml-commons-apis
Requires: isorelax
Requires: xerces-j2 >= 0:2.6.0
Requires: xml-commons-apis
BuildArch:      noarch

%description
This driver allows you to control the XML Schema 
validation engine of Xerces-2 through JARV, a 
vendor-neutral open-source interface for validation 
engines. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -T -c -n %{name}-%{version}
unzip -q %{SOURCE0}
find . -name "*.jar" -exec rm {} \;

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav

%build
export CLASSPATH=$(build-classpath \
isorelax \
xerces-j2 \
xml-commons-apis \
)
ant -Dbuild.sysclasspath=first

%install

# jars
install -Dpm 644 %{srcname}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*.jar
%doc {copying.txt,readme.txt}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20030530.6jpp1.7
- converted from JPackage by jppimport script

