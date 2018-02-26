Name: laf-plugin
Version: 1.0
Release: alt2
Summary: Generic plugin framework for Java look-and-feels

Group: Development/Java
License: BSD and zlib
Url: https://laf-plugin.dev.java.net/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: https://laf-plugin.dev.java.net/files/documents/4261/50297/%name-all.tar
Source1: %name-build.xml
BuildArch: noarch

BuildRequires: ant rpm-build-java asm2

%description
The goal of this project is to provide a generic plugin framework for
look-and-feels and define the interface of a common kind of plugins -
the component plugins.

%prep
%setup -q -c %name-%version
cp %SOURCE1 build.xml
rm -rf drop/*

%build
%ant all

%install

install -m644 drop/%name-50.jar -D %buildroot%_javadir/%name.jar

%files
%_javadir/%name.jar

%changelog
* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2
- Fix BuildRequires (ALT #21519)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- Initial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 16 2008 <mycae(a!t)yahoo.com> 1.0-4
- Fix changelog version numbering to (programver-specver)
- Change "ZLIB" to "zlib"

* Sun Nov 16 2008 <mycae(a!t)yahoo.com> 1.0-3
- Remove doc macro, fix licence to include zlib.
- Bump up version, due to maintainer change.

* Sat Nov 01 2008 <mycae(a!t)yahoo.com> 1.0-2
- "Touch" build, as S. Wesp marked bug 461407 as (WONTFIX),
   I can maintain package as required.

* Sun Sep 07 2008 Simon Wesp <cassmodiah@fedoraproject.org> 1.0-1
- Initial Release
