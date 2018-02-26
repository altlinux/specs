Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Summary:        Cluster-aware Caching for Java
Name:           swarmcache
Version:        1.0
Release:        alt3_0.cvs040225.8jpp5
Epoch:          0
License:        LGPL
URL:            http://swarmcache.sourceforge.net/
Group:          Development/Java
Source0:        swarmcache-1.0-cvs040225.tar.gz
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/swarmcache login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/swarmcache export -D20040225 swarmcache
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 0:1.6.1
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: jgroups
BuildRequires: jgroups
BuildRequires: junit
Requires: alternatives >= 0:0.4
Requires: jakarta-commons-collections
Requires: jakarta-commons-logging
Requires: jgroups
Requires: jgroups
Provides:       hibernate_in_process_cache
BuildArch:      noarch

%description
SwarmCache is a simple but effective distributed 
cache. It uses IP multicast to efficiently communicate 
with any number of hosts on a LAN. It is specifically 
designed for use by clustered, database-driven web 
applications. Such applications typically have many 
more read operations than write operations, which 
allows SwarmCache to deliver the greatest performance 
gains. SwarmCache uses JavaGroups internally to manage 
the membership and communications of its distributed 
cache.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{name}
find . -name "*.jar" | xargs rm

%build
export CLASSPATH=$(build-classpath \
commons-collections \
commons-logging \
jgroups \
jgroups \
junit)
export OPT_JAR_LIST=:
ant -Dbuild.sysclasspath=only test jar javadoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}RC2.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p all.library $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p changehog.txt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr conf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p readme.html $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p swarmcache.* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -p test* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr web/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
# FIXME: (dwalluck): breaks --short-circuit
rm -rf web/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr web/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# hibernate_in_process_cache ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/hibernate_in_process_cache.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/hibernate_in_process_cache_%{name}<<EOF
%{_javadir}/hibernate_in_process_cache.jar	%{_javadir}/%{name}.jar	40
EOF

%files
%_altdir/hibernate_in_process_cache_%{name}
%{_datadir}/%{name}-%{version}
%{_javadir}/*.jar
%exclude %{_javadir}/hibernate_in_process_cache.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.cvs040225.8jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.cvs040225.8jpp5
- converted from JPackage by jppimport script

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.cvs040225.7jpp1.7
- fixed alternatives intersection

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.cvs040225.7jpp1.7
- converted from JPackage by jppimport script

