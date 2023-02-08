%define _unpackaged_files_terminate_build 1
%filter_from_requires /^perl.unicore.Lbrk.pl./d
%define module_name PDF-Builder

Name: perl-PDF-Builder
Version: 3.025
Release: alt1

Summary: Facilitates the creation and modification of PDF files

License: open_source
Group: Development/Perl
Url: https://www.catskilltech.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PM/PMPERRY/%module_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
BuildRequires: perl(Compress/Zlib.pm) perl(Encode.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FileHandle.pm) perl(Font/TTF.pm) perl(Graphics/TIFF.pm) perl(IO/File.pm) perl(IPC/Cmd.pm) perl(Image/PNG/Const.pm) perl(Image/PNG/Libpng.pm) perl(List/Util.pm) perl(Math/Trig.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/Memory/Cycle.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Unicode/UCD.pm) perl(base.pm)

%description
use PDF::Builder;

    # Create a blank PDF file
    $pdf = PDF::Builder->new();

    # Open an existing PDF file
    $pdf = PDF::Builder->open('some.pdf');

    # Add a blank page
    $page = $pdf->page();

    # Retrieve an existing page
    $page = $pdf->openpage($page_number);

    # Set the page size
    $page->mediabox('Letter');

    # Add a built-in font to the PDF
    $font = $pdf->corefont('Helvetica-Bold');

    # Add an external TTF font to the PDF
    $font = $pdf->ttfont('/path/to/font.ttf');

    # Add some text to the page
    $text = $page->text();
    $text->font($font, 20);
    $text->translate(200, 700);
    $text->text('Hello World!');

    # Save the PDF
    $pdf->saveas('/path/to/new.pdf');

%package examples
Summary: %module_name examples
Group: Development/Perl
Requires: %name = %EVR

BuildArch: noarch

%description examples
Examples for %module_name.


%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes docs README.md examples CONTRIBUTING.md
%perl_vendor_privlib/P*

%files examples
%doc examples

%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 3.025-alt1
- new version

* Tue Sep 13 2022 Igor Vlasenko <viy@altlinux.org> 3.024-alt1
- new version

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.org> 3.023-alt1
- new version

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 3.022-alt1
- new version

* Wed Dec 30 2020 Igor Vlasenko <viy@altlinux.ru> 3.021-alt1
- new version

* Wed Dec 02 2020 Vitaly Lipatov <lav@altlinux.ru> 3.020-alt2
- human build for ALT Sisyphus
- separate examples to the subpackage

* Mon Nov 30 2020 Igor Vlasenko <viy@altlinux.ru> 3.020-alt1
- updated by package builder

* Wed Jul 29 2020 Igor Vlasenko <viy@altlinux.ru> 3.019-alt1
- updated by package builder

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 3.018-alt1
- updated by package builder

* Fri Jan 10 2020 Igor Vlasenko <viy@altlinux.ru> 3.017-alt1
- updated by package builder

* Sun Aug 18 2019 Igor Vlasenko <viy@altlinux.ru> 3.016-alt1
- updated by package builder

* Mon May 20 2019 Igor Vlasenko <viy@altlinux.ru> 3.015-alt1
- updated by package builder

* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.014-alt1
- updated by package builder

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 3.013-alt1
- initial import by package builder

