%define _unpackaged_files_terminate_build 1
%def_with check

Name: skinlf
Version: 6.7
Release: alt4

Summary: Skinning library for Java Swing applications
License: Apache-2.0 AND Zlib AND Apache-1.1
Group: Development/Java
Url: https://sourceforge.net/projects/skinlf/
BuildArch: noarch

Source: %name-%version.tar
Source1: SkinLFSmokeTest.java
Patch0: %name-%version-imageio.patch
Patch1: %name-%version-build.patch
Patch2: %name-%version-common.patch
Patch3: %name-%version-jdk-xpath.patch

BuildRequires(pre): rpm-build-java
BuildRequires: ant dos2unix java-1.8.0-devel laf-plugin

%description
Skin Look And Feel (SkinLF) is a skinning library for Java Swing
applications. It reads image-based GTK and KDE themes to customize
buttons, menus, scrollbars, tables, internal frames and other widgets.

%prep
%setup -q
%autopatch -p1

dos2unix LICENSE LICENSE_nanoxml

%build
ant
jar cf skinlf-%version.jar -C build/classes . \
    -C src com/l2fprod/gui/plaf/skin/resources

%install
install -Dm644 skinlf-%version.jar %buildroot%_javadir/skinlf-%version.jar
ln -s skinlf-%version.jar %buildroot%_javadir/skinlf.jar

%check
mkdir -p build/test-classes
javac -cp %buildroot%_javadir/skinlf-%version.jar \
    -d build/test-classes %SOURCE1
java -Djava.awt.headless=true \
    -cp build/test-classes:%buildroot%_javadir/skinlf-%version.jar:%_javadir/laf-plugin.jar \
    SkinLFSmokeTest lib/themepack.zip

%files
%doc LICENSE LICENSE_nanoxml
%_javadir/skinlf.jar
%_javadir/skinlf-%version.jar

%changelog
* Sat Nov 14 2026 Ajrat Makhmutov <rauty@altlinux.org> 6.7-alt4
- Fix FTBFS: remove the obsolete ant-nodeps build dependency.
- Remove prebuilt JARs and the Windows DLL from the source tree.
- Include resource bundles required for look-and-feel initialization.
- Add a headless smoke test for the packaged library.
- Spec cleanup.

* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 6.7-alt3.1
- NMU: java11 support

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.7-alt3
- Removed obsolete dos2unix options
- Updated build dependencies

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 6.7-alt2
- Fix BuildRequires (ALT #21520)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 6.7-alt1
- Initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

*Sat Dec 06 2008  <mycae(a!t)yahoo.com> 6.7-6
- Fixed jar dir
- Changed primary jar to name-version.jar, & linked.
- Added clean tarball generator

* Wed Dec 03 2008  <mycae(a!t)yahoo.com> 6.7-5
- Added LICENSE_nanoxml
- Updated licence spec line to include ASL 1.1 & zlib
- removed Clock.java due to incompatible license

* Sat Nov 29 2008 <mycae(a!t)yahoo.com> 6.7-4
- Updated BuildRequires to inlcude laf-plugin
- Silence several rpmlint errors
	- ASL 2.0 vs Apache Source Licence 2.0
	- Fix arch
	- Fix EOL on docs.

* Sun Nov 23 2008 <mycae(a!t)yahoo.com> 6.7-3
- Modify description field

* Sun Nov 16 2008 <mycae(a!t)yahoo.com> 6.7-2
- Fix version numbering
- Fix top level dir when building jar

* Sat Nov 01 2008 <mycae(a!t)yahoo.com> 6.7-1
- Create spec file
