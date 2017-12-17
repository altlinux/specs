##define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -MPrima::Const'
BuildRequires: perl(Text/Bidi.pm)
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: /usr/bin/xvfb-run perl(AnyEvent.pm) perl(AnyEvent/Socket.pm) perl-podlators
# END SourceDeps(oneline)
# need installed Prima
%add_findreq_skiplist %_bindir/VB
%add_findreq_skiplist %_bindir/podview
%add_findreq_skiplist */Prima/DetailedOutline.pm
%add_findreq_skiplist */Prima/HelpViewer.pm
%add_findreq_skiplist */Prima/KeySelector.pm
# Bareword "cs::Simple" not allowed
%add_findreq_skiplist */Prima/VB/*
%add_findreq_skiplist */Prima/examples/*
# -M Prima::Drawable
%add_findreq_skiplist */Prima/Drawable/*
%add_findreq_skiplist */Prima/Buttons.pm
%add_findreq_skiplist */Prima/*

# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run X11 tests
%{bcond_without perl_Prima_enables_x11_test}
# Use GTK2 file dialogs and fonts
%{bcond_without perl_Prima_enables_gtk2}
# Support colorful cursor via Xcursor
%{bcond_without perl_Prima_enables_xcursor}
# Support FreeType fonts via xft
%{bcond_without perl_Prima_enables_xft}

Name:           perl-Prima
Version:        1.52
Release:        alt3_3
Summary:        Perl graphic toolkit
# img/codec_jpeg.c:     EXIF parser is based on io-jpeg.c from gdk-pixbuf
#                       (LGPLv2+)
# img/imgscale.c:       Resizing filters are baes on magick/resize.c from
#                       ImageMagick (ImageMagick)
# include/unix/queue.h: BSD
# pod/prima-gencls.pod: BSD
# Prima.pm:             BSD
# Copying:              BSD text
# LICENSE:              BSD text
# img/codec_X11.c:      MIT
# pod/Prima/Widget/place.pod:   TCL
# src/Drawable.c:               TCL
# examples/tiger.eps:   AGPLv3+   (bundled from GhostScript? CPAN RT#122271)
License:        BSD and MIT and TCL and ImageMagick and LGPLv2+ and AGPLv3+
URL:            http://search.cpan.org/dist/Prima/
Source0:        http://www.cpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  libgif-devel
BuildRequires:  gcc-common
BuildRequires:  libjpeg-devel
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# pkgconfig is optional, but it provides better compiler options, so use it
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with perl_Prima_enables_gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.7
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
%if %{with perl_Prima_enables_xcursor}
BuildRequires:  pkgconfig(xcursor)
%endif
BuildRequires:  pkgconfig(xext)
%if %{with perl_Prima_enables_xft}
BuildRequires:  pkgconfig(xft)
%endif
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
# Getopt::Long not used at tests
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/RefHash.pm)
# Optional run-time:
# Text::Bidi::Constants 2.10 not used at tests
# Text::Bidi::Paragraph 2.10 not used at tests
# Tests:
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Test/More.pm)
%if %{with perl_Prima_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-xvfb xvfb-run
BuildRequires:  fontlang(en)
# Tests exhibit a proportional font
BuildRequires:  fonts-ttf-liberation
%endif
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
# Optional run-time:
Requires:     perl(Text/Bidi/Constants.pm) >= 2.100
Requires:     perl(Text/Bidi/Paragraph.pm) >= 2.100
# Public modules without package keyword:
Provides:       perl(Prima/noARGV.pm) = %{version}



# Do not export private modules (not starting with "Prima")


# Filter under-specified provides

Source44: import.info
%filter_from_provides /^perl\\((am|apc|bi|bs|bt|ci|cl|cm|CodeEditor|cr|cs|CustomPodView|Divider|dmfp|dt|Editor|fdo|fds|fe|fp|fr|fra|frr|fs|fw|gm|gr|grow|gsci|gt|gui|ict|im|is|ItemsOutline|kb|km|le|lj|lp|mb|mbi|MenuOutline|MPropListViewer|mt|MyOutline|nt|PackPropListViewer|PropListViewer|rop|Round3D|sbmp|ss|sv|ta|tb|tka|tm|tno|tns|tw|wc|ws).pm\\)/d
%filter_from_provides /^perl\\(Prima.pm\\)$/d

%description
Prima is a general purpose extensible graphical user interface toolkit with
a rich set of standard widgets and an emphasis on 2D image processing tasks.
A Perl program using PRIMA looks and behaves identically on X, Win32.

%package Test
Group: Development/Perl
Summary:        Test tools for Prima Perl graphic toolkit

%description Test
This Perl module contains a small set or tool used for testing of
Prima-related code together with standard Perl Test:: suite.


%prep
%setup -q -n Prima-%{version}

#sed -i -e '/use Prima /d' Prima/Const.pm
#sed -i -e 's/use Prima::Const/require Prima::Const/' Prima/Classes.pm

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" \
    CYGWIN_WINAPI=0 \
    WITH_GTK2=%{with perl_Prima_enables_gtk2} \
    WITH_ICONV=1 \
    WITH_OPENMP=1 \
    WITH_XFT=%{with perl_Prima_enables_xft} \
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc Copying LICENSE
# "examples" directory is installed into perl_vendorarch
%doc Changes README.md
%{_bindir}/*
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/prima-gencls.pod
%{perl_vendor_archlib}/Prima*
%exclude %{perl_vendor_archlib}/Prima/Stress.*
%exclude %{perl_vendor_archlib}/Prima/Test.*
%{_mandir}/man1/*

%files Test
%{perl_vendor_archlib}/Prima/Stress.*
%{perl_vendor_archlib}/Prima/Test.*

%changelog
* Sun Dec 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.52-alt3_3
- rebuild with perl 5.26

* Mon Dec 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.52-alt2_3
- hack; fixed build for perl 5.26

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1_3
- new version

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1.49-alt2
- rebuild to get rid of unmets

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- regenerated from template by package builder

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- regenerated from template by package builder

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- regenerated from template by package builder

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt2
- rebuild with perl 522

* Sat Nov 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- regenerated from template by package builder

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- regenerated from template by package builder

* Mon Dec 15 2014 Cronbuild Service <cronbuild@altlinux.org> 1.41-alt2
- rebuild to get rid of unmets

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- regenerated from template by package builder

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- initial import by package builder

