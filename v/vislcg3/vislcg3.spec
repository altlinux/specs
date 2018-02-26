Name: vislcg3
Version: 0.9.7
Release: alt1.6010.1

Summary: Constraint Grammar compiler/parser
License: GPLv3+
Group: Development/Other
Url: http://www.altlinux.org/SampleSpecs/program

Packager: Kirill Maslinsky <kirill@altlinux.org>
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-emacs
BuildRequires: libicu-devel gcc-c++ perl-Digest-SHA xml-utils xsltproc docbook-dtds docbook-style-xsl emacs23-nox

%description
Compiler and parser for the 3rd version of the CG formalism variant.
Supports unicode.

%prep
%setup

%build
%autoreconf -I m4
%configure
%make_build

%byte_compile_file emacs/cg.el

pushd manual
ln -s /usr/share/xml/docbook/dtd/4.5 docbook-dtd-45
ln -s /usr/share/xml/docbook/xsl-stylesheets-1.75.2 docbook-xsl
./singlefile.sh
popd

%check
./test/runall.pl

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot%_emacslispdir
cp -a emacs/cg.{el,elc} %buildroot%_emacslispdir

%files -f %name.lang
%doc LICENSE AUTHORS README TODO APERTIUM_FORMAT manual/index.html newsletters/
%_bindir/*
%_man1dir/*
%_emacslispdir/*

%changelog
* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1.6010.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Tue Jul 13 2010 Kirill Maslinsky <kirill@altlinux.org> 0.9.7-alt1.6010
- Initial build for Sisyphus

