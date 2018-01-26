%def_with python3
%define oname pythonmagick
Name: python-module-%oname
Version: 0.9.64
Release: alt1.20170528%ubt

Summary: Object-oriented Python interface to ImageMagick

License: Apache License 2.0
Group: Development/Python
Url: https://github.com/ImageMagick/PythonMagick

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ pkgconfig(Magick++) pkgconfig(MagickCore)
BuildRequires: libgomp-devel
BuildRequires: python-devel boost-python-devel
%if_with python3
BuildRequires: python3-devel boost-python3-devel
%endif

%description
Object-oriented Python interface to ImageMagick.
Python 2 version.

%package -n python3-module-%oname
Summary: Object-oriented Python interface to ImageMagick
Group: Development/Python3

%description -n python3-module-%oname
Object-oriented Python interface to ImageMagick.
Python 3 version.

%prep
%setup
%if_with python3
rm -fR ../python3-module-%oname
cp -fR . ../python3-module-%oname
%endif

%build
%autoreconf
%configure PYTHON=python2
%make_build

%if_with python3
pushd ../python3-module-%oname
%autoreconf
%configure PYTHON=python3
%make_build
popd
%endif

%install
%makeinstall_std

%if_with python3
pushd ../python3-module-%oname
%makeinstall_std
popd
%endif

%files
%doc README LICENSE ChangeLog
%python_sitelibdir/PythonMagick
%exclude %python_sitelibdir/PythonMagick/*.a
%exclude %python_sitelibdir/PythonMagick/*.la

%if_with python3
%files -n python3-module-%oname
%doc README LICENSE ChangeLog
%python3_sitelibdir/PythonMagick
%exclude %python3_sitelibdir/PythonMagick/*.a
%exclude %python3_sitelibdir/PythonMagick/*.la
%endif

%changelog
* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 0.9.64-alt1.20170528%ubt
- Fix FTBFS.

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 0.9.64-alt1.20170528.2
- Rebuilt for ImageMagick

* Wed Jun 07 2017 Anton Midyukov <antohami@altlinux.org> 0.9.64-alt1.20170528.1
- Initial build for ALT Linux Sisyphus (Closes: 33533).
