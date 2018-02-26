BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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


Name:           jisp2
Version:        2.5.1
Release:        alt2_6jpp6
Epoch:          0
Summary:        The Java Indexed Serialization Package
License:        Open Source, libpng-style
URL:            http://www.coyotegulch.com/jisp/
Group:          Development/Java
Source0:        jisp-2.5.1-source.tar.gz
Patch0:         jisp2-2.5.1-java5-enum.patch
Requires(post): alternatives
Requires(preun): alternatives
# jisp-3.0.0 won't work with jakarta-turbine-jcs
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  make
Requires:       jpackage-utils >= 0:1.7.5
Provides:       hibernate_in_process_cache
BuildArch:      noarch
Source44: import.info

%description
Jisp uses B-Tree and hash indexes for keyed access to variable-length 
serialized objects stored in files. 

%package demo
Summary:        Demo for %{name}
Group:          Development/Documentation

%description demo
Demo for %{name}

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n jisp-%{version}
%patch0 -p1
%{__perl} -pi -e 's/\r$//g' svfl.txt

%build
export CLASSPATH=
%{__make}
%{__make} jars
%{__make} docs

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p jisp.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
cp jisp-demo.jar $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
cp *.java $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp *.txt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# hibernate_in_process_cache ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/hibernate_in_process_cache.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/hibernate_in_process_cache_jisp2<<EOF
%{_javadir}/hibernate_in_process_cache.jar	%{_javadir}/%{name}.jar	30
EOF

%files
%_altdir/hibernate_in_process_cache_jisp2
%doc svfl.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%exclude %{_javadir}/hibernate_in_process_cache.jar

%files demo
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_6jpp6
- new jpp relase

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_5jpp5
- jpackage 5 build

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_4jpp1.7
- force build with java4

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

