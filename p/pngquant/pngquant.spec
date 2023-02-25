Group: Graphics
BuildRequires: libgomp-devel /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global libname libimagequant

Name:           pngquant
Version:        2.18.0
Release:        alt1_1
Summary:        PNG quantization tool for reducing image file size

License:        GPL-3.0-or-later

URL:            http://%{name}.org
Source0:        https://github.com/pornel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Comment out failing test on EL < 8 due to old libpng
Patch1:         pngquant-old_libpng.patch

BuildRequires:  gcc
BuildRequires:  libpng-devel libpng17-tools
BuildRequires:  zlib-devel >= 1.2.3
BuildRequires:  liblcms2-devel
BuildRequires:  %{libname}-devel

Requires:       libpng16 >= 1.2.46
Requires:       zlib >= 1.2.3
Requires:       %{libname}
Source44: import.info


%description
%{name} converts 24/32-bit RGBA PNG images to 8-bit palette with alpha channel
preserved.  Such images are compatible with all modern web browsers and a
compatibility setting is available to help transparency degrade well in
Internet Explorer 6.  Quantized files are often 40-70 percent smaller than
their 24/32-bit version. %{name} uses the median cut algorithm.


%prep
%setup -q
%if 0%{?rhel} &&  0%{?rhel} < 8
%patch1 -p1 -b .oldlibpng
%endif


%build
# add some speed-relevant compiler-flags
export CFLAGS="%{optflags} -fno-math-errno -funroll-loops -fomit-frame-pointer -fPIC"
%configure --with-openmp --with-libimagequant
%make_build


%install
%makeinstall_std


%check
%make_build test


%files
%doc README.md CHANGELOG
%doc --no-dereference COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.18.0-alt1_1
- update to new release by fcimport

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 2.17.0-alt1_0
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.16.0-alt1_1
- update to new release by fcimport

* Tue Sep 28 2021 Michael Shigorin <mike@altlinux.org> 2.15.1-alt1_2.2
- built for sisyphus

* Tue Sep 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.15.1-alt1_2.1
- added patch for Elbrus build

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 2.15.1-alt1_2
- update to new release by fcimport

* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 2.14.1-alt1_1
- update to new release by fcimport

* Sun Nov 22 2020 Igor Vlasenko <viy@altlinux.ru> 2.12.6-alt1_3
- build on armh

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 2.12.6-alt1_2
- update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.12.2-alt1_2
- to Sisyphus as dependency

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.11.2-alt1_2
- new version
- moved to autoimports (check fails)

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1
- update to new release by fcimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1
- converted for ALT Linux by srpmconvert tools

