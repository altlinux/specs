# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Work around koji build issues on ppc64
# See https://www.redhat.com/archives/fedora-devel-list/2009-March/msg00022.html
%global libreoffice_dir $(ls -d /usr/lib*/libreoffice)

Name:           jabref
Version:        2.9.2
Release:        alt1_1jpp7
Summary:        Graphical frontend to manage BibTeX bibliographical databases
License:        GPLv2+ and BSD
Group:          Publishing
Url:            http://jabref.sourceforge.net/

BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/%{name}/JabRef-%{version}-src.tar.bz2
Source1:        jabref.desktop
# Adapted from the man page included in the Debian jabref package
Source2:        jabref.1

# point to system jars; use correct encoding for javadocs
Patch0:  %{name}-%{version}-build_xml.patch
# Remove all uses of "SPL"
Patch1:  %{name}-2.8b-remove-spl.patch
# Don't try to integrate into Ubuntu menus
Patch2:  %{name}-2.9-ayatana.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant

BuildRequires:  antlr3-java
BuildRequires:  antlr3-tool
BuildRequires:  antlr-tool
BuildRequires:  apache-commons-logging
BuildRequires:  glazedlists
BuildRequires:  jempbox
BuildRequires:  jgoodies-forms >= 1.6.0
BuildRequires:  jgoodies-looks >= 2.5.0
BuildRequires:  jpf
BuildRequires:  jpfcodegen
BuildRequires:  libreoffice >= 3.5.2
BuildRequires:  microba
BuildRequires:  pdfbox
BuildRequires:  ritopt
BuildRequires:  spin
BuildRequires:  stringtemplate4
BuildRequires:  velocity
BuildRequires:  desktop-file-utils


Requires:       jpackage-utils

Requires:       antlr3-java
Requires:       antlr3-tool
Requires:       antlr-tool
Requires:       apache-commons-logging
Requires:       glazedlists
Requires:       jempbox
Requires:       jgoodies-forms >= 1.6.0
Requires:       jgoodies-looks >= 2.5.0
Requires:       jpf
Requires:       jpfcodegen
Requires:       microba
Requires:       pdfbox
Requires:       ritopt
Requires:       spin

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Source44: import.info

%description
JabRef is a graphical front-end to manage BibTeX databases, the standard
LaTeX bibliography reference format. JabRef is build to be platform
independent (requires Java >= 1.4.2). It merges and extends the
functionalities of BibKeeper (Morten O. Alver) and JBibtexManager (Nizar
Batada).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %%{name}.

%prep
%setup -q

# Clean up the build
%patch0 -p1

# Remove bundled "ritopt" package and clean up the source
rm -rf src/java/gnu

# Remove "sciplore" client
rm -rf src/java/net/sf/jabref/spl src/java/spl
%patch1 -p1

# Don't try to integrate into Ubuntu menus
%patch2 -p1

# Fix one file permission
chmod a-x src/txt/gpl2.txt

# Remove all pre-built jar files
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;


%build
# Use system jars
export CLASSPATH=$(build-classpath antlr antlr3 antlr3-runtime apache-commons-logging glazedlists jempbox jgoodies-common jgoodies-forms jgoodies-looks jpf jpf-boot jpfcodegen microba pdfbox ritopt spin velocity)
# Libreoffice jars (build dependency only)
export CLASSPATH=$CLASSPATH:%{libreoffice_dir}/program/classes/unoil.jar
export CLASSPATH=$CLASSPATH:%{libreoffice_dir}/ure/share/java/ridl.jar
export CLASSPATH=$CLASSPATH:%{libreoffice_dir}/ure/share/java/juh.jar
export CLASSPATH=$CLASSPATH:%{libreoffice_dir}/ure/share/java/jurt.jar
ant jars docs

%install
# Install Java stuff
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 build/lib/JabRef-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Javadoc
install -d -m 755 p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r build/docs/API/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install desktop file, icon, man page, and shell script
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps/
cp -p src/images/JabRef-icon-48.png \
        ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps/jabref.png
desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
        %{SOURCE1}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1
%jpackage_script net.sf.jabref.JabRefMain "" "" antlr:antlr3:antlr3-runtime:apache-commons-logging:glazedlists:jempbox:jgoodies-common:jgoodies-forms:jgoodies-looks:jpf:jpf-boot:jpfcodegen-rt:microba:pdfbox:ritopt:spin:jabref jabref true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf


%files
%doc src/txt/CHANGELOG src/txt/README src/txt/TODO src/txt/*.txt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1.gz
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%doc src/txt/gpl*.txt
%{_javadocdir}/%{name}

%changelog
* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.9.2-alt1_1jpp7
- new version

