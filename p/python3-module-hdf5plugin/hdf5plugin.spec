%define oname hdf5plugin

%def_with systemlibs
%def_with check

Name:    python3-module-%oname
Version: 6.0.0
Release: alt1

Summary: Set of compression filters for h5py
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/hdf5plugin
VCS:     https://github.com/silx-kit/hdf5plugin

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

Patch: fix-bzip2-name.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-cpuinfo
BuildRequires: python3-module-pkgconfig

BuildRequires: gcc-c++
BuildRequires: libhdf5-devel
BuildRequires: libgomp-devel
#BuildRequires: libblosc-devel
BuildRequires: libblosc2-devel
BuildRequires: bzip2-devel
# snappy is too old in Sisyphus
#BuildRequires: libsnappy-devel
BuildRequires: liblz4-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel

%if_with check
BuildRequires: python3-module-numpy
BuildRequires: python3-module-h5py
%endif

%description
hdf5plugin provides HDF5 compression filters (namely: Blosc, Blosc2, BitShuffle,
BZip2, FciDecomp, LZ4, Sperr, SZ, SZ3, Zfp, ZStd) and makes them usable
from h5py.

%prep
%setup
%patch -p1

%if_with systemlibs
rm -rv lib/hdf5
rm -rv lib/bzip2
#rm -rv lib/c-blosc
rm -rv lib/c-blosc2
#rm -rv lib/snappy
%endif

%build
export CFLAGS="%optflags"
export HDF5PLUGIN_HDF5_DIR=%_prefix

%ifarch %ix86
sed -i '/_get_sz_plugin,/d' setup.py
sed -i '/_get_sz3_plugin,/d' setup.py
export HDF5PLUGIN_NATIVE=False
export HDF5PLUGIN_SSE2=False
export HDF5PLUGIN_AVX=False
export HDF5PLUGIN_AVX512=False
%endif

#export HDF5PLUGIN_SYSTEM_LIBRARIES=blosc,blosc2,bzip2,lz4,snappy,zlib,zstd
export HDF5PLUGIN_SYSTEM_LIBRARIES=blosc2,bzip2,lz4,zlib,zstd
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/test.py

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Feb 06 2026 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1
- Initial build for Sisyphus.
