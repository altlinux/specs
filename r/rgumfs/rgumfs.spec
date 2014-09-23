Name: rgumfs
Version: 0.0
Release: alt1
Summary: VamPy Mel-Frequency Spectrum Plugin
License: GPLv2
Group: Sound
Url: http://sourceforge.net/projects/rgumfs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel

%description
VamPy plugin for the Mel-Frequency Spectrum approach described in detail
in:

Horsburgh, B., Craw, S. & Massie, S. (2012). Music-inspired texture
representation, Proceedings of the National Conference on Artificial
Intelligence (AAAI), pp. 52-58.

%package -n python-module-%name
Summary: VamPy Mel-Frequency Spectrum Plugin
Group: Development/Python

%description -n python-module-%name
VamPy plugin for the Mel-Frequency Spectrum approach described in detail
in:

Horsburgh, B., Craw, S. & Massie, S. (2012). Music-inspired texture
representation, Proceedings of the National Conference on Artificial
Intelligence (AAAI), pp. 52-58.

%prep
%setup

%install
install -d %buildroot%python_sitelibdir
install -p -m644 *.py %buildroot%python_sitelibdir/

%files -n python-module-%name
%doc *.txt
%python_sitelibdir/*

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1
- Initial build for Sisyphus

