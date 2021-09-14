%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Name: hts_engine
Version: 1.03
Release: alt2
Packager: Michael Pozhidaev <msp@altlinux.ru>

Summary: API version of hts_engine speech synthesis system
Group: Sound
License: Simplified BSD license
URL: http://hts-engine.sourceforge.net/
Source: %{name}_API-%version.tar.gz

%package -n libHTSEngine-devel
BuildArch: noarch
Summary: C/C++ development files for hts_engine
Group: Development/C
Requires: libHTSEngine-devel-static

%package -n libHTSEngine-devel-static
Summary: The static library for libHTSEngine
Group: Development/C

%description
The hts_engine is software to synthesize speech waveform from HMMs trained by the HMM-based
speech synthesis system (HTS).

%description -n libHTSEngine-devel
This package contains files used to include hts_engine functions into C/C++ programs.

%description -n libHTSEngine-devel-static
This package contains library used for static linking of llibHTSEngien.

%prep
%setup -q -n %{name}_API-%version
%build
%add_optflags -D_FILE_OFFSET_BITS=64
%configure
%make_build

%install
make DESTDIR=%buildroot install 

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_bindir/*

%files -n libHTSEngine-devel
%_includedir/*

%files -n libHTSEngine-devel-static
%_libdir/*.a

%changelog
* Tue Sep 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.03-alt2
- Fixed build with LTO.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.03-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Jul 28 2010 Michael Pozhidaev <msp@altlinux.ru> 1.03-alt1
- First release for ALT LInux Sisyphus

