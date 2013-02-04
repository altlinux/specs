# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/pkg-config pkgconfig(gio-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-image-converter
Name:           mate-file-manager-image-converter
Version:        1.5.0
Release:        alt1_0
Summary:        Caja extension to mass resize images

Group:          Graphical desktop/Other
License:        GPLv2+
URL:		http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  libglade2-devel >= 2.4.0
BuildRequires:	glib2-devel >= 2.15.0
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	gettext
BuildRequires:	perl(XML/Parser.pm)
BuildRequires:  mate-common
BuildRequires:  intltool
Requires:	/usr/bin/convert
 

%description
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.


%prep
%setup -q -n %{name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{oldname}
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;


%files -f %{oldname}.lang
%doc AUTHORS COPYING
%{_datadir}/%{oldname}/
%{_libdir}/caja/extensions-2.0/*.so


%changelog
* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

