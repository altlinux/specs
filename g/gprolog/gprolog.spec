Name: gprolog
Version: 1.3.1
Release: alt1
Summary: GNU Prolog is a free Prolog compiler

Group: Development/Other
License: GPLv2
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.gprolog.org
Source: http://www.gprolog.org/gprolog-%version.tar.gz
Patch1: gprolog-1.3.0-test.patch
Patch2: gprolog-1.3.0-linedit.patch

#ExclusiveArch: x86_64 %ix86 ppc alpha

%description
GNU Prolog is a native Prolog compiler with constraint solving over
finite domains (FD) developed by Daniel Diaz
(http://loco.inria.fr/~diaz).

GNU Prolog is a very efficient native compiler producing (small)
stand-alone executables. GNU-Prolog also offers a classical
top-level+debugger.

GNU Prolog conforms to the ISO standard for Prolog but also includes a
lot of extensions (global variables, DCG, sockets, OS interface,...).

GNU Prolog also includes a powerful constraint solver over finite
domains with many predefined constraints+heuristics.

%package examples
Summary: Examples for GNU Prolog
Group: Development/Other
Requires: %name = %version-%release

%description examples
Examples for GNU Prolog.

%package docs
Summary: Documentation for GNU Prolog
Group: Documentation
Requires: %name = %version-%release

%description docs
Documentation for GNU Prolog.

%prep
%setup -q
# %patch1 -p1
# %patch2 -p1

%build
cd src

# gprolog only acccept -O0 and don't like -fomit-frame-pointer

CFLG="$(echo $RPM_OPT_FLAGS | sed -s "s/\-O2/-O1/g" \
     		    | sed -e "s/\-fomit-frame-pointer//")"

# Based on a gentoo ebuild (??)
CFLG="$CFLG -funsigned-char"

# sed -i -e "s:TXT_FILES      = @TXT_FILES@:TXT_FILES=:" Makefile.in
./configure \
       --with-install-dir=$RPM_BUILD_ROOT%_libdir/gprolog-%version \
       --without-links-dir --without-examples-dir \
       --with-doc-dir=dist-doc \
      --with-c-flags="$CFLG"

# _smp_flags seems to make trouble
make

%check
cd src
#
export PATH=$RPM_BUILD_ROOT%_bindir:$PATH
#
make check

%install
cd src
(
    make install
    mkdir $RPM_BUILD_ROOT%_bindir
    cd $RPM_BUILD_ROOT%_libdir/gprolog-%version/bin
    for i in *; do
 	ln -s ../%_lib/gprolog-%version/bin/$i $RPM_BUILD_ROOT%_bindir/$i
    done
)
rm -f dist-doc/*.{chm,dvi,ps}
rm -f dist-doc/compil-scheme.pdf
rm -f dist-doc/debug-box.pdf

for file in ChangeLog COPYING NEWS VERSION
do
    rm -f $RPM_BUILD_ROOT%_libdir/gprolog-%version/$file
done

cd ../ExamplesPl

rm -rf BINPROLOG CIAO SICSTUS
rm -rf SWI WAMCC XSB YAP

%files
%doc README COPYING ChangeLog NEWS PROBLEMS VERSION
%_bindir/*
%_libdir/gprolog-%version

%files examples
%doc ExamplesC ExamplesFD ExamplesPl

%files docs
%doc src/dist-doc/*

%changelog
* Sat Oct 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1.3.1-alt1
- Build for Sisyphus

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-4
- Fix dependency issue

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-3
- Supporting noarch subpackages

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-1
- New upstream release

* Mon Jun 16 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-17
- Remove TRAILSZ and GLOBALSZ environment variables

* Sun Jun 15 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-16
- Fix FTBFS (#440495)

* Wed Apr  9 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-15
- Exclude x86_64 because a build failure (#440945)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 1.3.0-14
- Autorebuild for GCC 4.3

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-13
- Rebuild for gcc-4.3

* Wed Jan 23 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-12
- Rebuild

* Tue Oct  9 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-11
- Add the alpha architecture to tue supported plattforms (#313571)

* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-10
- Changing license tag

* Wed Jun 13 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-9
- Rebuild to solve a koji issue.

* Thu May 24 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-8
- Include the PPC arch to build
- Remove _smp_mflags becouse is make trouble
- Used unmodified optflags

* Sun Mar 25 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-1
- New upstream version

* Thu Sep  7 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-8
- Fix broken symlib (#205118)

* Mon Sep  4 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-7
- Exclude PPC arch, becouse it produced a strange error on FC-6

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-6
- Rebuild for FC-6

* Mon May 15 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-5
- Remove compil-scheme.pdf and debug-box.pdf from the docs package

* Wed Apr 19 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-3
- Delete unnecessaries files from ExamplesPI

* Thu Mar 30 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-2
- Remove sed-command
- Correct typo about usable compiler options
- Add comment about the source of the patches

* Wed Mar 29 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-1
- Initial RPM package for Fedora Extras
