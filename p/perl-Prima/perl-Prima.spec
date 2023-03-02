%define _unpackaged_files_terminate_build 1
## does not work, sed below does not help
##define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -MPrima::Const'
##sed -i -e '/use Prima /d' Prima/Const.pm
##sed -i -e 's/use Prima::Const/require Prima::Const/' Prima/Classes.pm
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: /usr/bin/xvfb-run libheif-devel perl(AnyEvent.pm) perl(AnyEvent/Socket.pm) perl-podlators
# END SourceDeps(oneline)
# need installed Prima
%add_findreq_skiplist %_bindir/VB
%add_findreq_skiplist %_bindir/podview
%add_findreq_skiplist %perl_vendor_archlib/Prima/DetailedOutline.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/HelpViewer.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/KeySelector.pm
# Bareword "cs::Simple" not allowed
%add_findreq_skiplist %perl_vendor_archlib/Prima/VB/*
%add_findreq_skiplist %perl_vendor_archlib/Prima/examples/*
# -M Prima::Drawable
%add_findreq_skiplist %perl_vendor_archlib/Prima/Drawable/*
%add_findreq_skiplist %perl_vendor_archlib/Prima/Buttons.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/ExtLists.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/ImageViewer.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/IntUtils.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/Label.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/Lists.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/Notebooks.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/PS/*.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/RubberBand.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/ScrollBar.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/ScrollWidget.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/Sliders.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/StartupWindow.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/Widgets.pm
%add_findreq_skiplist %perl_vendor_archlib/Prima/sys/*

# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform optional tests
%{bcond_without perl_Prima_enables_optional_test}
# Run X11 tests
%{bcond_without perl_Prima_enables_x11_test}
# Support bidirectional text with FriBidi library
%{bcond_without perl_Prima_enables_fribidi}
# Use GTK2 file dialogs and fonts
%{bcond_without perl_Prima_enables_gtk2}
# Use HarfBuzz library for rendering a text
%{bcond_without perl_Prima_enables_harfbuzz}
# Support colorful cursor via Xcursor
%{bcond_without perl_Prima_enables_xcursor}
# Support FreeType fonts via xft
%{bcond_without perl_Prima_enables_xft}
# Support WebP image format
%{bcond_without perl_Prima_enables_wepb}

Name:           perl-Prima
Version:        1.68002
Release:        alt1
Summary:        Perl graphic toolkit
# Copying:              BSD text
# examples/tiger.eps:   AGPLv3+   (bundled from GhostScript? CPAN RT#122271)
# img/codec_jpeg.c:     EXIF parser is based on io-jpeg.c from gdk-pixbuf
#                       (LGPLv2+)
# img/codec_X11.c:      MIT
# img/imgscale.c:       Resizing filters are baes on magick/resize.c from
#                       ImageMagick (ImageMagick)
# include/unix/queue.h: BSD
# LICENSE:              BSD text
# pod/Prima/Widget/place.pod:   TCL
# pod/prima-gencls.pod: BSD
# Prima.pm:             BSD
# Prima/PS/Unicode.pm:  BSD
# src/Drawable.c:       TCL
# unix/apc_render.c:    MIT
License:        BSD and MIT and TCL and ImageMagick and LGPLv2+ and AGPLv3+
URL:            https://metacpan.org/release/Prima
Source0:        http://www.cpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  libgif-devel
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
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
%if %{with perl_Prima_enables_fribidi}
BuildRequires:  pkgconfig(fribidi)
%endif
%if %{with perl_Prima_enables_gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.7
%endif
%if %{with perl_Prima_enables_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
%if %{with perl_Prima_enables_wepb}
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
%endif
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
BuildRequires:  perl(Fcntl.pm)
# Getopt::Long not used at tests
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Tie/Array.pm)
BuildRequires:  perl(Tie/RefHash.pm)
# Optional run-time:
BuildRequires:  perl(Compress/Raw/Zlib.pm)
# gv not used at a tests
# Tests:
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
%if %{with perl_Prima_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-xvfb xvfb-run
BuildRequires:  fontlang(en)
# Tests exhibit a proportional font
BuildRequires:  fonts-ttf-liberation
%endif
%if %{with perl_Prima_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
%endif
Requires:     perl(Compress/Raw/Zlib.pm)
Requires:       gv
# Public modules without a package keyword:
Provides:       perl(Prima/noARGV.pm) = %{version}
Provides:       perl(Prima/PS/Drawable/Path.pm) = %{version}
Provides:       perl(Prima/PS/Drawable/Region.pm) = %{version}
Provides:       perl(Prima/PS/Setup.pm) = %{version}



# Do not export private modules (not starting with "Prima")


Source44: import.info
%filter_from_provides /^perl(\(am\|apc\|bi\|bs\|bt\|ci\|cl\|cm\|CodeEditor\|cr\|cs\|CustomPodView\|Divider\|dmfp\|dt\|Editor\|fdo\|fds\|fe\|fp\|fr\|fra\|frr\|fs\|fw\|gm\|gr\|grow\|gsci\|gt\|gui\|ict\|im\|is\|ItemsOutline\|kb\|km\|le\|lj\|lp\|mb\|mbi\|MenuOutline\|MPropListViewer\|mt\|MyOutline\|nt\|PackPropListViewer\|PropListViewer\|rop\|Round3D\|sbmp\|ss\|sv\|ta\|tb\|tka\|tm\|tno\|tns\|tw\|wc\|ws\).pm)/d

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

%package tests
Group: Development/Perl
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Prima perl-Prima-Test
Requires:       coreutils
%if %{with perl_Prima_enables_x11_test}
Requires:       xorg-xvfb xvfb-run
Requires:       fontlang(en)
# TODO: see log message for fonts
# Tests exhibit a proportional font
Requires:       fonts-ttf-liberation
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Prima-%{version}

%if !%{with perl_Prima_enables_optional_test}
rm t/misc/pod.t
perl -i -ne 'print $_ unless m{\A\Qt/misc/pod.t\E}' MANIFEST
%endif
# Normalize end-of-lines
find -type f \( -name '*.pm' -o -name '*.pl' -o -name '*.PL' -o -name '*.t' \
     -o -name Changes -o -name README.md \) -exec perl -i -pe 's/\r\n/\n/' {} +
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS" \
    CYGWIN_WINAPI=0 \
    DEBUG=0 \
    VERBOSE=1 \
    WITH_FRIBIDI=%{with perl_Prima_enables_fribidi} \
    WITH_GTK2=%{with perl_Prima_enables_gtk2} \
    WITH_GTK3=0 \
    WITH_HARFBUZZ=%{with perl_Prima_enables_harfbuzz} \
    WITH_ICONV=1 \
    WITH_OPENMP=1 \
    WITH_XFT=%{with perl_Prima_enables_xft}
%{make_build}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
find $RPM_BUILD_ROOT -type f -name '*.a' -size 0 -delete
# %{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/misc/syntax.t
%if %{with perl_Prima_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/misc/pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/misc/fs.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset DISPLAY XDG_SESSION_TYPE
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -a prove -I . -r -j 1 t
%else
    prove -I . -r -j 1 t
%endif
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DISPLAY XDG_SESSION_TYPE
# Not parallel-safe
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc Copying AGPLv3 examples
# "examples" directory is installed into perl_vendorarch
%doc Changes README.md
%{_bindir}/*
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/prima-gencls.pod
%{perl_vendor_archlib}/Prima*
# pod image
%{perl_vendor_archlib}/vb-large.png
%exclude %{perl_vendor_archlib}/Prima/Stress.*
%exclude %{perl_vendor_archlib}/Prima/sys/Test.*
%{_mandir}/man1/*

%files Test
%{perl_vendor_archlib}/Prima/Stress.*
%{perl_vendor_archlib}/Prima/sys/Test.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Mar 02 2023 Igor Vlasenko <viy@altlinux.org> 1.68002-alt1
- automated CPAN update

* Wed Mar 01 2023 Igor Vlasenko <viy@altlinux.org> 1.68001-alt1
- automated CPAN update

* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 1.67001-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 1.67-alt1
- automated CPAN update

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 1.66-alt1
- automated CPAN update

* Fri Nov 26 2021 Igor Vlasenko <viy@altlinux.org> 1.63-alt1_1
- re-import
- properly link with libperl
- do not loose lib dependencies

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 1.63-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 1.61-alt1
- automated CPAN update

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.57-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.52-alt5_3
- rebuild with new perl 5.28.1

* Sun May 06 2018 Michael Shigorin <mike@altlinux.org> 1.52-alt4_3
- rebuild for e2kv4

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

