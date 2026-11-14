%define skia_version 3.119.4
%define native_soname 0.60831.0

Name: libHarfBuzzSharp
Version: 8.3.1.5
Release: alt1

Summary: System HarfBuzz native library for HarfBuzzSharp

License: MIT
Group: System/Libraries
URL: https://github.com/mono/SkiaSharp
# Source-url: https://github.com/mono/SkiaSharp/archive/refs/tags/v%skia_version.tar.gz
Source: %name-%version.tar
Source1: generate-shim.py
Source2: check-library.py
Source3: README.ALT.md

BuildRequires: gcc /usr/bin/python3 pkgconfig(harfbuzz) >= 8.3.1

%description
Native library loaded by HarfBuzzSharp, the .NET OpenType text shaping
bindings used by SkiaSharp 3.x and Avalonia. This thin library uses the
system HarfBuzz instead of bundling the native NuGet binary.

%prep
%setup
cp %SOURCE1 %SOURCE2 %SOURCE3 .

%build
python3 generate-shim.py binding/HarfBuzzSharp/HarfBuzzApi.generated.cs
gcc %optflags -fPIC -shared -fvisibility=hidden \
    $(pkg-config --cflags harfbuzz) shim.c \
    -Wl,-z,defs -Wl,-soname,%name.so.%native_soname \
    -Wl,--version-script=native/linux/libHarfBuzzSharp/libHarfBuzzSharp.map \
    $(pkg-config --libs harfbuzz) -o %name.so.%native_soname
ln -s %name.so.%native_soname %name.so

%check
python3 check-library.py ./%name.so symbols.txt

%install
install -Dm644 %name.so.%native_soname %buildroot%_libdir/%name.so.%native_soname
ln -s %name.so.%native_soname %buildroot%_libdir/%name.so

%files
%_libdir/%name.so
%_libdir/%name.so.%native_soname
%doc LICENSE* README.ALT.md symbols.txt check-library.py

%changelog
* Fri Nov 13 2026 Vitaly Lipatov <lav@altlinux.ru> 8.3.1.5-alt1
- initial build for ALT Linux with system HarfBuzz.

