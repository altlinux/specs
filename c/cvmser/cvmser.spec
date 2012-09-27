Name: cvmser
Version: r10
Release: alt1
Summary: OpenCV functions for MSER extraction
License: BSD, GPLv2+
Group: Graphics
Url: https://code.google.com/p/epnr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://epnr.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-c++ libopencv-devel

%description
OpenCV functions for MSER extraction

1. there are two different implementation of MSER, one for grey image,
   one for color image
2. the grey image algorithm is taken from: Linear Time Maximally Stable
   Extremal Regions;
   the paper claims to be faster than union-find method;
   it actually get 1.5~2m/s on my centrino L7200 1.2GHz laptop.
3. the color image algorithm is taken from: Maximally Stable Colour
   Regions for Recognition and Match;
   it should be much slower than grey image method ( 3~4 times );
   the chi_table.h file is taken directly from paper's source code which
   is distributed under GPL.
4. though the name is *contours*, the result actually is a list of point
   set.

%package -n lib%name
Summary: Library with OpenCV functions for MSER extraction
Group: System/Libraries

%description -n lib%name
OpenCV functions for MSER extraction

1. there are two different implementation of MSER, one for grey image,
   one for color image
2. the grey image algorithm is taken from: Linear Time Maximally Stable
   Extremal Regions;
   the paper claims to be faster than union-find method;
   it actually get 1.5~2m/s on my centrino L7200 1.2GHz laptop.
3. the color image algorithm is taken from: Maximally Stable Colour
   Regions for Recognition and Match;
   it should be much slower than grey image method ( 3~4 times );
   the chi_table.h file is taken directly from paper's source code which
   is distributed under GPL.
4. though the name is *contours*, the result actually is a list of point
   set.

%prep
%setup

%build
%add_optflags $(pkg-config opencv --cflags)
g++ %optflags %optflags_shared -c %name.cpp
g++ -shared *.o -o lib%name.so $(pkg-config opencv --libs)

%install
install -d %buildroot%_libdir
install -m644 lib%name.so %buildroot%_libdir

%files -n lib%name
%_libdir/*.so

%changelog
* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r10-alt1
- Initial build for Sisyphus

