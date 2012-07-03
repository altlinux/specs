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

%define beta            b5


Name:           puretls
Version:        0.9
Release:        alt2_0.b5.5jpp1.7
Summary:        Java implementation of SSLv3 and TLSv1
License:        BSD style
Group:          Development/Java
Source0:        %{name}-%{version}%{beta}.tar.gz
Url:            http://www.rtfm.com/puretls
Patch0:         puretls-build_xml.patch
Requires: cryptix
Requires: cryptix-asn1
BuildRequires: ant
BuildRequires: cryptix
BuildRequires: cryptix-asn1
BuildRequires: gnu.getopt
##BuildRequires: java-devel >= 1.4.0
%if ! %{gcj_support}
Buildarch:      noarch
%endif
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
PureTLS is a free Java-only implementation of the SSLv3 and TLSv1
(RFC2246) protocols. PureTLS was developed by Eric Rescorla for Claymore
Systems, Inc, but is being distributed for free because we believe that
basic network security is a public good and should be a commodity.

%package javadoc
Group:  Development/Java
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%package demo
Group:  Development/Java
Summary:        Demo for %{name}
Requires: %{name}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description demo
Demo for %{name}.

%prep
%setup -q -n %{name}-%{version}%{beta}
%patch0
# fix perl location
find . -type f |
    xargs grep -l "/usr/local/bin/perl5" | \
    xargs perl -pi -e "s|/usr/local/bin/perl5|%{_bindir}/perl|g;"
find . -type f |
    xargs grep -l "/usr/local/bin/perl" | \
    xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g;"

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

# remove an empty .java source file that upsets javadoc
rm src/COM/claymoresystems/sslg/CertVerifyPolicy.java

# delete test as it contains sun.* classes which will not work on different jvms
rm src/COM/claymoresystems/provider/test/DSATest.java

%build
export LANG=en_US.ISO8859-1
mkdir dist

for javaver in 1.4 ; do
        export JAVA_HOME=$(find %{_jvmdir} -name "java-$javaver*" -type d | sort | tail -1)
        export CLASSPATH=$(build-classpath cryptix cryptix-asn1 gnu.getopt)
        ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djdk.version=$javaver clean compile
        mv build/%{name}.jar dist/%{name}$javaver.jar
done

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}-ext

install -m 644 dist/%{name}1.4.jar $RPM_BUILD_ROOT%{_javadir}-ext/%{name}1.4-%{version}.%{beta}.jar

%add_jvm_extension %{name}1.4-%{version}.%{beta} %{name} 1.4.0 1.4.1 1.4.2
%add_jvm_extension %{name}1.4-%{version}.%{beta} %{name}-%{version}.%{beta} 1.4.0 1.4.1 1.4.2

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r build/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 build/%{name}demo.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-demo.jar
install -m 644 *.pem $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 test.pl $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi


%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post demo
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun demo
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc ChangeLog COPYRIGHT INSTALL LICENSE README
%{_javadir}-*/*.jar


%if %{gcj_support}
%{_libdir}/gcj/%{name}/puretls1.4-0.9.b5.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%if %{gcj_support}
%{_libdir}/gcj/%{name}/puretls-demo.jar.*
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_0.b5.5jpp1.7
- fixed build with java 7

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_0.b5.5jpp1.7
- converted from JPackage by jppimport script

