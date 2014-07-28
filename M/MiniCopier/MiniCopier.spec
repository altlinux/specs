# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		MiniCopier
Version:	0.5
Release:	alt1_6jpp7
Summary:	Graphical copy manager
Group:		File tools
License:	GPLv2+
URL:		http://www.adriancourreges.com/projects/minicopier/
Source0:	http://www.adriancourreges.com/projects/minicopier/releases/%{name}-source.tar
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	desktop-file-utils
BuildRequires:	PgsLookAndFeel

Requires:	jpackage-utils
Requires:	PgsLookAndFeel

Source1:	MiniCopier.desktop

#Patch0: remove classpath from manifest
Patch0:		%{name}-Manifest.txt.patch
#Patch1: change configuration file path to ~/.MiniCopier
Patch1:		%{name}-Configuration.java.patch
#Patch2: fix startup directory
Patch2:		%{name}-MiniCopier.sh.patch
#Patch3: start the application with native GTK LookAndFeel by default
Patch3:		%{name}-configuration.ini.patch
#Patch4: start the application centered on the screen
Patch4:		%{name}-MainFrame.java.patch
#Patch5: fix the lib directory path where the jar required for the build is expected to be
Patch5:		%{name}-build.xml.patch
#Patch6: fix the encoding of javadocs
Patch6: 	%{name}-javadoc-encoding.patch
Source44: import.info

%description
MiniCopier is a graphical copy manager. It provides more comfort and control
over files copy operations, than basic OS functions.

Features

    * processing of the transfers one after the other
    * add new tranfers to the queue while a copy is already being processed
    * dynamic management of the queue of remaining transfers
    * pause a copy
    * skip current transfer to proceed to the next one
    * resume a copy at the exact point where it failed (no need to start over)
    * choose another name for the target if a file already exists
    * can follow or ignore symbolic links (Unix systems only)
    * set a default behaviour if target file already exists
    * storage of the failed transfers into a list

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch:	noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n Minicopier-%{version}(sources)
%ant clean
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%ant jar doc

%install
install -D -p -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -rf -p javadoc/* %{buildroot}%{_javadocdir}/%{name}
install -D -p -m 644 class/img/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}

desktop-file-install					\
--dir=%{buildroot}%{_datadir}/applications		\
%{SOURCE1}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_javadir}/%{name}.jar

%files javadoc
%doc README
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_6jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_5jpp7
- new version

