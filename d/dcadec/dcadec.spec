Name: dcadec
Version: 0.2.0
Release: alt1

Summary: DTS Coherent Acoustics decoder
License: LGPL
Group: Sound

Source: %name-%version.tar

%description
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.
Supported features:
* Decoding of standard DTS core streams with up to 5.1 channels
* Decoding of DTS-ES streams with discrete back channel
* Decoding of High Resolution streams with up to 7.1 channels and extended bitrate
* Decoding of 96/24 core streams
* Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
* Downmixing to stereo and 5.1 using embedded coefficients

%package -n libdcadec
Summary: DTS Coherent Acoustics decoder shared library
Group: System/Libraries

%package -n libdcadec-devel
Summary: DTS Coherent Acoustics decoder shared library
Group: Development/C

%description -n libdcadec
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.
Supported features:
* Decoding of standard DTS core streams with up to 5.1 channels
* Decoding of DTS-ES streams with discrete back channel
* Decoding of High Resolution streams with up to 7.1 channels and extended bitrate
* Decoding of 96/24 core streams
* Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
* Downmixing to stereo and 5.1 using embedded coefficients
This package contains %name shared library

%description -n libdcadec-devel
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.
Supported features:
* Decoding of standard DTS core streams with up to 5.1 channels
* Decoding of DTS-ES streams with discrete back channel
* Decoding of High Resolution streams with up to 7.1 channels and extended bitrate
* Decoding of 96/24 core streams
* Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
* Downmixing to stereo and 5.1 using embedded coefficients
This package contains development part of %name

%prep
%setup
cat >> .config << E_O_F
CONFIG_SHARED=1
PREFIX=%prefix
LIBDIR=%_libdir
E_O_F

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/dcadec

%files -n libdcadec
%_libdir/*.so.*

%files -n libdcadec-devel
%_libdir/*.so
%_pkgconfigdir/dcadec.pc
%_includedir/libdcadec

%changelog
* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
