%define soname 18

Name: pynac
Version: 0.7.29
Release: alt1
Summary: Manipulation of symbolic expressions
License: GPL-2.0+
Group: System/Legacy libraries
Url: https://github.com/pynac/pynac

Source: https://github.com/pynac/pynac/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ libreadline-devel libcln-devel rpm-build-python3 libgmp-devel libflint2-devel libfactory-devel python3-devel

%description
Pynac is a derivative of the C++ library GiNaC, which allows manipulation of
symbolic expressions. It currently provides the backend for symbolic
expressions in Sage.

The main difference between Pynac and GiNaC is that Pynac relies on Sage to
provide the operations on numerical types, while GiNaC depends on CLN for this
purpose.

%package -n lib%name%soname
Summary: %summary
Group: System/Legacy libraries

%description -n lib%name%soname
Pynac is a derivative of the C++ library GiNaC, which allows manipulation of
symbolic expressions. It currently provides the backend for symbolic
expressions in Sage.

The main difference between Pynac and GiNaC is that Pynac relies on Sage to
provide the operations on numerical types, while GiNaC depends on CLN for this
purpose.

%package -n lib%name-devel
Summary: Pinac development libraries and header files
Group: Development/Other

%description -n lib%name-devel
Headers and libraries for developing with %{name}.

%prep
%setup -n pynac-%version

%build
%add_optflags -lpython%{_python3_version}
%autoreconf
%configure \
  --disable-static \
  --disable-silent-rules \
#
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_libdir/*.la

%files -n lib%name%soname
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/lib%{name}.so.%{soname}*

%files -n lib%name-devel
%_includedir/pynac/
%_libdir/lib%{name}.so
%_pkgconfigdir/pynac.pc

%changelog
* Mon Oct 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.7.29-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built for sagemath 9.4.
