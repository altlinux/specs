BuildRequires: libgomp-devel /proc
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libimagequant
Version:        2.11.3
Release:        alt1_1
Summary:        Palette quantization library

License:        GPLv3+ and MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-common
Source44: import.info

%description
Small, portable C library for high-quality conversion of RGBA images to 8-bit
indexed-color (palette) images.


%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q



%build
%configure --with-openmp
%make_build shared


%install
install -Dpm 0755 %{name}.so.0 %{buildroot}%{_libdir}/%{name}.so.0
ln -s %{name}.so.0 %{buildroot}%{_libdir}/%{name}.so
install -Dpm 0644 %{name}.h %{buildroot}%{_includedir}/%{name}.h


%files
%doc COPYRIGHT
%doc README.md CHANGELOG
%{_libdir}/%{name}.so.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so


%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.11.3-alt1_1
- new version

