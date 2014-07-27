BuildRequires: junit3
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           mars-sim
Version:        2.84
Release:        alt2_9jpp7
Summary:        Mars Simulation Project

Group:          Games/Other
License:        GPLv2+
URL:            http://mars-sim.sourceforge.net/
# The upstream tarball contains (useless) MPEG decoder binaries:
# http://download.sourceforge.net/mars-sim/MarsProject_%{version}.tar.gz
# Download the above tarball and strip it as follows:
# sh mars-sim-strip.sh MarsProject_2.84.tar.gz
Source0:        MarsProject_2.84-fedora.tar.gz
Source1:        mars-sim-strip.sh
Source2:        mars-sim
Source3:        mars-sim.png
Source4:        mars-sim.desktop
Patch0:         mars-sim-2.84-jfreegraph.patch
Patch1:         mars-sim-2.84-manifest.patch
Patch2:         mars-sim-2.84-paths.patch
Patch3:         mars-sim-2.84-java15.patch

Requires:       log4j apache-commons-collections jfreechart jcommon plexus-graph jpackage-utils
BuildRequires:  %{requires} ant ant-junit xerces-j2 >= 1.5 desktop-file-utils
BuildRequires:  java-devel-openjdk >= 1.5
BuildArch:      noarch
Source44: import.info

%description
The Mars Simulation Project is a free software Java project to create a
simulation of future human settlement of Mars.

The simulation is a multi-agent artificial society set in a detailed
virtual world.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1 -b .jfreegraph
%patch1 -p1 -b .manifest
%patch2 -p1 -b .paths
%patch3 -p1 -b .java15

# This is so that I can tap enter on a jar in mc to see manifest :)
find . -type f |xargs chmod -x


%build
# Remove prebuilt stuff -- map jar is not built
find \( -name '*.jar' -o -name '*.zip' \) \
        \! -name 'map_data.jar' -exec rm -f '{}' \;

# Encodings
for F in docs/*.txt
do
        # credits.txt has Mac line endings, other have PC
        sed 's/\r$//g;s/\r/\n/g' $F |
                iconv -f ISO-8859-1 -t UTF-8 >$F.conv
        touch -r $F $F.conv
        mv $F.conv $F
done

# Switch to native look and feel by default
# This can not be easily patched, as the file does not contain line breaks,
# and a xml editing tool would probably be an overkill
sed 's/look-and-feel="default"/look-and-feel="native"/' saved/ui_settings.xml >saved/ui_settings.xml.native
touch -r saved/ui_settings.xml saved/ui_settings.xml.native
mv saved/ui_settings.xml.native saved/ui_settings.xml

# Build classes and documentation
cd scripts
ant build document


%install

# Directory structure
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_javadir}/mars-sim
install -d $RPM_BUILD_ROOT%{_datadir}/mars-sim
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install JARs and version them
install -m 644 jars/*.jar *.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
(cd $RPM_BUILD_ROOT%{_javadir}/%{name}; for F in *.jar; do
        V=$(echo $F |sed 's/\.jar$/-%{version}.jar/')
        mv $F $V
        ln -s $V $F
done)

# JavaDoc and data files
cp -rp docs/help images sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp conf saved $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp docs/javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Executable
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/mars-sim

# Menu entry and icon
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/mars-sim.png
desktop-file-install --vendor=Fedora %{SOURCE4}         \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications

mkdir -p $RPM_BUILD_ROOT`dirname /etc/mars-sim.conf`
touch $RPM_BUILD_ROOT/etc/mars-sim.conf


%files
%{_javadir}/mars-sim
%{_datadir}/mars-sim
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_bindir}/mars-sim
%doc docs/configuration.txt docs/credits.txt
%doc docs/GPL_License.txt
%config(noreplace,missingok) /etc/mars-sim.conf
 

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.84-alt2_9jpp7
- fixed build

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2.84-alt1_9jpp7
- new version

