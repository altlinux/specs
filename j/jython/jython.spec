Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
#BuildRequires(pre): j2se-jdbc = 1.4.2
BuildRequires: jline
# recommends
Requires: jline libreadline-java
AutoReq: yes, nopython
BuildRequires: /proc
BuildRequires: jpackage-compat
%{expand: %%define pyver %(python -c 'import sys;print(sys.version[0:3])')}

%global cpython_version    %{pyver}
%global pyxml_version      0.8.3
%global svn_tag            Release_2_2_1
%global _python_bytecompile_errors_terminate_build 0

Name:                      jython
Version:                   2.2.1
Release:                   alt5_8jpp7
Summary:                   Jython is an implementation of Python written in pure Java.
License:                   ASL 1.1 and BSD and CNRI and JPython and Python
URL:                       http://www.jython.org/
# Use the included fetch-jython.sh script to generate the source drop
# for jython 2.2.1
# sh fetch-jython.sh \
#   jython https://jython.svn.sourceforge.net/svnroot Release_2_2_1
#
Source0:                   %{name}-fetched-src-%{svn_tag}.tar.bz2
Source2:                   fetch-%{name}.sh
Patch0:                    %{name}-cachedir.patch
# Make javadoc and copy-full tasks not depend upon "full-build"
# Also, copy python's license from source directory and not
# ${python.home}
Patch1:                    %{name}-nofullbuildpath.patch
Requires:                  jpackage-utils >= 0:1.5
Requires:                  jakarta-oro
Requires:                  servlet
Requires:                  libreadline-java >= 0.8.0-16
Requires:                  mysql-connector-java
BuildRequires:             ant
BuildRequires:             ht2html
BuildRequires:             libreadline-java >= 0.8.0-16
BuildRequires:             mysql-connector-java
BuildRequires:             jakarta-oro
BuildRequires:             python-module-PyXML >= %{pyxml_version}
BuildRequires:             servlet
Group:                     Development/Java

BuildArch:                 noarch
Source44: import.info

%description
Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100%% Pure Java. Jython is
freely available for both commercial and non-commercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting - Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to the
application. Interactive experimentation - Jython provides an interactive
interpreter that can be used to interact with Java packages or with
running Java applications. This allows programmers to experiment and debug
any Java system using Jython. Rapid application development - Python
programs are typically 2-10X shorter than the equivalent Java program.
This translates directly to increased programmer productivity. The
seamless interaction between Python and Java allows developers to freely
mix the two languages both during development and in shipping products.

%package javadoc
Summary:           Javadoc for %{name}
Group:             Development/Java
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package manual
Summary:           Manual for %{name}
Group:             Development/Java
BuildArch: noarch

%description manual
Usage documentation for %{name}.

%package demo
Summary:           Demo for %{name}
Requires:          jython = %{version}-%{release}
Group:             Development/Java
AutoReq: yes, nopython
#AutoProv: yes, nopython

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-svn-%{svn_tag}
%patch0 -p1
%patch1 -p1

%build
export CLASSPATH=$(build-classpath mysql-connector-java oro servlet)
# FIXME: fix jpackage-utils to handle multilib correctly
export CLASSPATH=$CLASSPATH:%{_libdir}/libreadline-java/libreadline-java.jar

rm -rf org/apache

perl -p -i -e 's|execon|apply|g' build.xml

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dpython.home=%{_bindir} \
  -Dht2html.dir=%{_datadir}/ht2html \
  -Dpython.lib=./CPythonLib \
  -Dpython.exe=%{_bindir}/python \
  -DPyXmlHome=%{_libdir}/python%pyver \
  -Dtargetver=1.3 \
  copy-dist


# remove #! from python files
pushd dist
  for f in `find . -name '*.py'`
  do
    sed --in-place  "s:#!\s*/usr.*::" $f
  done
popd

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/Doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
# these are not supposed to be distributed
find dist/Lib -type d -name test | xargs rm -rf

cp -pr dist/Lib $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr dist/Tools $RPM_BUILD_ROOT%{_datadir}/%{name}
# demo
cp -pr dist/Demo $RPM_BUILD_ROOT%{_datadir}/%{name}
# manual
rm -rf dist/Doc/javadoc
mv dist/Doc %{name}-manual-%{version}


# registry
install -m 644 registry $RPM_BUILD_ROOT%{_datadir}/%{name}
# scripts
install -d $RPM_BUILD_ROOT%{_bindir}

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script
# JPackage Project (http://jpackage.sourceforge.net)

