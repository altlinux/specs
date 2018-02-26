# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define oldname smc
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

%define gcj_support 0


Name:           jsmc
Version:        5.0.2
Release:	alt2_3jpp6
Epoch:          0
Summary:        State Machine Compiler
License:        Mozilla Public License 1.1
Group:          Development/Java
URL:            http://smc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/smc/SmcSrc_5_0_2.tgz
Source1:        %{oldname}-%{version}.pom

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  make

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Your application lives in a world of asynchronous, unordered
events: mouse clicks, timeouts, messages, and OS signals. 
And you're ready for them. You've carefully designed your 
objects. You're using robust patterns that facilitate reuse 
and anticipates future product direction. Your dynamic models 
allow your objects to recover from all but the most 
catestrophic events. Your application is ready for 
anything.
But there's a hitch. Your detailed state diagrams are only 
pictures. How are you going to translate your drawings into 
code? A transition matrix is cryptic while switch statements 
means your state machine logic is scattered all over your code. 
The state pattern looks like a great solution but that means 
writing and maintaining a class for each state - too much 
work.
Enter SMC - The State Machine Compiler. Now you put your state
diagram in one file using an easy-to-understand language. SMC
generates the state pattern classes for you. No more 
hand-maintained transition matrices. No more widely scattered 
switch statements. Instead, the state diagram is in one place, 
coded directly from the picture to the SMC language and is 
easily maintained.
SMC uses the state pattern to its fullest extent. In the real 
world, events don't always happen when they should. Dealing 
with unexpected events is a must for a robust application. By 
combining virtual methods with the state pattern, SMC allows 
you to define "Default" transitions - transitions which allow 
your objects to handle unexpected events, recover and continue 
providing service (rather than crashing, burning and getting 
you into trouble).
SMC is a Java application. That means SMC will work on any 
platform where Java 1.5.0 or better is supported. 

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{oldname}

%build
export LANG=en_US.ISO8859-1
pushd lib/Java
make all
popd
pushd net/sf/smc
make Smc.jar
popd
javadoc -d apidocs -sourcepath . net.sf.smc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 net/sf/smc/Smc.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{oldname}-%{version}.jar
%add_to_maven_depmap net.sf.smc %{oldname} %{version} JPP %{oldname}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{oldname}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
ln -sf %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname} # ghost

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{oldname}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{oldname}-%{version}
%doc %{_javadocdir}/%{oldname}

%files manual
%doc %{_docdir}/%{oldname}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.2-alt2_3jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.2-alt1_3jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.2-alt1_2jpp5
- rebuild with default profile

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0.2-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Jun 04 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1
- Initial for ALT

* Tue Jan 08 2008 Ian Chapman <packages[AT]amiga-hardware.com> 1.4.1-1
- Upgrade to 1.4.1

* Sat Dec 02 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.3-1
- Upgrade to 1.3
- Minor update to .desktop file due to new validation rules

* Sat Oct 20 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.2-1
- Upgrade to 1.2

* Fri Sep 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.1-1
- Upgrade to 1.1
- SPEC cleanups as latest version allows us to streamline the install a bit

* Wed Aug 08 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-1
- Upgrade to 1.0
- Changed license field to match new guidelines

* Sat Jun 23 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.7-1
- Upgrade to 0.99.7

* Sat Jun 02 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.6.1-1
- Upgrade to 0.99.6.1
- Dropped all patches as they are no longer needed.
- Changed .desktop category to Action Games
- Changed .desktop icon as it's now supplied with one.

* Tue Oct 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.2-1
- Upgrade to 0.99.2
- Dropped fonts patch in favour of using sed
- Updated fiximageset patch
- Added patch to fix the globals header

* Mon Oct 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.1-2
- Rebuild against latest libraries, seems to fix segfault on some machines

* Thu Sep 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99.1-1
- Upgrade to 0.99.1
- Dropped smc-0.99-fixuint.patch, fixed upstream

* Wed Aug 02 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.99-1
- Upgraded to 0.99
- Fixpaths patch reduced, fewer files need to be fixed
- Added patch to fix location of headers
- Added patch to convert uint to CEGUI::uint to avoid conflict
- Split imageset and fonts into separate patches for easier maintenance

* Sun Jul 16 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-3
- Added libpng-devel buildrequire for building under mock for fc5

* Sat Jul 08 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-2
- Corrected EOL chars in additional-licenses.txt
- Removed redundant params from %%setup
- Added automake buildrequire
- Removed pkgconfig buildrequire (required by cegui-devel)
- Moved icon installation to make it freedesktop compliant
- Added %%post and %%postun sections to update icon cache at installation
- Minor cleanups to smc.sh wrapper script
- Moved smc binary installation from /usr/games to %_bindir/smc.bin
- Enhanced the description

* Sat Jun 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.98.1-1
- Initial Release
