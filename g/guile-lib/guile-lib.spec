Name: guile-lib
Version: 0.1.6
Release: alt3

Summary: Guile-Lib -- a repository of useful code written in Guile Scheme
Packager: Paul Wolneykien <manowar@altlinux.ru>
License: GPLv2
Group: Development/Scheme
Url: http://gna.org/projects/guile-lib
BuildArch: noarch

Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Apr 21 2009
BuildRequires: guile-devel rpm-macros-fillup texinfo /usr/bin/tex

%description
Guile-Lib is intended as an accumulation place for pure-scheme Guile
modules, allowing for people to cooperate integrating their generic
Guile modules into a coherent library. Think "a down-scaled,
limited-scope CPAN for Guile".

%package doc
Summary: documentation and samples for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description doc
Documentation for the Guile-Lib -- a repository of useful code written
in Guile Scheme

%package examples
Summary: documentation and samples for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description examples
Examples for the Guile-Lib -- a repository of useful code written
in Guile Scheme

%package scheme
Summary: Miscellaneous Scheme language extensions for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description scheme
Miscellaneous Scheme language extensions for the Guile-Lib --
a repository of useful code written in Guile Scheme

%package config
Summary: Configuration modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description config
Program configuration-related  modules for the Guile-Lib --
a repository of useful code written in Guile Scheme

%package container
Summary: Interprocess comunication and synchronization modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description container
Interprocess comunication and synchronization-related modules for
the Guile-Lib -- a repository of useful code written in Guile Scheme

%package encription
Summary: Encription modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description encription
Encription-related modules for the Guile-Lib -- a repository of useful
code written in Guile Scheme

%package os
Summary: Operating system interaction modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description os
Operating system interaction modules for the Guile-Lib -- a repository
of useful code written in Guile Scheme

%package search
Summary: Search and sort-related modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description search
Search and sort-related modules for the Guile-Lib -- a repository
of useful code written in Guile Scheme

%package srfi
Summary: Additional SRFI modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description srfi
Additional SRFI modules for the Guile-Lib -- a repository
of useful code written in Guile Scheme.

Currently includes the following SRFIs:

 - SRFI-34 -- Exception Handling for Programs;
 - SRFI-35 -- Conditions;
 - SRFI-40 -- A Library of Streams (deprecated now).

%package term
Summary: Textual terminal handling modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description term
Textual terminal handling modules for the Guile-Lib -- a repository
of useful code written in Guile Scheme

%package unit-test
Summary: Program self-testing (unit-test) modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description unit-test
Program self-testing (unit-test) modules for the Guile-Lib --
a repository of useful code written in Guile Scheme

%package html
Summary: HTML-processing modules for %name
Group: Development/Scheme
Requires: %name = %version-%release

%description html
HTML-processing modules for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%package debugging
Summary: Program debug related modules for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description debugging
Program debug-related modules for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%package io
Summary: I/O extension modules for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description io
Input/Output extansion modules for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%package logging
Summary: Message logging modules for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description logging
Message logging modules for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%package parsing
Summary: Text parsing modules for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description parsing
Text parsing modules for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%package math
Summary: Implementation of various mathematical algorithms for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description math
Implementation of various mathematical algorithms for the Guile-Lib --
a repository of useful code written in Guile Scheme

%package text
Summary: Various text-processing algorithms for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-scheme = %version-%release

%description text
Various text-processing algorithms for the Guile-Lib --
a repository of useful code written in Guile Scheme

%package graph
Summary: Implementation of some Graph-theory related algorithms for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-math = %version-%release

%description graph
Implementation of some Graph-theory related algorithms for
the Guile-Lib -- a repository of useful code written in Guile Scheme

%package sxml
Summary: XML-processing modules for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-debugging = %version-%release
Requires: %name-io = %version-%release

%description sxml
XML-processing modules for the Guile-Lib -- a repository of useful
code written in Guile Scheme

%package documentation
Summary: Scheme code documentation suite for %name
Group: Development/Scheme
Requires: %name = %version-%release
Requires: %name-unit-test = %version-%release
Requires: %name-sxml = %version-%release
Requires: %name-container = %version-%release
Requires: %name-text = %version-%release
Requires: %name-scheme = %version-%release

%description documentation
Scheme code documentation suite for the Guile-Lib -- a repository of
useful code written in Guile Scheme

%prep
%setup

%build
autoreconf -fi
%configure
%make_build

%install
%make_install install \
	prefix=%buildroot%_prefix \
	bindir=%buildroot%_bindir \
	mandir=%buildroot%_mandir \
	datadir=%buildroot%_datadir \
	infodir=%buildroot/%_infodir

