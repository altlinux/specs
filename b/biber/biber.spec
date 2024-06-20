Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Text/Diff/Config.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform developer tests which exhibit a biber executable
%bcond_without biber_enables_extra_test

Name:           biber
# Export $BCF_VERSION from lib/Biber/Constants.pm, bug #2048536
%define bcfversion 3.8
Version:        2.17
Release:        alt2_2
Summary:        Command-line bibliographic manager, BibTeX replacement
# bin/biber:        Artistic 2.0
# data/texmap.xsl:  Artistic 2.0
# doc/biber.tex:    Artistic 2.0
# lib/Biber.pm:     Artistic 2.0
# lib/Biber/LaTeX/recode_data.xml:  Artistic 2.0
# README.md:        Artistic 2.0
## Not in any binary package
# Build.PL:         GPL+ or Artistic
## Not used at all
# etc/bibtex.g:     GPLv2+
# etc/parser.dlg:   GPLv2+ (generated from etc/bibtex.g)
# etc/tugboat.bib:  Public Domain
License:        (GPL+ or Artistic 2.0) and Artistic 2.0
URL:            http://biblatex-biber.sourceforge.net/
Source0:        https://github.com/plk/biber/archive/v%{version}.tar.gz
# not appropriate for upstream: http://github.com/plk/biber/pull/97
Patch0:         biber-drop-builddeps-for-monolithic-build.patch
# Do not use /bin/env in shebangs
Patch1:         biber-2.16-Normalize-shebangs.patch
Patch2:         biber-2.17-fix-for-new-perl.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl
BuildRequires:  perl(autovivification.pm)
BuildRequires:  perl(Business/ISBN.pm)
BuildRequires:  perl(Business/ISMN.pm)
BuildRequires:  perl(Business/ISSN.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Accessor.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Compare.pm)
BuildRequires:  perl(Data/Dump.pm)
BuildRequires:  perl(Data/Uniqid.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Calendar/Julian.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Encode/Alias.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Copy.pm)
# File::DosGlob not used on Linux
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Slurper.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
%if %{with biber_enables_extra_test}
BuildRequires:  perl(Getopt/Long.pm)
%endif
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(IPC/Cmd.pm)
BuildRequires:  perl(IPC/Run3.pm)
BuildRequires:  perl(Lingua/Translit.pm)
BuildRequires:  perl(List/AllUtils.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(locale.pm)
BuildRequires:  perl(Log/Log4perl.pm)
BuildRequires:  perl(Log/Log4perl/Appender/File.pm)
BuildRequires:  perl(Log/Log4perl/Appender/Screen.pm)
BuildRequires:  perl(Log/Log4perl/Layout/PatternLayout.pm)
BuildRequires:  perl(Log/Log4perl/Layout/SimpleLayout.pm)
%if %{with biber_enables_extra_test}
BuildRequires:  perl(Log/Log4perl/Level.pm)
%endif
BuildRequires:  perl(LWP/Protocol/https.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
# Mozilla::CA is not helpful
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Parse/RecDescent.pm)
%if %{with biber_enables_extra_test}
BuildRequires:  perl(Pod/Usage.pm)
%endif
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Regexp/Common.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(sigtrap.pm)
BuildRequires:  perl(Sort/Key.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Text/BibTeX.pm)
BuildRequires:  perl(Text/BibTeX/Name.pm)
BuildRequires:  perl(Text/BibTeX/NameFormat.pm)
BuildRequires:  perl(Text/CSV.pm)
BuildRequires:  perl(Text/Roman.pm)
BuildRequires:  perl(Text/Wrap.pm)
# Unicode::Collate::Locale version from Unicode::Collate in Build.PL
BuildRequires:  perl(Unicode/Collate/Locale.pm)
BuildRequires:  perl(Unicode/GCString.pm)
BuildRequires:  perl(Unicode/Normalize.pm)
BuildRequires:  perl(Unicode/UCD.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(vars.pm)
# Win32* not used on Linux
BuildRequires:  perl(XML/LibXML.pm)
BuildRequires:  perl(XML/LibXML/Simple.pm)
BuildRequires:  perl(XML/LibXSLT.pm)
BuildRequires:  perl(XML/Writer.pm)
# Tests:
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests:
# texlive-plain not helpful; The only "plain.tex" usage in t/utils.t checks
# that it exist on a file system.
# It would also create a build cycle: texlive-plain a.. texlive-biblatex a.. biber
# Extra tests:
%if %{with biber_enables_extra_test}
BuildRequires:  perl(File/Compare.pm)
%endif
Requires:       perl(autovivification.pm)
Requires:       perl(Business/ISBN.pm)
Requires:       perl(Business/ISMN.pm)
Requires:       perl(Business/ISSN.pm)
Requires:       perl(Lingua/Translit.pm) >= 0.280
Requires:       perl(LWP/UserAgent.pm)
Requires:       perl(LWP/Protocol/https.pm)
Requires:       perl(Text/BibTeX.pm) >= 0.880
# Unicode::Collate::Locale version from Unicode::Collate in Build.PL
Requires:       perl(Unicode/Collate/Locale.pm) >= 1.290
Requires:       perl(XML/LibXSLT.pm)
# Biber does not use biblatex, but it requires a compatible version of
# a biblatex control file (BCF) which is produced by biblatex. See @bcfversion
# definition in /usr/share/texlive/texmf-dist/tex/latex/biblatex/biblatex.sty
# and a corresponding $BCF_VERSION in lib/Biber/Constants.pm. Unfortunally,
# Biber supports only one version of BCF. See "Compatibility Matrix" in
# doc/biber.tex.
# Because Biber does not use texlive-biblatex, Biber cannot Require it's exact
# version. Because it is expensive to rebuild texlive, it's not good to
# Require a specific biber version from texlive-biblatex.
# Hence I proposed a bcfversion dependency which both packages can agree on
# (bug #2048536).
Provides:       bcfversion = %{bcfversion}
# Version at least the main module
Provides:       perl(Biber.pm) = %{version}

# Remove under-specified dependencies


Source44: import.info
%filter_from_requires /^perl(\(Text.BibTeX\|Unicode.Collate.Locale\).pm)/d
%filter_from_provides /^perl(Biber.pm)/d

%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.


%package tests
Group: Development/Tools
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".


%prep
%setup -q -n biber-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
# t/remote-files.t needs the Internet
for F in \
    t/remote-files.t \
%if !%{with biber_enables_extra_test}
    t/full-*.t \
%endif
; do
    rm "$F";
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\b}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done


%build
perl Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/data/schemata
ln -s %{perl_vendor_privlib}/Biber/biber-tool.conf \
    %{buildroot}%{_libexecdir}/%{name}/data
for F in {bcf,config}.{rnc,rng}; do
    ln -s %{perl_vendor_privlib}/Biber/"$F" \
        %{buildroot}%{_libexecdir}/%{name}/data/schemata
done
%if %{with biber_enables_extra_test}
mkdir %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/datalists.t via generate_bltxml_schema() writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset BIBER_DEV_TESTS ISBN_RANGE_MESSAGE PAR_TEMP PERL_LWP_SSL_CA_FILE
%if %{with biber_enables_extra_test}
export BIBER_DEV_TESTS=1
%endif
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test


%check
unset BIBER_DEV_TESTS ISBN_RANGE_MESSAGE PAR_TEMP PERL_LWP_SSL_CA_FILE
%if %{with biber_enables_extra_test}
export BIBER_DEV_TESTS=1
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test


%files
%doc README.md Changes TODO.org
%{_bindir}/%{name}
%{_mandir}/man1/*
%{perl_vendor_privlib}/Biber*

%files tests
%{_libexecdir}/%{name}


%changelog
* Thu Jun 20 2024 Ivan A. Melnikov <iv@altlinux.org> 2.17-alt2_2
- NMU: fix FTBFS

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 2.17-alt1_2
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.16-alt1_4
- update to new release by fcimport

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1_4
- fixed build

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1_1
- update to new release by fcimport

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2
- new version

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_4
- new version

* Mon Jan 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_0
- bootstrap build w/o texlive deps

