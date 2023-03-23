%define _unpackaged_files_terminate_build 1
%global optflags_lto %nil
# tests need network and access to google.com
%define _without_test 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Compile.pm) perl(PadWalker.pm) perl(Prima/Application.pm) perl(Prima/Buttons.pm) perl(Prima/Edit.pm) perl(Prima/Label.pm) perl(Prima/MsgBox.pm) perl(Prima/PodView.pm) perl(Prima/Utils.pm) perl(threads.pm) perl(threads/shared.pm) perl-podlators
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
%{bcond_without perl_PDL_enables_proj}

# Slatec does not work on PPC64 since 2.4.something
# could be a big endian related issue
%ifarch ppc64 s390 s390x
%{bcond_with perl_PDL_enables_slatec}
%else
%{bcond_without perl_PDL_enables_slatec}
%endif

# Run optional test
%{bcond_without perl_PDL_enables_optional_test}

Name:           perl-PDL
Version:        2.082
Release:        alt1
Summary:        The Perl Data Language
License:        GPL+ or Artistic
Url:            http://pdl.perl.org/
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/PDL-%{version}.tar.gz
# Uncomment to enable PDL::IO::Browser
# Patch0:         perl-PDL-2.4.10-settings.patch
# Disable Proj support when it's not compatible, bug #839651
Patch1:         PDL-2.4.10-Disable-PDL-GIS-Proj.patch
# Compile Slatec as PIC, needed for ARM
Patch2:         PDL-2.6.0.90-Compile-Slatec-code-as-PIC.patch
# Disable Slatec code crashing on PPC64, bug #1041304
Patch3:         PDL-2.51.0-Disable-PDL-Slatec.patch
# Fix numbering of line in test when shebang is added
Patch6:         PDL-2.28.0-Fix-numbering-of-line-in-test.patch
BuildRequires:  coreutils
BuildRequires:  libfftw3-devel
BuildRequires:  findutils
BuildRequires:  libfreeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libgd3-devel
BuildRequires:  libgsl-devel >= 1.0
%ifnarch %e2k %mips riscv64
# archdep, requires patching the patched source
BuildRequires:  hdf hdf-devel
%endif
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
# perl(Astro::FITS::Header) not packaged yet
BuildRequires:  perl(blib.pm)
# Modified perl(Carp) bundled
# Modified perl(Carp::Heavy) bundled
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/CheckLib.pm)
BuildRequires:  perl(Devel/REPL.pm)
BuildRequires:  perl(ExtUtils/Depends.pm)
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
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Math/Complex.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Pod/PlainText.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(SelfLoader.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Term/ReadKey.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(Benchmark.pm)
BuildRequires:  perl(ExtUtils/MakeMaker/Config.pm)
BuildRequires:  perl(ExtUtils/testlib.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(IPC/Cmd.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Warn.pm)
%if %{with perl_PDL_enables_optional_test}
# Optional tests:
# netpbm-progs for jpegtopnm
BuildRequires:  netpbm
BuildRequires:  perl(Convert/UU.pm)
BuildRequires:  perl(Storable.pm)
%endif

%if %{with perl_PDL_enables_proj}
# Needed by PDL::GIS::Proj
BuildRequires:  libproj-devel
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
# OpenGL >= 0.6702 is required but newer OpenGL-0.70 shortened the version
Requires:       perl(OpenGL.pm) >= 0.67.02
Requires:       perl(Prima/Application.pm)
Requires:       perl(Prima/Buttons.pm)
Requires:       perl(Prima/Edit.pm)
Requires:       perl(Prima/Label.pm)
Requires:       perl(Prima/PodView.pm)
Requires:       perl(Prima/Utils.pm)
Requires:       perl(Text/Balanced.pm) >= 1.890
#Provides:       perl(PDL/Config.pm) = %{version}
#Provides:       perl(PDL/DiskCache.pm) = %{version}
#Provides:       perl(PDL/PP/CType.pm) = %{version}
#Provides:       perl(PDL/PP/Dims.pm) = %{version}
#Provides:       perl(PDL/PP/PDLCode.pm) = %{version}
#Provides:       perl(PDL/PP/SymTab.pm) = %{version}
#Provides:       perl(PDL/PP/XS.pm) = %{version}
#Provides:       perl(PDL/Graphics/TriD/Objects.pm) = %{version}





# Remove under-specified dependencies

# Remove modules not compiled

Source44: import.info
%filter_from_requires /^perl(\(OpenGL.Config\|PDL.Demos.Screen\|PDL.Graphics.PGPLOT\|PDL.Graphics.PGPLOT.Window\|Tk\|Win32.DDE.Client\).pm)/d
%filter_from_provides /^perl(Inline.pm)/d
%filter_from_provides /^perl(Win32.*.pm)/d
%filter_from_requires /^perl(\(Data.Dumper\|File.Spec\|Filter.Simple\|Inline\|Module.Compile\|OpenGL\|Text.Balanced\).pm)/d
%filter_from_requires /^perl(\(PDL.GIS.Proj\|PDL.IO.HDF.*\).pm)/d
Patch33: PDL-2.063-alt-link-Slatec-hack.patch
Patch34: PDL-2.047-alt-gsl-hack.patch

%description
PDL ("Perl Data Language") gives standard Perl the ability to
compactly store and speedily manipulate the large N-dimensional data
arrays which are the bread and butter of scientific computing.  PDL
turns perl into a free, array-oriented, numerical language similar to
such commercial packages as IDL and MatLab.

%package tests
Group: Development/Other
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Devel/CheckLib.pm)

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n PDL-%{version}
# Uncomment to enable PDL::IO::Browser
# %%patch0 -p1 -b .settings
%if %{without perl_PDL_enables_proj}
%patch2 -p1 -b .proj
%endif
%patch3 -p1 -b .slatecpic
%if %{without perl_PDL_enables_slatec}
%patch4 -p1 -b .slatec
%endif
#patch6 -p1
# Fix shellbang
perl -MConfig -pi -e 's|^#!/usr/bin/env perl|$Config{startperl}|' Perldl2/pdl2

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
#patch33 -p1
%patch34 -p1

# failed on armh
[ %version == 2.047 ] && rm IO/FlexRaw/t/flexraw_fortran.t

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
CFLAGS="$CFLAGS" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$CFLAGS"
make OPTIMIZE="$CFLAGS" %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
perl -Mblib Doc/scantree.pl %{buildroot}%{perl_vendor_archlib}
perl -pi -e "s|%{buildroot}/|/|g" %{buildroot}%{perl_vendor_archlib}/PDL/pdldoc.db
find %{buildroot}%{perl_vendor_archlib} -type f -name "*.pm" | xargs chmod -x
find %{buildroot} -type f -name '*.bs' -empty -delete

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t m51.fits %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset DISPLAY
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

# %{_fixperms} %{buildroot}/*

%check
%ifarch armh
exit 0
%endif
unset DISPLAY
export PERL5LIB=`pwd`/blib/lib
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes INTERNATIONALIZATION README Bugs.pod Doc Example
%{_bindir}/*
%{perl_vendor_archlib}/Inline/*
%{perl_vendor_archlib}/PDL*
%{perl_vendor_archlib}/auto/PDL/
%{_mandir}/man1/*.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 2.082-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 2.081-alt1
- automated CPAN update

* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 2.080-alt1
- automated CPAN update

* Tue May 03 2022 Igor Vlasenko <viy@altlinux.org> 2.079-alt1
- automated CPAN update

* Mon Apr 11 2022 Igor Vlasenko <viy@altlinux.org> 2.078-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 2.077-alt1
- automated CPAN update

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 2.075-alt1
- automated CPAN update

* Tue Feb 08 2022 Igor Vlasenko <viy@altlinux.org> 2.074-alt1
- automated CPAN update

* Wed Feb 02 2022 Igor Vlasenko <viy@altlinux.org> 2.072-alt1
- new version

* Wed Feb 02 2022 Igor Vlasenko <viy@altlinux.org> 2.070-alt1
- automated CPAN update

* Sun Jan 30 2022 Igor Vlasenko <viy@altlinux.org> 2.068-alt1
- new version

* Fri Jan 28 2022 Igor Vlasenko <viy@altlinux.org> 2.066-alt1
- new version

* Fri Jan 28 2022 Igor Vlasenko <viy@altlinux.org> 2.064-alt1
- new version

* Fri Nov 26 2021 Igor Vlasenko <viy@altlinux.org> 2.063-alt1
- automated CPAN update

* Thu Oct 14 2021 Ivan A. Melnikov <iv@altlinux.org> 2.057-alt2
- riscv64 support

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 2.057-alt1
- automated CPAN update

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 2.054-alt1
- automated CPAN update

* Sun Jul 11 2021 Igor Vlasenko <viy@altlinux.org> 2.052-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 2.051-alt1
- automated CPAN update

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 2.047-alt2_2
- mipsel support thanks to iv@

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 2.047-alt1_2
- new version

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 2.034-alt1
- automated CPAN update

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 2.033-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 2.032-alt1
- automated CPAN update

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 2.029-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 2.026-alt1
- automated CPAN update

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 2.025-alt1
- automated CPAN update

* Mon Sep 28 2020 Igor Vlasenko <viy@altlinux.ru> 2.24.0-alt2_1
- manually removed BuildRequires:  libfftw3-devel

* Mon Sep 21 2020 Igor Vlasenko <viy@altlinux.ru> 2.24.0-alt1_1
- new version

* Fri Apr 17 2020 Igor Vlasenko <viy@altlinux.ru> 2.21.0-alt1_3
- added e2k patch

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 2.021-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.20.0-alt1_2
- new version

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.19.0-alt4_9
- update to new release by fcimport

* Sun Oct 06 2019 Vladislav Zavjalov <slazav@altlinux.org> 2.19.0-alt4
- rebuild with libproj 6.2.0
- remove dependency on proj-nad (all these data are in libproj package now)

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.19.0-alt3_5
- update to new release by fcimport

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 2.19.0-alt3_3
- rebuild with libproj 5.2.2

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.19.0-alt2_3
- rebuild with new perl 5.28.1

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.19.0-alt1_3
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.19.0-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.019-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.18.0-alt1_4.1
- rebuild with new perl 5.26.1

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.18.0-alt1_4
- new version (closes: #34130)

