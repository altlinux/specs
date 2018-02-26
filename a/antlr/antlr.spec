# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/cat /usr/bin/doxygen python-devel
# END SourceDeps(oneline)

%define gcj_support 1
BuildRequires: java-1.5.0-gcj-aot-compile

%define _with_native 1
BuildRequires: gcc-c++ java-1.5.0-gcj
%def_without jedit
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name antlr
%define version 2.7.7
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

#def_with native
%bcond_with native
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/antlr/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           antlr
Version:        2.7.7
Release:	alt9_13jpp6
Epoch:          0
Summary:        ANother Tool for Language Recognition
License:        Public Domain
URL:            http://www.antlr2.org/
Group:          Development/Java
Source0:        http://www.antlr2.org/download/antlr-2.7.7.tar.gz
Source1:        %{name}-build.xml
Source2:        %{name}-script
#http://www.antlr.org/share/1069557132934/makefile.gcj
Source3:        makefile.gcj
Source4:        antlr-component-info.xml
Source5:        http://repo2.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.pom
Patch0:         %{name}-jedit.patch
%if %with native
BuildRequires:  %{_bindir}/gcj
%else
##BuildArch: noarch
BuildRequires:  ant
BuildRequires:  java-javadoc
Requires:       jpackage-utils
Requires(post): alternatives
Requires(postun): alternatives
%endif
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info
Patch33: antlr-2.7.7-alt-gcc44.patch

%description
ANTLR, ANother Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing
C++ or Java actions [You can use PCCTS 1.xx to generate C-based
parsers].

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
BuildArch: noarch

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package tool
Group:          Development/Java
Summary:        ANother Tool for Language Recognition (java version)
Requires(post): alternatives
Requires(preun): alternatives
BuildArch: noarch
Provides: %name = %version-%release
Obsoletes: %name < %version-%release
Conflicts: %name < %version-%release

%description tool
ANTLR, ANother Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing
C++ or Java actions [You can use PCCTS 1.xx to generate C-based
parsers].  This package includes the java version of the antlr tool.

%package native
Group:          Development/Java
Summary:        ANother Tool for Language Recognition (native version)
Requires(post): alternatives
Requires(preun): alternatives

%description native
ANTLR, ANother Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing
C++ or Java actions [You can use PCCTS 1.xx to generate C-based
parsers].  This package includes the native version of the antlr tool.

%package        native-devel

# antlr.a vs antlr.so;
Conflicts: kde4sdk-libs
Group:          Development/C++
Summary:        ANother Tool for Language Recognition (native version)

%description    native-devel
ANTLR, ANother Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing
C++ or Java actions [You can use PCCTS 1.xx to generate C-based
parsers].  This package includes the headers and static library for
native version of the antlr tool.

%if %{gcj_support}
%package -n gcj-%{name}
Summary:        ANother Tool for Language Recognition (gcj library)
Group:          Development/Java

%description -n gcj-%{name}
ANTLR, ANother Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing
C++ or Java actions [You can use PCCTS 1.xx to generate C-based
parsers].

This subpackage contains a gcj-compiled library for antlr.
%endif

%package manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if_with jedit
%package jedit
Group:          Editors
Summary:        ANTLR mode for jEdit
Requires:       jedit >= 0:4.1
%endif #jedit

%if_with jedit
%description jedit
ANTLR mode for jEdit. To enable this mode, insert the following into your
%{_datadir}/jedit/modes/catalog:

  <MODE NAME="antlr" FILE="antlr.xml" FILE_NAME_GLOB="*.g"/>
%endif #jedit

%prep
%setup -q
find . -name "*.jar" | xargs -t rm
%patch0 -p0 -b .sav0
cp -p %{SOURCE1} build.xml
# fixup paths to manual
%{__perl} -pi -e 's|"doc/|"%{_docdir}/%{name}-%{version}/|g' \
  install.html
%{__perl} -pi -e 's/\r$//' LICENSE.txt
%patch33 -p1

%build
%if %with native
%{__make} -f %{SOURCE3} COMPOPTS="%{optflags}"
%endif
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dj2se.apidoc=%{_javadocdir}/java -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5

%configure \
  --enable-verbose \
  --with-javacflags="+ -source 1.5 -target 1.5" \
  --disable-java \
  --enable-cxx \
  --disable-python \
  --disable-csharp \


make

%install

install -dm 755 %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/antlr # for %%ghost

%if %with native
install -pm 755 cantlr %{buildroot}%{_bindir}/antlr-native
%endif
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p work/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap antlr antlr %{version} JPP %{name}

# script
cp -p %{SOURCE2} %{buildroot}%{_bindir}/antlr-java

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr work/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# jedit mode
mkdir -p %{buildroot}%{_datadir}/jedit/modes
cp -p extras/antlr-jedit.xml %{buildroot}%{_datadir}/jedit/modes/antlr.xml

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}/

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE4} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/antlr.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/antlr.pom
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%{name}_antlr<<EOF
%{_bindir}/antlr	%{_bindir}/antlr-java	10
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/%{name}_antlr-native<<EOF
%{_bindir}/antlr	%{_bindir}/antlr-native	20
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

# C++ lib and headers, antlr-config
%define headers %{_includedir}/%{name}

mkdir -p $RPM_BUILD_ROOT{%{headers},%{_libdir}}
install -m 644 lib/cpp/antlr/*.hpp $RPM_BUILD_ROOT%{headers}
install -m 644 lib/cpp/src/libantlr.a $RPM_BUILD_ROOT%{_libdir}
install -m 755 scripts/antlr-config $RPM_BUILD_ROOT%{_bindir}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with native
%files native
%_altdir/%{name}_antlr-native
%doc INSTALL.txt LICENSE.txt
#%defattr(0755,root,root,0755)
#%ghost %{_bindir}/antlr
%{_bindir}/antlr-native
%endif
%files tool
%_altdir/%{name}_antlr
%doc INSTALL.txt LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%attr(0755,root,root) %ghost %{_bindir}/antlr
%attr(0755,root,root) %{_bindir}/antlr-java

%files manual
%doc %{_docdir}/%{name}-%{version}/

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if_with jedit
%files jedit
%{_datadir}/jedit/modes/*
%else
%exclude %{_datadir}/jedit/modes/*
%endif #jedit

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%files native-devel
%{headers}/*.hpp
%{_libdir}/libantlr.a
%attr(0755,root,root) %{_bindir}/antlr-config

%if %{gcj_support}
%files -n gcj-%name
%{_libdir}/gcj/%{name}
%endif


%changelog
* Wed Jun 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt9_13jpp6
- added gcj and tool subpackage

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt8_13jpp6
- build with source and target 1.5

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt7_13jpp7
- restored antlr-native

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt7_13jpp6
- new jpp relase

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt7_1jpp5
- fixed misprint in repolib

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt6_1jpp5
- fixed build with gcc44

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt5_1jpp5
- added repolib

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt4_1jpp5
- fixed build with gcc43

* Mon Apr 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt4_1jpp1.7
- added conflict for .so

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt3_1jpp1.7
- fixed script permissions

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt2_1jpp1.7
- converted from JPackage by jppimport script

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.7-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.6-alt1
- 2.7.6
- Added README.txt to the docs list
- Set source and target compiler attributes

* Tue Feb 01 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.5-alt1
- New upstream release
- Converted to rpm-build-java macros

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.4-alt1
- New upstream release

* Sat Apr 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.3-alt1
- New upstream release

* Wed Sep 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.2-alt1
- Ported to ALT Linux from JPackage 2.7.2-2jpp
