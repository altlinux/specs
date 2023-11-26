# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libbpg
Version:	0.9.8
Release:	alt1_3
Summary:	A library of functions for manipulating BPG image format files
License:	LGPLv2+ and BSD
Group:		Graphics
Url:		http://bellard.org/bpg/
Source0:	http://bellard.org/bpg/%{name}-%{version}.tar.gz
Patch0:		libbpg-0.9.6-Makefile.patch
BuildRequires:	ccmake cmake ctest
BuildRequires:	yasm
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	libnuma-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(SDL_image)

ExcludeArch: %{arm}
Source44: import.info

%description
BPG (Better Portable Graphics) is a image format whose purpose is to
replace the JPEG image format when quality or file size is an issue. Its
main advantages are:

* High compression ratio. Files are much smaller than JPEG for similar quality.
* Supported by most Web browsers with a small Javascript decoder.
* Based on a subset of the HEVC open video compression standard.
* Supports the same chroma formats as JPEG (grayscale, YCbCr 4:2:0, 4:2:2,
  4:4:4) to reduce the losses during the conversion. An alpha channel is
  supported. The RGB, YCgCo and CMYK color spaces are also supported.
* Native support of 8 to 14 bits per channel for a higher dynamic range.
* Lossless compression is supported.
* Various metadata (such as EXIF, ICC profile, XMP) can be included.

%prep
%setup -q
%patch0 -p1


%build
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog README doc html post.js
%{_bindir}/bpgdec
%{_bindir}/bpgenc
%{_bindir}/bpgview


%changelog
* Sun Nov 26 2023 Igor Vlasenko <viy@altlinux.org> 0.9.8-alt1_3
- more arches

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_1
- new version

