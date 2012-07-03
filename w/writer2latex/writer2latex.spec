Name: writer2latex
Version: 1.1.5
Release: alt2

Summary: Flexible tool to convert OpenOffice documents into LaTeX2e and XHTML formats
License: LGPL
Group: Development/Java
Url: http://writer2latex.sourceforge.net/
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): /proc rpm-build-java rpm-build-texmf
# Automatically added by buildreq on Sat Jun 09 2007
BuildRequires: ant junit libreoffice xml-commons-resolver12

Requires: java

BuildArch: noarch

%description
Writer2LaTeX is a flexible tool to convert documents in OpenDocument format
(OpenOffice.org or LibreOffice) into LaTeX2e and XHTML.
It is written in Java.

You can use Writer2LaTeX
 
 * ...as a command line utility, independent of OpenOffice.org.
 * ...as an export filter for OpenOffice.org/LibreOffice/NeoOffice.
 * ...from another java program.

The current version is usable for short and medium-sized documents, but lacks a
few features for very long documents, see the feature list.

NOTE that stable version of Writer2LaTeX as an export filter is already included into 
OpenOffice.org package. This package provides command-line interface to writer2latex,
standard and sample config files for tuning output and documentation.

#%package javadoc
#Summary: Javadoc for %name
#Group: Development/Documentation
#Requires: java-common

#%description javadoc
#Javadoc for %name.

%prep
%setup -q -n %name-%version
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.zip" -exec rm -f {} \;
# we have to use precompiled .class files due to OOo SDK unavailability
#find . -name "*.class" -exec rm -f {} \;

%build
export CLASSPATH=$(build-classpath junit) 

%ant \
           -DURE_CLASSES %_libdir/libreoffice/ure/share/java \
           -DOFFICE_CLASSES=%_libdir/libreoffice/basis3.4/program/classes \
	jar

sed -i 's,^W2LPATH=.*,W2LPATH=%_javadir,' source/distro/w2l

#build docs
java -jar target/lib/%name.jar -xhtml source/distro/doc/user-manual.odt

%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 target/lib/%name.jar %buildroot%_javadir
# data
install -d -m 755 %buildroot%_datadir/%name
install -m 644 source/distro/xslt/*.xsl %buildroot%_datadir/%name
install -m 644 source/java/writer2latex/latex/config/*.xml %buildroot%_datadir/%name

# wrapper script
install -d -m 755 %buildroot%_bindir
install -m 755 source/distro/w2l %buildroot%_bindir

# texmf stuff
install -d -m 755 %buildroot%_texmfmain/tex/latex/%name
install -m 644 source/distro/latex/*.sty source/distro/latex/obsolete/*.sty %buildroot%_texmfmain/tex/latex/%name

# javadoc
#%__install -d -m 755 %buildroot%_javadocdir/%name
#%__cp -pr target/docs/api/* %buildroot%_javadocdir/%name
#%__rm -rf target/docs/api

%files
%doc source/distro/{doc/*,samples,*.txt}
%_javadir/%name.jar
%_datadir/%name
%_bindir/w2l
%_texmfmain/tex/latex/%name

#%files javadoc
#%doc %_javadocdir/%name

%changelog
* Tue Nov 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.1.5-alt2
- rebuilt with libreoffice

* Thu Jan 20 2011 Kirill Maslinsky <kirill@altlinux.org> 1.1.5-alt1.20110120
- 1.1.5 + scm 20110120

* Thu Jan 20 2011 Kirill Maslinsky <kirill@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Mar 02 2010 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt3
- rebuilt with OpenOffice 3.2

* Tue Oct 13 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt2
- 1.0 final

* Wed May 20 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1.beta3
- 1.0beta3
  + require java rather than java-common
  + place .sty files into texmf tree

* Mon Oct 06 2008 Kirill Maslinsky <kirill@altlinux.org> 0.5.fix02-alt2
- fixed build
  + java paths adjusted to jar relocations in openoffice.org 3.0

* Thu Sep 18 2008 Kirill Maslinsky <kirill@altlinux.org> 0.5.fix02-alt1
- version up (0.5 -> 0.5.0.2)
  + this is an upstream bugfix release
  + fixed build

* Tue Dec 25 2007 Kirill Maslinsky <kirill@altlinux.org> 0.5final-alt1
- final 0.5 release
	several bugfixes since beta3, see changelog05.txt for details

* Wed Sep 12 2007 Kirill Maslinsky <kirill@altlinux.org> 0.5beta3-alt1
- new beta(3) release, mostly bugfix
	see changelog05.txt for information on upstream changes
- minor packaging fixes:
	+ drop workaround (buildig with 1.4 java), fixed upstream
	+ package more documentation


* Wed Jun 27 2007 Kirill Maslinsky <kirill@altlinux.ru> 0.5b-alt2
- fixed macro that was left unsubstituted in w2l

* Sat Jun 09 2007 Kirill Maslinsky <kirill@altlinux.ru> 0.5b-alt1
- Initial build for Sisyphus
- Build options
  + quick and dirty
  + used javac -source 1.4 (due to 'enum' usage that is keyword in java >= 1.5)
  + build only .jar, no javadoc and OOo filter package

