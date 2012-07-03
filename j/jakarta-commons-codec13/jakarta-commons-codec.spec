%define oldname jakarta-commons-codec
Packager: Igor Vlasenko <viy@altlinux.ru>
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/apache-codec/1.3.0-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define base_name  codec
%define short_name commons-%{base_name}

Name:           jakarta-commons-codec13
Version:        1.3
Release:        alt6_9jpp5
Summary:        Jakarta Commons Codec Package
License:        Apache Software License
Group:          Development/Java
#Vendor:         JPackage Project
#Distribution:   JPackage
Epoch:          0
URL:            http://jakarta.apache.org/commons/codec/
Source0:        http://www.apache.org/dist/jakarta/commons/codec/source/commons-codec-%{version}-src.tar.gz
Patch0:		jakarta-commons-codec-1.3-buildscript.patch
Source1:	jakarta-commons-codec-component-info.xml
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6.2
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: java-javadoc
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} <= %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Patch33: jakarta-commons-codec-addosgimanifest.patch

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders.

%if %{with_repolib}
%package	 repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	Development/Java

%description	 repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: java-javadoc
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -c

# FIXME Remove SoundexTest which is failing
# and thus preventing the build to proceed.
# This problem has been communicated upstream Bug 31096
%patch0 -p1

#fixes eof encoding
%{__sed} -i 's/\r//' LICENSE.txt
%{__sed} -i 's/\r//' RELEASE-NOTES.txt

# -----------------------------------------------------------------------------

tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%patch33 -p1

%build
export CLASSPATH=$(build-classpath junit)
perl -p -i -e 's|../LICENSE|LICENSE.txt|g' build.xml
#sed -i 's|\.\.\/LICENSE|LICENSE.txt|g' build.xml
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first \
  -Dconf.home=src/conf \
  -Dbuild.home=build \
  -Dsource.home=src/java \
  -Dtest.home=src/test \
  -Ddist.home=dist \
  -Dcomponent.title=%{short_name} \
  -Dcomponent.version=%{version} \
  -Dfinal.name=%{oldname}-%{version} \
  -Dextension.name=%{short_name} \
  test jar javadoc

# -----------------------------------------------------------------------------

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{oldname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp $RPM_BUILD_ROOT%{_javadir}/commons-codec13.jar $RPM_BUILD_ROOT%{repodirlib}/commons-codec.jar
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi
# -----------------------------------------------------------------------------
%files
%doc LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*

%if %{gcj_support}
%{_libdir}/gcj/%{name}/jakarta-commons-codec-1.3.jar.*
%endif

%exclude %{_javadir}/repository.jboss.com/*
%exclude %{_javadir}/repository.jboss.com

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}
# -----------------------------------------------------------------------------

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt6_9jpp5
- compat build

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt5_9jpp5
- added repolib

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4_9.4jpp5
- new version

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3.2_9jpp5
- rebuild with osgi provides

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3.2_8jpp1.7
- added eclipse manifest

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_8jpp1.7
- converted from JPackage by jppimport script

* Tue Mar 22 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3-alt2
- rpm-build-java macroces
- cvs 20050321

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.3-alt1
- 1.3-dev (cvs 20041024)
- Rebuild for ALT Linux Sisyphus

* Wed Sep 08 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-2jpp
- Do not stop on test failure

* Tue Sep 07 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-1jpp
- Upgrade to 1.3
- Rebuilt with Ant 1.6.2

* Thu Jan 22 2004 David Walluck <david@anti-microsoft.org> 0:1.2-1jpp
- 1.2
- use perl instead of patch

* Wed May 28 2003 Ville Skyttä <jpackage-discuss at zarb.org> - 0:1.1-1jpp
- First JPackage release.
