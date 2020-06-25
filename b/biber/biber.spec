Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime.pm) perl(DateTime/TimeZone.pm) perl(IO/String.pm) perl(LWP/UserAgent.pm) perl(Pod/Usage.pm) perl(Text/Diff/Config.pm) perl(parent.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           biber
Version:        2.14
Release:        alt1_1
Summary:        Command-line bibliographic manager, BibTeX replacement
License:        (GPL+ or Artistic 2.0) and Artistic 2.0
URL:            http://biblatex-biber.sourceforge.net/
Source0:        https://github.com/plk/biber/archive/v%{version}.tar.gz
# not appropriate for upstream: http://github.com/plk/biber/pull/97
Patch0:         biber-drop-builddeps-for-monolithic-build.patch
BuildArch:      noarch

BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(autovivification.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Business/ISBN.pm)
BuildRequires:  perl(Business/ISMN.pm)
BuildRequires:  perl(Business/ISSN.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Accessor.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dump.pm)
BuildRequires:  perl(Data/Compare.pm)
BuildRequires:  perl(Data/Uniqid.pm)
BuildRequires:  perl(Date/Simple.pm)
BuildRequires:  perl(DateTime/Calendar/Julian.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Encode/Alias.pm)
BuildRequires:  perl(Encode/EUCJPASCII.pm)
BuildRequires:  perl(Encode/HanExtra.pm)
BuildRequires:  perl(Encode/JIS2K.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Compare.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Slurper.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IPC/Cmd.pm)
BuildRequires:  perl(IPC/Run3.pm)
BuildRequires:  perl(Lingua/Translit.pm)
BuildRequires:  perl(List/AllUtils.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(List/MoreUtils/XS.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(locale.pm)
BuildRequires:  perl(Log/Log4perl.pm)
BuildRequires:  perl(Log/Log4perl/Appender/File.pm)
BuildRequires:  perl(Log/Log4perl/Appender/Screen.pm)
BuildRequires:  perl(Log/Log4perl/Layout/PatternLayout.pm)
BuildRequires:  perl(Log/Log4perl/Layout/SimpleLayout.pm)
BuildRequires:  perl(LWP/Protocol/https.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Parse/RecDescent.pm)
BuildRequires:  perl(PerlIO/utf8_strict.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(re.pm)
BuildRequires:  perl(Regexp/Common.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(sigtrap.pm)
BuildRequires:  perl(Sort/Key.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Text/CSV.pm)
BuildRequires:  perl(Text/CSV_XS.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Text/BibTeX.pm)
BuildRequires:  perl(Text/BibTeX/Name.pm)
BuildRequires:  perl(Text/BibTeX/NameFormat.pm)
BuildRequires:  perl(Text/Roman.pm)
BuildRequires:  perl(Text/Wrap.pm)
BuildRequires:  perl(Unicode/UCD.pm)
BuildRequires:  perl(Unicode/LineBreak.pm)
BuildRequires:  perl(Unicode/Normalize.pm)
BuildRequires:  perl(Unicode/GCString.pm)
BuildRequires:  perl(Unicode/Collate/Locale.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XML/LibXML.pm)
BuildRequires:  perl(XML/LibXML/Simple.pm)
BuildRequires:  perl(XML/LibXSLT.pm)
BuildRequires:  perl(XML/Writer.pm)
# For tests
BuildRequires:  texlive-collection-basic
Requires:       perl(autovivification.pm)
Requires:       perl(Business/ISBN.pm)
Requires:       perl(Business/ISMN.pm)
Requires:       perl(Business/ISSN.pm)
# Upstream confirmed [1] deps on Encode::* and List::MoreUtils (c.f., [2]).
# [1] https://github.com/plk/biber/issues/98
# [2] https://bugzilla.redhat.com/show_bug.cgi?id=1165620
Requires:       perl(Encode/EUCJPASCII.pm)
Requires:       perl(Encode/HanExtra.pm)
Requires:       perl(Encode/JIS2K.pm)
Requires:       perl(List/MoreUtils.pm)
Requires:       perl(List/MoreUtils/XS.pm)
Requires:       perl(LWP/UserAgent.pm)
Requires:       perl(LWP/Protocol/https.pm)
Requires:       perl(Mozilla/CA.pm) >= 20141217
Requires:       perl(PerlIO/utf8_strict.pm)
Requires:       perl(Text/BibTeX.pm) >= 0.880
Requires:       perl(Text/Roman.pm)
Requires:       perl(Unicode/Collate/Locale.pm)
Requires:       perl(XML/LibXSLT.pm)
Requires:       texlive-collection-basic texlive-dist
# Biber need a minimum biblatex (src: doc/biber.tex "Compatibility Matrix")
#     biber | texlive-biblatex
#     ------+-----------------
#     1.8   | 2.8a
#     2.1   | 3.0
#     2.6   | 3.5, 3.6
#     2.7   | 3.7       (#1401482)
#     2.8   | 3.8
#     2.9   | 3.9
#     2.10  | 3.10
#     2.11  | 3.11
#     2.12  | 3.12
#     2.13  | 3.13
#     2.14  | 3.14
# (biblatex also has minimum biber requirements)

# filter autogenerated runtime dep, instead use constraint above

Source44: import.info
%filter_from_requires /^perl(Text.BibTeX.pm)/d


%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.


%prep
%setup -q -n biber-%{version}
%patch0 -p1


%build
perl Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
chmod u+w %{buildroot}%{_bindir}/*


%check
./Build test verbose=1


%files
%doc README.md Changes TODO.org
%{_bindir}/%{name}
%{_mandir}/man1/*
%{perl_vendor_privlib}/Biber*


%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1_1
- update to new release by fcimport

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2
- new version

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1_4
- new version

* Mon Jan 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_0
- bootstrap build w/o texlive deps

