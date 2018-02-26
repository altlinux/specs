Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0

%define jmailver 1.3.1
%define inetlibver 1.1.1

Name:           classpathx-mail
Version:        1.1.2
Release:        alt3_1jpp5
Epoch:          0
Summary:        GNU JavaMail(tm)

Group:          Development/Java
License:        GPL with library exception
URL:            http://www.gnu.org/software/classpathx/
Source0:        http://ftp.gnu.org/gnu/classpathx/mail-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/classpath/inetlib-1.1.1.tar.gz
# see bz157685
#Patch1:         %{name}-docbuild.patch
Patch2:         %{name}-add-inetlib.patch
Patch3:         %{name}-remove-inetlib.patch
# see bz157685
Patch4:         classpath-inetlib-docbuild.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
#BuildRequires: classpathx-jaf >= 0:1.1
BuildRequires: %{_bindir}/perl
Requires: jaf_1_1_api
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       javamail_1_3_1_api

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info
# required for fedora tomcat
Provides: javamail = 0:1.3.1
Provides: javamail-monolithic = 0:1.3.1

%description
GNU JavaMail(tm) is a free implementation of the JavaMail API.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       javamail-javadoc = 0:%{jmailver}
BuildRequires: java-javadoc jaf-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q -n mail-%{version}
#%patch1 -p0
%patch2 -p0
%patch3 -p0
rm -f libmail.so
gzip -dc %{SOURCE1} | tar -xf -
pushd inetlib-%{inetlibver}
%patch4 -p0
  mkdir -p source/org/jpackage/mail
  mv source/gnu/inet source/org/jpackage/mail
popd
# assume no filename contains spaces
perl -p -i -e 's/gnu(.)inet/org${1}jpackage${1}mail${1}inet/' `grep gnu.inet -lr *`


%build
# build inetlib
pushd inetlib-%{inetlibver}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java inetlib.jar doc
popd
mkdir classes
cp -r inetlib-%{inetlibver}/classes/org classes

# build mail
#export CLASSPATH=%(build-classpath jaf_1_1_api)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
	 -Dactivation.available=true \
  -Dj2se.apidoc=%{_javadocdir}/java \
  -Djaf.apidoc=%{_javadocdir}/jaf \
  dist javadoc

# build monolithic
mkdir monolithic
pushd monolithic
for jar in gnumail gnumail-providers ; do jar xf ../$jar.jar; done
rm -f META-INF/MANIFEST.MF
jar cf ../monolithic.jar *
popd
rm -Rf monolithic

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/classpathx-mail

# API
install -pm 644 gnumail.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/mail-%{jmailver}-api-%{version}.jar
ln -s mail-%{jmailver}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/mail-%{jmailver}-api.jar
ln -s mail-%{jmailver}-api.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/mailapi.jar

# Providers
install -pm 644 gnumail-providers.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/mail-%{jmailver}-providers-%{version}.jar
ln -s mail-%{jmailver}-providers-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/mail-%{jmailver}-providers.jar
ln -s mail-%{jmailver}-providers.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/providers.jar
for prov in imap nntp pop3 smtp ; do
  ln -s mail-%{jmailver}-providers.jar \
    $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/$prov-%{jmailver}.jar
  ln -s providers.jar $RPM_BUILD_ROOT%{_javadir}/classpathx-mail/$prov.jar
done

install -pm 644 monolithic.jar \
  $RPM_BUILD_ROOT%{_javadir}/classpathx-mail-%{jmailver}-monolithic-%{version}.jar
ln -s classpathx-mail-%{jmailver}-monolithic-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/classpathx-mail-%{jmailver}-monolithic.jar
touch $RPM_BUILD_ROOT%{_javadir}/javamail.jar # for %ghost

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{jmailver}
cp -pR docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{jmailver}
ln -s %{name}-%{jmailver} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_%{name}<<EOF
%{_javadir}/javamail.jar	%{_javadir}/classpathx-mail-1.3.1-monolithic.jar	010301
EOF

%files
%_altdir/javamail_%{name}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%dir %{_javadir}/classpathx-mail
%{_javadir}/classpathx-mail/mail-%{jmailver}-api-%{version}.jar
%{_javadir}/classpathx-mail/mail-%{jmailver}-api.jar
%{_javadir}/classpathx-mail/mailapi.jar
%{_javadir}/classpathx-mail/mail-%{jmailver}-providers-%{version}.jar
%{_javadir}/classpathx-mail/mail-%{jmailver}-providers.jar
%{_javadir}/classpathx-mail/providers.jar
%{_javadir}/classpathx-mail/imap-%{jmailver}.jar
%{_javadir}/classpathx-mail/imap.jar
%{_javadir}/classpathx-mail/nntp-%{jmailver}.jar
%{_javadir}/classpathx-mail/nntp.jar
%{_javadir}/classpathx-mail/pop3-%{jmailver}.jar
%{_javadir}/classpathx-mail/pop3.jar
%{_javadir}/classpathx-mail/smtp-%{jmailver}.jar
%{_javadir}/classpathx-mail/smtp.jar
# Monolithic jar
%{_javadir}/classpathx-mail-%{jmailver}-monolithic-%{version}.jar
%{_javadir}/classpathx-mail-%{jmailver}-monolithic.jar
%exclude %{_javadir}/javamail.jar

%if %{gcj_support}
%{_libdir}/gcj/%{name}/classpathx-mail-1.3.1-monolithic-1.1.1.jar.*
%endif

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{jmailver}
%doc %{_javadocdir}/%{name}


%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt3_1jpp5
- build without classpathx-jaf

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_1jpp5
- build w/o classpathx-jaf dependency

* Thu May 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_1jpp5
- added javamail provides

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_1jpp5
- new version

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_4jpp1.7
fixed jaf requires

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

