Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/pkg-config pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-file-manager-image-converter
Version:        1.6.0
Release:        alt1_1
Summary:        MATE file manager image converter
License:        GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  mate-file-manager-devel
BuildRequires:  mate-doc-utils
Requires:  mate-file-manager-extensions
Requires:  ImageMagick
Source44: import.info

%description
Caja-Image-Converter extension allows you to resize/rotate images from Caja.

%prep
%setup -q
%build

NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
%find_lang %{name} --all-name
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-image-converter

%changelog
* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

