# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(PadWalker.pm) perl(Prima/Application.pm) perl(Prima/Buttons.pm) perl(Prima/Edit.pm) perl(Prima/Label.pm) perl(Prima/MsgBox.pm) perl(Prima/PodView.pm) perl(Prima/Utils.pm) perl(threads.pm) perl(threads/shared.pm) perl-podlators
# END SourceDeps(oneline)
# tries to run
%add_findreq_skiplist %_bindir/pdl2
# plug-ins
%add_findreq_skiplist */PDL/Demos/*
%add_findreq_skiplist */PDL/Graphics/*
BuildRequires: libjpeg-devel libf2c-ng-devel
BuildRequires: gcc-c++
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Proj has proved not beeing compatible all the time, bug #839651
%{bcond_without proj}

# Slatec does not work on PPC64 since 2.4.something
# could be a big endian related issue
%ifarch ppc64 s390 s390x
%{bcond_with slatec}
%else
%{bcond_without slatec}
%endif

Name:           perl-PDL
%global cpan_version 2.018
Version:        2.18.0
Release:        alt1_4.1
Summary:        The Perl Data Language
Group:          Development/Other
License:        GPL+ or Artistic
Url:            http://pdl.perl.org/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHM/PDL-%{cpan_version}.tar.gz
# Uncomment to enable PDL::IO::Browser
# Patch0:         perl-PDL-2.4.10-settings.patch
Patch1:         perl-PDL-2.8.0-hdf.patch
# Disable Proj support when it's not compatible, bug #839651
Patch2:         PDL-2.4.10-Disable-PDL-GIS-Proj.patch
# Compile Slatec as PIC, needed for ARM
Patch3:         PDL-2.6.0.90-Compile-Slatec-code-as-PIC.patch
# Disable Slatec code crashing on PPC64, bug #1041304
Patch4:         PDL-2.14.0-Disable-PDL-Slatec.patch
Patch5:         PDL-2.17.0-Update-additional-deps-for-Basic-Core.patch
BuildRequires:  coreutils
BuildRequires:  libfftw-devel
BuildRequires:  findutils
BuildRequires:  libfreeglut-devel
BuildRequires:  gcc-fortran
BuildRequires:  libgd2-devel
BuildRequires:  libgsl-devel >= 1.0
BuildRequires:  hdf-devel hdf-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
# perl(Astro::FITS::Header) not packaged yet
# Modified perl(Carp) bundled
# Modified perl(Carp::Heavy) bundled
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/CheckLib.pm)
BuildRequires:  perl(Devel/REPL.pm)
BuildRequires:  perl(ExtUtils/F77.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(lib.pm)
# OpenGL >= 0.6702 is required but newer OpenGL-0.70 shortened the version
BuildRequires:  perl(OpenGL.pm)
# OpenGL::Config is private OpenGL hash
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(Pod/Select.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(autodie.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Devel/REPL/Plugin.pm)
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(English.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(fields.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(FileHandle.pm)
BuildRequires:  perl(File/Map.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Filter/Simple.pm)
BuildRequires:  perl(Filter/Util/Call.pm)
BuildRequires:  perl(Inline.pm)
BuildRequires:  perl(Inline/C.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/Compile.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Pod/PlainText.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(SelfLoader.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(Benchmark.pm)
BuildRequires:  perl(ExtUtils/testlib.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(IPC/Cmd.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Warn.pm)
# Optional tests:
BuildRequires:  perl(Convert/UU.pm)
BuildRequires:  perl(Storable.pm)

%if %{with proj}
# Needed by PDL::GIS::Proj
BuildRequires:  libproj-devel
BuildRequires:  proj-nad
%endif
# Need by PDL::IO::Browser, currently disabled
# BuildRequires:  ncurses-devel
BuildRequires:  sharutils
Requires:       perl(ExtUtils/Liblist.pm)
Requires:       perl(ExtUtils/MakeMaker.pm)
Requires:       perl(ExtUtils/MM.pm)
Requires:       perl(File/Map.pm) >= 0.570
Requires:       perl(File/Spec.pm) >= 0.600
Requires:       perl(Filter/Simple.pm) >= 0.880
Requires:       perl(Inline.pm) >= 0.430
Requires:       perl(Module/Compile.pm) >= 0.230
# OpenGL >= 0.6702 is required but newer OpenGL-0.70 shortened the version
Requires:       perl(OpenGL.pm) >= 0.67.02
Requires:       perl(Prima/Application.pm)
Requires:       perl(Prima/Buttons.pm)
Requires:       perl(Prima/Edit.pm)
Requires:       perl(Prima/Label.pm)
Requires:       perl(Prima/PodView.pm)
Requires:       perl(Prima/Utils.pm)
Requires:       perl(Text/Balanced.pm) >= 1.890
Provides:       perl(PDL/Config.pm)
Provides:       perl(PDL/PP/CType.pm)
Provides:       perl(PDL/PP/Dims.pm)
Provides:       perl(PDL/PP/PDLCode.pm)
Provides:       perl(PDL/PP/SymTab.pm)
Provides:       perl(PDL/PP/XS.pm)
Provides:       perl(PDL/Lite.pm)
Provides:       perl(PDL/LiteF.pm)
Provides:       perl(PDL/Graphics/TriD.pm)
Provides:       perl(PDL/Graphics/TriD/GL.pm)
Provides:       perl(PDL/Graphics/TriD/Contours.pm)
Provides:       perl(PDL/Graphics/TriD/Image.pm)
Provides:       perl(PDL/Graphics/TriD/Objects.pm)
Provides:       perl(PGPLOT.pm)





# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\((OpenGL.Config|PDL.Demos.Screen|Tk|Win32.DDE.Client).pm\\)$/d
%filter_from_provides /^perl\\(Inline.pm\\)$/d
%filter_from_provides /^perl\\(Win32.*.pm\\)$/d
%filter_from_requires /^perl\\((Data.Dumper|File.Spec|Filter.Simple|Inline|Module.Compile|OpenGL|Text.Balanced).pm\\)$/d
Patch33: PDL-2.018-alt-link-Slatec-hack.patch

%description
PDL ("Perl Data Language") gives standard Perl the ability to
compactly store and speedily manipulate the large N-dimensional data
arrays which are the bread and butter of scientific computing.  PDL
turns perl into a free, array-oriented, numerical language similar to
such commercial packages as IDL and MatLab.

%prep
%setup -q -n PDL-%{cpan_version}
# Uncomment to enable PDL::IO::Browser
# %%patch0 -p1 -b .settings
%patch1 -p1 -b .hdf
%if %{without proj}
%patch2 -p1 -b .proj
%endif
%patch3 -p1 -b .slatecpic
%if %{without slatec}
%patch4 -p1 -b .slatec
%endif
%patch5 -p1
# Fix shellbang
sed -e 's,^#!/usr/bin/env perl,%(perl -MConfig -e 'print $Config{startperl}'),' -i Perldl2/pdl2
%patch33 -p1

%build
# Suppress numerous warnings about unused variables
CFLAGS="%{optflags} -Wno-unused"
# Fused multiply-add instructions cause segfaults on 64-bit PowerPC if GSL
# support is enabled (the same option is in gsl.spec), bug #1410162
%ifarch ppc64 ppc64le s390 s390x
CFLAGS="$CFLAGS -ffp-contract=off"
%endif
# Uncomment to enable PDL::IO::Browser
# CFLAGS="$CFLAGS -DNCURSES"
CFLAGS="$CFLAGS" perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$CFLAGS"
make OPTIMIZE="$CFLAGS" %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
perl -Mblib Doc/scantree.pl %{buildroot}%{perl_vendor_archlib}
perl -pi -e "s|%{buildroot}/|/|g" %{buildroot}%{perl_vendor_archlib}/PDL/pdldoc.db
find %{buildroot}%{perl_vendor_archlib} -type f -name "*.pm" | xargs chmod -x
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
chmod -R u+w %{buildroot}/*

%check
unset DISPLAY
export PERL5LIB=`pwd`/blib/lib
make test

%files
%doc COPYING Changes INTERNATIONALIZATION Known_problems README TODO
%{_bindir}/*
%{perl_vendor_archlib}/Inline/*
%{perl_vendor_archlib}/PDL*
%{perl_vendor_archlib}/auto/PDL/
%{_mandir}/man1/*.1*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.18.0-alt1_4.1
- rebuild with new perl 5.26.1

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.18.0-alt1_4
- new version (closes: #34130)

