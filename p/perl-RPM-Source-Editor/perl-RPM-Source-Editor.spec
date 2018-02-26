%define module RPM-Source-Editor
%def_without hashertarbuild

Name: perl-%module
Version: 0.784
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for src.rpm and spec file editing
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# due to rpmbuild -bE
# Recommends: rpm-build

# Automatically added by buildreq on Wed Nov 06 2010
BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl-RPM perl(Clone.pm)
# for RPM::Source::Tools
BuildRequires: perl-upstreamwatch perl-DistroMap

Obsoletes: hashertarbuild < 0.73
Conflicts: hashertarbuild < 0.73


%description
Perl extension for editing src.RPMs and spec files

%if_with hashertarbuild
%package -n hashertarbuild
Group: Development/Other
Summary: a tool to create source tarballs for hasher
Requires: %name = %version-%release

%description -n hashertarbuild
A tool to create rpm-based source tarballs for hasher.
Sometimes rpmbuild -bs --nodeps does not work due to macros abcent. 
Use hashertarbuild <spec> to create source tarball ready for hasher.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

install -m755 -D hashertarbuild %buildroot%_bindir/hashertarbuild
for i in hashertarbuild; do
    pod2man  --name $i --center 'hashertarbuild' --section 1 --release %version $i > $i.1
done

mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/srpmtools/hooks
install -Dm644 stdheaders.txt %buildroot%_datadir/srpmtools/data/stdheaders.txt

%files
%doc Changes
#doc README
%_bindir/srpm*
%perl_vendor_privlib/RPM*
#perl_vendor_man3dir/*
%dir %_datadir/srpmtools
%dir %_datadir/srpmtools/hooks
%_datadir/srpmtools/data
%_bindir/buildreq-*
%_man1dir/buildreq-*

#files -n hashertarbuild
%_bindir/hashertarbuild
%_man1dir/hashertarbuild*

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.784-alt1
- new version

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.783-alt1
- new version

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.782-alt1
- new version

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.781-alt1
- new version

* Wed May 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.780-alt3
- bugfix release

* Tue May 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.780-alt2
- bugfix release

* Tue May 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.780-alt1
- initial perl support

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.779-alt1
- new version

* Mon May 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.778-alt2
- bugfix release

* Fri May 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.778-alt1
- SourceAnalyzer: support for gir build deps

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt8
- bugfix release

* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt7
- bugfix release

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt6
- bugfix release

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt5
- bugfix release

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt4
- bugfix release

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt3
- bugfix release

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.777-alt2
- bugfix release

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.777-alt1
- new version

* Sun Dec 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.776-alt1
- new version

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.775-alt1
- bugfix release

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.774-alt3
- bugfix release

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.774-alt2
- bugfix release

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.774-alt1
- new version

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.773-alt1
- new version

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.772-alt1
- bugfix release

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.771-alt1
- bugfix release
