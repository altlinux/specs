%define optflags_lto %nil

Name: chafa
Version: 1.10.3
Release: alt1
%global sum     Image-to-text converter for terminal
Summary: %sum
License: LGPLv3+
Group: Graphics
Url: https://hpjansson.org/chafa/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/hpjansson/%name/releases/download/%version/%name-%version.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: ImageMagick-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: libfreetype-devel

Requires: %name-libs = %version-%release

%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

It is highly configurable, with support for alpha transparency and multiple
color modes and color spaces, combining a range of Unicode characters for
optimal output.

%package libs
Summary: %sum (library)
Group: Graphics
# Version in libnsgif/README-chafa
Provides: bundled(libnsgif) = 0.2.1-chafa
# Version in lodepng/lodepng.h
Provides: bundled(lodepng) = 20220109

%description libs
Shared library for %name.

%package static
Summary: %sum (static library)
Group: Development/C
%description static
Static library for %name.

%package devel
Summary: %sum (development files)
Requires: %name-libs%{?_isa} = %version-%release
Group: Development/C
%description devel
Development files for %name, such as headers.

%package doc
Summary: %sum (documentation)
Group: Development/Documentation
#Recommends:     %name-devel

%description doc
Documentation for %name, such as headers.

%prep
%setup

%build
autoreconf -ivf
%configure --disable-rpath
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.LESSER README* NEWS
%doc COPYING.LESSER
%_bindir/%name
%_man1dir/%name.1*

%files libs
%doc AUTHORS
%doc COPYING.LESSER
%_libdir/lib%name.so.0
%_libdir/lib%name.so.0.7.1

%files static
%doc AUTHORS
%doc COPYING.LESSER
%_libdir/lib%name.a

%files devel
%doc AUTHORS
%doc COPYING.LESSER
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so
%_libdir/%name/include/chafaconfig.h

%files doc
%doc AUTHORS
%doc COPYING.LESSER
%doc %_datadir/gtk-doc/html/%name

%changelog
* Thu Mar 30 2023 Artyom Bystrov <arbars@altlinux.org> 1.10.3-alt1
- initial build for ALT Sisyphus

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.10.3-3
- Rebuild for ImageMagick 7

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 06 2022 Miro Hrončok <mhroncok@redhat.com> - 1.10.3-1
- Update to 1.10.3
- Fixes: rhbz#1809122
- Contains security fix for CVE-2022-1507
- Fixes: rhbz#2080294
- Provide bundled libnsgif and lodepng

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-2
- Rebuilt for ImageMagick 6.9.12

* Mon Sep 20 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.8.0-1
- Update to 1.8.0
- Fixes: rhbz#1809122

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-1
- Update to 1.2.1 (#1742491)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Update to 1.0.1 (soversion 0.0.0 -> 0.1.1)
- Rebuilt for new ImageMagick 6.9.10 (#1623249)

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-1
- Initial package

