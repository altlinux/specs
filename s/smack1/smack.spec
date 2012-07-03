Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define oldname smack
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


Name:           smack1
Version:        1.5.0
Release:        alt3_3jpp5
Epoch:          0
Summary:        Open Source XMPP (Jabber) client library

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.jivesoftware.org/smack/
Source0:        http://www.jivesoftware.org/download-landing.jsp?file=builds/smack/smack-dev-1.5.0.tar.gz

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-contrib >= 0:1.0
BuildRequires: junit >= 0:3.8.1
BuildRequires: xpp3
Requires: xpp3

%description
Smack is an Open Source XMPP (Jabber) client library for instant 
messaging and presence. A pure Java library, it can be embedded 
into your applications to create anything from a full XMPP client 
to simple XMPP integrations such as sending notification messages.

%package        javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -q -n %{oldname}-dev-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
pushd build
ln -sf $(build-classpath ant-contrib)
ln -sf $(build-classpath junit)
pushd merge
ln -sf $(build-classpath xpp3) xpp.jar
popd
popd
ant -f build/build.xml jar javadoc jar-test

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 %{oldname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{oldname}x.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{oldname}x1-%{version}.jar

install -m 644 %{oldname}-test.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-test-%{version}.jar
install -m 644 %{oldname}x-debug.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oldname}x1-debug-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr documentation/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Mar 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_3jpp5
- renamed smack1x1.jar to smackx1.jar

* Mon Mar 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt2_3jpp5
- removed conflicts with smack3

* Tue May 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp5
- compat build

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_1jpp5
- new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

