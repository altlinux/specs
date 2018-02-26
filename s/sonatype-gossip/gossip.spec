%define oldname gossip
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

#def_with gcj_support
%bcond_with gcj_support
%bcond_with repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           sonatype-gossip
Version:        1.5
Release:        alt2_1jpp6
Epoch:          0
Summary:        Gossip
License:        ASL 2.0
URL:            http://gossip.fusesource.org
Group:          Development/Java
# git clone git://github.com/jdillon/gossip.git && cd gossip && git checkout gossip-1.5 && rm -rf .git && cd .. && mv gossip gossip-1.5 && tar cjf gossip-1.5.tar.bz2 gossip-1.5
Source0:        gossip-1.5.tar.bz2
Source1:        %{oldname}-settings.xml
Source2:        %{oldname}-jpp-depmap.xml
Patch0:         gossip-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jansi >= 0:1.4
Requires: jpackage-utils
BuildRequires: apache-commons-parent
# FIXME: this is for forge-parent
BuildRequires: plexus-build-api
BuildRequires: jansi >= 0:1.4
BuildRequires: maven-surefire-provider-junit4
BuildArch:      noarch
Source44: import.info

%description
Gossip is a plugin for SLF4j which has simple and flexible configuration.

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p0 -b .sav0

%build
export MAVEN_REPO_LOCAL=$(pwd)/maven2-brew
%{__mkdir_p} ${MAVEN_REPO_LOCAL}

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        -Dmaven.test.skip=true \
         install \
        javadoc:aggregate \
%if 0
        site
%endif

find $(pwd)/maven2-brew

%install

mkdir -p %{buildroot}%{_javadir}
cp -p maven2-brew/org/sonatype/gossip/gossip-core/%{version}/gossip-core-%{version}.jar %{buildroot}%{_javadir}/
cp -p maven2-brew/org/sonatype/gossip/gossip-slf4j/%{version}/gossip-slf4j-%{version}.jar %{buildroot}%{_javadir}/
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p maven2-brew/org/sonatype/gossip/gossip/%{version}/gossip-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-gossip.pom
cp -p maven2-brew/org/sonatype/gossip/gossip-core/%{version}/gossip-core-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-gossip-core.pom
cp -p maven2-brew/org/sonatype/gossip/gossip-slf4j/%{version}/gossip-slf4j-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-gossip-slf4j.pom

%add_to_maven_depmap org.sonatype.gossip gossip %{version} JPP gossip
%add_to_maven_depmap org.sonatype.gossip gossip-core %{version} JPP gossip-core
%add_to_maven_depmap org.sonatype.gossip gossip-slf4j %{version} JPP gossip-slf4j

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{oldname}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oldname}-%{version}
ln -s %{oldname}-%{version} %{buildroot}%{_javadocdir}/%{oldname}

%if 0
# manual
mkdir -p %{buildroot}%{_docdir}/%{oldname}-%{version}
cp -pr target/site/* %{buildroot}%{_docdir}/%{oldname}-%{version}
rm -r %{buildroot}%{_docdir}/%{oldname}-%{version}/apidocs
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%doc README.md
%{_javadir}*/gossip-core-%{version}.jar
%{_javadir}*/gossip-core.jar
%{_javadir}*/gossip-slf4j-%{version}.jar
%{_javadir}*/gossip-slf4j.jar
%{_datadir}/maven2/poms/JPP-gossip.pom
%{_datadir}/maven2/poms/JPP-gossip-core.pom
%{_datadir}/maven2/poms/JPP-gossip-slf4j.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{oldname}-%{version}
%{_javadocdir}/%{oldname}

%if 0
%files manual
%doc %{_docdir}/%{oldname}-%{version}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build with maven3

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt2.git20090422
- rebuild with libebook-1.2.so.10

* Tue May 12 2009 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1.git20090422
- 0.32 git 20090422 version
- update BuildRequires
- removed libgnomeui and libgnomevfs deps, add libcanberra-gtk

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.31-alt2
- removed obsolete %%post{,in} scripts
- updated buildreqs

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.31-alt1
- 0.31
- rebuild with libgalago-0.5.2 (soname so.3)

* Sat Jul 12 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt3
- fix desktop file

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt2
- add Packager tag

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 0.29-alt1
- 0.28 -> 0.29

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt2
- Update Url
- add %%update_menus to %%post script
- add %%clean_menus to %%postun script

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 0.28-alt1
- 0.26 -> 0.28

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt2
- fix build with new intltool

* Tue Jun 19 2007 Igor Zubkov <icesik@altlinux.org> 0.26-alt1
- 0.17 -> 0.26
- buildreq and update build requires

* Wed Dec 27 2006 Igor Zubkov <icesik@altlinux.org> 0.17-alt1.1
- rebuild with new dbus

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.17-alt1
- Updated to 0.17
- Updated versioned dependencies
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12-alt1
- Release 0.12
- Patch0 is obsolete

* Fri Jun 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.2-alt1
- Release 0.11.2

* Tue Jun 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt2
- Patch0: port to libgalago 0.5, from GNOME bug 339333
- Rebuilt with libgalago 0.5

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1-alt1
- Release 0.11.1

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11-alt1
- Release 0.11
- Enabled libnotify back
- Compressed ChangeLog

* Sun Mar 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- Release 0.10.2
- Buildreq

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- Release 0.10.1
- Disabled libnotify support until the API stabilizes

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10-alt1
- 0.10
- Buildreq
- Optional Galago support, enabled by default
- Removed Debian-style menu

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt1
- New upstream release
- Patch0 is obsolete

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt3
- Patch for new dbus from Fedora (thanks Rider) [Patch0]
- Requires dbus 0.34

* Sun Jan 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt2
- Added the common menu entry (bug #5909)

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8-alt1
- New upstream release

* Sat Dec 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt3
- Added /usr/share/gossip directory to the file list

* Mon Oct 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt2
- Stricter installtime versioned dependencies copied from the buildtime
  dependencies, which are in turn copied from configure dependencies
  (bug #5393)

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.8-alt1
- Updated to the new upstream release
- Conditionally build with dbus

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.5-alt1
- New upstream release

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.4-alt1
- New upstream release

* Sat Feb 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.2-alt1
- New upstream release
- Run automake

* Fri Jan 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.1-alt1
- New upstream release

* Sat Jan 10 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.6-alt1
- New upstream release

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.5-alt1
- New version

* Mon Jul 21 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt1
- Ported to ALT Linux
