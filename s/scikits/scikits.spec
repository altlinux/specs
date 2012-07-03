%define oname scikits

%def_enable docs

BuildRequires(pre): rpm-build-python
%define python_noarch %_libexecdir/python%_python_version/site-packages

%define dirs1 ann audiolab delaunay timeseries hydroclimpy odes
#define dirs1 audiolab delaunay timeseries hydroclimpy odes
%define dirs2 samplerate optimization rsformats talkbox umfpack vectorplot
%define dirs %dirs1 %dirs2 statsmodels

%define docs_src0 audiolab/docs samplerate/docs talkbox/docs
%define docs_src %docs_src0 statsmodels/scikits/statsmodels/docs

%define longdesc SciKits (short for SciPy Toolkits), are add-on packages for SciPy, \
hosted and developed separately from the main SciPy distribution. All \
SciKits are available under the 'scikits' namespace and are licensed \
under OSI-approved licenses.

Name: %oname
Version: 2267
Release: alt5.1
Summary: Add-on packages for SciPy
License: OSI-approved licenses
Group: Sciences/Other
Url: http://scikits.appspot.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.scipy.org/svn/scikits/trunk
Source: %name-%version.tar.gz
# git://github.com/cournape/audiolab.git
Source1: audiolab.tar.gz
# git://github.com/cournape/samplerate.git
Source2: samplerate.tar.gz
# git://github.com/cournape/talkbox.git
Source3: talkbox.tar.gz
Source4: site.cfg
# bzr branch lp:statsmodels
Source5: statsmodels.tar.gz
# https://github.com/mbrucher/scikit-optimization.git
Source6: optimization.tar.gz

BuildPreReq: python-module-sphinx-devel /usr/bin/latex
BuildPreReq: python-devel python-module-scipy swig gcc-c++ gcc-fortran
BuildPreReq: libsuitesparse-devel libann-devel libsndfile-devel boost-devel
BuildPreReq: libglpk-devel >= 4.38 python-module-cvxopt python-module-pswarm_py
BuildPreReq: python-module-pyipopt python-module-pywrapper libgotoblas-devel
BuildPreReq: libsamplerate-devel python-module-Cython python-module-tables
BuildPreReq: python-module-h5py python-module-BeautifulSoup libalsa-devel
#BuildPreReq: python-module-pyproj python-module-rpy libnumpy-devel
BuildPreReq: python-module-pyproj libnumpy-devel
BuildPreReq: python-module-matplotlib-sphinxext
#BuildPreReq: libsundials-devel python-module-pysundials

%description
%longdesc

%package -n python-module-%name
Summary: Add-on packages for SciPy
Group: Development/Python
%setup_python_module %name
%add_python_req_skip models pyhdf
# awaiting packages:
%add_python_req_skip pysundials

%description -n python-module-%name
%longdesc

This package contains SciKits python modules.

%description -n python-module-%name
%longdesc

This package contains SciKits python modules.

%package -n python-module-%name.ann
Summary: Approximate Nearest Neighbor library wrapper for Numpy
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.ann
%longdesc

The ANN module provides a numpy-compatible python wrapper around the
Approximate Nearest Neighbor library.

%package -n python-module-%name.audiolab
Summary: Python package for audio file IO using numpy arrays
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.audiolab
%longdesc

Audiolab is a python package for audio file IO using numpy arrays. It supports
many different audio formats, including wav, aiff, au, flac, ogg, htk. It can
also be used for sound output to audio device (Mac OS X and Linux only).

A matlab-like API is provided for simple import/export; a more complete API
is available for more advanced usage. Audiolab is essentially a wrapper
around Erik de Castro Lopo's excellent libsndfile.

%package -n python-module-%name.delaunay
Summary: Delaunay triangulation and interpolation tools
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.delaunay
%longdesc

This package contains delaunay triangulation and interpolation tools.

%package -n python-module-%name.hydroclimpy
Summary: Environmental time series manipulation
Group: Development/Python
Requires: python-module-%name = %version-%release
Requires: python-module-%name.timeseries = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.hydroclimpy
%longdesc

The scikits.hydroclimpy module is a collection of tools for manipulating and
plotting environmental time series of various frequencies. This package is
an extension for scikits.timeseries, focusing on tools for the analysis of
hydroclimatologic datasets.

