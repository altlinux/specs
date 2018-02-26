Name: blender-plugins-localdocs
Version: 0.0.1
Release: alt1.1

Summary: Opens local manual directly from Blender menu
License: GPL2+
Group: Graphics

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source0: blender_localdocs.py

Requires: blender-docs

%description
This simple script opens the user's default web browser
at locally installed Blender's manual.

%prep

%build

%install
install -d -m755 %buildroot%_libdir/blender/scripts
install -p -m644 %SOURCE0 %buildroot%_libdir/blender/scripts/help_manual_local.py

%files
%_libdir/blender/scripts/*

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.1
- Rebuild with Python-2.7

* Tue Jan  5 2010 Sergey Kurakin <kurakin@altlinux.org> 0.0.1-alt1
- first build
