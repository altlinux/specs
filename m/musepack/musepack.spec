Name: musepack
Version: r475
Release: alt2
Summary: Portable Musepack decoder library
License: BSD
Group: Sound
Url: https://www.musepack.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake libcuefile-devel libreplaygain-devel

Requires: libmpcdec0 = %EVR

%description
Musepack is a free, high performance, high quality lossy audio
compression codec. For more information on musepack visit
http://www.musepack.net.

%package -n libmpcdec0
Summary: Library that decodes musepack compressed audio data
Group: System/Libraries

%description -n libmpcdec0
libmpcdec is a library that decodes musepack compressed audio data.

%package -n libmpcdec0-devel
Summary: Development files of libmpcdec
Group: Development/C
Requires: libmpcdec0 = %EVR
Conflicts: libmpcdec-devel

%description -n libmpcdec0-devel
libmpcdec is a library that decodes musepack compressed audio data.

This package contains development files of libmpcdec.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%_bindir/*

%files -n libmpcdec0
%_libdir/*.so.*

%files -n libmpcdec0-devel
%doc docs/mainpage.txt
%_includedir/*
%_libdir/*.so

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r475-alt2
- Applied repocop patch

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r475-alt1
- Initial build for Sisyphus

