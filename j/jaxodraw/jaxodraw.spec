# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global major 2.0
%global minor 1

Name:		jaxodraw
Version:	%{major}.%{minor}
Release:	alt1_12jpp7
Summary:	A Java program for drawing Feynman diagrams
Group:		Engineering
License:	GPLv2+
URL:		http://jaxodraw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{major}-%{minor}_src.tar.gz
# LaTeX file for exporting figures
Source1:	http://downloads.sourceforge.net/%{name}/axodraw4j_2008_11_19.tar.gz
# Desktop file, icon and man page
Source2:	http://downloads.sourceforge.net/%{name}/installer-%{major}-%{minor}.tar.gz
# Wrapper skeleton
Source3:	jaxodraw.sh

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	desktop-file-utils
# java-devel, we need at least 1.6.0
BuildRequires:	jpackage-utils
# Unit testing capabilities
BuildRequires:	ant-junit

Requires:	jpackage-utils
Source44: import.info

%description
JaxoDraw is a Java program for drawing Feynman diagrams. It has a complete
graphical user interface that allows to carry out all actions in a mouse
click-and-drag fashion. Fine-tuning of the diagrams is also possible through
keyboard entries. Graphs may be exported to (encapsulated) postscript and can
be saved in XML files to be used in later sessions.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package latex
Summary:	LaTeX style file axodraw4j.sty for documents generated with jaxodraw
Group:		Engineering
License:	LPPL
# In order to compile documents one needs a LaTeX compiler
Requires: /usr/bin/latex texlive-latex-recommended

%description latex
This package contains the LaTeX style file that is needed for EPS export
functionality in jaxodraw.

You need this if you want the export to EPS function to work or if you want to
compile LaTeX files generated with jaxodraw.

%prep
%setup -q -n JaxoDraw-%{major}-%{minor} -a 1 -a 2
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Convert documentation encoding
for file in src/doc/{TODO,CHANGELOG,README,BUGS} src/doc/legal/{GNU-,}LICENSE; do
 sed 's/\r//' $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

# Create invocation script
sed "s|JARFILE|%{_javadir}/%{name}.jar|g" %{SOURCE3} > %{name}
touch -r %{SOURCE3} %{name}

%build
ant jar javadoc

%install
# Install jar file
install -D -p -m 644 build/%{name}-%{major}-%{minor}.jar %{buildroot}%{_javadir}/%{name}.jar
# Install invocation script
install -D -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}

# Desktop file and icon
desktop-file-install --dir=%{buildroot}%{_datadir}/applications installer-%{major}-%{minor}/OS/Linux/%{name}.desktop
install -D -p -m 644 installer-%{major}-%{minor}/OS/Linux/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
# Man page
install -D -p -m 644 installer-%{major}-%{minor}/OS/Linux/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# LaTeX style
install -D -p -m 644 axodraw4j.sty %{buildroot}%{_datadir}/texmf/tex/latex/axodraw4j/axodraw4j.sty

%check
# Unit tests fail with Open JDK
#ant test

%files
%doc src/doc/* axodraw4j-summary.txt
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%files javadoc
%{_javadocdir}/%{name}/

%files latex
%{_datadir}/texmf/tex/latex/axodraw4j/

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_12jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_11jpp7
- new version

