Name: dbeaver
Version: 21.1.4
Release: alt1

Summary: Universal Database Manager
Summary(ru_RU.UTF-8): Универсальный менеджер баз данных
License: Apache-2.0
Group: Databases

URL: https://%name.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64 ppc64le

# https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.desktop
Source2: maven-local-repository.tar

Patch0: %name-alt-arch.patch
Patch1: %name-alt-autoupdate.patch

BuildRequires: /proc
BuildRequires: java-11-openjdk-headless
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-testng
BuildRequires: rpm-build-java
BuildRequires: xmvn-install
BuildRequires: xmvn-minimal
BuildRequires: xmvn-mojo
BuildRequires: xmvn-resolve
BuildRequires: xmvn-subst

Requires: java-11-openjdk-headless

%description
DBeaver is free and open source universal database tool for developers and database administrators.

*  Usability is the main goal of this project, program UI is carefully designed and implemented.
*  It is free and open-source (ASL).
*  It is multiplatform.
*  It is based on opensource framework and allows writing of various extensions (plugins).
*  It supports any database having a JDBC driver.
*  It may handle any external datasource which may or may not have a JDBC driver.
*  There is a set of plugins for different databases and different database management utilities (e.g. ERD, data transfer, compare, data export/import, mock data generation, etc).
*  It has a great number of features.

%prep
%setup -b 2
%patch0 -p1
%patch1 -p1

%__rm -rf ~/.m2
%__mv -Tf ../.m2 ~/.m2

%build
xmvn --batch-mode --offline package

%install
# Create  directories
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_libexecdir
%__mkdir_p %buildroot%_pixmapsdir

# Install icons into /usr/share/icons/hicolor
for _size in 16 32 48 64 128 256 512
do
	%__install -Dp -m 0644 product/community/icons-sources/icon_${_size}x${_size}.png %buildroot%_iconsdir/hicolor/${_size}x${_size}/apps/%name.png
done

# Move into the target directory
%__cp -r product/community/target/products/org.jkiss.dbeaver.core.product/linux/gtk/%_arch/%name %buildroot%_libexecdir

# Move shared data to /usr/share/dbeaver
for _file in  .eclipseproduct artifacts.xml configuration dbeaver.ini licenses readme.txt
do
	%__mv %buildroot%_libexecdir/%name/${_file} %buildroot%_datadir/%name
	%__ln_s ../../..%_datadir/%name/${_file} %buildroot%_libexecdir/%name/
done

%ifarch x86_64
%__rm %buildroot%_libexecdir/%name/%name.png
%endif

# Install icons into /usr/share/pixmaps
%__mv %buildroot%_libexecdir/%name/icon.xpm %buildroot%_pixmapsdir/%name.xpm

# Install executable script into /usr/bin
%__ln_s ../..%_libexecdir/%name/%name %buildroot%_bindir/%name

# Install application launcher into /usr/share/applications
%__install -Dp -m 0755 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%config %_datadir/%name/%name.ini
%_iconsdir/hicolor/*/apps/%name.png
%_libexecdir/%name
%_pixmapsdir/%name.xpm

%changelog
* Wed Aug 04 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.4-alt1
- Version 21.1.4

* Mon Jul 19 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.3-alt1
- Version 21.1.3

* Wed Jul 14 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.2-alt1
- Version 21.1.2

* Mon Jun 21 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.1-alt1
- Version 21.1.1

* Mon May 31 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.0-alt1
- Version 21.1.0

* Thu May 20 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.5-alt1
- Version 21.0.5

* Mon May 03 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.4-alt1
- Version 21.0.4

* Sun Apr 18 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.3-alt1
- Version 21.0.3

* Mon Apr 05 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.2-alt1
- Version 21.0.2

* Thu Mar 25 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt3
- Reduce maven local repository

* Mon Mar 22 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt2
- Improved build
- Disable auto update check by default

* Mon Mar 22 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt1
- Version 21.0.1

* Thu Mar 04 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt3
- Build on ppc64le

* Mon Mar 01 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt2
- Build on AArch64

* Sun Feb 28 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt1
- Version 21.0.0

* Fri Feb 26 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt3
- Add requires on java-openjdk-headless

* Thu Feb 25 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt2
- Build with maven

* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt1
- Initial build for ALT Linux
