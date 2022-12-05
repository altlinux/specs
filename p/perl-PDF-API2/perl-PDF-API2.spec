# SPEC file for Perl module PDF::API2
%define _unpackaged_files_terminate_build 1
%define real_name PDF-API2

Name: perl-PDF-API2
Version: 2.044
Release: alt1

Summary: Perl module for creation and modification PDF files
Summary(ru_RU.UTF-8): модуль Perl для создания и изменения файлов PDF

License: %lgpl2plus
Group: Development/Perl
URL: https://metacpan.org/dist/PDF-API2/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar
Patch0: %real_name-2.042-alt-fix_fonts_path.patch
Patch1: %real_name-0.51-alt-Lbrk_pl.patch

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: fontconfig gem-power-assert perl perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Devel-Cycle perl-Encode perl-IO-Compress perl-JSON-PP perl-Math-Complex perl-PadWalker perl-Parse-CPAN-Meta perl-Sub-Uplevel perl-Unicode-Normalize perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Font-TTF perl-GD perl-Test-Exception perl-Test-Memory-Cycle perl-unicore

%description
PDF::API2 is a Perl module to facilitate the creation and
modification of high-quality "Portable Document Format"
(PDF) files. PDF::API2:
- works with more than one PDF file open at once;
- presents an object-oriented API to the user;
- supports the 14 base PDF Core Fonts, subset of PDF CJK Fonts, 
  Adobe Type1 (.pfa/pfb), TrueType (.ttf) and OpenType (.ttf/otf)
  fonts;
- supports images in JPEG, PND, GIF, TIFF, PBM, PGM, PPM formats;
- supports EAN13, CODE39, CODE39EXT, CODE25INT, CODABAR barcodes;
- supports rudimentary modification and import from existing PDFs.

%description -l ru_RU.UTF-8
PDF::API2 - модуль  Perl для  создания и изменения файлов в
формате PDF (Portable Document Format). PDF::API2:
- позволяет одновременно работать с более чем одним открытым 
  файлом PDF;
- предоставляет пользователю объектно-ориентированный интерфейс;
- поддерживает 14 базовых шрифтов PDF, подмножество шрифтов CJK.
  шрифты Adobe Type1 (.pfa/pfb), TrueType (.ttf) и OpenType 
  (.ttf/otf);
- поддерживает работу с изображениями в форматах JPEG, PND, GIF, 
  TIFF, PBM, PGM и PPM;
- поддерживает штрихкоды в кодировках EAN13, CODE39, CODE39EXT, 
  CODE25INT, CODABAR;
- поддерживает простую модификацию и импорт из существующих 
  документов PDF.

%prep
%setup  -n %real_name-%version
%patch0
%patch1

mv -f -- LICENSE LICENSE.LGPL.orig
ln -s -- $(relative %_licensedir/LGPL %_docdir/%name/LICENSE) LICENSE

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README PATENTS
%doc contrib*
%doc --no-dereference LICENSE

%perl_vendor_privlib/PDF/API2*
%exclude /.perl.req

%changelog
* Sun Dec 04 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.044-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.043-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.042-alt1
- New version

* Sat May 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.040-alt1
- New version
- Update URL

* Fri Mar 12 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.039-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.038-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.037-alt1
- New version

* Sat Aug 17 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.035-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.034-alt1
- New version

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.033-alt1
- New version

* Tue Jul 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.032-alt1
- New version

* Mon Mar 20 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.031-alt2
- Fix build with Perl 5.24.1

* Sun Jan 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.031-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.030-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.028-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.027-alt1
- New version

* Mon Sep 28 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.025-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.023-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.020-alt1
- New version

* Fri Oct 19 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.019-alt1
- New version
- Fix defaul fonts search path (Closes: 24393)

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.73-alt1.1
- rebuilt with perl 5.12
- buildarch -> noarch

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.73-alt1
- New version 0.73

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.72-alt1
- New version 0.72.003

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.69-alt1
- New version 0.69

* Wed Aug 29 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.63-alt1
- New version 0.63

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.62-alt1
- New version 0.62
- Fix typos in package description
- Spec file cleanup

* Thu Apr 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.60-alt1
- New version 0.60

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.59.002-alt1
- New version 0.59.002

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt1
- New version 0.55
  * several bugfixes

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.53-alt1
- Initial build for ALT Linux

* Sat Jul 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.53-alt0
- 0.53

* Mon May 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt0.1
- Fix Summary, description

* Sat May 06 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt0
- Initial build

