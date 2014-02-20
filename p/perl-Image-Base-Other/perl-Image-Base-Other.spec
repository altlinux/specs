# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Image/Base.pm) perl(List/Util.pm) perl(Test.pm)
# END SourceDeps(oneline)
%define module_version 9
%define module_name Image-Base-Other
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 9
Release: alt2
Summary: Misc other helpers for Image::Base.
Group: Development/Perl
License: gpl
URL: http://user42.tuxfamily.org/image-base-other/index.html

Source0: http://cpan.org.ua/authors/id/K/KR/KRYDE/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
`Image::Base::Text' extends `Image::Base' to create or update text files
treated as grids of characters, or just to create a grid of characters in
memory.

Colours for drawing can be a single character to set in the image, or
there's an experimental `-colour_to_character' attribute to map names to
characters.  Currently black, #000000, #000000000000 and clear all become
spaces and anything else becomes a "*".  Perhaps that will
change.

Perl wide characters can be used, in new enough Perl, though currently
there's nothing to set input or output encoding for file read/write (making
it fairly useless, unless perhaps you've got global PerlIO layers setup).


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc COPYING Changes
%perl_vendor_privlib/I*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 9-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 9-alt1
- initial import by package builder

