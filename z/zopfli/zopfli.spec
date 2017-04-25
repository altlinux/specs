Name: zopfli
Version: 1.0.1
Release: alt1

Summary: Zlib compatible better compressor

License: ASL 2.0
Group: File tools
Url: https://github.com/google/zopfli

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/google/%name/archive/%name-%version.tar.gz
Source: %name-%version.tar

# https://github.com/google/zopfli/pull/92
Patch: 0001-Honor-user-C-XX-FLAGS.patch

BuildRequires: gcc-c++

%description
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5 percent) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

%prep
%setup

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" %make_build \
    zopfli zopflipng

%install
mkdir -p %buildroot%_bindir
install -m 0755 zopfli zopflipng %buildroot%_bindir/

%files
%doc COPYING
%doc CONTRIBUTORS README README.zopflipng
%_bindir/zopfli
%_bindir/zopflipng

%changelog
* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar  2 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-2
- Ship zopflipng

* Wed Feb 10 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-1
- Update to 1.0.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.0-1
- upstream release 1.0.0

* Sun Mar 03 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.20130303gitacc035
- initial spec
