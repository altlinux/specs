Name: quickjs-ng
Version: 0.18.0
Release: alt1

Summary: Embeddable JavaScript engine
License: MIT
Group: Development/Other
URL: https://quickjs-ng.github.io/quickjs
VCS: https://github.com/quickjs-ng/quickjs

Source0: %name-%version.tar

BuildRequires: meson

%package -n libqjs
Summary: QuickJS shared library
Group: System/Libraries

%package -n libqjs-devel
Summary: QuickJS development part
Group: Development/C

%define desc\
QuickJS is a small and embeddable JavaScript engine. It aims to support\
the latest ECMAScript specification.\
This project is a fork of the original QuickJS project by Fabrice Bellard\
and Charlie Gordon, after it went dormant, with the intent of reigniting\
its development.

%description %desc

%description -n libqjs %desc
This package contains QuickJS shared library.

%description -n libqjs-devel %desc
This package contains QuickJS devilopment part.

%define _customdocdir %_docdir/%name

%prep
%setup

%build
%meson -Ddefault_library=shared -Ddocdir=%_customdocdir
%meson_build

%install
%meson_install
install -pm0644 -D qjs.man %buildroot%_man1dir/qjs.1
install -pm0644 qjsc.man %buildroot%_man1dir/qjsc.1

%files
%doc LICENSE README.md
%exclude %_customdocdir/examples
%_bindir/qjs
%_bindir/qjsc
%_man1dir/qjs.1*
%_man1dir/qjsc.1*

%files -n libqjs
%_libdir/libqjs.so.*

%files -n libqjs-devel
%_customdocdir/examples
%_includedir/quickjs-ng/quickjs.h
%_libdir/libqjs.so
%_pkgconfigdir/quickjs-ng.pc

%changelog
* Fri Nov 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.18.0-alt1
- initial
