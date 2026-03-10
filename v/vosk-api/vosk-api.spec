%global descr Vosk is an offline open source speech recognition toolkit. It enables\
speech recognition for 20+ languages and dialects - English, Indian English,\
German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese,\
Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino, Ukrainian, Kazakh,\
Swedish, Japanese, Esperanto, Hindi, Czech, Polish. More to come.

%global abiversion 0

%global pypi_name vosk
%global oname vosk

Name: vosk-api
Version: 0.3.50
Release: alt1
Epoch: 1

Summary: Offline speech recognition toolkit
License: Apache-2.0
Group: Development/C++
Url: https://alphacephei.com/vosk
Vcs: https://github.com/alphacep/vosk-api.git

Source0: %name-%version.tar
# https://github.com/alphacep/kaldi/archive/93ef0019b847272a239fbb485ef97f29feb1d587.tar.gz
Source1: kaldi-alphacep.tar
Patch0: kaldi-FEDORA-fst.patch
Patch1: kaldi-FEDORA&ALT-lapack.patch
Patch2: kaldi-FEDORA-openblas.patch
Patch3: vosk-FEDORA-lapack.patch
Patch4: vosk-FEDORA-lib_fst.patch
Patch5: fix-python3-module-vosk-ALT-remove_arch_files_in_noarch-setup.py.patch
Patch6: fix-python3-module-vosk-ALT-SharedLibsPolicy-__init.py__.patch

BuildRequires(Pre): rpm-build-cmake
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libblas-devel
BuildRequires: libflexiblas-devel
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: libopenfst-devel
BuildRequires: openfst-tools
BuildRequires: python3-module-cffi
BuildRequires: python3-module-setuptools

ExcludeArch: %ix86

%description
%descr

%package -n lib%oname%abiversion
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%oname%abiversion
%descr
%summary.

%package -n lib%oname-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%oname%abiversion
Provides: %name

%description -n lib%oname-devel
%descr
%summary.

%package -n python3-module-%pypi_name
Summary: This is a Python module for Vosk
Group: Development/Python3
Requires: lib%oname%abiversion

%description -n python3-module-%pypi_name
%descr
%summary.

%prep
%setup -a1
%autopatch -p1
sed -i -e 's|@_libdir@|%_libdir|g' \
	-e 's|@abiversion@|%abiversion|g' python/vosk/__init__.py

pushd kaldi/tools
mkdir -p OpenBLAS/install/include
ln -sf %_includedir/openblas/* OpenBLAS/install/include
ln -sf %_includedir/flexiblas/* OpenBLAS/install/include
mkdir -p OpenBLAS/install/lib
ln -sf %_libdir/* OpenBLAS/install/lib
mkdir -p openfst/include openfst/lib
ln -sf %_includedir/fst openfst/include
ln -sf %_libdir/* openfst/lib
popd

%build
pushd kaldi/src
CXXFLAGS='-std=c++17 -Wno-template-id-cdtor' \
	./configure \
	--mathlib=OPENBLAS_NO_F2C \
	--shared \
	--use-cuda=no
%make_build clean depend
%make_build online2 lm rnnlm
popd

pushd src
%make_build \
	EXTRA_LDFLAGS='-Wl,-lopenblas -llapack -lblas' \
	KALDI_ROOT=../kaldi
mv libvosk.so libvosk.so.%version
popd

pushd python
%pyproject_build
popd

%install
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_libdir
install -Dpm 644 src/vosk_api.h %buildroot%_includedir
install -Dpm 644 src/libvosk.so.%version %buildroot%_libdir
pushd %buildroot%_libdir
ln -s libvosk.so.%version libvosk.so.%abiversion
ln -s libvosk.so.%version libvosk.so
popd

pushd python
%pyproject_install
popd

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%files -n lib%oname%abiversion
%_libdir/libvosk.so.%{abiversion}*

%files -n lib%oname-devel
%doc README.md
%_includedir/vosk_api.h
%_libdir/libvosk.so

%files -n python3-module-%pypi_name
%_bindir/vosk-transcriber
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Mar 03 2026 Ulysses Apokin <ulysses@altlinux.org> 1:0.3.50-alt1
- Initial build for Sisyphus.
