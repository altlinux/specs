Summary: Docutils -- Python Documentation Utilities - compat names
Version: 0.1
Release: alt1
Name: python-module-docutils-compat
License: public domain
Group: Development/Python
BuildArch: noarch
#Requires: python-module-docutils

%description
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

This package contains symlinks for commonly used docutils names.

%prep

%build

%install
mkdir -p %buildroot%_bindir/
# compat symlinks
for i in rst2html rst2latex rst2man rst2odt rst2odt_prepstyles rst2pseudoxml rst2s5 rst2xetex rst2xml rstpep2html ; do
	ln -s $i.py %buildroot%_bindir/$i
done

%files
%_bindir/*

%changelog
* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- compat symlinks in /usr/bin
