%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: oneDNN
Version: 3.13.3
Release: alt1

Summary: oneAPI Deep Neural Network Library
Summary(ru_RU.UTF-8): Библиотека примитивов глубокого обучения oneDNN

License: Apache-2.0
Group: Sciences/Computer science
Url: https://github.com/uxlfoundation/oneDNN
Vcs: https://github.com/uxlfoundation/oneDNN.git

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc gcc-c++
BuildRequires: libgomp-devel
BuildRequires: libblas-devel

%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

The oneAPI specification is available at:
https://oneapi-spec.uxlfoundation.org/specifications/oneapi/latest/elements/onednn/source/

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

%description -l ru_RU.UTF-8
oneAPI Deep Neural Network Library (oneDNN) — открытая кроссплатформенная
библиотека базовых примитивов для приложений глубокого обучения. Проект oneDNN
является частью фонда UXL и реализацией компонента oneDNN спецификации oneAPI.

Спецификация oneAPI доступна по адресу:
https://oneapi-spec.uxlfoundation.org/specifications/oneapi/latest/elements/onednn/source/

Библиотека oneDNN предназначена для разработчиков приложений и программных
платформ глубокого обучения, заинтересованных в повышении производительности
приложений на центральных и графических процессорах.

%prep
%setup

%build
%cmake -GNinja \
    -Wno-dev \
    -DONEDNN_BUILD_EXAMPLES=OFF \
    -DONEDNN_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%doc %_docdir/dnnl

%package -n libdnnl
Summary: oneDNN shared library
Summary(ru_RU.UTF-8): Разделяемая библиотека oneDNN
Group: Sciences/Computer science

%description -n libdnnl
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

This package contains the dnnl shared library.

%description -n libdnnl -l ru_RU.UTF-8
oneAPI Deep Neural Network Library (oneDNN) — открытая кроссплатформенная
библиотека базовых примитивов для приложений глубокого обучения. Проект oneDNN
является частью фонда UXL и реализацией компонента oneDNN спецификации oneAPI.

Библиотека oneDNN предназначена для разработчиков приложений и программных
платформ глубокого обучения, заинтересованных в повышении производительности
приложений на центральных и графических процессорах.

Этот пакет содержит разделяемую библиотеку dnnl.

%files -n libdnnl
%_libdir/libdnnl.so.3
%_libdir/libdnnl.so.3.13

%package -n libdnnl-devel
Summary: development files for the oneDNN shared library
Summary(ru_RU.UTF-8): Файлы для разработки с разделяемой библиотекой oneDNN
Group: Development/C

%description -n libdnnl-devel
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

This package contains development files and headers for the dnnl shared library.

%description -n libdnnl-devel -l ru_RU.UTF-8
oneAPI Deep Neural Network Library (oneDNN) — открытая кроссплатформенная
библиотека базовых примитивов для приложений глубокого обучения. Проект oneDNN
является частью фонда UXL и реализацией компонента oneDNN спецификации oneAPI.

Библиотека oneDNN предназначена для разработчиков приложений и программных
платформ глубокого обучения, заинтересованных в повышении производительности
приложений на центральных и графических процессорах.

Этот пакет содержит файлы и заголовки для разработки с разделяемой библиотекой
dnnl.

%files -n libdnnl-devel
%_libdir/libdnnl.so
%_libdir/cmake/dnnl
%_includedir/oneapi/dnnl
%_includedir/dnnl*.h
%_includedir/dnnl*.hpp

%changelog
* Wed Sep 30 2026 Georgij Tsarin <crystarm@altlinux.org> 3.13.3-alt1
- 3.8.1 -> 3.13.3

* Wed Aug 06 2025 Arseny Maslennikov <arseny@altlinux.org> 3.8.1-alt1
- Initial build for ALT Sisyphus.
