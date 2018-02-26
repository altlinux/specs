Packager: Igor Vlasenko <viy@altlinux.ru>
%def_without javadoc
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%define rname xdoclet

Name:           xdoclet-jboss4
Version:        1.2.2
Release:        alt2_3jpp5
Epoch:          0
Summary:        XDoclet Attribute Orientated Programming Framework
License:        XDoclet Open Source Licence
Group:          Development/Java
URL:            http://xdoclet.sourceforge.net
Source0:        %{rname}-src-%{version}.tgz
Patch0:         %{name}-build_xml.patch
Patch1:         %{name}-XDocletModulesEjbMessages.patch
Patch2:         %{name}-ant.not-required.patch
Patch3:         %{name}-WebLogicSubTask.patch
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: junit
BuildRequires: javacc
BuildRequires: jrefactory
BuildRequires: bsf
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: log4j
BuildRequires: mockobjects
BuildRequires: struts
BuildRequires: velocity
BuildRequires: xalan-j2
BuildRequires: xml-commons-apis
BuildRequires: xjavadoc = 0:1.1
#
Requires: bsf
Requires: jakarta-commons-collections
Requires: jakarta-commons-logging
Requires: log4j
Requires: mockobjects
Requires: velocity
Requires: xalan-j2
Requires: xml-commons-apis
Requires: xjavadoc = 0:1.1

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
This package contains the XDoclet Attribute Orientated Programming Framework
in a version suitable for JBoss-4.0.X

%if_with javadoc
%package javadoc
Summary:        XDoclet Javadoc
Group:          Development/Documentation
%endif #javadoc

%if_with javadoc
%description javadoc
This package contains XDoclet javadoc
%endif #javadoc

%package manual
Summary:        XDoclet Sample Manuals and Documentation
Group:          Development/Documentation

%description manual
This package contains XDoclet documentation.

%prep
%setup -q -n %{rname}-%{version}
find . -name "*.jar" -exec rm {} \;
#for j in $(find . -name "*.jar"); do
#    mv $j $j.no
#done

for j in xjavadoc-1.1 jrefactory javacc junit bsf commons-collections commons-logging log4j velocity xalan-j2 xjavadoc xml-commons-apis mockobjects-core; do
        ln -s $(build-classpath $j) lib/$j.jar
done

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav

sed -i -e 's,http://xdoclet.sourceforge.net/dtds/xtags_1_1.dtd,'`pwd`/'xdocs/dtds/xtags_1_1.dtd,' `grep -rl 'http://xdoclet.sourceforge.net/dtds/xtags_1_1.dtd' .`

%build
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 core modules docs l10n

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 target/lib/%{rname}*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
#install -m 644 target/lib/maven-%{rname}*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr 'target/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/docs/api

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%if_with javadoc
%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}
%endif #javadoc

%if_with javadoc
%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi
%endif #javadoc

%files
%defattr(-, root, root, -)
%{_javadir}/%{name}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{rname}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{rname}-*-module-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if_with javadoc
%files javadoc
%defattr(-, root, root, -)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif #javadoc

%files manual
%defattr(-, root, root, -)
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_3jpp5
- fixed build

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp5
- fixed build

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