%make_install install-pdf \
	pdfdir=%buildroot%_docdir/%name-%version

%make_install install-html \
	htmldir=%buildroot%_docdir/%name-%version/html

install -p -m640 -D examples/document-module.scm %buildroot%_datadir/%name-%version/examples/document-module.scm
install -p -m640 -D examples/sxw2words %buildroot%_datadir/%name-%version/examples/sxw2words

%files
%_infodir/guile-library.info.bz2

%files documentation
%_datadir/guile/site/apicheck.scm
%_datadir/guile/site/texinfo.scm
%_datadir/guile/site/texinfo/docbook.scm
%_datadir/guile/site/texinfo/html.scm
%_datadir/guile/site/texinfo/indexing.scm
%_datadir/guile/site/texinfo/nodal-tree.scm
%_datadir/guile/site/texinfo/plain-text.scm
%_datadir/guile/site/texinfo/reflection.scm
%_datadir/guile/site/texinfo/serialize.scm

%files config
%_datadir/guile/site/config/load.scm

%files container
%_datadir/guile/site/container/async-queue.scm
%_datadir/guile/site/container/delay-tree.scm
%_datadir/guile/site/container/nodal-tree.scm
%_datadir/guile/site/container/queue.scm

%files debugging
%_datadir/guile/site/debugging/assert.scm
%_datadir/guile/site/debugging/time.scm
%_datadir/guile/site/statprof.scm

%files graph
%_datadir/guile/site/graph/topological-sort.scm

%files html
%_datadir/guile/site/htmlprag.scm

%files io
%_datadir/guile/site/io/string.scm

%files logging
%_datadir/guile/site/logging/logger.scm
%_datadir/guile/site/logging/port-log.scm
%_datadir/guile/site/logging/rotating-log.scm

%files parsing
%_datadir/guile/site/match-bind.scm
%_datadir/guile/site/text/parse-lalr.scm

%files math
%_datadir/guile/site/math/minima.scm
%_datadir/guile/site/math/primes.scm
%_datadir/guile/site/math/rationalize.scm

%files encription
%_datadir/guile/site/md5.scm

%files os
%_datadir/guile/site/os/process.scm

%files scheme
%_datadir/guile/site/scheme/documentation.scm
%_datadir/guile/site/scheme/kwargs.scm
%_datadir/guile/site/scheme/session.scm

%files search
%_datadir/guile/site/search/basic.scm

%files srfi
%_datadir/guile/site/srfi/srfi-34.scm
%_datadir/guile/site/srfi/srfi-35.scm
%_datadir/guile/site/srfi/srfi-40.scm

%files text
%_datadir/guile/site/string/completion.scm
%_datadir/guile/site/string/soundex.scm
%_datadir/guile/site/string/transform.scm
%_datadir/guile/site/string/wrap.scm

%files sxml
%_datadir/guile/site/sxml/apply-templates.scm
%_datadir/guile/site/sxml/fold.scm
%_datadir/guile/site/sxml/simple.scm
%_datadir/guile/site/sxml/ssax-simple.scm
%_datadir/guile/site/sxml/ssax.scm
%_datadir/guile/site/sxml/ssax/input-parse.scm
%_datadir/guile/site/sxml/transform.scm
%_datadir/guile/site/sxml/upstream/SSAX-expanded.scm
%_datadir/guile/site/sxml/upstream/SSAX.scm
%_datadir/guile/site/sxml/upstream/SXML-tree-trans.scm
%_datadir/guile/site/sxml/upstream/SXPath-old.scm
%_datadir/guile/site/sxml/upstream/assert.scm
%_datadir/guile/site/sxml/upstream/input-parse.scm
%_datadir/guile/site/sxml/upstream/packages.scm
%_datadir/guile/site/sxml/xpath.scm

%files term
%_datadir/guile/site/term/ansi-color.scm

%files unit-test
%_datadir/guile/site/unit-test.scm

%files doc
%_docdir/%name-%version/*.pdf
%_docdir/%name-%version/html

%files examples
%_datadir/%name-%version/examples/*

%changelog
* Wed Nov 25 2009 Paul Wolneykien <manowar@altlinux.ru> 0.1.6-alt3
- Remove depricated [un]install_info calls.

* Wed Apr 22 2008 Paul Wolneykien <manowar@altlinux.ru> 0.1.6-alt2
- Info system directory file update hooks.

* Tue Apr 21 2008 Paul Wolneykien <manowar@altlinux.ru> 0.1.6-alt1
- Initial release for ALTLinux.
