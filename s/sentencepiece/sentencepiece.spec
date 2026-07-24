%define _unpackaged_files_terminate_build 1
%define pypi_name sentencepiece
%define mod_name %pypi_name

%define sover 0

Name: sentencepiece
Version: 0.2.1
Release: alt2

Summary: Unsupervised text tokenizer for neural network-based text generation
License: Apache-2.0
Group: Sciences/Computer science
Url: https://github.com/google/sentencepiece

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libprotobuf-devel
BuildRequires: libabseil-cpp-devel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
SentencePiece is an unsupervised text tokenizer and detokenizer mainly
designed for neural network-based text generation systems where the
vocabulary size is predetermined before model training.

This package contains command line tools for training, encoding,
decoding and inspecting SentencePiece models.

%package -n lib%name%sover
Summary: Shared libraries for SentencePiece
Group: System/Libraries

%description -n lib%name%sover
SentencePiece is an unsupervised text tokenizer and detokenizer mainly
designed for neural network-based text generation systems.

This package contains the shared libraries used by applications linked
with SentencePiece.

%package -n lib%name-devel
Summary: Development files for SentencePiece
Group: Development/C++
AutoReq: yes, nocpp
Requires: lib%name%sover = %EVR
Requires: libprotobuf-devel

%description -n lib%name-devel
This package contains headers, pkg-config metadata and linker files
needed to build applications using SentencePiece.

%package -n python3-module-%pypi_name
Summary: Unsupervised text tokenizer and detokenizer
Group: Development/Python3
Requires: lib%name%sover = %EVR
Url: https://pypi.org/project/sentencepiece/
Vcs: https://github.com/google/sentencepiece

%description -n python3-module-%name
Python wrapper for SentencePiece. This API will offer the encoding,
decoding and training of Sentencepiece.

%prep
%setup

# init_test calls ParseCommandLineFlags() after test_main already parsed flags.
sed -i '/init_test\.cc/d' src/CMakeLists.txt

%build
%cmake -GNinja \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_INSTALL_LIBDIR:PATH=%_lib \
	-DSPM_BUILD_TEST:BOOL=ON \
	-DSPM_ENABLE_TCMALLOC:BOOL=OFF \
	-DSPM_PROTOBUF_PROVIDER:STRING=package \
	-DSPM_ABSL_PROVIDER:STRING=package \
	%nil

%cmake_build

cd python
export CPATH=../src # Points to headers dir
export PKG_CONFIG_PATH=../%_cmake__builddir # Points to dir with pkg-conf file
export LIBRARY_PATH=../%_cmake__builddir/src # Points to library dir
%pyproject_build

%install
%cmake_install

# Upstream always builds and installs static libraries.
# Do not package them in the main -devel package.
rm -f %buildroot%_libdir/libsentencepiece.a
rm -f %buildroot%_libdir/libsentencepiece_train.a

cd python
%pyproject_install

%check
%ctest

cd python
export LD_LIBRARY_PATH=%buildroot%_libdir
%pyproject_run_pytest -ra

%files
%doc README.md
%_bindir/spm_decode
%_bindir/spm_encode
%_bindir/spm_export_vocab
%_bindir/spm_normalize
%_bindir/spm_train

%files -n lib%name%sover
%doc README.md
%_libdir/libsentencepiece.so.%sover
%_libdir/libsentencepiece.so.%sover.*
%_libdir/libsentencepiece_train.so.%sover
%_libdir/libsentencepiece_train.so.%sover.*

%files -n lib%name-devel
%_includedir/sentencepiece*.h
%_libdir/libsentencepiece.so
%_libdir/libsentencepiece_train.so
%_pkgconfigdir/sentencepiece.pc

%files -n python3-module-%name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 24 2026 Anton Zhukharev <ancieg@altlinux.org> 0.2.1-alt2
- NMU: Packaged python bindings.

* Wed May 20 2026 Artyom Sinyugin <writers@altlinux.org> 0.2.1-alt1
- Initial build.
