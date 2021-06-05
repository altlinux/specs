Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           java-wakeonlan
Version:        1.0.0
Release:        alt1_17jpp11
Summary:        Wake On Lan client and java library

License:        LGPLv2
URL:            http://www.moldaner.de/wakeonlan
BuildArch:      noarch
Source0:        %{url}/download/wakeonlan-%{version}.zip

                # Build configuration, no need to upstream.
Patch1:         0001-Update-target-and-source-to-1.5.patch
		# Will upstream
Patch2:         0002-Adding-Swedish-and-Italian-translations.patch


BuildRequires:  ant-junit
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick-tools
BuildRequires:  java-javadoc
BuildRequires:  javapackages-local
BuildRequires:  jpackage-utils
BuildRequires:  jsap

Requires:       jsap
# Explicit requires for javapackages-tools since wakeonlan script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info


%description
wakeonlan is a small OS independent java program that sends 'magic packets'
to wake-on-lan enabled ethernet adapters and motherboards in order to switch
on the called machine. It runs on any machine with an installed 1.4+ java
runtime.

wakeonlan can be used by command line or by a graphical user interface. You
can use wakeonlan as a java library too. It provides a utility class to wake
up remote machines. See wakeonlan javadoc for more information.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc API documentation for %{name}.


%prep
%setup -qn wakeonlan-%{version}
%patch1  -p1
%patch2  -p1
find \( -name '*.jar' -o -name '*.class' \) -delete
sed -i '/class-path/I d' etc/META_INF/METAINF.MF
cd lib
ln -s $(build-classpath jsap)  .
ln -s $(build-classpath junit)  .


%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  deploy javadoc

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=wakeonlan
GenericName=%{name}
Comment=A wake on lan client
Exec=wakeonlan
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;
EOF


%check
ant test


%install
rm -f %{buildroot}%{_bindir}/wakeonlan
%jpackage_script wol.WakeOnLan "" ""  jsap:java-wakeonlan wakeonlan

mv deploy/doc/javadoc .
%mvn_artifact de.moldaner:wakeonlan:%{version} deploy/wakeonlan.jar
%mvn_install -J javadoc

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
convert etc/javaws/wakeonlan64x64.gif -geometry 64x64 \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

desktop-file-install --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop



%files -f .mfiles
%dir %{_datadir}/java/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}*
%doc --no-dereference deploy/doc/COPYING
%doc deploy/doc/README
%{_bindir}/wakeonlan

%files  -f .mfiles-javadoc javadoc
%doc --no-dereference doc/COPYING


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.0.0-alt1_17jpp11
- new version

