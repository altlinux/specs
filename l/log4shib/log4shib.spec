%define soname 2
%define pkgdocdir %_docdir/%name-%version

Name: log4shib
Version: 2.0.1
Release: alt1

Summary: Log for C++, Shibboleth Edition

License: LGPL-2.1
Group: System/Libraries
Url: https://wiki.shibboleth.net/confluence/display/OpenSAML/log4shib

Source: http://shibboleth.net/downloads/log4shib/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ doxygen

%description
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.

%package -n liblog4shib%soname
Summary: Log for C++, Shibboleth Edition
Group: System/Libraries

%description -n liblog4shib%soname
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.

This package contains just the shared library.

%package -n liblog4shib-devel
Summary: Development tools for Log for C++
Group: Development/C++

%description -n liblog4shib-devel
The static libraries and header files needed for development with log4shib.

%prep
%setup

%build
# The default C++ standard used in GCC-11 is C++17,
# which does not support log4shib codebase.
export CXXFLAGS="-std=c++11 %optflags"
%autoreconf
%configure \
  --disable-static \
  --enable-doxygen
%make_build

%install
make DESTDIR=%buildroot apidir=%buildroot%pkgdocdir install
# If we use %%doc down below to package the README files from the build tree,
# it will blow away the package's docdir folder, and the installed API docs with it.
# Instead, copy the README files manually into the platform's docdir.
config/install-sh -d %buildroot%pkgdocdir
config/install-sh -m 644 -c AUTHORS COPYING NEWS README THANKS ChangeLog %buildroot%pkgdocdir

# We don't want to ship these
find %buildroot -type f -name "*.la" -delete -print

%files -n liblog4shib%soname
%_libdir/lib*.so.%{soname}*

%files -n liblog4shib-devel
%_includedir/%name
%_man3dir/*
%_libdir/lib*.so
%_pkgconfigdir/log4shib.pc
%doc %pkgdocdir

%changelog
* Thu Apr 14 2022 Leontiy Volodin <lvol@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
