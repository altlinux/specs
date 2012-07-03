Name: otl
Version: 0.54
Release: alt1.qa1

Summary: a customizable text processor for generating markup from simple text

License: GPL
Group: Text tools
Url: http://outl.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/outl/%{name}_%version.tar.bz2

%description
otl converts a text file written in a simple user-defined format
to another user-defined format (by default, XHTML). For example, by
default "--joebob-- is big" is converted to "<span style="font-weight:
bold;">joebob</span> is big". otl is more than a search/replace
front-end. otl can process structures such as ordered and unordered lists
(nested or unnested), add custom "headers" and "footers" to documents,
etc. The conversion process is customizable and utilizes perl regex,
adding quite a bit of flexibility to the transformation process. Since
other types of markup (e.g., XHTML tags) can be included in the source
text file to be processed, any markup (e.g., markup which otl currently
doesn't produce by default such as MathML) can be included in the document
in a straightforward fashion. Since both the syntax of the source file
and of the output can be readily customized, otl can be used for many
types of conversions (feel free to submit your ".otl" file if you make
a new one). The package also includes tag-remove, a script for stripping
XML tags from documents.

%prep
%setup -q -n %{name}_%version

%build

%install
mkdir -p %buildroot%perl_vendorlib %buildroot%_bindir
cp DatPlUtils.pm %buildroot%perl_vendorlib
install otl.pl %buildroot%_bindir/otl
install otlsub.pl %buildroot%_bindir/otlsub

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find . \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%doc README asciidoc/*.txt css/ examples/*.txt
%_bindir/otl
%_bindir/otlsub
%perl_vendorlib/*.pm

%changelog
* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.54-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * backup-file-in-package for otl
  * postclean-05-filetriggers for spec file

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.54-alt1
- new version 0.54

* Sat Oct 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.50-alt1
- new version 0.50 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt0.1
- new version 0.42 (with rpmrb script)

* Sun Nov 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.35-alt0.1
- initial build for ALT Linux Sisyphus
