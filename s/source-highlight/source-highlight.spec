Name: source-highlight
Version: 3.1.4
Release: alt2.3

Summary: syntax highlighting for source documents
License: GPL
Group: Text tools
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

Url: http://www.gnu.org/software/src-highlite/
Source: %name-%version.tar

BuildRequires: boost-devel gcc-c++ ctags help2man doxygen tetex-core texinfo

%description
This program, given a source file, produces a document
with syntax highlighting.  Both source languages and output formats
can be specified with a simple syntax and added dynamically.  At the
moment this package can handle many programming languages, such as,
e.g., Java, C/C++, Prolog, Perl, Php3, Python, Flex, ChangeLog, etc.
as source languages, and some output formats such, as, e.g., HTML,
XHTML, LaTeX, etc.

%package -n lib%name
Summary: source highlighting library
License: GPL
Group: Development/C++

%description -n lib%name
This package contains the data files used by the libsource-highlight
library, which is the library that underlies the source-highlight
program suite. The library converts source code to a document with
syntax highlighting and supports many file formats. The library can be
used by other C++ programs to get source code highlighting capabilities.

%package -n lib%name-devel
Summary: Header files for libsource-highlight library
License: GPL
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is a development package for lib%name. It includes
headers and documentation.

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Development/Other
BuildArch: noarch

%description -n bash-completion-%name
%summary

%prep
%setup

%build
%autoreconf
%configure \
	--enable-maintainer-mode \
	--with-boost-regex=boost_regex

%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_mandir/man?/*
%_defaultdocdir/%name
%_infodir/%name.info*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/srchilite
%_libdir/*.so
%_pkgconfigdir/*.pc
%_infodir/%name-lib*

%files -n bash-completion-%name
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/*

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.1
- Rebuilt with Boost 1.47.0

* Mon Mar 14 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 3.1.4-alt2
- Rebuild with libboost_regex.so.1.46.0.

* Thu Jan 27 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 3.1.4-alt1
- Initial build for Sisyphus.
