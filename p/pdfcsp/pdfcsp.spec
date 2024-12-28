%define _unpackaged_files_terminate_build 1

Name: pdfcsp
Version: 0.2
Release: alt1
Summary: Library for CryptoPro pdf electronic signatures support.
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.basealt.space/proskurinov/csp_pdf

Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake ninja-build rpm-macros-cmake rpm-build-licenses
BuildRequires: libqpdf-devel boost-devel-headers boost-interprocess-devel glibc-devel libsignimage_c_wrapper-devel libspdlog-devel libfmt-devel
BuildRequires: boost-locale-devel gettext-tools boost-program_options-devel
%description
Library for CryptoPro pdf electronic signatures support.


%package -n libaltcsp
Summary: The shared library for CryptoPro 5 support.
Group: System/Libraries 
Requires: glibc-core glibc-pthread
%description -n libaltcsp
The shared library for CryptoPro 5 support.

%package -n libaltcsp-devel
Summary: Developer headers for libaltcsp library
Group: Development/C
Requires: libaltcsp
%description -n libaltcsp-devel
Developer headers for libaltcsp 

%package -n libcspforpoppl-devel
Summary: Developer headers to use within the Poppler library
Group: Development/C
BuildArch: noarch
%description -n libcspforpoppl-devel
Summary: Developer headers to use within the Poppler library

%package -n libcsppdf
Summary: The shared library for pdf electronic signatures support.
Group: System/Libraries
Provides: libcsppdf
Requires: libaltcsp libsignimage_c_wrapper-devel libqpdf-devel
%description -n libcsppdf
The shared library for pdf electronic signatures support.

%package -n libcsppdf-devel
Summary: Developer headers for libcsppdf library
Group: Development/C
Requires: libcsppdf
%description -n libcsppdf-devel 
Developer headers for libcsppdf 

%package -n pdfcspcli
Summary: Command line tools for pdf signatures
Group: Office
Requires: libcsppdf glibc-locales
%description -n pdfcspcli
Command line tools for pdf signatures

%prep
%setup

%ifarch %ix86
%define _pvoid_size 4
%else
%define _pvoid_size 8
%endif

%build

%cmake  -DCMAKE_BUILD_TYPE:STRING=Release -DSIZEOF_VOID_P=%_pvoid_size -DIPC_EXEC_DIR=%_usr/libexec/ -DTRANSLATIONS_INSTALL_DIR=%_datadir/locale/ -G Ninja
%cmake_build

%install libaltcsp
%cmake_install --config Release

%files -n libaltcsp
%_libdir/libaltcsp.so.0.1
%_libdir/libaltcsp.so.0
%_libdir/libcsp_c_bridge.so.0.1
%_libdir/libcsp_c_bridge.so.0

%_usr/libexec/altcspIpcProvider
%_libdir/libcsp_ipc_client.so.0.1
%_libdir/libcsp_ipc_client.so.0

%files -n libaltcsp-devel
%_libdir/libaltcsp.so
%_libdir/libcsp_c_bridge.so
%_libdir/libcsp_ipc_client.so

%_includedir/%name/altcsp.hpp
%_includedir/%name/message.hpp
%_includedir/%name/asn1.hpp
%_includedir/%name/certificate.hpp
%_includedir/%name/d_name.hpp
%_includedir/%name/ocsp.hpp
%_includedir/%name/resolve_symbols.hpp
%_includedir/%name/typedefs.hpp
%_includedir/%name/bool_results.hpp
%_includedir/%name/bridge_obj_storage.hpp
%_includedir/%name/c_bridge.hpp
%_includedir/%name/pod_structs.hpp
%_includedir/%name/ipc_client.hpp
%_includedir/%name/ipc_result.hpp
%_includedir/%name/ipc_typedefs.hpp
%_includedir/%name/cert_common_info.hpp
%_includedir/%name/logger_utils.hpp

%files -n libcspforpoppl-devel
%_includedir/%name/csp_for_poppl.hpp
%_includedir/%name/structs.hpp

%files -n libcsppdf
%_libdir/libcsppdf.so.0.1
%_libdir/libcsppdf.so.0

%files -n libcsppdf-devel
%_libdir/libcsppdf.so
%_includedir/%name/csppdf.hpp
%_includedir/%name/pdf_pod_structs.hpp
%_includedir/%name/pdf_structs.hpp
%_includedir/%name/pdf_defs.hpp
%_includedir/%name/pdf_update_object_kit.hpp
%_includedir/%name/acro_form.hpp
%_includedir/%name/form_x_object.hpp
%_includedir/%name/image_obj.hpp
%_includedir/%name/sig_field.hpp
%_includedir/%name/sig_val.hpp
%_includedir/%name/pdf_csp_c.hpp

%files -n pdfcspcli
%_bindir/signpdf
%_datadir/locale/ru_RU/LC_MESSAGES/signpdf.mo

%changelog
* Thu Dec 26 2024 Oleg Proskurin <proskur@altlinux.org> 0.2-alt1
- 0.2 Bug fixing [svacer + valgrind]

* Tue Dec 24 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt3
- CLI tool was added

* Thu Dec 19 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt2
- License info was added

* Thu Aug 29 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
