BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		taggle
Version:	1.0
Release:	alt2_3jpp7
Summary:	An online french word game

Group:		Games/Other
License:	GPLv3+
URL:		http://www.inouire.net/baggle/
Source0:	http://www.inouire.net/fedora/baggle_%{version}_src.tar.gz
Source1:	%{name}.sh
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	%{name}-server.sh

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	desktop-file-utils

Requires:	jpackage-utils
Source44: import.info

%description
Taggle is an online french word game that lets you play
against your friends. Letters are displayed at random
in a grid and players attempt to find words in sequence
of adjacent letters

%package server
Summary:	Server for %{name}
Group:		Games/Other
Requires:	jpackage-utils

%description server
The server for the taggle game

%prep
%setup -q -n baggle_%{version}_src

%build
# for legal reason, entirely rename the software
find . -name \*.java | xargs sed -i s/B@ggle/T@ggle/g
find . -name \*.java | xargs sed -i s/b@ggle/t@ggle/g

# Build client
cd baggle_client_%{version}_src
mkdir -p classes/META-INF
javac -encoding utf-8 -d classes boggleclient/Main.java
cp -R icons classes
# fix the class-path-in-manifest rpmlint issue
sed -i '/class-path/I d' MANIFEST.MF
cp MANIFEST.MF classes/META-INF
cd classes
jar cmvf META-INF/MANIFEST.MF %{name}.jar boggleclient/ GUI/ icons/ Thread/
cd ..
mv classes/%{name}.jar ..

# Build server
cd ../baggle_server_%{version}_src
mkdir -p classes/META-INF
javac -encoding utf-8 -d classes boggleserver/Main.java
sed -i '/class-path/I d' MANIFEST.MF
cp MANIFEST.MF classes/META-INF
cp Dico/dico.txt classes/Dico
cd classes
jar cvmf META-INF/MANIFEST.MF %{name}_server.jar boggleserver/ boggle/ Dico/
cd ..
mv classes/%{name}_server.jar ..


%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_bindir}
install -D -p %{name}.jar %{buildroot}%{_javadir}
install -D -p -m 0755 %{S:1} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{S:3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications	%{S:2}

install -D -p %{name}_server.jar %{buildroot}%{_javadir}/%{name}-server.jar
install -D -p -m 0755 %{S:4} %{buildroot}%{_bindir}/%{name}-server

%files
%doc baggle_client_%{version}_src/COPYING
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files server
%doc baggle_server_%{version}_src/COPYING
%{_javadir}/%{name}-server.jar
%{_bindir}/%{name}-server

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_3jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_2jpp6
- update to new release by jppimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp6
- import by jppimport

