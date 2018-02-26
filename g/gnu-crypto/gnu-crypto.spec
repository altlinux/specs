BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define gcj_support 0

Name:           gnu-crypto
Version:        2.1.0
Release:        alt3_2jpp1.7
Epoch:          0
Summary:        GNU Crypto library for Java

Group:          Development/Java
License:        GPL with library exception
URL:            http://www.gnu.org/software/gnu-crypto/
Source0:        http://ftp.gnupg.org/GnuPG/gnu-crypto/gnu-crypto-2.1.0.tar.bz2
Source1:	ftp://ftp.gnu.org/gnu/classpath/classpath-0.92.tar.gz	
Source2:	gnu-crypto-security-Makefile.am
Patch0:		%{name}-makefile.patch
Patch1:         %{name}-configure.patch
Patch2:		%{name}-sources-Makefile.patch

BuildRequires: automake autoconf
%if !%{gcj_support}
Requires(post): jpackage-utils >= 0:1.6.3-1jpp_1rh
Requires(postun): jpackage-utils >= 0:1.6.3-1jpp_1rh
%else
Requires: jce
Requires: jpackage-utils >= 0:1.6.2-1jpp_5rh
%endif
Requires: java-sasl
%if %{gcj_support}

BuildRequires: java-gcj-compat-devel >= 1.0.31
Requires(post): java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31
%else
BuildArch:      noarch
%endif

%description
GNU Crypto, part of the GNU project, released under the aegis of GNU,
aims at providing free, versatile, high-quality, and provably correct
implementations of cryptographic primitives and tools in the Java
programming language for use by programmers and end-users.

%package        sasl-jdk1.4
Summary:        Gnu Crypto SASL API
Group:          Development/Java
Provides:       java-sasl

%description    sasl-jdk1.4
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc

%description    javadoc
%{summary}.


%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
tar xzf %{SOURCE1}
mkdir -p security/javax/security
mv classpath-0.92/javax/security/sasl security/javax/security
cp %{SOURCE2} security/Makefile.am

%build
./autogen.sh
%configure --build=%_arch --host=%_arch
make

%install

%if %{gcj_support}
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/3000-gnu.crypto.jce.GnuCrypto
%endif

install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_javadir}-ext
install -dm 755 $RPM_BUILD_ROOT%{_javadir}-1.4.2
install -pm 644 source/gnu-crypto.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%if %{gcj_support}
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed
ln -s %{_javadir}/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/gcj-endorsed/%{name}-%{version}.jar
%endif

install -pm 644 security/javax-security.jar \
  $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-sasl-jdk1.4.jar
ln -s %{_javadir}-ext/%{name}-sasl-jdk1.4.jar \
    $RPM_BUILD_ROOT%{_javadir}-1.4.2/sasl.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pR source/overview.html $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

#%%check || :
# ant check # takes a looooong time


%clean

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-security-providers ]
then
  %{_bindir}/rebuild-security-providers
fi
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi

%postun
if [ -x %{_bindir}/rebuild-security-providers ]
then
  %{_bindir}/rebuild-security-providers
fi
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README THANKS
%{_javadir}/%{name}*.jar
%if %{gcj_support}
%{_sysconfdir}/java/security/security.d/3000-gnu.crypto.jce.GnuCrypto
%{_javadir}/gcj-endorsed/%{name}-%{version}.jar
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files sasl-jdk1.4
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README THANKS
%{_javadir}-ext/%{name}-sasl-jdk1.4.jar
%{_javadir}-1.4.2/sasl.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-sasl-jdk1.4.jar.*
%endif

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt3_2jpp1.7
- built with java 6

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt2_2jpp1.7
- fixed dependency on java-devel

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

