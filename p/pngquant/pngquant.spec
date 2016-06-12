Group: Graphics
BuildRequires: libgomp-devel /proc
# add some speed-relevant compiler-flags
%global optflags %(echo %{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC )

%global libname libimagequant

Name:       pngquant
Version:    2.7.0
Release:    alt1_1
Summary:    PNG quantization tool for reducing image file size

License:    GPLv3+

URL:        http://%{name}.org
Source0:    https://github.com/pornel/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  libpng-devel >= 1.2.46
BuildRequires:  zlib-devel >= 1.2.3
BuildRequires:  liblcms2-devel
Requires:       libpng%{?_isa} >= 1.2.46
Requires:       zlib%{?_isa} >= 1.2.3
Requires:       %{libname}%{?_isa} = %{version}
Source44: import.info


%description
%{name} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha channel
preserved.  Such images are compatible with all modern web browsers and a
compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{name} uses the median cut algorithm.


%package -n %{libname}
Group: Graphics
Summary:    Small, portable C lib for HQ conversion of RGBA to 8-bit indexed-color


%description -n %{libname}
%{libname} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha
channel preserved.  Such images are compatible with all modern web browsers and
a compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{libname} uses the median cut algorithm.


%package -n %{libname}-devel
Group: Graphics
Summary:    Development files for %{libname}
Requires:   %{libname}%{?_isa} = %{version}


%description -n %{libname}-devel
This package contains files for development with %{libname}.
There is also some brief API-documentation.


%prep
%setup -q
rm -f lib/configure


%build
%configure --with-openmp
%make_build bin.shared


%install
%makeinstall_std

mkdir -p %{buildroot}%{_includedir}/imagequant \
    %{buildroot}%{_libdir}

# install libimagequant
install -pm 0755 lib/%{libname}.so.0 \
    %{buildroot}%{_libdir}
ln -fs %{libname}.so.0 %{buildroot}%{_libdir}/%{libname}.so

install -pm 0644 lib/*.h \
    %{buildroot}%{_includedir}/imagequant

%check
# needed by ld / testsuite to find libimagequant
export LD_LIBRARY_PATH="$(pwd)/lib:$LD_LIBRARY_PATH"
make test.shared


%files
# EPEL6 support https://fedoraproject.org/wiki/EPEL:Packaging#The_.25license_tag
%{!?_licensedir:%global license %doc}
%doc README.md CHANGELOG
%doc COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
# EPEL6 support https://fedoraproject.org/wiki/EPEL:Packaging#The_.25license_tag
%{!?_licensedir:%global license %doc}
%doc lib/COPYRIGHT
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%doc lib/MANUAL.md
%{_includedir}/imagequant
%{_libdir}/%{libname}.so


%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1
- converted for ALT Linux by srpmconvert tools

