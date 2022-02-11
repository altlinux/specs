%define git_commit dadc19cf1b90c5743f2776c675faac990e397a56
%define gtk_version 3
%define so_version 0

Name: gtk-sharp
Version: 2.99.4
Release: alt2.gitdadc19c

Summary: C-Sharp Language Bindings for GTK+
License: LGPLv2
Group: Development/Other

Url: https://www.mono-project.com/docs/gui/gtksharp/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

# https://github.com/mono/%name/archive/%git_commit/%name-%git_commit.tar.gz
Source: %name-%git_commit.tar

BuildRequires: /proc
BuildRequires: libgtk+3-devel
BuildRequires: mono-data-oracle
BuildRequires: mono-data-sqlite
BuildRequires: mono-devel
BuildRequires: mono-dyndata
BuildRequires: mono-locale-extras
BuildRequires: mono-mono2-compat-devel
BuildRequires: mono-reactive-winforms
BuildRequires: perl-XML-LibXML
BuildRequires: rpm-build-mono

%description
This package contains C-Sharp bindings for Gtk+, Gdk, Atk, and Pango.
for use with Mono.

%package -n lib%name%gtk_version
Summary: C-Sharp Language Bindings for GTK+
Group: Development/Other

%description -n lib%name%gtk_version
This package contains C-Sharp bindings for Gtk+, Gdk, Atk, and Pango.
for use with Mono.

%package -n lib%name%gtk_version-devel
Summary: .NET/C-Sharp Bindings for GIO
Group: Development/Other
Requires: lib%name%gtk_version = %EVR

%description -n lib%name%gtk_version-devel
Files for developing programs using the C-Sharp bindings for Gtk+, Gdk, Atk, and Pango.

%package -n lib%name%gtk_version-gapi
Summary: C Source Parser and C Generator
Group: Development/Other

%description -n lib%name%gtk_version-gapi
The gtk-sharp-gapi package includes the parser and code generator used
by the GTK if you want to bind GObject-based libraries, or need to
compile a project that uses it to bind such a library.

%package -n lib%name%gtk_version-gapi-devel
Summary: .NET/C-Sharp Bindings for GIO
Group: Development/Other
Requires: lib%name%gtk_version-gapi = %EVR

%description -n lib%name%gtk_version-gapi-devel
Files for developing programs that use gapi-sharp3.

%package -n lib%name%gtk_version-glib
Summary: Mono bindings for glib
Group: Development/Other

%description -n lib%name%gtk_version-glib
This package contains Mono bindings for glib.

%package -n lib%name%gtk_version-gio
Summary: Mono bindings for gio
Group: Development/Other

%description -n lib%name%gtk_version-gio
This package contains Mono bindings for gio-sharp.

%package -n lib%name%gtk_version-gio-devel
Summary: .NET/C-Sharp Bindings for GIO
Group: Development/Other
Requires: lib%name%gtk_version-gio = %EVR

%description -n lib%name%gtk_version-gio-devel
Files for developing programs that use gio-sharp

%package -n libmono-profiler-gui-thread-check%so_version
Summary: Profiler for %name%gtk_version
Group: System/Libraries

%description -n libmono-profiler-gui-thread-check%so_version
A profiler called "gui-thread-check" is included as
part of the install for debugging purposes.

%package -n libmono-profiler-gui-thread-check-devel
Summary: Profiler for %name%gtk_version
Group: Development/Other

%description -n libmono-profiler-gui-thread-check-devel
A profiler called "gui-thread-check" is included as
part of the install for debugging purposes.

%package -n lib%name%gtk_version-docs
Summary: Monodoc documentation for %name%gtk_version
Group: Documentation
BuildArch: noarch

%description -n lib%name%gtk_version-docs
This package contains the %name%gtk_version documentation for monodoc.

%prep
%setup -n %name-%git_commit

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
%__mkdir_p %buildroot%_monodocdir
%__mv %buildroot%_libexecdir/monodoc/sources/* %buildroot%_monodocdir
%__rm %buildroot%_libdir/*.la

%files -n lib%name%gtk_version
%_libdir/libatksharpglue-3.so
%_libdir/libgtksharpglue-3.so
%_libdir/libgiosharpglue-3.so
%_libdir/libpangosharpglue-3.so
%_monodir/gtk-sharp-3.0/atk-sharp.dll
%_monodir/gtk-sharp-3.0/cairo-sharp.dll
%_monodir/gtk-sharp-3.0/gdk-sharp.dll
%_monodir/gtk-sharp-3.0/gtk-dotnet.dll
%_monodir/gtk-sharp-3.0/gtk-sharp.dll
%_monodir/gtk-sharp-3.0/pango-sharp.dll
%_monogacdir/atk-sharp
%_monogacdir/cairo-sharp
%_monogacdir/gdk-sharp
%_monogacdir/gtk-dotnet
%_monogacdir/gtk-sharp
%_monogacdir/pango-sharp

%files -n lib%name%gtk_version-devel
%_pkgconfigdir/gtk-sharp-3.0.pc
%_pkgconfigdir/gdk-sharp-3.0.pc
%_pkgconfigdir/gtk-dotnet-3.0.pc
%_pkgconfigdir/glib-sharp-3.0.pc

%files -n lib%name%gtk_version-gapi
%dir %_libexecdir/gapi-3.0
%_bindir/gapi3-*
%_datadir/gapi-3.0
%_libexecdir/gapi-3.0

%files -n lib%name%gtk_version-gapi-devel
%_pkgconfigdir/gapi-3.0.pc

%files -n lib%name%gtk_version-glib
%_monogacdir/glib-sharp
%_monodir/gtk-sharp-3.0/glib-sharp.dll

%files -n lib%name%gtk_version-gio
%_monogacdir/gio-sharp
%_monodir/gtk-sharp-3.0/gio-sharp.dll

%files -n lib%name%gtk_version-gio-devel
%_pkgconfigdir/gio-sharp-3.0.pc

%files -n libmono-profiler-gui-thread-check%so_version
%_libdir/libmono-profiler-gui-thread-check.so.*

%files -n libmono-profiler-gui-thread-check-devel
%_libdir/libmono-profiler-gui-thread-check.so

%files -n lib%name%gtk_version-docs
%doc README
%_monodocdir

%changelog
* Fri Feb 11 2022 Nazarov Denis <nenderus@altlinux.org> 2.99.4-alt2.gitdadc19c
- Fix requires on devel subpackages

* Mon Jan 17 2022 Nazarov Denis <nenderus@altlinux.org> 2.99.4-alt1.gitdadc19c
- Initial build for ALT Linux
