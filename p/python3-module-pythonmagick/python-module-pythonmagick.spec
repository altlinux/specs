%define oname pythonmagick

Name: python3-module-%oname
Version: 0.9.64
Release: alt4

Summary: Object-oriented Python interface to ImageMagick
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ImageMagick/PythonMagick

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ pkgconfig(Magick++) pkgconfig(MagickCore)
BuildRequires: libgomp-devel
BuildRequires: python3-devel boost-python3-devel


%description
Object-oriented Python interface to ImageMagick.
Python 2 version.

%prep
%setup

%build
%autoreconf
%configure PYTHON=python3
%make_build

%install
%makeinstall_std
rm -vf %buildroot%python3_sitelibdir/PythonMagick/*.*a

%files
%doc README LICENSE ChangeLog
%python3_sitelibdir/PythonMagick

%changelog
* Fri Sep 10 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.64-alt4
- Fixed removing of static libraries.
- Fixed license tag.

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.64-alt3
- disable python2

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.64-alt2.20170528
- Rebuild for python3.7.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64-alt1.20170528.S1.2
- NMU: rebuilt with boost-1.67.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64-alt1.20170528.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 0.9.64-alt1.20170528.S1
- Fix FTBFS.

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 0.9.64-alt1.20170528.2
- Rebuilt for ImageMagick

* Wed Jun 07 2017 Anton Midyukov <antohami@altlinux.org> 0.9.64-alt1.20170528.1
- Initial build for ALT Linux Sisyphus (Closes: 33533).
