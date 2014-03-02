Name: gst-validate
Version: 0.0.1.1
Release: alt1
Group: System/Base
License: GNU GPLv2.1
Summary: GstValidate tools
URL: http://anongit.freedesktop.org/gstreamer/gst-devtools
Source: %name-%version.tar

BuildRequires: gtk-doc glib2-devel libgio-devel gstreamer1.0-devel gst-plugins-base1.0 gst-plugins1.0-devel

%description
The goal of GstValidate is to be able to detect when elements are not
behaving as expected and report it to the user so he knows how things
are supposed to work inside a GstPipeline. In the end, fixing issues
found by the tool will ensure that all elements behave all together in
the expected way.

The easiest way of using GstValidate is to use one of its command-line
tools, located at tools/ directory. It is also possible to monitor
GstPipelines from any application by using the LD_PRELOAD gstvalidate
lib. The third way of using it is to write your own application that
links and uses libgstvalidate.

%package -n lib%name
Summary: GstValidate library
Group: System/Base
%description -n lib%name
Library for GstValidate

%package -n lib%name-devel-static
Summary: Static GstValidate library
Group: System/Base
%description -n lib%name-devel-static
Static version of GstValidate library

%package -n lib%name-devel
Summary: Headers for development with GstValidate library
Group: System/Base
%description -n lib%name-devel
Headers of GstValidate library

%prep
%setup

%build
%autoreconf
%configure \
    --with-html-dir=%_gtk_docdir \
    --enable-static

%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Fri Feb 28 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1.1-alt1
- Build for ALT
