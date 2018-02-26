Name: nickle
Version: 2.68
Release: alt1.1
Summary: A programming language-based prototyping environment

Group: Development/Other
License: MIT
Url: http://nickle.org
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://nickle.org/release/nickle-%version.tar.gz

BuildRequires: libncurses-devel, libreadline-devel

%description
Nickle is a programming language based prototyping environment with
powerful programming and scripting capabilities. Nickle supports a
variety of datatypes, especially arbitrary precision numbers. The
programming language vaguely resembles C. Some things in C which do
not translate easily are different, some design choices have been made
differently, and a very few features are simply missing.

Nickle provides the functionality of UNIX bc, dc and expr in
much-improved form. It is also an ideal environment for prototyping
complex algorithms. Nickle's scripting capabilities make it a nice
replacement for spreadsheets in some applications, and its numeric
features nicely complement the limited numeric functionality of
text-oriented languages such as AWK and PERL.

%package devel
Summary: Include files for Nickle
Group: Development/Other
Requires: %name = %version-%release

%description devel
Include files for Nickle, used for bulding external FFI (foreign
function interface) libraries (e.g. the Cairo interface for Nickle).

%prep
%setup

%build
%configure
make %{?_smp_flags}

#check
#cd test
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm `find examples -name 'Makefile*'`
rm examples/COPYING

# Fix permissions on example files
chmod a-x examples/menace2.5c
chmod a-x examples/turtle/snowflake.5c

%files
%doc README README.name COPYING AUTHORS NEWS TODO examples
%_bindir/nickle
%_datadir/nickle/
%exclude %_datadir/nickle/COPYING
%exclude %_datadir/nickle/examples
%_man1dir/nickle.1*

%files devel
%_includedir/nickle

%changelog
* Sun Aug 23 2009 Slava Semushin <php-coder@altlinux.ru> 2.68-alt1.1
- NMU
- Rebuild with gcc 4.4.1-alt1 to fix crash after start (Closes: #21061)

* Thu Aug 13 2009 Ilya Mashkin <oddity@altlinux.ru> 2.68-alt1
- Build for ALT Linux

* Wed Mar 11 2009 Michel Salim <salimma@fedoraproject.org> - 2.68-1
- Update to 2.68
- Enable checks

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun  6 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.67-1
- Update to 2.67

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.62-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.62-1
- Update to 2.62

* Sun Sep 23 2007 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.58-1
- Update to 2.58

* Sat Nov  4 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.54-2
- Only package example files once, remove leftover Makefiles

* Thu Nov  2 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.54-1
- Update to 2.54
- Use exclude macro instead of ghost

* Sun Mar 19 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-3
- Moved examples to doc
- Removed redundant COPYING files from examples

* Sun Mar  5 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-2
- Removed INSTALL from installed documentation
- Added description for devel package

* Sat Feb 18 2006 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.53-1
- Initial Fedora package

* Thu Mar  1 2004 Mike A. Harris <mharris@www.linux.org.uk> - 2.29-2
- Initial rpm spec file

