%define _name rnnoise
%define sover 0
# cat model_version
%define model_version 0b50c45
%def_disable doc

Name: lib%_name
Version: 0.2
Release: alt1.1

Summary: Recurrent neural network for audio noise reduction
License: BSD-2-Clause
Group: System/Libraries
Url: https://gitlab.xiph.org/xiph/rnnoise

Source: %name-%version.tar
# see autogen.sh & download_model.sh
Source1: https://media.xiph.org/rnnoise/models/rnnoise_data-%model_version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
%{?_enable_doc:BuildRequires: doxygen graphviz}

%description
RNNoise is a noise suppression library based on a recurrent neural network.

While it is meant to be used as a library, a simple command-line tool is
provided as an example. It operates on RAW 16-bit (machine endian) mono PCM
files sampled at 48 kHz. It can be used as:

./examples/rnnoise_demo <noisy speech> <output denoised>

The output is also a 16-bit raw PCM file.

%package devel
Group: Development/C
Summary: Devel files for %name
Requires: %name = %EVR

%description devel
Devel files for %name.

%prep
%setup -a1
%patch -p1

cat > package_version << _EOF_
    PACKAGE_VERSION=%version
_EOF_

%build
%ifarch %ix86
%add_optflags -msse2
%endif
%autoreconf
%configure \
    --disable-static \
    %{subst_enable doc} \
%ifarch x86_64
    --enable-x86-rtcd
%endif
%nil
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/

%check
%make -k check VERBOSE=1

%files
%doc COPYING
%doc TRAINING-README AUTHORS README
%_libdir/%name.so.%{sover}*

%files devel
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Sat Dec 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1.1
- fixed build for aarch64

* Sat Dec 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2
- switched build to upstream git

* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 0-alt0.3.20210312git7f449bf
- initial build for ALT Sisyphus (thanks, Fedora!)

* Sat Mar 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.3.20210312git7f449bf
- build(update): 20210312git7f449bf

* Sun Jan 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20210122git1cbdbcf
- Initial package
