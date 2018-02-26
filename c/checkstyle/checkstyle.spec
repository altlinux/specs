Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jakarta-commons-lang
BuildRequires: ant-optional
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%bcond_with tests
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           checkstyle
Version:        5.0
Release:        alt3_1jpp5
Epoch:          0
Summary:        Java source code checker
License:        LGPLv2+
Group:          Development/Java
URL:            http://checkstyle.sourceforge.net/
Source0:        http://download.sf.net/checkstyle/checkstyle-src-5.0.tar.gz
Source1:        checkstyle-5.0-script
Source2:        checkstyle-5.0.catalog
Patch0:         checkstyle-5.0-build.patch
Patch1:         checkstyle-5.0-javadoc-crosslink.patch
Patch2:         checkstyle-5.0-google-collections.patch
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
Requires: ant >= 0:1.6
Requires: antlr >= 0:2.7.1
Requires: google-collections
Requires: jakarta-commons-logging
Requires: jakarta-commons-cli
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jpackage-utils >= 0:1.7.2
Requires: jaxp_parser_impl
BuildRequires: ant >= 0:1.6
BuildRequires: ant-javadoc
BuildRequires: ant-nodeps >= 0:1.6
BuildRequires: antlr >= 0:2.7.1
BuildRequires: antlr-javadoc
BuildRequires: google-collections
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-beanutils-javadoc
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-logging
BuildRequires: java-javadoc
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: junit4
BuildRequires: velocity
BuildRequires: xalan-j2
# xerces-j2 because tests fail with gnujaxp...
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis-javadoc
%if %with tests
BuildRequires: ant-junit >= 0:1.6
BuildRequires: emma
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
A tool for checking Java source code for adherence to a set of rules.

%package demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Manual for %{name}.

%prep
%setup -q -n checkstyle-src-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%{__perl} -pi -e 's/\r$//g;' \
build.xml \
checkstyle_checks.xml \
java.header \
LICENSE.apache20 \
LICENSE \
README \
RIGHTS.antlr \
sun_checks.xml \
suppressions.xml \
src/xdocs/css/*.css \
src/xdocs/*.xml \
src/xdocs/stylesheets/*.vsl \
src/xdocs/stylesheets/*.xml

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`
export CLASSPATH=$(build-classpath commons-collections commons-lang)

pushd lib
ln -sf $(build-classpath antlr) .
ln -sf $(build-classpath commons-beanutils-core) .
ln -sf $(build-classpath commons-cli) commons-cli-1.1.jar
ln -sf $(build-classpath commons-logging) .
%if %with tests
ln -sf $(build-classpath emma) .
ln -sf $(build-classpath emma_ant) .
%endif
ln -sf $(build-classpath google-collections) google-collect-snapshot-20090211.jar
ln -sf $(build-classpath jdom) jdom-b9.jar
ln -sf $(build-classpath junit4) junit-4.4.jar
ln -sf $(build-classpath velocity) velocity-dep-1.4.jar
popd

%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=first \
  -Dant.javadoc=%{_javadocdir}/ant \
  -Dantlr.javadoc=%{_javadocdir}/antlr \
  -Djava.javadoc=%{_javadocdir}/java \
  -Djaxp.javadoc=%{_javadocdir}/xml-commons-apis \
  -Dbeanutils.javadoc=%{_javadocdir}/jakarta-commons-beanutils \
%if %with tests
  \
%endif
  build.bindist

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/dist/checkstyle-%{version}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `echo $jar| %__sed "s|-%{version}||g"`; done)

# poms
%add_to_maven_depmap checkstyle checkstyle %{version} JPP %{name}
%add_to_maven_depmap com.puppycrawl.tools checkstyle %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.pom

# script
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# dtds
%{__mkdir_p} %{buildroot}%{_datadir}/xml/%{name}
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/xml/%{name}/catalog
%{__cp} -p src/checkstyle/com/puppycrawl/tools/checkstyle/*.dtd %{buildroot}%{_datadir}/xml/%{name}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sgml
/bin/touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/dist/checkstyle-%{version}/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# docs
# FIXME: (dwalluck): breaks --short-circuit
%{__rm} -rf target/dist/%{name}-%{version}/docs/api
%{__ln_s} %{_javadocdir}/%{name} target/dist/%{name}-%{version}/docs/api

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr target/dist/%{name}-%{version}/contrib/* %{buildroot}%{_datadir}/%{name}

# ant.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ant.d
%{__cat} > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
checkstyle antlr google-collections jakarta-commons-beanutils jakarta-commons-cli jakarta-commons-logging jakarta-commons-collections jaxp_parser_impl
EOF

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post
/bin/touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat 2>/dev/null
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null 2>&1 || :
fi

%postun
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null 2>&1 || :
fi

%files
%doc LICENSE LICENSE.apache20 README RIGHTS.antlr
%doc build.xml checkstyle_checks.xml java.header sun_checks.xml suppressions.xml
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/xml/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}
#%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files demo
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc --no-dereference target/dist/%{name}-%{version}/docs/*

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_1jpp5
- added to depmap com.puppycrawl.tools:checkstyle

* Sat Mar 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_1jpp5
- full version

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_0jpp0
- temporary stub for 4.4

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2
- temporary stub to repair other packages rebuild

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_0.beta01.4jpp5
- converted from JPackage by jppimport script

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt3_1jpp1.7
branch 4.0 compatible build

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_1jpp1.7
- require new commons-cli

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt2_3jpp1.7
- converted from JPackage by jppimport script

* Sun Mar 26 2006 Vladimir Lettiev <crux@altlinux.ru> 4.1-alt2
- Fix build with j2se1.5

* Sun Dec 18 2005 Vladimir Lettiev <crux@altlinux.ru> 4.1-alt1
- Initial build for ALTLinux Sisyphus

