%define oldname itext
Packager: Igor Vlasenko <viy@altlinux.ru>
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


Summary:        A Free Java-PDF library
Name:           itext1
Version:        1.4
Release:        alt2_5jpp6
Epoch:          1
License:        Mozilla Public License & LGPL
URL:            http://www.lowagie.com/iText/
Group:          Development/Java
Source0:        itext-src-1.4.tar.gz
# svn export https://itext.svn.sourceforge.net/svnroot/itext/tags/iText_1_4 itext
# tar czf itext-src-1.4.tar.gz itext
Source2:	    itext-1.3-manifest.mf
Source3:	    %{oldname}.pom
Patch0:         %{oldname}-usefreesoftware.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: ant-trax
BuildArch:      noarch

%description
iText is a library that allows you to generate 
PDF files on the fly. The iText classes are very 
useful for people who need to generate read-only, 
platform independent documents containing text, 
lists, tables and images. The library is especially 
useful in combination with Java(TM) technology-based 
Servlets: The look and feel of HTML is browser 
dependent; with iText and PDF you can control 
exactly how your servlet's output will look.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{oldname}
mkdir -p src/META-INF
cp %{SOURCE2} src/META-INF/MANIFEST.MF
find . -name "*.jar" -exec rm {} \;

%patch0

%build
pushd src
export OPT_JAR_LIST="ant/ant-trax"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc tutorial lowagie.com
popd

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/itext
cp -p build/bin/iText.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/lowagie/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/examples $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/tutorial $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# Install the pom
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -pr %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
%add_to_maven_depmap itext itext 1.3 JPP %{name}
%add_to_maven_depmap com.lowagie itext 1.3 JPP %{name}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/MPL-1.1.txt
%doc %{_docdir}/%{name}-%{version}/lgpl.txt
%{_javadir}
%{_datadir}/maven2
%{_mavendepmapfragdir}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/*

# -----------------------------------------------------------------------------

%changelog
* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt2_5jpp6
- renamed to itext1

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_5jpp6
- fixed pom

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_3jpp5
- doungrade due to old maven-doxia; anyway current is 2.1

* Sat Sep 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.8-alt1_0.2jpp1.7
- converted from JPackage by jppimport script
- resurrected from orphaned

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt0.1
- new version 1.4.8 (with rpmrb script)

* Thu Feb 16 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.1
- new version

* Wed Oct 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt0.1
- new version

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt0.1
- first build for ALT Linux Sisyphus

* Thu Aug 26 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.3-1jpp
- Upgrade to 1.3
- Now one jar only

* Wed Aug 25 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.02b-2jpp
- Build with ant-1.6.2
- Relax some versioned dependencies

* Fri Feb 27 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.02b-1jpp
- First JPackage release
