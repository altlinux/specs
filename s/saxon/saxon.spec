Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Summary:        Java XPath, XSLT 2.0 and XQuery implementation
Name:           saxon
Version:        9.3.0.4
Release:        alt2_7jpp7
# net.sf.saxon.om.XMLChar is from ASL-licensed Xerces
# net/sf/saxon/option/jdom/ is MPLv1.1
# net/sf/saxon/serialize/codenorm/ is UCD
# net/sf/saxon/expr/sort/GenericSorter.java is MIT
# net/sf/saxon/expr/Tokenizer.java and few other bits are BSD
License:        MPLv1.0 and MPLv1.1 and ASL 1.1 and UCD and MIT
Group:          Text tools
URL:            http://saxon.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.3/saxon9-3-0-4source.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.saxonq.script
Source3:        %{name}.build.script
Source4:        %{name}.1
Source5:        %{name}q.1
Source6:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.3/saxon-resources9-3.zip
Source7:        http://irrational.googlecode.com/svn/trunk/maven-repo/net/sf/saxon/saxon-he/9.3.0.4/saxon-he-9.3.0.4.pom
Source8:        http://www.mozilla.org/MPL/1.0/index.txt#/mpl-1.0.txt
Source9:        http://www.mozilla.org/MPL/1.0/index.txt#/mpl-1.1.txt
BuildRequires:  unzip
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  bea-stax-api
BuildRequires:  xml-commons-apis
BuildRequires:  xom
BuildRequires:  jdom >= 0:1.0-0.b7
BuildRequires:  java-javadoc
BuildRequires:  jdom-javadoc >= 0:1.0-0.b9.3jpp
BuildRequires:  dom4j
Requires:       jpackage-utils
Requires:       bea-stax-api
Requires:       bea-stax
Requires:       chkconfig
Provides:       jaxp_transform_impl = %{version}-%{release}

# Older versions were split into multile packages
Obsoletes:  %{name}-xpath < %{version}-%{release}
Obsoletes:  %{name}-xom < %{version}-%{release}
Obsoletes:  %{name}-sql < %{version}-%{release}
Obsoletes:  %{name}-jdom < %{version}-%{release}
Obsoletes:  %{name}-dom < %{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Saxon HE is Saxonica's non-schema-aware implementation of the XPath 2.0,
XSLT 2.0, and XQuery 1.0 specifications aligned with the W3C Candidate
Recommendation published on 3 November 2005. It is a complete and
conformant implementation, providing all the mandatory features of
those specifications and nearly all the optional features.


%package        manual
Summary:        Manual for %{name}
Group:          Text tools
BuildArch: noarch

%description    manual
Manual for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demos for %{name}
Group:          Text tools
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        scripts
Summary:        Utility scripts for %{name}
Group:          Text tools
Requires:       jpackage-utils >= 0:1.5
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    scripts
Utility scripts for %{name}.


%prep
%setup -q -c

unzip -q %{SOURCE6}
cp -p %{SOURCE3} ./build.xml

# deadNET
rm -rf net/sf/saxon/dotnet

# Depends on XQJ (javax.xml.xquery)
rm -rf net/sf/saxon/xqj

# This requires a EE edition feature (com.saxonica.xsltextn)
rm -rf net/sf/saxon/option/sql/SQLElementFactory.java

# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
find . \( -name "*.jar" -name "*.pyc" \) -delete

cp %{SOURCE8} %{SOURCE9} .

%build
mkdir -p build/classes
cat >build/classes/edition.properties <<EOF
config=net.sf.saxon.Configuration
platform=net.sf.saxon.java.JavaPlatform
EOF

export CLASSPATH=%(build-classpath xml-commons-apis jdom xom bea-stax-api dom4j)
ant \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom


%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}q
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}q.1

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar

# a simple POM
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
sed -i -e 's/saxon-he/saxon/' $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_transform_impl_saxon<<EOF
%{_javadir}/jaxp_transform_impl.jar	%{_javadir}/%{name}.jar	25
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%_altdir/jaxp_transform_impl_saxon
%doc mpl-1.0.txt mpl-1.1.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files manual
%doc doc/*

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%files scripts
%{_bindir}/%{name}
%{_bindir}/%{name}q
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}q.1*


%changelog
* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt1_5jpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_3jpp6
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt1_1jpp5
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt1_5jpp1.7
- converted from JPackage by jppimport script

