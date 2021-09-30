Name:		pure-doc
Version:	0.3
Release:	alt4
Summary:	A simple utility for documenting source code in the Pure programming language
Source:		http://pure-lang.googlecode.com/files/%name-%version.tar.gz
URL:		http://code.google.com/p/pure-lang
Group:		Development/Functional
License:	GPLv.3
Packager:	Fr. Br. George <george@altlinux.ru>
BuildRequires:	gcc-c++ flex
BuildRequires:	python3-module-docutils

Patch1: %name-%version-alt-compat.patch
Patch2: %name-0.3-gcc8-fix.patch

%description
pure-doc is a simple utility for literate programming and documenting source
code written in the Pure programming language. It is designed to be used with
the excellent docutils_ tools and the gentle markup format supported by these,
called RST_ a.k.a. "|RST|", usually pronounced "rest".

The basic idea is that you just comment your code as usual, but using RST
markup instead of plain text. In addition, you can also designate literate
programming fragments in your code, which will be translated to RST literal
blocks automatically. You then run pure-doc on your source files to extract
all marked up comments and the literate code blocks. The resulting RST source
can then be processed with the docutils utilities like rst2html and
rst2latex to create the documentation in a variety of formats.

%prep
%setup
#patch1 -p2
%patch2 -p1

%build
make realclean
%make all html

%install
install -Ds %name %buildroot%_bindir/%name

%files
%doc *.html README
%_bindir/%name


%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt4
- NMU: use python3 docutils

* Thu Feb 14 2019 Pavel Moseev <mars@altlinux.org> 0.3-alt3
- no return statement in the non-void function fixed (according g++8)

* Wed Sep 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt2
- NMU: rebuilt with new python-module-docutils.

* Thu Apr 16 2009 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from scratch

