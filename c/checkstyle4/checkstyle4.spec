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

%define gcj_support 0

%define oname checkstyle

Name:           checkstyle4
Version:        4.4
Release:        alt2_5jpp6
Epoch:          0
Summary:        Java source code checker
License:        LGPL
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/checkstyle/checkstyle-src-4.4.tar.gz
Source1:        %{name}-%{version}-script
Source2:        %{name}-%{version}.catalog

URL:            http://checkstyle.sourceforge.net/
Requires: ant >= 0:1.7.1
Requires: antlr >= 0:2.7.1
Requires: regexp >= 0:1.4
Requires: jakarta-commons-logging
Requires: jakarta-commons-cli
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jpackage-utils >= 0:1.7.5
Requires: jaxp_parser_impl
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: junit
BuildRequires: antlr >= 0:2.7.1
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-cli
BuildRequires: xalan-j2
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-collections
# xerces-j2 because tests fail with gnujaxp...
BuildRequires: xerces-j2
BuildRequires: antlr-javadoc
BuildRequires: xml-commons-jaxp-1.3-apis-javadoc
BuildRequires: jakarta-commons-beanutils-javadoc
BuildRequires: ant-javadoc
BuildRequires: /usr/bin/perl
BuildRequires: excalibur-avalon-logkit
BuildRequires: emma
BuildRequires: jdom
BuildRequires: velocity14
BuildRequires: jpackage-utils >= 0:1.7.5
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
#Provides:       %{oname} = %{epoch}:%{version}

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info
Source45: import.info


%description
A tool for checking Java source code for adherence to a set of rules.

%package        demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires: %{name} = %{epoch}:%{version}

%description    demo
Demonstrations and samples for %{name}.

%package        javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description    manual
Manual for %{name}.

%package        optional
Group:          Development/Java
Summary:        Optional functionality for %{name}
Requires: %{name} = %{epoch}:%{version}
Provides:       %{oname}-optional = %{epoch}:%{version}
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description    optional
Optional functionality for %{name}.

%prep
%setup -q -n %{oname}-src-%{version}

#%__perl -p -i -e 's|\./{\@docRoot}/\.\./index\.html|%{_docdir}/%{name}-manual-%{version}/index.html|' build.xml

# remove all binary libs
#find . -name "*.jar" -exec %__rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-nodeps ant/ant-trax jdom velocity14"
export CLASSPATH=$(build-classpath excalibur/avalon-logkit commons-collections commons-lang xalan-j2)

pushd lib
ln -sf $(build-classpath antlr) .
ln -sf $(build-classpath commons-beanutils-core) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-cli) .
ln -sf $(build-classpath commons-lang) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath emma) .
ln -sf $(build-classpath emma_ant) .
ln -sf $(build-classpath jdom) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath velocity14) .
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=first \
  -Dant.javadoc=%{_javadocdir}/ant \
  -Dantlr.javadoc=%{_javadocdir}/antlr \
  -Djaxp.javadoc=%{_javadocdir}/xml-commons-apis \
  -Dbeanutils.javadoc=%{_javadocdir}/jakarta-commons-beanutils \
  run.tests build.bindist

%install
%__rm -rf %{buildroot}

# jars
%__install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%__install -pm 644 target/dist/%{oname}-%{version}/%{oname}-%{version}.jar \
                     $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%__install -pm 644 target/dist/%{oname}-%{version}/%{oname}-optional-%{version}.jar \
                     $RPM_BUILD_ROOT%{_javadir}/%{name}-optional-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do %__ln_s ${jar} `echo $jar| %__sed "s|-%{version}||g"`; done)

%add_to_maven_depmap checkstyle checkstyle %{version} JPP %{name}
%add_to_maven_depmap checkstyle checkstyle-optional %{version} JPP %{name}-optional

# poms
%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%__install -pm 644 pom.xml \
            $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%__install -pm 644 pom-optional.xml \
            $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-optional.pom

# script
%__install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
%__install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# dtds
%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/xml/%{name}
%__install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xml/%{name}/catalog
%__cp -a src/checkstyle/com/puppycrawl/tools/checkstyle/*.dtd \
            $RPM_BUILD_ROOT%{_datadir}/xml/%{name}

# javadoc
%__install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%__cp -ar target/dist/%{oname}-%{version}/docs/api/* \
            $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%__rm -rf target/dist/%{oname}-%{version}/docs/api
%__ln_s %{_javadocdir}/%{name} target/dist/%{oname}-%{version}/docs/api
%__ln_s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# demo
%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -ar target/dist/%{oname}-%{version}/contrib/* \
                     $RPM_BUILD_ROOT%{_datadir}/%{name}

# ant.d
%__install -d -m 755  $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
%__cat > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name} << EOF
checkstyle4 antlr regexp jakarta-commons-beanutils jakarta-commons-cli jakarta-commons-logging jakarta-commons-collections jaxp_parser_impl
EOF

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%postun
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%post optional
%__grep -q checkstyle-optional %{_sysconfdir}/ant.d/%{name} || \
%__perl -p -i -e 's|checkstyle|checkstyle4 checkstyle4-optional|' %{_sysconfdir}/ant.d/%{name}

%postun optional
%__grep -q checkstyle4-optional %{_sysconfdir}/ant.d/%{name} && \
%__perl -p -i -e 's|checkstyle4-optional ||' %{_sysconfdir}/ant.d/%{name} || :

%files
%doc LICENSE LICENSE.apache README RIGHTS.antlr
%doc build.xml checkstyle_checks.xml java.header sun_checks.xml suppressions.xml
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/xml/%{name}
%attr(0755,root,root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files demo
%{_datadir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc --no-dereference target/dist/%{oname}-%{version}/docs/*

%files optional
%{_javadir}/%{name}-optional.jar
%{_javadir}/%{name}-optional-%{version}.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-optional-%{version}.jar.*
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt2_5jpp6
- fixed build with maven3

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_5jpp6
- new jpp release

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_4jpp5
- new version

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt7_1jpp5
- added scheckstyle4*jars

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt6_1jpp5
- removed conflicts (for stub support)

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt5_1jpp5
- provides checkstyle-optional

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_1jpp5
- compatibility package

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

%changelog