# Source functions library
. %{_datadir}/java-utils/java-functions

# Source system prefs
if [ -f %{_sysconfdir}/%{name}.conf ] ; then
  . %{_sysconfdir}/%{name}.conf
fi

# Source user prefs
if [ -f \$HOME/.%{name}rc ] ; then
  . \$HOME/.%{name}rc
fi

# Arch-specific location of dependency
case \$(uname -m) in
   x86_64 | ia64 | s390x | ppc64 | sparc64 )
      JYTHONLIBDIR="/usr/lib64" ;;
   * )
      JYTHONLIBDIR="/usr/lib" ;;
esac

# Configuration
MAIN_CLASS=org.python.util.%{name}
BASE_FLAGS=-Dpython.home=%{_datadir}/%{name}
BASE_JARS="%{name} oro servlet mysql-connector-java"

BASE_FLAGS="\$BASE_FLAGS -Dpython.console=org.python.util.ReadlineConsole"
BASE_FLAGS="\$BASE_FLAGS -Djava.library.path=\$JYTHONLIBDIR/libreadline-java"
BASE_FLAGS="\$BASE_FLAGS -Dpython.console.readlinelib=Editline"

# Set parameters
set_jvm
CLASSPATH=\$CLASSPATH:\$JYTHONLIBDIR/libreadline-java/libreadline-java.jar
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run "\$@"
EOF

cat > $RPM_BUILD_ROOT%{_bindir}/%{name}c << EOF
#!/bin/sh
#
# %{name}c script
# JPackage Project (http://jpackage.sourceforge.net)

%{_bindir}/%{name} %{_datadir}/%{name}/Tools/%{name}c/%{name}c.py "\$@"
EOF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jython.conf`
touch $RPM_BUILD_ROOT/etc/jython.conf

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/jython/cachedir/packages
ln -s $(relative %{_localstatedir}/jython/cachedir %{_datadir}/jython/) $RPM_BUILD_ROOT%{_datadir}/jython/

%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}                     
%add_to_maven_depmap org.python %{name} %{version} JPP %{name}                  

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cat > $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom <<'EOF'
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>jython</groupId>
  <artifactId>jython</artifactId>
  <version>%version</version>

  <distributionManagement>
    <relocation>
      <groupId>org.python</groupId>
    </relocation>
  </distributionManagement>

</project>
EOF

%post 

echo "creating jython cache..."
echo | /usr/bin/jython ||:

%preun
# cleanup
if [ "$1" -eq 0 ]
then
    rm %{_localstatedir}/jython/cachedir/packages/*.{pkc,idx}
    find /usr/share/jython/Lib -name "*py.class" -delete
fi || :


%files
%doc ACKNOWLEDGMENTS NEWS LICENSE.txt README.txt
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}c
%{_javadir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Lib
%{_datadir}/%{name}/Tools
%{_datadir}/%{name}/registry
%config(noreplace,missingok) /etc/jython.conf

%{_localstatedir}/jython
# is it worth ghosting?
#%ghost %{_localstatedir}/jython/cachedir/packages
%{_datadir}/jython/cachedir
# pom
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%files manual
%doc LICENSE.txt README.txt
%doc %{name}-manual-%{version}

%files demo
%doc ACKNOWLEDGMENTS NEWS LICENSE.txt README.txt
%doc %{_datadir}/%{name}/Demo

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_8jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_7jpp6
- update to new release by jppimport

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_0.1.Release_2_2_1.1.2jpp5
- really added pom

* Sat Jan 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt4_0.1.Release_2_2_1.1.2jpp5
- restored pom

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt3_0.1.Release_2_2_1.1.2jpp5
- fix for missing /proc

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_2.1jpp5
- raised epoch: to 0 (alt rpm quirk)

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_0.1.Release_2_2_1.1.2jpp5
- converted from JPackage by jppimport script

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_0.rc2.1jpp5
- fixed build w/java5; 
- python cache creation is now optional

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_0.rc2.1jpp1.7
- rebuild with mysql-connector-java

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_0.rc2.1jpp1.7
- added cleanup of *py.class in %%postun

* Fri Nov 16 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_0.rc2.1jpp1.7
- added processing jars in %%post

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_0.rc2.1jpp1.7
- converted from JPackage by jppimport script

