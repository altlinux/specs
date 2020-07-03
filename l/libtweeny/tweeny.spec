Name: libtweeny
Version: 3.1.0
Release: alt1

Summary: An inbetweening library for complex animations (C++)

Group: Development/Other
License: MIT
Url: https://github.com/mobius3/tweeny/tree/2/cmake

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: cmake gcc-c++ doxygen

%description
Tweeny is an inbetweening library designed for the creation of complex animations for games and other beautiful interactive software. It leverages features of modern C++ to empower developers with an intuitive API for declaring tweenings of any type of value, as long as they support arithmetic operations.

The goal of Tweeny is to provide means to create fluid interpolations when animating position, scale, rotation, frames or other values of screen objects, by setting their values as the tween starting point and then, after each tween step, plugging back the result.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%prep
%setup
%patch -p1

%build
%cmake -DTWEENY_BUILD_DOCUMENTATION=1 \
       -DDOC_INSTALL_DIR:PATH=%_datadir/doc/%name-devel-%version

%cmake_build

%install
%cmakeinstall_std
rm -fv BUILD/doc/man/man3/_usr_src_RPM_BUILD*
mv BUILD/doc/man/man3/tweeny_tween_\ T\ _.3 \
   BUILD/doc/man/man3/tweeny_tween_T_.3
for f in BUILD/doc/man/man3/*.3; do \
	install -D -m0644 $f %buildroot%_man3dir/${f##*/}; \
done
install -D -m0644 README.md %buildroot%_datadir/doc/%name-devel-%version/README.md
install -D -m0644 LICENSE %buildroot%_datadir/doc/%name-devel-%version/LICENSE
	
%files devel
%_includedir/tweeny
%_libdir/cmake/Tweeny
%_man3dir/*.3.*
%_datadir/doc/%name-devel-%version

%changelog
* Thu Jul 02 2020 Paul Wolneykien <manowar@altlinux.org> 3.1.0-alt1
- Fresh up to v3.1.0.
- Fixed TweenyTargets installation path.
- Fixed packaging of the README and LICENSE files.

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt1
- Initial version (3.0.0).
