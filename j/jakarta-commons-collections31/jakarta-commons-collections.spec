%define oldname jakarta-commons-collections
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'
%define _without_maven 1

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name       collections
%define short_name      commons-%{base_name}

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/apache-collections/3.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:		jakarta-commons-collections31
Version:	3.1
Release:	alt6_9jpp5
Epoch:		1
Summary:	Jakarta Commons Collections Package
License:	Apache Software License v2
Group:		Development/Java
#Vendor:		JPackage Project
#Distribution:	JPackage
#Source0:	http://www.apache.org/dist/jakarta/commons/collections/source/commons-collections-3.1-src.tar.gz
Source0:        %{short_name}-%{version}-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        commons-collections-3.1-jpp-depmap.xml
Source5:        commons-build.tar.gz
Source6:        collections-tomcat5-build.xml
Source7:	jakarta-commons-collections-component-info.xml

Patch0:         %{oldname}-javadoc-nonet.patch
Patch1:         commons-collections-3.1-project_xml.patch
Patch2:         commons-collections-3.1-navigation_xml.patch
Patch3:         commons-collections-3.1-project_properties.patch
Patch4:         commons-collections-3.1-build_xml.patch

Url:		http://jakarta.apache.org/commons/%{base_name}/
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: xml-commons-jaxp-1.3-apis
%if %{with_maven}
BuildRequires: maven >= 0:1.1
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-changes
BuildRequires: maven-plugin-jdepend
BuildRequires: maven-plugin-jdiff
BuildRequires: maven-plugin-jxr
BuildRequires: maven-plugin-tasklist
BuildRequires: maven-plugin-developer-activity
BuildRequires: maven-plugin-file-activity
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
#Provides:       %{short_name} = %{epoch}:%{version}-%{release}
#Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

%package testframework
Summary:        Testframework for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description testframework
%{summary}.

%if %{with_repolib}
%package	 repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	Development/Java

%description	 repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
Requires(post): %{__rm}
Requires(postun): %{__rm}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package tomcat5
Summary:        Collection dependency for Tomcat5
Group:          Development/Java

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description tomcat5
Collections dependency for Tomcat5

%package testframework-javadoc
Summary:        Javadoc for %{name}-testframework
Group:          Development/Documentation
Requires(post): %{__rm}
Requires(postun): %{__rm}

%description testframework-javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
cat <<EOT

                If you dont want to build with maven,
                give rpmbuild option '--without maven'

EOT

%setup -q -n %{short_name}-%{version}
gzip -dc %{SOURCE5} | tar xf -
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

#%patch0 -p0
%patch0 -p1
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
# Avoid fail on error for GCJ. See FIXME below.
%if %{gcj_support}
%patch4 -b .sav
%endif
cp %{SOURCE6} .

tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}

%build
%if %{with_maven}
export DEPCAT=$(pwd)/commons-collections-3.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > commons-collections-3.1-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

#        -Dmaven.test.failure.ignore=true \
maven \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate xdoc:transform
ant tf.javadoc
%else
#FIXME Enabling tests with gcj causes memory leaks!
# See http://gcc.gnu.org/bugzilla/show_bug.cgi?id=28423
%if %{gcj_support}
ant -Djava.io.tmpdir=. -Dant.build.javac.source=1.4 jar javadoc tf.validate tf.jar dist.bin dist.src tf.javadoc
%else
ant -Djava.io.tmpdir=. -Dant.build.javac.source=1.4 test dist tf.javadoc
%endif
%endif

# commons-collections-tomcat5
ant -f collections-tomcat5-build.xml

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %{with_maven}
install -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%else
install -m 644 build/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%endif

#tomcat5
install -m 644 collections-tomcat5/%{short_name}-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/docs/apidocs

# testframework-javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
cp -pr build/docs/testframework/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework # ghost symlink

# manual
%if %{with_maven}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp $RPM_BUILD_ROOT%{_javadir}/commons-collections31.jar $RPM_BUILD_ROOT%{repodirlib}/commons-collections.jar
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%post testframework-javadoc
rm -f %{_javadocdir}/%{name}-testframework
ln -s %{name}-testframework-%{version} %{_javadocdir}/%{name}-testframework

%postun testframework-javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}-testframework
fi

%files
%doc PROPOSAL.html README.txt STATUS.html LICENSE.txt RELEASE-NOTES.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}31-%{version}.jar
%{_javadir}/%{short_name}31.jar

%if %{gcj_support}
%{_libdir}/gcj/%{name}/jakarta-commons-collections-3.1.jar.*
%endif

%files testframework
%{_javadir}/%{name}-testframework-%{version}.jar
%{_javadir}/%{name}-testframework.jar
%{_javadir}/%{short_name}31-testframework-%{version}.jar
%{_javadir}/%{short_name}31-testframework.jar

%if %{gcj_support}
%{_libdir}/gcj/%{name}/jakarta-commons-collections-testframework-3.1.jar.*
%endif

%files tomcat5
%{_javadir}/*-tomcat5*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/*-tomcat5*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files testframework-javadoc
%{_javadocdir}/%{name}-testframework-%{version}
%ghost %{_javadocdir}/%{name}-testframework

%if %{with_maven}
%files manual
%{_docdir}/%{name}-%{version}
%endif

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt6_9jpp5
- fixed build with moved maven1

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt5_9jpp5
- compat build

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt4_9jpp5
- fixed pre/trigger bug

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt3_9jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_9jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt2_11jpp1.7
- rebuilt with maven1

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.1-alt1_11jpp1.7
- converted from JPackage by jppimport script

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1
- added JPackage compatible stuff

* Mon Mar 21 2005 Vladimir Lettiev <crux@altlinux.ru> 3.2-alt0.2
- rpm-build-java macroces
- cvs 20050321

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 3.2-alt0.1
- 3.2-dev (cvs 20041024)
- fix build with j2se1.5

* Thu Sep 09 2004 Vladimir Lettiev <crux@altlinux.ru> 3.1-alt1
- 3.1
- spec cleanup

* Wed Sep 08 2004 Vladimir Lettiev <crux@altlinux.ru> 0:2.1.1-alt1
- Rebuild for ALT Linux Sisyphus

* Sun Jun 27 2004 Kaj J. Niemi <kajtzu@fi.basen.net> 0:2.1.1-1jpp
- Update to 2.1.1

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:2.1-4jpp
- update for JPackage 1.5

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org > 2.1-3jpp
- For jpackage-utils 1.5

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 2.1-2jpp
- fix ASF license and add package tag

* Thu Oct 24 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.1-1jpp
- 2.1
- remove build patch about Java APIS link

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-4jpp
- override java.io.tmpdir to avoid build use /tmp

* Mon Jun 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-3jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x

* Fri Jun 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-2jpp
- added short names in %_javadir, as does jakarta developpers

* Mon May 06 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.0-1jpp
- 2.0
- distribution tag
- group tag
- regenerated patch

* Sat Jan 19 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-5jpp
- renamed to %oldname
- additional sources in individual archives
- versioned dir for javadoc
- section macro

* Fri Dec 7 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-4jpp
- javadoc into javadoc package

* Sat Nov 3 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-3jpp
- used original summary
- added missing license

* Sat Oct 13 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-2jpp
- first unified release
- used web page description
- s/jPackage/JPackage

* Mon Aug 27 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-1mdk
- first Mandrake release
