Name: source-highlight
Version: 3.1.8
Release: alt5%ubt

Summary: syntax highlighting for source documents
License: GPL
Group: Text tools

Url: http://www.gnu.org/software/src-highlite/
# git://git.savannah.gnu.org/src-highlite.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: boost-devel gcc-c++ ctags help2man doxygen texlive-collection-basic texinfo
BuildRequires: flex

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
Requires: lib%name = %EVR

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
	--enable-static=no \
	--enable-maintainer-mode \
	--with-boost-regex=boost_regex \
	--with-doxygen

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
%doc lib/srchilite/html
%_includedir/srchilite
%_libdir/*.so
%_pkgconfigdir/*.pc
%_infodir/%name-lib*

%files -n bash-completion-%name
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/*

%changelog
* Tue Apr 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.8-alt5%ubt
- Rebuilt with new boost.

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.8-alt4%ubt
- NMU: rebuild with TeXLive instead of TeTeX

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.8-alt3%ubt
- Rebuilt with boost 1.65.0.
- Added %%ubt to release.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.8-alt2
- Updated to upstream release version 3.1.8

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.1.8-alt1.git20121231.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 3.1.8-alt1.git20121231.1
- rebuild with boost 1.57.0

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.8-alt1.git20121231
- Version 3.1.8

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.6
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.5
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt2.4
- Rebuilt with Boost 1.51.0

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
