Name: ruby-doc-extra
Version: 0.1
Release: alt7

Summary: A set of extra documentation for Ruby language
License: Distributable
Group: Development/Ruby

Url: http://pragmaticprogrammer.com
Source0: ProgrammingRuby-cvs.tar.bz2
Source1: http://www.rubycentral.com/faq/rubyfaq_a4.pdf
Source2: http://www.approximity.com/euruko03/slides/tobias/peters.pdf
Source3: http://www.approximity.com/euruko03/slides/hal/rubyesque.tar.gz
Source4: http://www.rubycentral.com/downloads/files/ProgrammingRuby-0.3a.tar.bz2
Source5: pruby-permission.txt
Source6: URLs.txt
Patch0: ProgrammingRuby-1.8.1.patch.bz2
Packager: Michael Shigorin <mike@altlinux.org>

AutoReq: no
BuildRequires: tetex, tetex-latex, tetex-dvips, urw-fonts, ruby1.8, libruby1.8-devel, ruby1.8-stdlibs-tk, groff-base, ghostscript-utils

BuildArch: noarch
ExclusiveArch: %ix86

%description
This package provides a set of extra docs for the Ruby language
(please note that it's relevant for 1.6, mostly relevant for 1.8
and somewhat relevant for 1.9+).

Among the other components it includes:
 - Ruby FAQ;
 - "Programming Ruby" by David Thomas and Andy Hunt in HTML and PDF;
 - various talks from Ruby conferences across the world.

Install this documentation package if you want to know more about Ruby.

%prep
%setup -c -T -b 0

pushd ProgrammingRuby
%patch -p1
popd

mkdir extra
pushd extra
# Install third-party documentation
cp %SOURCE1 .
mkdir -p euruko03
cp %SOURCE2 euruko03/GarbageCollectionInExtensions.pdf
tar xzf %SOURCE3 -C euruko03
tar xjf %SOURCE4 
rm -f ProgrammingRuby-0.3a/html/.pr_style.css.swp ProgrammingRuby-0.3a/xml/ref_c_object.xml~
popd

cp %SOURCE5 .

%build
pushd ProgrammingRuby/latex
make book.ps
ps2pdf book.ps ../../ProgrammingRuby.pdf
popd

%files
%doc ProgrammingRuby.pdf pruby-permission.txt extra/*

# TODO:
# - update with new and juicy pieces?
#   [euruko05 didn't yield obvious to me]

%changelog
* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 0.1-alt7
- rebuilt for Sisyphus as ruby1.8 is back

* Tue May 06 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt6
- removed cruft, thanks viy@

* Tue Apr 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt5
- fixed summary/description, thanks php-coder@

* Fri Apr 04 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt4
- fix build: the content is way more interesting than
  noarch package build on x86_64 (examples include
  C code which breaks there)

* Sun Nov 12 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- adopted an orphan
- seems like build was broken due to build system being broken,
  as it just rebuilds OK now
- added URLs.txt with a first strike at online reading bootstrap

* Wed Mar 24 2004 Alexander Bokovoy <ab@altlinux.ru> 0.1-alt2
- Got permission from Dave Thomas for building book from TeX sources.

* Sat Sep 27 2003 Alexander Bokovoy <ab@altlinux.ru> 0.1-alt1
- Initial release, moved extra documentation to this package from ruby-doc

