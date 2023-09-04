%define _unpackaged_files_terminate_build 1
%define pypi_name lief

%def_with check

Name: liblief
Version: 0.12.3
Release: alt1

Summary: Library to instrument executable formats
License: Apache-2.0
Group: System/Libraries

Url: https://github.com/lief-project/LIEF
VCS: https://github.com/lief-project/LIEF.git

Source0: %name-%version.tar
Source1: %name-%version-lief_tests.tar

Patch1: 0001-fix-link-with-libpython3.so.patch
Patch2: 0002-fix-warning-Kmulti-line-comment.patch
Patch3: 0003-fix-modules-for-python-test.patch
Patch4: 0004-tests-elf-test_dynamic.py-skip-some-tests-for-aarch6.patch
Patch5: 0005-tests-elf-test_bin2lib.py-skip-some-tests-for-armh-i.patch
Patch6: 0006-tests-elf-test_static.py-skip-some-tests-for-armh-an.patch
Patch7: 0007-tests-pe-test_authenticode.py-skip-some-tests-for-p10.patch
Patch8: 0008-fix-build-for-gcc13.patch

Provides: python3(%pypi_name.PE)

BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%define _description \
The purpose of this project is to provide a cross platform library \
which can parse, modify and abstract ELF, PE and MachO formats.

%description
%_description

%package devel
Summary: Development files for LIEF
Group: Development/C++
Requires: %name
%description devel
This package contains development headers for LIEF.

%_description

%package -n python3-module-%pypi_name
Summary: Python 3 interface for LIEF
Group: Development/Python3
Requires: %name
%description -n python3-module-%pypi_name
%_description

%prep
%setup -a1
%autopatch -p1

%build
# debug and parallel jobs
sed -i "s|inplace=1|inplace=1\ndebug=1\nparallel=%_smp_build_ncpus|" setup.cfg
%pyproject_build

%check
%if_with check
# module utils provides methods for testing library
cp tests/utils.py.in tests/utils.py
# add os env variable "LIEF_SAMPLES_DIRECTORY"
sed -i "s|\"@LIEF_SAMPLES_DIRECTORY@\"|os.environ['LIEF_SAMPLES_DIRECTORY']|" tests/utils.py
# fix import files mismatch
mv tests/elf/test_parser.py tests/elf/test_parser_elf.py
sed -i "s|test_parser.py|test_parser_elf.py|" tests/elf/CMakeLists.txt
mv tests/pe/test_builder.py tests/pe/test_builder_pe.py
sed -i "s|test_builder.py|test_builder_pe.py|" tests/elf/CMakeLists.txt
# run
LIEF_SAMPLES_DIRECTORY=$PWD/lief_tests PYTHONPATH=$PWD/tests \
python3 -m pytest
%endif

%install
python3 -m pyproject_installer -v install --destdir=%buildroot --no-strip-dist-info
cp Acknowledgements AUTHORS CHANGELOG README.md \
%buildroot%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
# liblief.so
# libLIEF.so -> liblief.so
# lief.so -> liblief.so
pushd %buildroot%_libdir
find -name lief*.so -exec mv "{}" liblief.so \;
ln -s  liblief.so libLIEF.so
popd
# lief.so -> ../../liblief.so
pushd %buildroot%python3_sitelibdir
ln -s ../../liblief.so %pypi_name.so
popd
# collecting the necessary files for devel:
%define LIEF_DIR %buildroot%_includedir/LIEF/
%define LIEF_DIR_internal %LIEF_DIR/third-party/internal/
mkdir -p %buildroot%_includedir
cp -r include/LIEF %buildroot%_includedir/
find build/ -name config.h -exec cp "{}" %LIEF_DIR \;
find build/*/include/ -name version.h -exec cp "{}" %LIEF_DIR \;
mkdir -p %LIEF_DIR_internal
find build/*/include/ -name span.hpp -exec cp "{}" %LIEF_DIR_internal \;
find build/*/include/ -name leaf.hpp -exec cp "{}" %LIEF_DIR_internal \;

%files
%doc Acknowledgements AUTHORS CHANGELOG LICENSE README.md
%_libdir/liblief.so
%_libdir/libLIEF.so
%_libdir/lief.so

%files devel
%_includedir/LIEF

%files -n python3-module-%pypi_name
%_bindir/elf_reader.py
%_bindir/macho_reader.py
%_bindir/pe_reader.py
%python3_sitelibdir/%pypi_name.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 28 2023 Vasiliy Kovalev <kovalev@altlinux.org> 0.12.3-alt1
- Initial build for Sisyphus
