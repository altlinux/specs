# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: cppcheck
Version: 1.50
Release: alt1

Summary: A tool for static C/C++ code analysis

License: GPLv3
Group: Development/Tools
Url: http://sourceforge.net/projects/cppcheck/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://downloads.sourceforge.net/cppcheck/cppcheck-%version.tar.bz2
Patch0: cppcheck-makefile-docbook_xsl.patch

BuildRequires: gcc-c++ docbook-style-xsl xsltproc libpcre-devel

%description
Static analysis of C/C++ code. Checks for: memory leaks, mismatching
allocation-deallocation, buffer overrun, and many more. The goal is
0%% false positives.

%prep
%setup
%patch0 -p2

%build
%make_build --silent --no-print-directory \
	CXXFLAGS="%optflags -W -Werror" \
	CPPFLAGS="$(pkg-config --cflags libpcre)"

%make_build --silent --no-print-directory man

# Generate html documentation
xsltproc \
	-o manual.html \
	/usr/share/xml/docbook/xsl-stylesheets/xhtml/docbook.xsl man/manual.docbook

%check
%make_build --silent --no-print-directory test

%install
%makeinstall_std --silent --no-print-directory

install -pD -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc readme.txt manual.html
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 1.50-alt1
- Updated to 1.50

* Fri May 06 2011 Slava Semushin <php-coder@altlinux.ru> 1.48-alt1
- Updated to 1.48
- I not maintain this package any more

* Thu Feb 10 2011 Slava Semushin <php-coder@altlinux.ru> 1.47-alt1
- Updated to 1.47

* Wed Dec 29 2010 Slava Semushin <php-coder@altlinux.ru> 1.46.1-alt1
- Updated to 1.46.1

* Sat Oct 30 2010 Slava Semushin <php-coder@altlinux.ru> 1.45-alt1
- Updated to 1.45

* Fri Jul 16 2010 Slava Semushin <php-coder@altlinux.ru> 1.44-alt1
- Updated to 1.44

* Mon May 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.43-alt1
- Updated to 1.43

* Thu Mar 11 2010 Slava Semushin <php-coder@altlinux.ru> 1.42-alt1
- Updated to 1.42

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 1.40-alt1
- Updated to 1.40

* Sat Dec 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.39-alt1
- Updated to 1.39
- Include manual.html to documentation

* Sat Oct 31 2009 Slava Semushin <php-coder@altlinux.ru> 1.38-alt1
- Updated to 1.38
- Moved "make test" to %%check section

* Wed Sep 23 2009 Slava Semushin <php-coder@altlinux.ru> 1.37-alt1
- Updated to 1.37

* Sun Aug 16 2009 Slava Semushin <php-coder@altlinux.ru> 1.35-alt1
- Updated to 1.35

* Sun Jul 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.34-alt1
- Updated to 1.34

* Wed Jun 10 2009 Slava Semushin <php-coder@altlinux.ru> 1.33-alt1
- Updated to 1.33
- Run test suite during build

* Mon May 11 2009 Slava Semushin <php-coder@altlinux.ru> 1.32-alt1
- Updated to 1.32

* Tue May 05 2009 Slava Semushin <php-coder@altlinux.ru> 1.31-alt1
- Initial build for ALT Linux

