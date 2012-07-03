Name: gtkaml
Version: 0.5.92
Release: alt1.svn869
Summary: An Application Markup Language for GTK+Vala

Group: Development/Other
License: GPL
URL: http://code.google.com/p/%name

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

Requires: lib%name = %version-%release
BuildRequires: glib2-devel libgtk+2-devel libxml2-devel libvala-devel

%description
Gtkaml is a markup language based on Vala which lets you create Gtk+
composite widgets through concise XML or by using Gtkon object notation.
Features:
 * compact XML syntax for describing Gtk widgets
 * JSON-like and less verbose Gtkon syntax
 * code 'islands' (written in Vala) for signal handling and other
   methods/signals/properties/ in your widget class (so you don't modify
   the generated code ever)
 * you don't depend on gtkaml at run-time
 * much more readable than the usual UI boilerplate (e.g. you don't need
   to worry about temporary variable names, or ever write hundreds of
   lines of code)
 * works with any library that has a .vapi file, not just Gtk+
   (composition methods can be specified in the .implicits file)

%package -n lib%name
Summary: gtkaml shared libraries
Group: System/Libraries

%description -n lib%name
This package contains gtkaml shared libraries

%package -n lib%name-devel
Summary: gtkaml development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains gtkaml development files (headers and libraries links)

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/%{name}c
%_datadir/%name
%_man1dir/*.gz
%doc AUTHORS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name-*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_vapidir/*

%changelog
* Thu Mar 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.92-alt1.svn869
- 0.6 beta1
- build with vala-0.16

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.3-alt2.svn838
- svn snapshot for build with vala-0.14

* Thu Jun 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- New version 0.4.0

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.11-alt1
- New version 0.2.11

* Mon Oct 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.10-alt2
- rebuild

* Mon May 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.10-alt1
- New version 0.2.10

* Sun Dec 13 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.9.1-alt1
- new version
- fix build with vala 0.7.8

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.8-alt1
- new version
- patch1 moved to upstream
- fix build with vala 0.7.6

* Wed Jun 17 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.7-alt1
- initial build