%package -n python-module-%name.learn
Summary: A set of python modules for machine learning and data mining
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.learn
%longdesc

This package contains s set of python modules for machine learning and
data mining.

%package -n python-module-%name.odes
Summary: Scikit toolkit for scipy to add some extra ode solvers
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.odes
%longdesc

Odes is a scikit toolkit for scipy to add some extra ode solvers.
At present it provides dae solvers you can use, extending the capabilities
offered in scipy.integrade.ode.

%package -n python-module-%name.optimization
Summary: Scikit python module for numerical optimization
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.optimization
%longdesc

This package contains scikit python module for numerical optimization.

%package -n python-module-%name.rsformats
Summary: Tools for reading remote sensing formats
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.rsformats
%longdesc

This package contains tools for reading remote sensing formats.

%package -n python-module-%name.samplerate
Summary: Python package to resample audio data in numpy arrays
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.samplerate
%longdesc

Samplerate is a small python package to resample audio data in numpy
arrays to a difference sampling rate: it is basically a wrapper around
the Secret Rabbit Code from Erik de Castro Lopo
(http://www.mega-nerd.com/SRC/).  This package only makes sense for
audio data, and has high quality converters based on the work of J.O
Smith from CCRMA (see http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package -n python-module-%name.statsmodels
Summary: Statistical computations and models for use with SciPy
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.statsmodels
%longdesc

Statsmodels is a python package that provides an interface to scipy for
statistical computations including descriptive statistics and
fitting statistical models.

%package -n python-module-%name.talkbox
Summary: Scikit for signal/speech processing
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.talkbox
%longdesc

Talkbox is a scikit for signal/speech processing, to extend scipy
capabilities in that domain.

%package -n python-module-%name.timeseries
Summary: Time series manipulation
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.timeseries
%longdesc

The scikits.timeseries module provides classes and functions for
manipulating, reporting, and plotting time series of various
frequencies. The focus is on convenient data access and manipulation
while leveraging the existing mathematical functionality in Numpy and
SciPy.

%package -n python-module-%name.umfpack
Summary: Python interface to the UMFPACK sparse linear solver
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.umfpack
%longdesc

The umfpack scikit provides wrappers of UMFPACK sparse direct solver to
SciPy.

%package -n python-module-%name.vectorplot
Summary: Vector fields plotting algorithms
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release

%description -n python-module-%name.vectorplot
%longdesc

Algorithms to plot vector fields. For the moment, it only contains the
line integral convolution algorithm.

%package -n python-module-%name-examples
Summary: Documentation for SciPy Toolkits (SciKits)
Group: Development/Python
Requires: python-module-%name = %version-%release
Conflicts: python-module-%name < %version-%release
#py_requires scikits.learn.machine.manifold_learning.compression
#py_requires scikits.learn.machine.svm
%py_requires scikits.statsmodels.docs.sphinxext.docscrape
%py_requires scikits.statsmodels.docs.sphinxext.docscrape_sphinx
#py_requires scikits.openopt.solvers.optimizers
%add_python_req_skip compression docscrape docscrape_sphinx
%add_python_req_skip optimizers svm

%description -n python-module-%name-examples
%longdesc

This package contains tests and examples for SciKits.

%if_enabled docs

%package -n python-module-%name-doc
Summary: Documentation for SciPy Toolkits (SciKits)
Group: Development/Documentation
BuildArch: noarch
Requires: python-module-%name.audiolab-doc = %version-%release
Requires: python-module-%name.samplerate-doc = %version-%release
Requires: python-module-%name.statsmodels-doc = %version-%release
Requires: python-module-%name.statsmodels-doc = %version-%release

%description -n python-module-%name-doc
%longdesc

This package contains documentation for SciKits.


%package -n python-module-%name.audiolab-doc
Summary: Documentation for Audiolab SciKit
Group: Development/Documentation
BuildArch: noarch
Conflicts: python-module-%name-doc < %version-%release

%description -n python-module-%name.audiolab-doc
%longdesc

This package contains documentation for Audiolab SciKit.

%package -n python-module-%name.samplerate-doc
Summary: Documentation for Samplerate SciKit
Group: Development/Documentation
BuildArch: noarch
Conflicts: python-module-%name-doc < %version-%release

%description -n python-module-%name.samplerate-doc
%longdesc

This package contains documentation for Samplerate SciKit.

%package -n python-module-%name.statsmodels-doc
Summary: Documentation for Statsmodels SciKit
Group: Development/Documentation
BuildArch: noarch
Conflicts: python-module-%name-doc < %version-%release

%description -n python-module-%name.statsmodels-doc
%longdesc

This package contains documentation for Statsmodels SciKit.

%package -n python-module-%name.talkbox-doc
Summary: Documentation for Talkbox SciKit
Group: Development/Documentation
BuildArch: noarch
Conflicts: python-module-%name-doc < %version-%release

%description -n python-module-%name.talkbox-doc
%longdesc

This package contains documentation for Talkbox SciKit.

%package -n python-module-%name.talkbox-pickles
Summary: Pickles for Scikit for signal/speech processing
Group: Development/Python

%description -n python-module-%name.talkbox-pickles
%longdesc

Talkbox is a scikit for signal/speech processing, to extend scipy
capabilities in that domain.

This package contains pickles for Talkbox.

%package -n python-module-%name.audiolab-pickles
Summary: Pickles for Python package for audio file IO using numpy arrays
Group: Development/Python

%description -n python-module-%name.audiolab-pickles
%longdesc

Audiolab is a python package for audio file IO using numpy arrays. It supports
many different audio formats, including wav, aiff, au, flac, ogg, htk. It can
also be used for sound output to audio device (Mac OS X and Linux only).

A matlab-like API is provided for simple import/export; a more complete API
is available for more advanced usage. Audiolab is essentially a wrapper
around Erik de Castro Lopo's excellent libsndfile.

This package contains pickles for Python package for audio file IO using
numpy arrays.

%package -n python-module-%name.samplerate-pickles
Summary: Pickles for Python package to resample audio data in numpy arrays
Group: Development/Python

%description -n python-module-%name.samplerate-pickles
%longdesc

Samplerate is a small python package to resample audio data in numpy
arrays to a difference sampling rate: it is basically a wrapper around
the Secret Rabbit Code from Erik de Castro Lopo
(http://www.mega-nerd.com/SRC/).  This package only makes sense for
audio data, and has high quality converters based on the work of J.O
Smith from CCRMA (see http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

This package contains pickles for Python package to resample audio data
in numpy arrays.



%endif

%prep
%setup
tar -xzf %SOURCE1
tar -xzf %SOURCE2
tar -xzf %SOURCE3
tar -xzf %SOURCE5
rm -fR optimization
tar -xzf %SOURCE6

install -p -m644 %SOURCE4 .
%ifarch x86_64
SUFF=64
%endif
sed -i "s|@SUFF@|$SUFF|" site.cfg

%if_enabled docs
%prepare_sphinx .
ln -s $PWD/objects.inv statsmodels/scikits/statsmodels/docs/
%endif
for i in umfpack audiolab samplerate
do
	ln -s ../site.cfg $i/
	ln -s ../../objects.inv $i/docs
done

sed -i 's|import\ version|from scikits.talkbox import version|' \
	talkbox/scikits/talkbox/__init__.py

sed -i 's|quiet\=True|quiet=False|' */setup.py

%build
%add_optflags %optflags_shared -fno-strict-aliasing
for dir in %dirs; do
	pushd $dir
	%python_build_debug
	popd
done

%if_enabled docs
#sed -i "s|,\ 'numpydoc',\ 'only_directives'||" \
sed -i "s|,\ 'only_directives'||" \
	audiolab/docs/src/conf.py \
	samplerate/docs/src/conf.py \
	talkbox/docs/src/conf.py

cat <<EOF >talkbox/docs/src/talkbox_version.py
short_version = "0.2.3"
version = "0.2.3.release"
EOF
%endif

%install
for dir in %dirs; do
	pushd $dir
	%python_install
	popd
done

echo 'version="0.2.3"' > \
	%buildroot%python_sitelibdir/%name/talkbox/version.py

%ifarch x86_64
# rsformats, statsmodels, optimization
mv %buildroot%python_noarch/%name/* \
       %buildroot%python_sitelibdir/%name/
mv %buildroot%python_noarch/%name.* \
       %buildroot%python_sitelibdir/
%endif

# docs

%if_enabled docs
export PYTHONPATH=%buildroot%python_sitelibdir
for i in %docs_src; do
	pushd $i
	%make html
	popd
done

for i in %docs_src statsmodels/%oname/statsmodels/docs
do
	DIR=$(echo $i|sed 's|\([^/]*\).*|\1|')
	install -d %buildroot%_docdir/%name/$DIR
	cp -fR $i/build/html/* %buildroot%_docdir/%name/$DIR/
done
%endif

# examples

for i in odes/docs/src/examples hydroclimpy/examples \
	rsformats/scikits/rsformats/examples
do
	DIR=$(echo $i|sed 's|\([^/]*\).*|\1|')
	install -d %buildroot%python_sitelibdir/%name/$DIR
	touch %buildroot%python_sitelibdir/%name/$DIR/__init__.py
	cp -fR $i %buildroot%python_sitelibdir/%name/$DIR/
done
for i in $(find %buildroot%python_sitelibdir -name tests) \
	$(find %buildroot%python_sitelibdir -name examples)
do
	touch $i/__init__.py
done
touch %buildroot%python_sitelibdir/%name/rsformats/examples/aster/__init__.py
touch %buildroot%python_sitelibdir/%name/rsformats/examples/odl_parsing/__init__.py

# pickles

%if_enabled docs
for i in audiolab samplerate talkbox
do
	make -C $i/docs pickle
	install -d %buildroot%python_sitelibdir/%name.$i
	cp -fR $i/docs/build/pickle %buildroot%python_sitelibdir/%name.$i/
done
%endif

%files -n python-module-%name
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/*.py*

%files -n python-module-%name.ann
%doc ann/license.txt
%python_sitelibdir/%name/ann
%python_sitelibdir/%name.ann*

%files -n python-module-%name.audiolab
%doc audiolab/COPYING.txt audiolab/NEWS audiolab/README.txt audiolab/TODO
%python_sitelibdir/%name/audiolab
%exclude %python_sitelibdir/%name/audiolab/tests
%python_sitelibdir/%name.audiolab*
%if_enabled docs
%exclude %python_sitelibdir/%name.audiolab/pickle
%endif

%files -n python-module-%name.delaunay
%python_sitelibdir/%name/delaunay
%python_sitelibdir/%name.delaunay*

%files -n python-module-%name.hydroclimpy
%python_sitelibdir/%name/hydroclimpy
%exclude %python_sitelibdir/%name/hydroclimpy/*/tests
%exclude %python_sitelibdir/%name/hydroclimpy/examples
%python_sitelibdir/%name.hydroclimpy*

#files -n python-module-%name.learn
#python_sitelibdir/%name/learn
#exclude %python_sitelibdir/%name/learn/*/*/tests
#exclude %python_sitelibdir/%name/learn/*/*/examples
#exclude %python_sitelibdir/%name/learn/*/*/*/tests
#python_sitelibdir/%name.learn*

%files -n python-module-%name.optimization
#python_sitelibdir/%name/openopt
#exclude %python_sitelibdir/%name/openopt/tests
#exclude %python_sitelibdir/%name/openopt/examples
#exclude %python_sitelibdir/%name/openopt/*/*/tests
#python_sitelibdir/%name.openopt*
%python_sitelibdir/%name/optimization
%exclude %python_sitelibdir/%name/optimization/tests
%exclude %python_sitelibdir/%name/optimization/*/tests
%python_sitelibdir/%name.optimization*

%files -n python-module-%name.rsformats
%python_sitelibdir/%name/rsformats
%exclude %python_sitelibdir/%name/rsformats/examples
%python_sitelibdir/%name.rsformats*

%files -n python-module-%name.odes
%doc odes/README
%python_sitelibdir/%name/odes
%exclude %python_sitelibdir/%name/odes/tests
%exclude %python_sitelibdir/%name/odes/examples
%python_sitelibdir/%name.odes*

%files -n python-module-%name.samplerate
%doc samplerate/README samplerate/COPYING samplerate/TODO
%python_sitelibdir/%name/samplerate
%exclude %python_sitelibdir/%name/samplerate/tests
%if_enabled docs
%exclude %python_sitelibdir/%name.samplerate/pickle
%endif
%python_sitelibdir/%name.samplerate*

%files -n python-module-%name.statsmodels
%doc statsmodels/README.txt
%python_sitelibdir/%name/statsmodels
%exclude %python_sitelibdir/%name/statsmodels/tests
%exclude %python_sitelibdir/%name/statsmodels/*/*/tests
%exclude %python_sitelibdir/%name/statsmodels/examples
%python_sitelibdir/%name.statsmodels*

%files -n python-module-%name.talkbox
%doc talkbox/README talkbox/LICENSE.txt talkbox/TODO
%python_sitelibdir/%name/talkbox
%exclude %python_sitelibdir/%name/talkbox/*/tests
%if_enabled docs
%exclude %python_sitelibdir/%name.talkbox/pickle
%endif
%python_sitelibdir/%name.talkbox*

%files -n python-module-%name.timeseries
%doc timeseries/README.txt timeseries/LICENSE.txt
%python_sitelibdir/%name/timeseries
%python_sitelibdir/%name.timeseries*

%files -n python-module-%name.umfpack
%doc umfpack/README
%python_sitelibdir/%name/umfpack
%exclude %python_sitelibdir/%name/umfpack/tests
%python_sitelibdir/%name.umfpack*

%files -n python-module-%name.vectorplot
%python_sitelibdir/%name/vectorplot
%python_sitelibdir/%name.vectorplot*

%files -n python-module-%name-examples
%python_sitelibdir/%name/*/tests
%python_sitelibdir/%name/*/*/tests
%python_sitelibdir/%name/*/*/*/tests
#python_sitelibdir/%name/*/*/*/*/tests
%python_sitelibdir/%name/*/examples
#python_sitelibdir/%name/*/*/*/examples

%if_enabled docs
%files -n python-module-%name-doc
%dir %_docdir/%name

%files -n python-module-%name.audiolab-doc
%dir %_docdir/%name
%_docdir/%name/audiolab

%files -n python-module-%name.samplerate-doc
%dir %_docdir/%name
%_docdir/%name/samplerate

%files -n python-module-%name.statsmodels-doc
%dir %_docdir/%name
%_docdir/%name/statsmodels

%files -n python-module-%name.talkbox-doc
%dir %_docdir/%name
%_docdir/%name/talkbox

%files -n python-module-%name.audiolab-pickles
%dir %python_sitelibdir/%name.audiolab
%python_sitelibdir/%name.audiolab/pickle

%files -n python-module-%name.samplerate-pickles
%dir %python_sitelibdir/%name.samplerate
%python_sitelibdir/%name.samplerate/pickle

%files -n python-module-%name.talkbox-pickles
%dir %python_sitelibdir/%name.talkbox
%python_sitelibdir/%name.talkbox/pickle

%endif

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2267-alt5.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2267-alt5
- Enabled docs

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2267-alt4.1
- Rebuild with Python-2.7

* Thu Oct 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2267-alt4
- Rebuilt with updated SciPy

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2267-alt3
- Rebuilt with updated SciPy

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2267-alt2
- Fixed build of scikits.ann

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2267-alt1
- Version 2267
- Built with GotoBLAS instead of ATLAS

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt9
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt8
- Rebuilt with python-module-sphinx-devel

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt7
- Added -g into compiler flags

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt6
- Rebuilt with Boost 1.46.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt5
- Rebuilt for debuginfo

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt4
- Fixed build

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt3
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt2
- Fixed underlinking

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2252-alt1
- New snapshot

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt10
- Changed requirement: pythonX.Y(nipy) -> python-module-nipy

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt9
- Rebuilt with shared libraries of PSwarm
- Added pickles packages for audiolab, samplerate and talkbox

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt8
- Rebuilt with %%prepare_sphinx

* Sun Jan 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt7
- Fixed finding of required libraries
- Extracted tests and examples into separate package

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt6
- Rebuilt without python-module-Numeric
- Updated some packages

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt5
- Rebuilt with python 2.6

* Sun Nov 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt4
- Moved components into subpackages

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt3
- Changed requirement: toms_587 -> toms587

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt2
- Enabled requirements on existent packages; awaiting updates for
  PySUNDIALS in upstream
- Built with texlive instead of tetex

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2216-alt1
- Initial build for Sisyphus

