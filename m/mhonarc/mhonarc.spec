Name: mhonarc
Version: 2.6.24
Release: alt0.1
Summary: Perl mail-to-HTML converter

Group: Networking/Mail
License: GPLv2+
Url: https://metacpan.org/release/MHonArc
Source0: https://cpan.metacpan.org/authors/id/L/LD/LDIDRY/MHonArc-%version.tar

BuildArch: noarch
BuildRequires: coreutils
BuildRequires: perl(Config.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(FileHandle.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(Symbol.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(Time/Local.pm)
BuildRequires: perl(Unicode/String.pm)
BuildRequires: perl(Unicode/MapUTF8.pm)
BuildRequires: perl(Encode/Alias.pm)
Provides: MHonArc = %version-%release

# added manually
Requires: perl(Unicode/MapUTF8.pm)
Requires: perl(Unicode/String.pm)

%filter_from_requires /perl(.*\.pl)/d;/perl(MHonArc.*)/d
%filter_from_provides /perl(.*\.pm)/d
%add_perl_lib_path %buildroot%_datadir/MHonArc
%add_perl_lib_path %buildroot%_datadir/MHonArc/MHonArc
# findreq broken here
%add_findreq_skiplist */MHonArc/MHonArc/UTF8/MapUTF8.pm

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name = %EVR

%description doc
Documentation for %name.

%prep
%setup -n MHonArc-%version

%build
# Nothing to build

%install
%__perl install.me -batch -libpath %buildroot%_datadir/MHonArc \
  -nodoc -manpath %buildroot%_mandir -binpath %buildroot%_bindir
# Aww, remainders of buildroot and /usr/local, weed 'em out.
%__perl -pi -e \
  "s|%buildroot\b||g ; s|/usr/local/bin/perl\b|%__perl|g" \
  %buildroot%_bindir/* examples/mha*

%files
%doc COPYING
%doc ACKNOWLG BUGS CHANGES RELNOTES TODO
%doc examples extras
%_bindir/mh*
%_datadir/MHonArc
%_man1dir/mh*.1*

%files doc
%doc doc logo

%changelog
* Mon Nov 08 2021 L.A. Kostis <lakostis@altlinux.ru> 2.6.24-alt0.1
- Initial build for ALTLinux.
- Move doc and logo to -doc package.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
