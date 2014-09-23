Name: vampy
Version: 2.0
Release: alt1.hg20140806
Summary: VamPy: Vamp Plugins in Python
License: MIT
Group: Sound
Url: http://www.vamp-plugins.org/vampy.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/vampy
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel libnumpy-devel
BuildPreReq: python-devel

%description
VamPy is a wrapper plugin written by Gyorgy Fazekas that enables you to
use Vamp plugins written in Python in any Vamp host.

It provides a (nearly) complete wrapper implementation of the Vamp
plugin API that can be used to write efficient plugins very easily,
taking advantage of the wide range of Python libraries already available
for scientific work.

This package contains vamp plugin of vampy.

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python

%description -n python-module-%name
VamPy is a wrapper plugin written by Gyorgy Fazekas that enables you to
use Vamp plugins written in Python in any Vamp host.

It provides a (nearly) complete wrapper implementation of the Vamp
plugin API that can be used to write efficient plugins very easily,
taking advantage of the wide range of Python libraries already available
for scientific work.

This package contains Python module of vampy.

%prep
%setup

%build
%make_build -f Makefile.linux all

%install
%makeinstall_std -f Makefile.linux LIBDIR=%_libdir

install -d %buildroot%python_sitelibdir
install -m644 vampymod.so %buildroot%python_sitelibdir/
ln -s vampymod.so %buildroot%python_sitelibdir/vampy.so

%files
%doc README Example\ VamPy\ plugins
%_libdir/vamp

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.hg20140806
- Initial build for Sisyphus

