%define _unpackaged_files_terminate_build 1

Name: OmniGraph
Version: 0.1.1
Release: alt2

Summary: A multiplatform desktop application that lets you build graphs
License: MIT
Group: Sciences/Mathematics
Url: https://github.com/Todense/OmniGraph
Vcs: https://github.com/Todense/OmniGraph.git
# JavaFX v17+ doesn't support arch i586.
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: omnigraph.png

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java-osgi
BuildRequires: maven-local
BuildRequires: /proc
BuildRequires: java-21-openjdk-devel

%description
A multiplatform desktop application that lets you build
graphs and visualize a collection of algorithms.
Build in JavaFX.

%prep
%setup -a1
%pom_xpath_inject pom:build/pom:plugins \
    '<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-resources-plugin</artifactId><version>2.6</version></plugin><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-jar-plugin</artifactId><version>2.4</version></plugin><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-install-plugin</artifactId><version>2.4</version></plugin>'

%build
export MAVEN_REPO_LOCAL=".m2/repository"

mvn install \
  -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
  -Dmaven.compiler.source=11 \
  -Dmaven.compiler.target=11 \
  --offline \
  #

%install
mkdir -pv \
  %buildroot/%_desktopdir \
  %buildroot/%_bindir \
  #

cat > %buildroot/%_desktopdir/omnigraph.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=OmniGraph
Exec=omnigraph
Icon=%_iconsdir/hicolor/64x64/apps/omnigraph.png
Categories=Science;
EOF

cat > %buildroot/%_bindir/omnigraph << 'EOF'
#!/bin/sh
exec java -jar %_javadir/OmniGraph/OmniGraph.jar "\$@"
EOF

install -Dm 644 \
  .m2/repository/groupId/OmniGraph-master/1.0-SNAPSHOT/OmniGraph-master-1.0-SNAPSHOT.jar \
  %buildroot/%_javadir/OmniGraph/OmniGraph.jar

install -Dm 644 %SOURCE2 \
  -t %buildroot/%_iconsdir/hicolor/64x64/apps/

%files
%doc README.md LICENSE
%attr(755,root,root) %_bindir/omnigraph
%_desktopdir/omnigraph.desktop
%_iconsdir/hicolor/64x64/apps/omnigraph.png
%_javadir/OmniGraph/OmniGraph.jar

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 0.1.1-alt2
- Fix FTBFS: Pin the bundled offline lifecycle plugins.

* Sun May 11 2025 Ivan Hanas <xeno@altlinux.org> 0.1.1-alt1
- Initial Build For Alt Linux Sisyphus.
