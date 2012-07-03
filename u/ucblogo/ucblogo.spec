Name: ucblogo
Version: 6.0
Release: alt2
Summary: An interpreter for the Logo programming language
Group: Development/Functional
License: GPLv2+
Source: ftp://ftp.cs.berkeley.edu/pub/ucblogo/ucblogo-%version.tar.gz
Source1: logo-mode.tar.gz
Patch0: ucblogo-5.5-ospeed.patch
Patch1: ucblogo-6.0-wx.patch
#Patch2: ucblogo-tetexi2html.patch
Url: http://www.cs.berkeley.edu/~bh

# Automatically added by buildreq on Fri Nov 05 2010
BuildRequires: emacs-nox gcc-c++ ghostscript-utils libSM-devel libX11-devel libncurses-devel libwxGTK-devel texi2html texlive-base

%description
Berkeley Logo (ucblogo) is an interpreter for the Logo programming
language. Logo is a computer programming language designed for use by
learners, including children. This dialect of Logo features
random-access arrays, variable number of inputs to user-defined
procedures, various error handling improvements, comments and
continuation lines, first-class instruction and expression templates,
and macros.

%package emacs
Summary: Emacs Logo mode
Group: Development/Functional
BuildArch: noarch
Requires: %name = %version-%release

%description emacs
Emacs mode for UCBLogo.

%prep
%setup -q
%setup -q -a 1
%patch0 -p1 -b .ospeed
%patch1 -p1 -b .wx
#patch2 -p0
sed -i 's|letter|a4|' docs/makefile

sed -i 's|everything|all|g' makefile*

# no dot files in directories
sed -i  's|\.logo|dot.logo|g' emacs/dot.*
sed -i 's|/\.logo|/dot.logo|g' emacs/makefile
sed -i 's|\.LOOPS|dot.LOOPS|g' emacs/dot.*
sed -i 's|/\.LOOPS|/dot.LOOPS|g' emacs/makefile

# correct directories /usr/lib -> /usr/share and /usr/local ->  /usr
sed -i 's|/local/lib/logo|/share/logo|g' emacs/*
sed -i 's|/local/lib/logo|/share/logo|g' *.c README
sed -i 's|/lib/logo|/share/logo|g' emacs/*
sed -i 's|/lib/logo|/share/logo|g' *.c makefile*
sed -i 's|/usr/local/bin/logo|/usr/bin/logo|g' docs/html/usermanual_1.html
sed -i 's|/usr/local/bin/logo|/usr/bin/logo|g' docs/ucblogo.info*
sed -i 's|/usr/local/bin/logo|/usr/bin/logo|g' docs/usermanual.texi
sed -i 's|/usr/local/bin/logo|/usr/bin/logo|g' README
sed -i 's|/usr/local/info|/usr/share/info|g' emacs/logo.el emacs/README
sed -i 's|/usr/local/info|/usr/share/info|g' README
sed -i 's|\$\(prefix\)/info|/usr/share/info|' emacs/makefile

# use cursesw instead of curses
#sed -i 's|lcurses|lcursesw|' configure

find -name 'CVS' | xargs rm -rf
find -name '.svn' | xargs rm -rf

%build
# build WX version
rm config.cache
%configure --x-includes=%_includedir --x-libraries=%_libdir --with-x --wx-enable --wx-config_path=/usr/bin/wx-config
%make_build logo
mv logo logo-wx
# build traditional version
make clean
%configure --x-includes=%_includedir --x-libraries=%_libdir --with-x
%make_build
# compile emacs files
%make -C emacs BINDIR=%_bindir EMACSDIR=%_datadir/emacs/site-lisp/logo INFODIR=%_infodir LIBLOC=%_datadir/logo

%make make-docs
sed -i '2a\
INFO-DIR-SECTION Programming Languages\
START-INFO-DIR-ENTRY\
* UCBLogo: (ucblogo).           Berkeley Logo User Manual.\
END-INFO-DIR-ENTRY' docs/ucblogo.info

%install
%makeinstall

install -m0755 logo-wx $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_datadir/info
mv -f $RPM_BUILD_ROOT%prefix/info/* $RPM_BUILD_ROOT%_datadir/info
rm -fr $RPM_BUILD_ROOT%prefix/info
rm -fr $RPM_BUILD_ROOT%_datadir/logo/docs

# install emacs files
%make -C emacs install BINDIR=$RPM_BUILD_ROOT%_bindir EMACSDIR=$RPM_BUILD_ROOT%_datadir/emacs/site-lisp/logo
mkdir -p $RPM_BUILD_ROOT%_datadir/emacs/site-lisp/site-start.d
cp -f emacs/dot.emacs $RPM_BUILD_ROOT%_datadir/emacs/site-lisp/site-start.d/logo-mode.el
rm -f $RPM_BUILD_ROOT%_bindir/install-logo-mode
rm -f $RPM_BUILD_ROOT%_datadir/emacs/site-lisp/logo/README
rm -f $RPM_BUILD_ROOT%_datadir/emacs/site-lisp/logo/*.el

%files
%doc docs/html docs/usermanual.pdf README gpl plm changes.txt
%doc
%_bindir/*
%_datadir/logo
%_infodir/*

%files emacs
%doc emacs/README
%_datadir/emacs/site-lisp/logo
%_datadir/emacs/site-lisp/site-start.d

%changelog
* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 6.0-alt2
- Resurrect build:
- tetex-related patch nd pre/post section removed
- documentation fixes

* Sun Mar 01 2009 Fr. Br. George <george@altlinux.ru> 6.0-alt1
- Initial build from FC

* Sat Nov 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-2
- re-add emacs logo-mode from previous release as a separate package

* Thu Nov 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-1
- new release 6.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.5-10
- Autorebuild for GCC 4.3

* Thu Feb 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-9
- add patch for fixing ncurses problem

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-8
- add fix to use cursesw instead of curses

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-7
- replace BR libtermcap-devel by BR ncurses-devel

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-6
- rebuild to use ncurses

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-5
- Rebuild for FE6

* Thu Jun 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-4
- added BR texi2html
- added BR libXt-devel
- added include and libs options for X11 to configure

* Sat Jun  3 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-3
- added BuildReq: texinfo-tex
- make owned the directory %_datadir/emacs/site-lisp/site-start.d

* Sun Aug 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.5-2
- New Version 5.5

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- New Version 5.4

* Thu Feb 26 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.2
- Install info files
- Install emacs site-start file

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.1
- First Fedora release
