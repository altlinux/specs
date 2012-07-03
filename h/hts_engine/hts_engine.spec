
Name: hts_engine
Version: 1.03
Release: alt1
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
* Wed Jul 28 2010 Michael Pozhidaev <msp@altlinux.ru> 1.03-alt1
- First release for ALT LInux Sisyphus

