%define sover 0

%def_enable check


%ifarch x86_64 i586 aarch64
%def_enable valgrind
%else
%def_disable valgrind
%endif

Name: qm-dsp
Version: 1.7.1
Release: alt1

Summary: A C++ library for audio analysis
License: GPLv2+
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/qm-dsp
Vcs: https://github.com/c4dm/qm-dsp

Source: %name-%version.tar
Patch:  %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: imake
BuildRequires: libopenblas-devel
BuildRequires: liblapack-devel

%if_enabled check
BuildRequires: boost-devel
%{?_enable_valgrind:BuildRequires: valgrind}
%endif

# for docs:
BuildRequires: doxygen graphviz fonts-ttf-dejavu

%description
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

%package -n lib%name
Summary: A C++ library for audio analysis
Group: System/Libraries

%description -n lib%name
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

%package -n lib%name-devel
Summary: Development files of a C++ library for audio analysis
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for a C++ library for audio analysis
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

This package contains development documentation for lib%name.

%prep
%setup
%autopatch -p1

rm -rf build/linux/amd64 build/mingw32
rm -vf include/{cblas.h,clapack.h}


%build
%add_optflags  -DUSE_PTHREADS

CFLAGS="%optflags $(pkg-config --cflags openblas lapack)" \
CXXFLAGS="%optflags $(pkg-config --cflags openblas lapack)" \
%make_build -f build/general/Makefile.inc

g++ -shared %optflags \
        -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
        -Wl,-soname=lib%name.so.%sover \
        -o lib%name.so.%sover \
        $(pkg-config --libs openblas lapack)

doxygen

%install
find . -type d -name ext -prune -o -name '*.h' -print \
| while read header; do
  install -Dpm644 "$header" "%buildroot%_includedir/%name/$header"
done

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%check
%if_disabled valgrind
sed -i 's/^VG.*$/VG :=/' tests/Makefile
%endif

%make_build -C tests


%files -n lib%name
%doc *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc doc/html/*

%changelog
* Tue Oct 10 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.1-alt1
- 1.7.1, switch to official upstream github;
- major build dependencies cleanup, spec cleanup;
- link with lapack instead of clapack;
- add %%check section.

* Mon Dec 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7-alt4
- rebuilt for non-x86 arches

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt3.hg20140805
- Rebuilt for new c++ ABI.

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2.hg20140805
- Built with dataquay-minefeld instead of dataquay

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20140805
- Initial build for Sisyphus
